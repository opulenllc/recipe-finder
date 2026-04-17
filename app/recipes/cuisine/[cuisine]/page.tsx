"use client";
import { useState } from "react";
import { Metadata } from "next";

type CuisineMeta = {
  label: string;
  headline: string;
  description: string;
  commonIngredients: string[];
  keywords: string[];
};

const cuisineMeta: Record<string, CuisineMeta> = {
  italian: { label: "Italian", headline: "Italian Recipes by Ingredient", description: "Enter ingredients like pasta, tomatoes, or mozzarella and find authentic Italian recipes you can cook tonight.", commonIngredients: ["pasta", "tomatoes", "garlic", "olive oil", "basil", "mozzarella", "parmesan", "onion"], keywords: ["Italian recipes by ingredient", "pasta recipes", "easy Italian dinner ideas"] },
  mexican: { label: "Mexican", headline: "Mexican Recipes by Ingredient", description: "Have chicken, beans, or tortillas on hand? Find Mexican recipes that use exactly what is in your kitchen.", commonIngredients: ["chicken", "black beans", "tortillas", "cumin", "lime", "avocado", "salsa", "cheese"], keywords: ["Mexican recipes by ingredient", "taco recipes", "easy Mexican dinner ideas"] },
  chinese: { label: "Chinese", headline: "Chinese Recipes by Ingredient", description: "Soy sauce, ginger, rice - search your pantry and find Chinese recipes ready in minutes.", commonIngredients: ["soy sauce", "ginger", "garlic", "rice", "sesame oil", "chicken", "broccoli", "eggs"], keywords: ["Chinese recipes by ingredient", "stir fry recipes", "easy Chinese dinner ideas"] },
  indian: { label: "Indian", headline: "Indian Recipes by Ingredient", description: "Got lentils, chickpeas, or spices? Discover Indian recipes that transform everyday ingredients into flavourful curries.", commonIngredients: ["lentils", "chickpeas", "cumin", "turmeric", "garam masala", "onion", "tomatoes", "garlic"], keywords: ["Indian recipes by ingredient", "curry recipes", "easy Indian dinner ideas"] },
  japanese: { label: "Japanese", headline: "Japanese Recipes by Ingredient", description: "Miso, rice, and soy sauce open up a world of Japanese cooking. Find ramen, donburi, teriyaki, and more.", commonIngredients: ["miso", "soy sauce", "rice", "dashi", "mirin", "tofu", "ginger", "sesame oil"], keywords: ["Japanese recipes by ingredient", "ramen recipes", "easy Japanese dinner ideas"] },
  thai: { label: "Thai", headline: "Thai Recipes by Ingredient", description: "Fish sauce, coconut milk, and lime leaves can take you far in Thai cooking. Find Thai recipes from your pantry.", commonIngredients: ["fish sauce", "coconut milk", "lemongrass", "lime", "chilli", "garlic", "ginger", "rice"], keywords: ["Thai recipes by ingredient", "Thai curry recipes", "easy Thai dinner ideas"] },
  american: { label: "American", headline: "American Recipes by Ingredient", description: "Ground beef, potatoes, cheese - classic American cooking starts in the pantry. Find comfort food recipes.", commonIngredients: ["ground beef", "potatoes", "cheddar cheese", "bacon", "onion", "garlic", "butter", "eggs"], keywords: ["American recipes by ingredient", "comfort food recipes", "easy American dinner ideas"] },
  mediterranean: { label: "Mediterranean", headline: "Mediterranean Recipes by Ingredient", description: "Olive oil, feta, chickpeas, and fresh vegetables define Mediterranean cooking. Find healthy vibrant dishes.", commonIngredients: ["olive oil", "feta", "chickpeas", "cucumber", "lemon", "garlic", "tomatoes", "olives"], keywords: ["Mediterranean recipes by ingredient", "Greek recipes", "easy Mediterranean dinner ideas"] },
};

