with open('app/recipes/cuisine/[cuisine]/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Replace the entire component with an improved version
old = '''export default function CuisinePage({ params }: { params: { cuisine: string } }) {
  const meta = cuisineMeta[params.cuisine];
  if (!meta) return <p>Cuisine not found.</p>;

  return (
    <div className="min-h-screen bg-orange-50 flex flex-col">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <header className="bg-white shadow-sm py-5 px-6">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <a href="/" className="flex items-center gap-3">
            <span className="text-4xl">🍳</span>
            <div>
              <h1 className="text-2xl font-bold text-orange-600">My Recipe Match</h1>
              <p className="text-xs text-gray-400">Find recipes using ingredients you already have</p>
            </div>
          </a>
        </div>
      </header>
      <main className="flex-1 max-w-4xl mx-auto w-full px-4 py-10">
        <h2 className="text-3xl font-bold text-gray-800 mb-4">{meta.headline}</h2>
        <p className="text-gray-600 mb-6">{meta.description}</p>
        <div className="bg-white rounded-2xl shadow-sm p-6 mb-6">
          <h3 className="text-lg font-bold text-gray-800 mb-3">Common {meta.label} Ingredients</h3>
          <div className="flex flex-wrap gap-2">
            {meta.commonIngredients.map((ing) => (
              <a key={ing} href={"/?ingredients=" + encodeURIComponent(ing)} className="bg-orange-100 hover:bg-orange-200 text-orange-700 px-3 py-1 rounded-full text-sm font-medium">
                {ing}
              </a>
            ))}
          </div>
        </div>
        <div className="bg-white rounded-2xl shadow-sm p-6">
          <h3 className="text-lg font-bold text-gray-800 mb-3">Find {meta.label} Recipes Now</h3>
          <p className="text-gray-600 mb-4">Click any ingredient above or go back to the homepage and enter your own ingredients.</p>
          <a href="/" className="inline-block bg-orange-500 hover:bg-orange-600 text-white font-semibold px-6 py-3 rounded-xl">Search Recipes</a>
        </div>
      </main>
      <footer className="bg-white border-t border-gray-100 py-4 px-6 text-center text-sm text-gray-400">
        myrecipematch.com · Recipes by Spoonacular · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>
      </footer>
    </div>
  );
}'''

new = '''"use client";
import { useState } from "react";

export default function CuisinePage({ params }: { params: { cuisine: string } }) {
  const meta = cuisineMeta[params.cuisine];
  const [selected, setSelected] = useState<string[]>([]);

  if (!meta) return <p>Cuisine not found.</p>;

  const toggleIngredient = (ing: string) => {
    setSelected(prev =>
      prev.includes(ing) ? prev.filter(i => i !== ing) : [...prev, ing]
    );
  };

  const searchUrl = "/?ingredients=" + encodeURIComponent(selected.join(","));

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    name: meta.label + " Recipes",
    description: meta.description,
    url: "https://www.myrecipematch.com/recipes/cuisine/" + params.cuisine,
  };

  return (
    <div className="min-h-screen bg-orange-50 flex flex-col">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <header className="bg-white shadow-sm py-5 px-6">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <a href="/" className="flex items-center gap-3">
            <span className="text-4xl">🍳</span>
            <div>
              <h1 className="text-2xl font-bold text-orange-600">My Recipe Match</h1>
              <p className="text-xs text-gray-400">Find recipes using ingredients you already have</p>
            </div>
          </a>
        </div>
      </header>
      <main className="flex-1 max-w-4xl mx-auto w-full px-4 py-10">
        <h2 className="text-3xl font-bold text-gray-800 mb-4">{meta.headline}</h2>
        <p className="text-gray-600 mb-6">{meta.description}</p>
        <div className="bg-white rounded-2xl shadow-sm p-6 mb-6">
          <h3 className="text-lg font-bold text-gray-800 mb-1">Common {meta.label} Ingredients</h3>
          <p className="text-sm text-gray-400 mb-4">Select one or more ingredients then click Search</p>
          <div className="flex flex-wrap gap-2 mb-5">
            {meta.commonIngredients.map((ing) => (
              <button
                key={ing}
                onClick={() => toggleIngredient(ing)}
                className={"px-3 py-1.5 rounded-full text-sm font-medium border-2 transition-colors " + (selected.includes(ing) ? "bg-orange-500 text-white border-orange-500" : "bg-orange-50 text-orange-700 border-orange-200 hover:bg-orange-100")}
              >
                {selected.includes(ing) ? "✓ " : ""}{ing}
              </button>
            ))}
          </div>
          {selected.length > 0 && (
            <div className="flex items-center gap-3 flex-wrap">
              <p className="text-sm text-gray-500">Selected: <span className="font-medium text-orange-600">{selected.join(", ")}</span></p>
              
                href={searchUrl}
                className="bg-orange-500 hover:bg-orange-600 text-white font-semibold px-5 py-2 rounded-xl text-sm"
              >
                Search Recipes →
              </a>
              <button
                onClick={() => setSelected([])}
                className="text-sm text-gray-400 hover:text-gray-600 underline"
              >
                Clear
              </button>
            </div>
          )}
          {selected.length === 0 && (
            <p className="text-xs text-gray-400 italic">Click ingredients above to select them</p>
          )}
        </div>
        <div className="bg-white rounded-2xl shadow-sm p-6">
          <h3 className="text-lg font-bold text-gray-800 mb-3">Or Search With Your Own Ingredients</h3>
          <p className="text-gray-600 mb-4">Enter any ingredients you have at home and instantly find matching recipes.</p>
          <a href="/" className="inline-block bg-orange-500 hover:bg-orange-600 text-white font-semibold px-6 py-3 rounded-xl">Go to Recipe Search</a>
        </div>
      </main>
      <footer className="bg-white border-t border-gray-100 py-4 px-6 text-center text-sm text-gray-400">
        myrecipematch.com · Recipes by Spoonacular · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>
      </footer>
    </div>
  );
}'''

content = content.replace(old, new)

with open('app/recipes/cuisine/[cuisine]/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done! Replaced:', old[:50] in open('app/recipes/cuisine/[cuisine]/page.tsx', encoding='utf-8').read())