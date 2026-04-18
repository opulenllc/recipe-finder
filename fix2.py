with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Add visibleCount state
old = '  const [activeCuisines, setActiveCuisines] = useState<string[]>([]);'
new = '  const [activeCuisines, setActiveCuisines] = useState<string[]>([]);\n  const [visibleCount, setVisibleCount] = useState(9);'
content = content.replace(old, new)

# Reset visibleCount on new search
old = '    setShowAll(false);\n    setIngredients(searchTerm);'
new = '    setShowAll(false);\n    setVisibleCount(9);\n    setIngredients(searchTerm);'
content = content.replace(old, new)

# Slice recipes by visibleCount
old = '  const filteredRecipes = showAll || searchMode === "name" || activeCuisines.length > 0\n    ? recipes\n    : recipes.filter((recipe) => isPerfectMatch(recipe));'
new = '''  const allFilteredRecipes = showAll || searchMode === "name" || activeCuisines.length > 0
    ? recipes
    : recipes.filter((recipe) => isPerfectMatch(recipe));
  const filteredRecipes = allFilteredRecipes.slice(0, visibleCount);'''
content = content.replace(old, new)

# Update results count to show total
old = '            {filteredRecipes.length === 0 ? "No matches found" : "Found " + filteredRecipes.length + " recipe" + (filteredRecipes.length === 1 ? "" : "s") + (activeCuisines.length > 0 ? " · " + activeCuisines.map(c => c.charAt(0).toUpperCase() + c.slice(1)).join(", ") : "")}'
new = '            {allFilteredRecipes.length === 0 ? "No matches found" : "Found " + allFilteredRecipes.length + " recipe" + (allFilteredRecipes.length === 1 ? "" : "s") + (activeCuisines.length > 0 ? " · " + activeCuisines.map(c => c.charAt(0).toUpperCase() + c.slice(1)).join(", ") : "")}'
content = content.replace(old, new)

# Add Show More button after recipe grid
old = '        )}\n      </main>'
new = '''        )}
        {allFilteredRecipes.length > visibleCount && !loading && (
          <div className="flex flex-col items-center gap-2 mt-6">
            <p className="text-xs text-gray-400">Showing {visibleCount} of {allFilteredRecipes.length} recipes</p>
            <button
              onClick={() => setVisibleCount(prev => prev + 9)}
              className="bg-orange-500 hover:bg-orange-600 text-white font-semibold px-8 py-3 rounded-xl"
            >
              Show More Recipes
            </button>
          </div>
        )}
      </main>'''
content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')