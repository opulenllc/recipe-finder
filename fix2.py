for filepath in [
    'app/recipes/[slug]/page.tsx',
    'app/recipes/cuisine/[cuisine]/client.tsx',
]:
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    content = content.replace(
        'myrecipematch.com · Recipes by Spoonacular · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>',
        'myrecipematch.com · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>'
    )
    content = content.replace(
        'Recipe data by Spoonacular · myrecipematch.com',
        'myrecipematch.com'
    )
    content = content.replace(
        'Recipe data by Spoonacular',
        ''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(filepath + ' done!')