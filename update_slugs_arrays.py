path_seo = "update_seo.py"
path_sitemap = "app/sitemap.ts"

new_slugs_list = [
    "chicken-and-zucchini",
    "chicken-and-sweet-potato",
    "ground-beef-and-onions",
    "shrimp-and-garlic",
    "salmon-and-potatoes",
    "pasta-and-tomatoes",
    "eggs-and-spinach",
    "chicken-and-carrots",
    "beef-and-mushrooms",
    "tuna-and-rice",
    "chicken-and-corn",
    "shrimp-and-broccoli",
    "ground-beef-and-tomatoes",
    "pasta-and-mushrooms",
    "chicken-and-beans",
    "eggs-and-mushrooms",
    "salmon-and-lemon",
    "beef-and-carrots",
    "chicken-and-avocado",
]

# --- Update update_seo.py slugs array ---
with open(path_seo, "r", encoding="utf-8") as f:
    seo_content = f.read()

old_slugs_end = '    "shrimp-and-pasta",\n  ];'
new_entries = "\n".join(f'    "{s}",' for s in new_slugs_list)
new_slugs_end = f'    "shrimp-and-pasta",\n{new_entries}\n  ];'

if old_slugs_end in seo_content:
    seo_content = seo_content.replace(old_slugs_end, new_slugs_end, 1)
    with open(path_seo, "w", encoding="utf-8") as f:
        f.write(seo_content)
    print("update_seo.py slugs array: Updated!")
else:
    print("update_seo.py slugs array: Marker not found - check manually")

# --- Update sitemap.ts slugs array ---
with open(path_sitemap, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

old_sitemap_end = '    "shrimp-and-pasta",\n  ];'
new_sitemap_entries = "\n".join(f'    "{s}",' for s in new_slugs_list)
new_sitemap_end = f'    "shrimp-and-pasta",\n{new_sitemap_entries}\n  ];'

if old_sitemap_end in sitemap_content:
    sitemap_content = sitemap_content.replace(old_sitemap_end, new_sitemap_end, 1)
    with open(path_sitemap, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("sitemap.ts slugs array: Updated!")
else:
    print("sitemap.ts slugs array: Marker not found - check manually")
