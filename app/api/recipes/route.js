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
    const cacheKey = "ing_" + ingredients.toLowerCase().trim() + (cuisine ? "_" + cuisine : "");
    if (cache[cacheKey] && Date.now() - cache[cacheKey].timestamp < CACHE_DURATION) {
      return Response.json(cache[cacheKey].data);
    }
    try {
      let url;
      if (cuisine) {
        url = "https://api.spoonacular.com/recipes/complexSearch?includeIngredients=" + encodeURIComponent(ingredients) + "&cuisine=" + encodeURIComponent(cuisine) + "&number=9&addRecipeInformation=false&fillIngredients=true&apiKey=" + apiKey;
        const res = await fetch(url);
        const json = await res.json();
        const results = (json.results || []).map((r) => ({
          id: r.id,
          title: r.title,
          image: r.image,
          usedIngredients: ingredients.split(",").map(i => ({ name: i.trim() })),
          missedIngredients: [],
          likes: 0,
          isCuisineSearch: true,
          cuisine: cuisine,
        }));
        cache[cacheKey] = { data: results, timestamp: Date.now() };
        return Response.json(results);
      } else {
        url = "https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + ingredients + "&number=9&apiKey=" + apiKey;
        const res = await fetch(url);
        const data = await res.json();
        cache[cacheKey] = { data, timestamp: Date.now() };
        return Response.json(data);
      }
    } catch (error) {
      return Response.json({ error: "Failed to fetch recipes" }, { status: 500 });
    }
  }

  return Response.json({ error: "No parameters provided" }, { status: 400 });
}
