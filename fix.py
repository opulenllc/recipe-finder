with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Clean URL after reading params
old = '    const referrer = searchParams.get("from");\n    if (referrer) setReferrerPage(decodeURIComponent(referrer));\n    const cuisineParam = searchParams.get("cuisine");\n    if (cuisineParam) setActiveCuisines([cuisineParam]);'
new = '''    const referrer = searchParams.get("from");
    if (referrer) setReferrerPage(decodeURIComponent(referrer));
    const cuisineParam = searchParams.get("cuisine");
    if (cuisineParam) setActiveCuisines([cuisineParam]);
    // Clean URL params after reading them
    if (window.history.replaceState) {
      window.history.replaceState({}, "", "/");
    }'''
content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')