with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Add cuisine state
old = '  const [referrerPage, setReferrerPage] = useState<string | null>(null);'
new = '  const [referrerPage, setReferrerPage] = useState<string | null>(null);\n  const [activeCuisine, setActiveCuisine] = useState<string | null>(null);'
content = content.replace(old, new)

# Read cuisine from URL params
old = '    const referrer = searchParams.get("from");\n    if (referrer) setReferrerPage(decodeURIComponent(referrer));'
new = '    const referrer = searchParams.get("from");\n    if (referrer) setReferrerPage(decodeURIComponent(referrer));\n    const cuisineParam = searchParams.get("cuisine");\n    if (cuisineParam) setActiveCuisine(cuisineParam);'
content = content.replace(old, new)

# Pass cuisine to fetch
old = '    const url = currentMode === "name"\n      ? "/api/recipes?query=" + encodeURIComponent(searchTerm)\n      : "/api/recipes?ingredients=" + searchTerm;'
new = '    const url = currentMode === "name"\n      ? "/api/recipes?query=" + encodeURIComponent(searchTerm)\n      : "/api/recipes?ingredients=" + searchTerm + (activeCuisine ? "&cuisine=" + activeCuisine : "");'
content = content.replace(old, new)

# Show cuisine badge near search results count
old = '            {filteredRecipes.length === 0 ? "No matches found" : "Found " + filteredRecipes.length + " recipe" + (filteredRecipes.length === 1 ? "" : "s")}'
new = '            {filteredRecipes.length === 0 ? "No matches found" : "Found " + filteredRecipes.length + " recipe" + (filteredRecipes.length === 1 ? "" : "s") + (activeCuisine ? " · " + activeCuisine.charAt(0).toUpperCase() + activeCuisine.slice(1) + " cuisine" : "")}'
content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')