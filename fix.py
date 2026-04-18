with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

old = '''        // First: add ingredient results that overlap with cuisine (best matches)
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

new = '''        // HARD FILTER: only show recipes that match cuisine
        // First: overlap (ingredient + cuisine match) - best results
        for (const r of overlap) {
          if (!seenIds.has(r.id)) {
            seenIds.add(r.id);
            results.push(r);
          }
        }

        // Second: cuisine-only results that were not in ingredient results
        // These are cuisine matches that may use the ingredient in a different way
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