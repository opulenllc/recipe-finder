with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

old = '''      if (cuisine) {
        const cuisineList = cuisine.split(",").map(c => c.trim().toLowerCase());
        const res = await fetch("https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + ingredients + "&number=20&apiKey=" + apiKey);
        const recipes = await res.json();
        if (!Array.isArray(recipes)) {
          cache[cacheKey] = { data: [], timestamp: Date.now() };
          return Response.json([]);
        }
        const ids = recipes.map(r => r.id).join(",");
        const infoRes = await fetch("https://api.spoonacular.com/recipes/informationBulk?ids=" + ids + "&apiKey=" + apiKey);
        const infos = await infoRes.json();
        const infoMap = {};
        if (Array.isArray(infos)) {
          infos.forEach(info => { infoMap[info.id] = info; });
        }
        console.log("INFO SAMPLE:", JSON.stringify(infos[0]?.cuisines));
        const filtered = recipes.filter(r => {
          const info = infoMap[r.id];
          if (!info) return false;
          const recipeCuisines = (info.cuisines || []).map(c => c.toLowerCase());
          if (recipeCuisines.length === 0) return true;
          return cuisineList.some(c => recipeCuisines.some(rc => rc.includes(c) || c.includes(rc)));
        });
        const results = (filtered.length > 0 ? filtered : recipes.slice(0, 9)).slice(0, 9);
        cache[cacheKey] = { data: results, timestamp: Date.now() };
        return Response.json(results);
      } else {'''

new = '''      if (cuisine) {
        const cuisineList = cuisine.split(",").map(c => c.trim().toLowerCase());
        // Fetch cuisine-specific recipes and ingredient-based recipes in parallel
        const cuisineFetches = cuisineList.map(c =>
          fetch("https://api.spoonacular.com/recipes/complexSearch?cuisine=" + encodeURIComponent(c) + "&number=20&addRecipeInformation=false&apiKey=" + apiKey)
            .then(r => r.json())
            .then(j => (j.results || []).map(r => ({ ...r, matchedCuisine: c })))
            .catch(() => [])
        );
        const ingredientFetch = fetch("https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + ingredients + "&number=20&apiKey=" + apiKey)
          .then(r => r.json())
          .then(d => Array.isArray(d) ? d : [])
          .catch(() => []);
        const [cuisineResultsArrays, ingredientResults] = await Promise.all([
          Promise.all(cuisineFetches),
          ingredientFetch,
        ]);
        // Flatten cuisine results and build a set of cuisine recipe IDs
        const cuisineRecipes = cuisineResultsArrays.flat();
        const cuisineIdSet = new Set(cuisineRecipes.map(r => r.id));
        // Find ingredient results that also appear in cuisine results
        const overlap = ingredientResults.filter(r => cuisineIdSet.has(r.id));
        let results;
        if (overlap.length >= 3) {
          results = overlap.slice(0, 9);
        } else if (overlap.length > 0) {
          // Supplement with cuisine-only results
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
              likes: 0,
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
              likes: 0,
              isCuisineSearch: true,
            }));
        }
        cache[cacheKey] = { data: results, timestamp: Date.now() };
        return Response.json(results);
      } else {'''

content = content.replace(old, new)

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')