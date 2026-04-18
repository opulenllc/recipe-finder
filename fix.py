with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

# Increase max results based on number of cuisines selected
old = '        const perCuisine = Math.max(1, Math.floor(9 / cuisineList.length));'
new = '        const totalResults = Math.min(9 * cuisineList.length, 27);\n        const perCuisine = Math.max(3, Math.floor(totalResults / cuisineList.length));'
content = content.replace(old, new)

old = '        if (results.length >= 9) break;\n          if (!seenIds.has(r.id)) {\n            seenIds.add(r.id);\n            results.push(r);\n          }\n        }\n\n        // Then fill evenly from each cuisine\n        for (const arr of cuisineResultsArrays) {\n          let added = 0;\n          for (const r of arr) {\n            if (results.length >= 9) break;\n            if (added >= perCuisine) break;'
new = '        if (results.length >= totalResults) break;\n          if (!seenIds.has(r.id)) {\n            seenIds.add(r.id);\n            results.push(r);\n          }\n        }\n\n        // Then fill evenly from each cuisine\n        for (const arr of cuisineResultsArrays) {\n          let added = 0;\n          for (const r of arr) {\n            if (results.length >= totalResults) break;\n            if (added >= perCuisine) break;'
content = content.replace(old, new)

old = '        // If still not enough, fill remaining slots from any cuisine\n        for (const r of cuisineRecipes) {\n          if (results.length >= 9) break;'
new = '        // If still not enough, fill remaining slots from any cuisine\n        for (const r of cuisineRecipes) {\n          if (results.length >= totalResults) break;'
content = content.replace(old, new)

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')