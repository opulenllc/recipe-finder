with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# When cuisines are active, show all results without perfect match filtering
old = '  const filteredRecipes = showAll || searchMode === "name"\n    ? recipes\n    : recipes.filter((recipe) => isPerfectMatch(recipe));'
new = '  const filteredRecipes = showAll || searchMode === "name" || activeCuisines.length > 0\n    ? recipes\n    : recipes.filter((recipe) => isPerfectMatch(recipe));'
content = content.replace(old, new)

# Also hide the "show exact matches only" toggle when cuisines are active
old = '            {searchMode === "ingredients" && recipes.length > 0 && ('
new = '            {searchMode === "ingredients" && recipes.length > 0 && activeCuisines.length === 0 && ('
content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')