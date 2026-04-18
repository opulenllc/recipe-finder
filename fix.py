with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

# Remove the totalResults limit - return everything
old = '        const totalResults = Math.min(9 * cuisineList.length, 27);\n        const perCuisine = Math.max(3, Math.floor(totalResults / cuisineList.length));'
new = '        const perCuisine = 20;'
content = content.replace(old, new)

old = '        if (results.length >= totalResults) break;\n          if (!seenIds.has(r.id)) {\n            seenIds.add(r.id);\n            results.push(r);\n          }\n        }\n\n        // Then fill evenly from each cuisine\n        for (const arr of cuisineResultsArrays) {\n          let added = 0;\n          for (const r of arr) {\n            if (results.length >= totalResults) break;\n            if (added >= perCuisine) break;'
new = '        if (!seenIds.has(r.id)) {\n            seenIds.add(r.id);\n            results.push(r);\n          }\n        }\n\n        // Then fill evenly from each cuisine\n        for (const arr of cuisineResultsArrays) {\n          let added = 0;\n          for (const r of arr) {\n            if (added >= perCuisine) break;'
content = content.replace(old, new)

old = '        // If still not enough, fill remaining slots from any cuisine\n        for (const r of cuisineRecipes) {\n          if (results.length >= totalResults) break;'
new = '        // Fill any remaining from any cuisine\n        for (const r of cuisineRecipes) {'
content = content.replace(old, new)

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')