with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

old = '''      if (cuisine) {
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
      } else {'''

new = '''      if (cuisine) {
        const cuisineList = cuisine.split(",");
        const allResults = [];
        const seenIds = new Set();
        for (const c of cuisineList) {
          try {
            const res = await fetch("https://api.spoonacular.com/recipes/complexSearch?includeIngredients=" + encodeURIComponent(ingredients) + "&cuisine=" + encodeURIComponent(c.trim()) + "&number=9&addRecipeInformation=false&fillIngredients=true&apiKey=" + apiKey);
            const json = await res.json();
            for (const r of (json.results || [])) {
              if (!seenIds.has(r.id)) {
                seenIds.add(r.id);
                allResults.push({
                  id: r.id,
                  title: r.title,
                  image: r.image,
                  usedIngredients: ingredients.split(",").map(i => ({ name: i.trim() })),
                  missedIngredients: [],
                  likes: 0,
                  isCuisineSearch: true,
                  cuisine: c.trim(),
                });
              }
            }
          } catch (e) {}
        }
        cache[cacheKey] = { data: allResults, timestamp: Date.now() };
        return Response.json(allResults);
      } else {'''

content = content.replace(old, new)

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')