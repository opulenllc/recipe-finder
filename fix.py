with open('app/recipes/[slug]/page.tsx', encoding='utf-8') as f:
    content = f.read()

old = '''                  <div className="mt-auto flex flex-col gap-2">
                    <a href={"/?recipeId=" + recipe.id + "&ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-500 hover:bg-orange-600 text-white font-semibold px-4 py-2 rounded-lg transition-colors text-sm">View Full Recipe</a>
                    <a href={"/?ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors text-sm">Find Similar Recipes</a>
                  </div>'''

new = '''                  <div className="mt-auto flex flex-col gap-2">
                    <a href={"/?recipeId=" + recipe.id + "&recipeTitle=" + encodeURIComponent(recipe.title) + "&recipeImage=" + encodeURIComponent(recipe.image || "") + "&ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-500 hover:bg-orange-600 text-white font-semibold px-4 py-2 rounded-lg transition-colors text-sm">View Full Recipe</a>
                    <a href={"/?ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors text-sm">Find Similar Recipes</a>
                  </div>'''

content = content.replace(old, new)

with open('app/recipes/[slug]/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')