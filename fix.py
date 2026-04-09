with open('app/recipes/[slug]/page.tsx', encoding='utf-8') as f:
    content = f.read()

old = '''                <img
                  src={recipe.image}
                  alt={recipe.title}
                  className="w-full h-48 object-cover"
                  onError={() => {}}
                />'''

new = '''                <img
                  src={recipe.image}
                  alt={recipe.title}
                  className="w-full h-48 object-cover"
                />'''

content = content.replace(old, new)

with open('app/recipes/[slug]/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')