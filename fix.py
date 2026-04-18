with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Update handleClear to also clear cuisine
old = '  const handleClear = () => {\n    setIngredients("");\n    setRecipes([]);\n    setSearched(false);\n    setShowAll(false);\n  };'
new = '  const handleClear = () => {\n    setIngredients("");\n    setRecipes([]);\n    setSearched(false);\n    setShowAll(false);\n    setActiveCuisine(null);\n  };'
content = content.replace(old, new)

# Add cuisine badge after the mode toggle buttons and before the search box
old = '        <div className="flex gap-2 mb-2">'
new = '''        {activeCuisine && (
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
        )}
        <div className="flex gap-2 mb-2">'''
content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')