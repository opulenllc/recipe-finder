with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

old = '''      if (cuisine) {
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

new = '''      if (cuisine) {
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

content = content.replace(old, new)

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')