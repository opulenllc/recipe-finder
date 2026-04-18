with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Update cuisine badge to show "Also in [cuisine]" vs just cuisine name
old = '                  {recipe.isCuisineSearch && (\n                    <div className="absolute top-2 left-2 bg-blue-500 text-white text-xs font-bold px-2 py-1 rounded-full shadow capitalize">🌍 {recipe.matchedCuisine || activeCuisines[0]}</div>\n                  )}'
new = '                  {recipe.isCuisineSearch && (\n                    <div className="absolute top-2 left-2 bg-blue-500 text-white text-xs font-bold px-2 py-1 rounded-full shadow capitalize">🌍 {activeCuisines.length === 1 ? activeCuisines[0] : "Cuisine Match"}</div>\n                  )}'
content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')