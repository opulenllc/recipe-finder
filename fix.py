with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Replace single cuisine state with multi-cuisine array
old = '  const [activeCuisine, setActiveCuisine] = useState<string | null>(null);'
new = '  const [activeCuisines, setActiveCuisines] = useState<string[]>([]);'
content = content.replace(old, new)

# Update where cuisine param is read from URL
old = '    const cuisineParam = searchParams.get("cuisine");\n    if (cuisineParam) setActiveCuisine(cuisineParam);'
new = '    const cuisineParam = searchParams.get("cuisine");\n    if (cuisineParam) setActiveCuisines([cuisineParam]);'
content = content.replace(old, new)

# Update fetch to use cuisines array
old = '      : "/api/recipes?ingredients=" + searchTerm + (activeCuisine ? "&cuisine=" + activeCuisine : "");'
new = '      : "/api/recipes?ingredients=" + searchTerm + (activeCuisines.length > 0 ? "&cuisine=" + activeCuisines.join(",") : "");'
content = content.replace(old, new)

# Update results count badge
old = '            {filteredRecipes.length === 0 ? "No matches found" : "Found " + filteredRecipes.length + " recipe" + (filteredRecipes.length === 1 ? "" : "s") + (activeCuisine ? " · " + activeCuisine.charAt(0).toUpperCase() + activeCuisine.slice(1) + " cuisine" : "")}'
new = '            {filteredRecipes.length === 0 ? "No matches found" : "Found " + filteredRecipes.length + " recipe" + (filteredRecipes.length === 1 ? "" : "s") + (activeCuisines.length > 0 ? " · " + activeCuisines.map(c => c.charAt(0).toUpperCase() + c.slice(1)).join(", ") : "")}'
content = content.replace(old, new)

# Update handleClear
old = '    setActiveCuisine(null);'
new = '    setActiveCuisines([]);'
content = content.replace(old, new)

# Replace cuisine badge section with new multi-cuisine selector
old = '''        {activeCuisine && (
          <div className="flex items-center gap-2 mb-3 bg-orange-100 border border-orange-200 rounded-xl px-4 py-2 w-fit">
            <span className="text-sm text-orange-700 font-medium">🍽️ Filtering by: <span className="font-bold capitalize">{activeCuisine} cuisine</span></span>
            <button
              onClick={() => setActiveCuisine(null)}
              className="text-orange-400 hover:text-orange-600 font-bold text-lg leading-none ml-1"
              title="Remove cuisine filter"
            >
              ×
            </button>
          </div>
        )}'''

new = '''        <div className="mb-3">
          <div className="flex flex-wrap gap-2 items-center">
            <span className="text-xs text-gray-400 font-medium">Filter by cuisine:</span>
            {["italian","mexican","chinese","indian","japanese","thai","american","mediterranean"].map(c => (
              <button
                key={c}
                onClick={() => setActiveCuisines(prev => prev.includes(c) ? prev.filter(x => x !== c) : [...prev, c])}
                className={"text-xs font-semibold px-3 py-1 rounded-full border-2 transition-colors capitalize " + (activeCuisines.includes(c) ? "bg-orange-500 text-white border-orange-500" : "bg-white text-gray-500 border-gray-200 hover:border-orange-300 hover:text-orange-600")}
              >
                {activeCuisines.includes(c) ? "✓ " : ""}{c}
              </button>
            ))}
            {activeCuisines.length > 0 && (
              <button onClick={() => setActiveCuisines([])} className="text-xs text-gray-400 hover:text-gray-600 underline">Clear filters</button>
            )}
          </div>
        </div>'''

content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')