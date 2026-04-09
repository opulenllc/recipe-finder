with open('app/recipes/[slug]/page.tsx', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'onError={() => {}}',
    ''
)

with open('app/recipes/[slug]/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')