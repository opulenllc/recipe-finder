path = "app/sitemap.ts"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = "{ url: baseUrl + '/blog/what-to-cook-with-20-minutes-and-random-ingredients', lastModified: new Date(), changeFrequency: 'monthly' as const, priority: 0.6 },"
new = """{ url: baseUrl + '/blog/what-to-cook-with-20-minutes-and-random-ingredients', lastModified: new Date(), changeFrequency: 'monthly' as const, priority: 0.6 },
    { url: baseUrl + '/blog/beginners-guide-to-cooking-chicken-without-drying-it-out', lastModified: new Date(), changeFrequency: 'monthly' as const, priority: 0.6 },
    { url: baseUrl + '/blog/how-to-turn-leftovers-into-a-completely-different-meal', lastModified: new Date(), changeFrequency: 'monthly' as const, priority: 0.6 },
    { url: baseUrl + '/blog/10-things-you-can-make-with-a-can-of-chickpeas', lastModified: new Date(), changeFrequency: 'monthly' as const, priority: 0.6 },
    { url: baseUrl + '/blog/why-meal-prepping-one-ingredient-beats-prepping-full-meals', lastModified: new Date(), changeFrequency: 'monthly' as const, priority: 0.6 },
    { url: baseUrl + '/blog/best-spice-combinations-every-home-cook-should-know', lastModified: new Date(), changeFrequency: 'monthly' as const, priority: 0.6 },"""

if old in content:
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Sitemap updated!")
else:
    print("Pattern not found")
