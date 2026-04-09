with open('app/recipes/[slug]/page.tsx', encoding='utf-8') as f:
    lines = f.readlines()

lines[170] = '                  <div className="mt-auto flex flex-col gap-2">\n'
lines[171] = '                    <a href={"/?recipeId=" + recipe.id + "&recipeTitle=" + encodeURIComponent(recipe.title) + "&recipeImage=" + encodeURIComponent(recipe.image || "") + "&ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-500 hover:bg-orange-600 text-white font-semibold px-4 py-2 rounded-lg transition-colors text-sm">View Full Recipe</a>\n'
lines[172] = '                    <a href={"/?ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors text-sm">Find Similar Recipes</a>\n'
lines[173] = '                  </div>\n'
lines[174] = '                </div>\n'
lines[175] = '              </div>\n'
lines[176] = '            ))}\n'
lines[177] = '          </div>\n'
lines[178] = '        ) : (\n'
lines[179] = '          <div className="text-center py-12 mb-8">\n'
lines[180] = '            <p className="text-gray-400">No recipes found. Try searching with your own ingredients!</p>\n'
lines[181] = '          </div>\n'
lines[182] = '        )}\n'

del lines[183]
del lines[183]
del lines[183]
del lines[183]

with open('app/recipes/[slug]/page.tsx', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Done!')