const navCuisines = [
  { label: "Italian", href: "/recipes/cuisine/italian" },
  { label: "Mexican", href: "/recipes/cuisine/mexican" },
  { label: "Chinese", href: "/recipes/cuisine/chinese" },
  { label: "Indian", href: "/recipes/cuisine/indian" },
  { label: "Japanese", href: "/recipes/cuisine/japanese" },
  { label: "Thai", href: "/recipes/cuisine/thai" },
  { label: "American", href: "/recipes/cuisine/american" },
  { label: "Mediterranean", href: "/recipes/cuisine/mediterranean" },
];

const navRecipes = [
  { label: "Chicken and Rice", href: "/recipes/chicken-and-rice" },
  { label: "Chicken and Broccoli", href: "/recipes/chicken-and-broccoli" },
  { label: "Beef and Broccoli", href: "/recipes/beef-and-broccoli" },
  { label: "Shrimp and Pasta", href: "/recipes/shrimp-and-pasta" },
  { label: "Eggs and Cheese", href: "/recipes/eggs-and-cheese" },
  { label: "Ground Beef and Rice", href: "/recipes/ground-beef-and-rice" },
  { label: "Salmon and Rice", href: "/recipes/salmon-and-rice" },
  { label: "Pasta and Cheese", href: "/recipes/pasta-and-cheese" },
  { label: "Tuna and Pasta", href: "/recipes/tuna-and-pasta" },
  { label: "Chicken and Pasta", href: "/recipes/chicken-and-pasta" },
];

function NavBar() {
  const [cuisinesOpen, setCuisinesOpen] = useState(false);
  const [recipesOpen, setRecipesOpen] = useState(false);

  return (
    <nav className="bg-white border-b border-gray-100 px-6">
      <div className="max-w-4xl mx-auto flex items-center gap-1 h-10">
        <a href="/" className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors">Home</a>
        <div className="relative">
          <button onClick={() => { setCuisinesOpen(!cuisinesOpen); setRecipesOpen(false); }} className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors flex items-center gap-1">
            Cuisines <span className="text-gray-400">{cuisinesOpen ? "▲" : "▼"}</span>
          </button>
          {cuisinesOpen && (
            <div className="absolute top-full left-0 bg-white border border-gray-100 rounded-xl shadow-lg z-50 py-2 min-w-40">
              {navCuisines.map(c => (
                <a key={c.href} href={c.href} className="block px-4 py-1.5 text-xs text-gray-600 hover:text-orange-600 hover:bg-orange-50">{c.label}</a>
              ))}
            </div>
          )}
        </div>
        <div className="relative">
          <button onClick={() => { setRecipesOpen(!recipesOpen); setCuisinesOpen(false); }} className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors flex items-center gap-1">
            Recipes <span className="text-gray-400">{recipesOpen ? "▲" : "▼"}</span>
          </button>
          {recipesOpen && (
            <div className="absolute top-full left-0 bg-white border border-gray-100 rounded-xl shadow-lg z-50 py-2 min-w-48">
              {navRecipes.map(r => (
                <a key={r.href} href={r.href} className="block px-4 py-1.5 text-xs text-gray-600 hover:text-orange-600 hover:bg-orange-50">{r.label}</a>
              ))}
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}

export default function CuisinePage({ params }: { params: { cuisine: string } }) {
  const meta = cuisineMeta[params.cuisine];
  const [selected, setSelected] = useState<string[]>([]);
  const [cuisinesOpen, setCuisinesOpen] = useState(false);
  const [recipesOpen, setRecipesOpen] = useState(false);

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
      <NavBar />
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
          {selected.length > 0 ? (
            <div className="flex items-center gap-3 flex-wrap">
              <p className="text-sm text-gray-500">Selected: <span className="font-medium text-orange-600">{selected.join(", ")}</span></p>
              <a href={searchUrl} className="bg-orange-500 hover:bg-orange-600 text-white font-semibold px-5 py-2 rounded-xl text-sm">Search Recipes →</a>
              <button onClick={() => setSelected([])} className="text-sm text-gray-400 hover:text-gray-600 underline">Clear</button>
            </div>
          ) : (
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
}
