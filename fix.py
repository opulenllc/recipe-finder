with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

old = '''        // First add overlap results (ingredient + cuisine match)
        for (const r of overlap) {
          if (!seenIds.has(r.id)) {
            seenIds.add(r.id);
            results.push(r);
          }
        }

        // Then fill evenly from each cuisine
        for (const arr of cuisineResultsArrays) {
          let added = 0;
          for (const r of arr) {
            if (added >= perCuisine) break;
            if (!seenIds.has(r.id)) {
              seenIds.add(r.id);
              added++;
              results.push({
                id: r.id,
                title: r.title,
                image: r.image,
                usedIngredients: ingredients.split(",").map(i => ({ name: i.trim() })),
                missedIngredients: [],
                isCuisineSearch: true,
              });
            }
          }
        }

        // Fill any remaining from any cuisine
        for (const r of cuisineRecipes) {
          if (!seenIds.has(r.id)) {
            seenIds.add(r.id);
            results.push({
              id: r.id,
              title: r.title,
              image: r.image,
              usedIngredients: ingredients.split(",").map(i => ({ name: i.trim() })),
              missedIngredients: [],
              isCuisineSearch: true,
            });
          }
        }'''

new = '''        // First: add ingredient results that overlap with cuisine (best matches)
        for (const r of overlap) {
          if (!seenIds.has(r.id)) {
            seenIds.add(r.id);
            results.push(r);
          }
        }

        // Second: add remaining ingredient results (no cuisine match but uses ingredients)
        for (const r of ingredientResults) {
          if (!seenIds.has(r.id)) {
            seenIds.add(r.id);
            results.push(r);
          }
        }

        // Third: fill with cuisine-only results clearly marked
        for (const arr of cuisineResultsArrays) {
          for (const r of arr) {
            if (!seenIds.has(r.id)) {
              seenIds.add(r.id);
              results.push({
                id: r.id,
                title: r.title,
                image: r.image,
                usedIngredients: [],
                missedIngredients: [],
                isCuisineSearch: true,
              });
            }
          }
        }'''

content = content.replace(old, new)

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')