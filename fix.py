with open('app/api/recipes/route.js', encoding='utf-8') as f:
    content = f.read()

# Increase API fetch to max Spoonacular allows (100)
content = content.replace(
    '"&number=20&addRecipeInformation=false&apiKey=" + apiKey)',
    '"&number=100&addRecipeInformation=false&apiKey=" + apiKey)'
)

# Remove perCuisine limit
content = content.replace(
    '        const perCuisine = 20;',
    '        const perCuisine = 999;'
)

# Also increase ingredient fetch
content = content.replace(
    '"?ingredients=" + encodeURIComponent(ingredients) + "&number=20&apiKey=" + apiKey)',
    '"?ingredients=" + encodeURIComponent(ingredients) + "&number=100&apiKey=" + apiKey)'
)

with open('app/api/recipes/route.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')