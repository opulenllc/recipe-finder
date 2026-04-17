with open('app/recipes/[slug]/page.tsx', encoding='utf-8') as f:
    content = f.read()

old = '<a href={"/?recipeId=" + recipe.id + "&recipeTitle=" + encodeURIComponent(recipe.title) + "&recipeImage=" + encodeURIComponent(recipe.image || "") + "&ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-500 hover:bg-orange-600 text-white font-semibold px-4 py-2 rounded-lg transition-colors text-sm">View Full Recipe</a>'

new = '<a href={"/?recipeId=" + recipe.id + "&recipeTitle=" + encodeURIComponent(recipe.title) + "&recipeImage=" + encodeURIComponent(recipe.image || "") + "&ingredients=" + data.ingredients + "&from=" + encodeURIComponent("https://www.myrecipematch.com/recipes/" + slug)} className="inline-block w-full text-center bg-orange-500 hover:bg-orange-600 text-white font-semibold px-4 py-2 rounded-lg transition-colors text-sm">View Full Recipe</a>'

content = content.replace(old, new)

with open('app/recipes/[slug]/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')