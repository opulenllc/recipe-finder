with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

old = '        url = "https://api.spoonacular.com/recipes/complexSearch?includeIngredients=" + encodeURIComponent(ingredients) + "&cuisine=" + encodeURIComponent(cuisine) + "&number=9&addRecipeInformation=false&apiKey=" + apiKey;'
new = '        url = "https://api.spoonacular.com/recipes/complexSearch?includeIngredients=" + encodeURIComponent(ingredients) + "&cuisine=" + encodeURIComponent(cuisine) + "&number=9&addRecipeInformation=false&fillIngredients=true&apiKey=" + apiKey;'
content = content.replace(old, new)

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')