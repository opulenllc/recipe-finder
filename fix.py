with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'myrecipematch.com · Recipes by Spoonacular · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>',
    'myrecipematch.com · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>'
)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')