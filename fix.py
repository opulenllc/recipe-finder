with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

old = '''        const cuisineFetches = cuisineList.map(c =>
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
        );'''

new = '''        const cuisineFetches = cuisineList.map(c =>
          fetch("https://api.spoonacular.com/recipes/complexSearch?cuisine=" + encodeURIComponent(c) + "&includeIngredients=" + encodeURIComponent(ingredients) + "&number=50&addRecipeInformation=false&apiKey=" + apiKey)
            .then(r => r.json())
            .then(j => (j.results || []).map(r => ({
              id: r.id,
              title: r.title,
              image: r.image,
              usedIngredients: ingredients.split(",").map(i => ({ name: i.trim() })),
              missedIngredients: [],
              likes: 0,
              isCuisineSearch: true,
              cuisineLabel: c,
            })))
            .catch(() => [])
        );
        // If includeIngredients returns nothing, fall back to cuisine-only
        const cuisineFallbackFetches = cuisineList.map(c =>
          fetch("https://api.spoonacular.com/recipes/complexSearch?cuisine=" + encodeURIComponent(c) + "&number=50&addRecipeInformation=false&apiKey=" + apiKey)
            .then(r => r.json())
            .then(j => (j.results || []).map(r => ({
              id: r.id,
              title: r.title,
              image: r.image,
              usedIngredients: [],
              missedIngredients: [],
              likes: 0,
              isCuisineSearch: true,
              cuisineLabel: c,
            })))
            .catch(() => [])
        );'''

content = content.replace(old, new)

old = '''        const cuisineResultsArrays = await Promise.all(cuisineFetches);
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
        return Response.json(results);'''

new = '''        const [cuisineResultsArrays, cuisineFallbackArrays] = await Promise.all([
          Promise.all(cuisineFetches),
          Promise.all(cuisineFallbackFetches),
        ]);

        const seenIds = new Set();
        const results = [];

        // First add ingredient+cuisine matches
        for (const arr of cuisineResultsArrays) {
          for (const r of arr) {
            if (!seenIds.has(r.id)) {
              seenIds.add(r.id);
              results.push(r);
            }
          }
        }

        // If no ingredient matches found, use cuisine-only results
        if (results.length === 0) {
          for (const arr of cuisineFallbackArrays) {
            for (const r of arr) {
              if (!seenIds.has(r.id)) {
                seenIds.add(r.id);
                results.push(r);
              }
            }
          }
        }

        return Response.json(results);'''

content = content.replace(old, new)

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')