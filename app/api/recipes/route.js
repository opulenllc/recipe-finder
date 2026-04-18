const cache = {};
const CACHE_DURATION = 60 * 60 * 1000;

export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const ingredients = searchParams.get("ingredients");
  const id = searchParams.get("id");
  const type = searchParams.get("type");
  const query = searchParams.get("query");
  const cuisine = searchParams.get("cuisine");
  const apiKey = "6b6dd0f982c448f7adef501f6ca84f88";

  if (id && type === "info") {
    const cacheKey = "info_" + id;
    if (cache[cacheKey] && Date.now() - cache[cacheKey].timestamp < CACHE_DURATION) {
      return Response.json(cache[cacheKey].data);
    }
    try {
      const res = await fetch("https://api.spoonacular.com/recipes/" + id + "/information?includeNutrition=true&apiKey=" + apiKey);
      const data = await res.json();
      cache[cacheKey] = { data, timestamp: Date.now() };
      return Response.json(data);
    } catch (error) {
      return Response.json({ error: "Failed" }, { status: 500 });
    }
  }

  if (id && type === "instructions") {
    const cacheKey = "instr_" + id;
    if (cache[cacheKey] && Date.now() - cache[cacheKey].timestamp < CACHE_DURATION) {
      return Response.json(cache[cacheKey].data);
    }
    try {
      const res = await fetch("https://api.spoonacular.com/recipes/" + id + "/analyzedInstructions?apiKey=" + apiKey);
      const data = await res.json();
      cache[cacheKey] = { data, timestamp: Date.now() };
      return Response.json(data);
    } catch (error) {
      return Response.json([], { status: 500 });
    }
  }

  if (query) {
    const cacheKey = "query_" + query.toLowerCase().trim();
    if (cache[cacheKey] && Date.now() - cache[cacheKey].timestamp < CACHE_DURATION) {
      return Response.json(cache[cacheKey].data);
    }
    try {
      const res = await fetch("https://api.spoonacular.com/recipes/complexSearch?query=" + encodeURIComponent(query) + "&number=9&addRecipeInformation=false&apiKey=" + apiKey);
      const json = await res.json();
      const results = (json.results || []).map((r) => ({
        id: r.id,
        title: r.title,
        image: r.image,
        usedIngredients: [],
        missedIngredients: [],
        likes: 0,
        isNameSearch: true,
      }));
      cache[cacheKey] = { data: results, timestamp: Date.now() };
      return Response.json(results);
    } catch (error) {
      return Response.json({ error: "Failed to fetch recipes" }, { status: 500 });
    }
  }

  if (ingredients) {
    if (cuisine) {
      // CUISINE SEARCH: fetch cuisine recipes directly, no caching
      const cuisineList = cuisine.split(",").map(c => c.trim().toLowerCase()).sort();
      try {
        const cuisineFetches = cuisineList.map(c =>
          fetch("https://api.spoonacular.com/recipes/complexSearch?cuisine=" + encodeURIComponent(c) + "&query=" + encodeURIComponent(ingredients) + "&number=50&addRecipeInformation=true&apiKey=" + apiKey)
            .then(r => r.json())
            .then(j => (j.results || []).map(r => ({
              id: r.id,
              title: r.title,
              image: r.image,
              usedIngredients: (r.usedIngredients || []).length > 0 ? r.usedIngredients : [],
              missedIngredients: (r.missedIngredients || []).length > 0 ? r.missedIngredients : [],
              likes: r.aggregateLikes || 0,
              isCuisineSearch: true,
              cuisineLabel: c,
            })))
            .catch(() => [])
        );
        const cuisineResultsArrays = await Promise.all(cuisineFetches);
        const seenIds = new Set();
        const results = [];
        for (const arr of cuisineResultsArrays) {
          for (const r of arr) {
            if (!seenIds.has(r.id)) {
              seenIds.add(r.id);
              results.push(r);
            }
          }
        }
        return Response.json(results);
      } catch (error) {
        return Response.json({ error: "Failed to fetch recipes" }, { status: 500 });
      }
    } else {
      // NORMAL INGREDIENT SEARCH
      const cacheKey = "ing_" + ingredients.toLowerCase().trim();
      if (cache[cacheKey] && Date.now() - cache[cacheKey].timestamp < CACHE_DURATION) {
        return Response.json(cache[cacheKey].data);
      }
      try {
        const res = await fetch("https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + encodeURIComponent(ingredients) + "&number=100&apiKey=" + apiKey);
        const data = await res.json();
        cache[cacheKey] = { data: Array.isArray(data) ? data : [], timestamp: Date.now() };
        return Response.json(Array.isArray(data) ? data : []);
      } catch (error) {
        return Response.json({ error: "Failed to fetch recipes" }, { status: 500 });
      }
    }
  }

  return Response.json({ error: "No parameters provided" }, { status: 400 });
}
