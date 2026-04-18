content = """const cache = {};
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
    const cacheKey = "ing_" + ingredients.toLowerCase().trim() + "_" + (cuisine || "none");
    if (cache[cacheKey] && Date.now() - cache[cacheKey].timestamp < CACHE_DURATION) {
      return Response.json(cache[cacheKey].data);
    }
    try {
      if (cuisine) {
        const cuisineList = cuisine.split(",").map(c => c.trim().toLowerCase());

        // Fetch cuisine recipes and ingredient recipes in parallel
        const cuisineFetches = cuisineList.map(c =>
          fetch("https://api.spoonacular.com/recipes/complexSearch?cuisine=" + encodeURIComponent(c) + "&number=20&addRecipeInformation=false&apiKey=" + apiKey)
            .then(r => r.json())
            .then(j => (j.results || []).map(r => ({ ...r, matchedCuisine: c })))
            .catch(() => [])
        );

        const ingredientFetch = fetch("https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + encodeURIComponent(ingredients) + "&number=20&apiKey=" + apiKey)
          .then(r => r.json())
          .then(d => Array.isArray(d) ? d : [])
          .catch(() => []);

        const [cuisineResultsArrays, ingredientResults] = await Promise.all([
          Promise.all(cuisineFetches),
          ingredientFetch,
        ]);

        const cuisineRecipes = cuisineResultsArrays.flat();
        const cuisineIdSet = new Set(cuisineRecipes.map(r => r.id));

        // Find ingredient results that are also in cuisine results
        const overlap = ingredientResults.filter(r => cuisineIdSet.has(r.id));

        let results;
        if (overlap.length >= 3) {
          results = overlap.slice(0, 9);
        } else if (overlap.length > 0) {
          const overlapIds = new Set(overlap.map(r => r.id));
          const cuisineOnly = cuisineRecipes
            .filter(r => !overlapIds.has(r.id))
            .slice(0, 9 - overlap.length)
            .map(r => ({
              id: r.id,
              title: r.title,
              image: r.image,
              usedIngredients: ingredients.split(",").map(i => ({ name: i.trim() })),
              missedIngredients: [],
              isCuisineSearch: true,
            }));
          results = [...overlap, ...cuisineOnly].slice(0, 9);
        } else {
          // No overlap — show cuisine results only
          const seenIds = new Set();
          results = cuisineRecipes
            .filter(r => { if (seenIds.has(r.id)) return false; seenIds.add(r.id); return true; })
            .slice(0, 9)
            .map(r => ({
              id: r.id,
              title: r.title,
              image: r.image,
              usedIngredients: ingredients.split(",").map(i => ({ name: i.trim() })),
              missedIngredients: [],
              isCuisineSearch: true,
            }));
        }

        cache[cacheKey] = { data: results, timestamp: Date.now() };
        return Response.json(results);
      } else {
        const res = await fetch("https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + encodeURIComponent(ingredients) + "&number=9&apiKey=" + apiKey);
        const data = await res.json();
        cache[cacheKey] = { data: Array.isArray(data) ? data : [], timestamp: Date.now() };
        return Response.json(Array.isArray(data) ? data : []);
      }
    } catch (error) {
      return Response.json({ error: "Failed to fetch recipes" }, { status: 500 });
    }
  }

  return Response.json({ error: "No parameters provided" }, { status: 400 });
}
"""

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')