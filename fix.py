with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Add referrerPage state
old = '  const [searchMode, setSearchMode] = useState<"ingredients" | "name">("ingredients");'
new = '  const [searchMode, setSearchMode] = useState<"ingredients" | "name">("ingredients");\n  const [referrerPage, setReferrerPage] = useState<string | null>(null);'
content = content.replace(old, new)

# Detect referrer in useEffect
old = '    const ing = searchParams.get("ingredients");'
new = '    const referrer = searchParams.get("from");\n    if (referrer) setReferrerPage(decodeURIComponent(referrer));\n    const ing = searchParams.get("ingredients");'
content = content.replace(old, new)

# Add back button after header closing tag
old = '      <main className="flex-1 max-w-4xl mx-auto w-full px-4 py-10 print:hidden">'
new = '''      <main className="flex-1 max-w-4xl mx-auto w-full px-4 py-10 print:hidden">
        {referrerPage && (
          <a href={referrerPage} className="inline-flex items-center gap-2 text-sm text-orange-600 hover:text-orange-700 font-medium mb-4 bg-white px-4 py-2 rounded-xl shadow-sm border border-orange-100">
            ← Back to {referrerPage.split("/recipes/")[1] ? referrerPage.split("/recipes/")[1].split("-").map((w: string) => w.charAt(0).toUpperCase() + w.slice(1)).join(" ") + " Recipes" : "Recipes"}
          </a>
        )}'''
content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')