"use client";
import { useState } from "react";

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
  { label: "Chicken Breast and Rice", href: "/recipes/chicken-breast-and-rice" },
  { label: "Chicken and Pasta", href: "/recipes/chicken-and-pasta" },
  { label: "Chicken and Potatoes", href: "/recipes/chicken-and-potatoes" },
  { label: "Chicken and Mushrooms", href: "/recipes/chicken-and-mushrooms" },
  { label: "Chicken and Spinach", href: "/recipes/chicken-and-spinach" },
  { label: "Chicken and Tomatoes", href: "/recipes/chicken-and-tomatoes" },
  { label: "Chicken and Garlic", href: "/recipes/chicken-and-garlic" },
  { label: "Chicken and Lemon", href: "/recipes/chicken-and-lemon" },
  { label: "Beef and Broccoli", href: "/recipes/beef-and-broccoli" },
  { label: "Beef and Potatoes", href: "/recipes/beef-and-potatoes" },
  { label: "Ground Beef and Pasta", href: "/recipes/ground-beef-and-pasta" },
  { label: "Ground Beef and Rice", href: "/recipes/ground-beef-and-rice" },
  { label: "Ground Beef and Potatoes", href: "/recipes/ground-beef-and-potatoes" },
  { label: "Shrimp and Rice", href: "/recipes/shrimp-and-rice" },
  { label: "Shrimp and Pasta", href: "/recipes/shrimp-and-pasta" },
  { label: "Salmon and Rice", href: "/recipes/salmon-and-rice" },
  { label: "Tuna and Pasta", href: "/recipes/tuna-and-pasta" },
  { label: "Pork and Rice", href: "/recipes/pork-and-rice" },
  { label: "Pork and Potatoes", href: "/recipes/pork-and-potatoes" },
  { label: "Eggs and Bread", href: "/recipes/eggs-and-bread" },
  { label: "Eggs and Cheese", href: "/recipes/eggs-and-cheese" },
  { label: "Eggs and Potatoes", href: "/recipes/eggs-and-potatoes" },
  { label: "Pasta and Cheese", href: "/recipes/pasta-and-cheese" },
  { label: "Potatoes and Cheese", href: "/recipes/potatoes-and-cheese" },
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
            Cuisines <span className="text-gray-400">{cuisinesOpen ? "\u25b2" : "\u25bc"}</span>
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
            Recipes <span className="text-gray-400">{recipesOpen ? "\u25b2" : "\u25bc"}</span>
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

type Props = {
  cuisine: string;
  label: string;
  headline: string;
  description: string;
  commonIngredients: string[];
};

export default function CuisineClient({ cuisine, label, headline, description, commonIngredients }: Props) {
  const [selected, setSelected] = useState<string[]>([]);

  const toggleIngredient = (ing: string) => {
    setSelected(prev =>
      prev.includes(ing) ? prev.filter(i => i !== ing) : [...prev, ing]
    );
  };

  const searchUrl = "/?ingredients=" + encodeURIComponent(selected.join(",")) + "&cuisine=" + cuisine;

  return (
    <div className="min-h-screen bg-orange-50 flex flex-col">
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
        <h2 className="text-3xl font-bold text-gray-800 mb-4">{headline}</h2>
        <p className="text-gray-600 mb-6">{description}</p>
        <div className="bg-white rounded-2xl shadow-sm p-6 mb-6">
          <h3 className="text-lg font-bold text-gray-800 mb-1">Common {label} Ingredients</h3>
          <p className="text-sm text-gray-400 mb-4">Select one or more ingredients then click Search</p>
          <div className="flex flex-wrap gap-2 mb-5">
            {commonIngredients.map((ing) => (
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
