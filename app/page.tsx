"use client";
import { useState, useEffect } from "react";
import { useSearchParams } from "next/navigation";
import { Suspense } from "react";

function RecipeModal({ recipe, data, onClose }: { recipe: any; data: any; onClose: () => void }) {
  const info = data?.info || {};
  const instructions = data?.instructions || [];
  const steps = instructions.length > 0 ? instructions[0].steps || [] : [];
  const nutrients = info?.nutrition?.nutrients || [];
  const calories = nutrients.find((n: any) => n.name === "Calories");
  const protein = nutrients.find((n: any) => n.name === "Protein");
  const fat = nutrients.find((n: any) => n.name === "Fat");
  const carbs = nutrients.find((n: any) => n.name === "Carbohydrates");
  const fiber = nutrients.find((n: any) => n.name === "Fiber");
  const sugar = nutrients.find((n: any) => n.name === "Sugar");
  const sodium = nutrients.find((n: any) => n.name === "Sodium");
  const highResImage = recipe.image ? recipe.image.replace("312x231", "636x393") : null;
  const equipment = steps.flatMap((s: any) => s.equipment || []).filter((e: any, i: number, arr: any[]) => arr.findIndex((x: any) => x.name === e.name) === i);

  return (
    <div className="fixed inset-0 bg-black bg-opacity-60 z-50 flex items-center justify-center p-4 print:relative print:inset-auto print:bg-white print:p-0" onClick={(e) => { if (e.target === e.currentTarget) onClose(); }}>
      <div className="bg-white rounded-2xl w-full max-w-2xl max-h-[90vh] overflow-y-auto flex flex-col print:rounded-none print:max-h-none print:overflow-visible">
        
        <div className="print:hidden sticky top-0 bg-white z-10 flex items-center justify-between p-4 border-b border-gray-100">
          <h2 className="text-base font-bold text-gray-800 pr-4 leading-tight">{recipe.title}</h2>
          <div className="flex gap-2 flex-shrink-0">
            <button onClick={() => window.print()} className="bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-3 py-1.5 rounded-lg text-sm">Print</button>
            <button onClick={onClose} className="bg-gray-100 hover:bg-gray-200 text-gray-600 font-semibold px-3 py-1.5 rounded-lg text-sm">Close</button>
          </div>
        </div>

        <div className="hidden print:block p-6 border-b">
          <h1 className="text-2xl font-bold text-gray-800 mb-1">{recipe.title}</h1>
          <p className="text-sm text-gray-500">myrecipematch.com</p>
        </div>

        <img
          src={highResImage || recipe.image}
          alt={recipe.title}
          className="w-full h-56 object-cover print:h-40"
          onError={(e) => { e.currentTarget.src = recipe.image || "https://placehold.co/600x400?text=No+Image"; }}
        />

        <div className="p-5">
          <div className="flex flex-wrap gap-6 mb-4 pb-4 border-b border-gray-100">
            {info.readyInMinutes && <div><p className="text-xs text-gray-400">Ready In</p><p className="text-sm font-bold text-gray-700">{info.readyInMinutes} min</p></div>}
            {info.servings && <div><p className="text-xs text-gray-400">Servings</p><p className="text-sm font-bold text-gray-700">{info.servings}</p></div>}
            {calories && <div><p className="text-xs text-gray-400">Calories</p><p className="text-sm font-bold text-gray-700">{Math.round(calories.amount)} kcal</p></div>}
            {info.pricePerServing && <div><p className="text-xs text-gray-400">Cost/Serving</p><p className="text-sm font-bold text-gray-700">${(info.pricePerServing / 100).toFixed(2)}</p></div>}
          </div>

          {info.diets && info.diets.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-4">
              {info.diets.map((diet: string) => (
                <span key={diet} className="bg-green-100 text-green-700 text-xs font-semibold px-2 py-1 rounded-full capitalize">{diet}</span>
              ))}
            </div>
          )}

          {info.extendedIngredients && info.extendedIngredients.length > 0 && (
            <div className="mb-5">
              <h3 className="text-sm font-bold text-gray-800 mb-2">Ingredients</h3>
              <ul className="grid grid-cols-2 gap-x-4 gap-y-1">
                {info.extendedIngredients.map((ing: any, i: number) => (
                  <li key={i} className="flex items-start gap-1.5 text-xs text-gray-600">
                    <span className="w-1.5 h-1.5 bg-orange-400 rounded-full flex-shrink-0 mt-1"></span>
                    {ing.original}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {equipment.length > 0 && (
            <div className="mb-5">
              <h3 className="text-sm font-bold text-gray-800 mb-2">Equipment</h3>
              <div className="flex flex-wrap gap-2">
                {equipment.map((eq: any) => (
                  <span key={eq.name} className="bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded-lg capitalize">{eq.name}</span>
                ))}
              </div>
            </div>
          )}

          {steps.length > 0 && (
            <div className="mb-5">
              <h3 className="text-sm font-bold text-gray-800 mb-2">Instructions</h3>
              <ol className="space-y-3">
                {steps.map((step: any) => (
                  <li key={step.number} className="flex gap-2.5">
                    <span className="bg-orange-500 text-white text-xs font-bold rounded-full w-5 h-5 flex items-center justify-center flex-shrink-0 mt-0.5">{step.number}</span>
                    <p className="text-xs text-gray-600 leading-relaxed">{step.step}</p>
                  </li>
                ))}
              </ol>
            </div>
          )}

          {(protein || fat || carbs || fiber || sugar || sodium) && (
            <div className="mb-5 bg-gray-50 rounded-xl p-4">
              <h3 className="text-sm font-bold text-gray-800 mb-3">Nutrition per serving</h3>
              <div className="grid grid-cols-3 gap-3">
                {[
                  { label: "Protein", val: protein },
                  { label: "Fat", val: fat },
                  { label: "Carbs", val: carbs },
                  { label: "Fiber", val: fiber },
                  { label: "Sugar", val: sugar },
                  { label: "Sodium", val: sodium },
                ].filter(n => n.val).map(n => (
                  <div key={n.label} className="text-center bg-white rounded-lg p-2">
                    <p className="text-xs text-gray-400">{n.label}</p>
                    <p className="text-sm font-bold text-gray-700">{Math.round(n.val.amount)}{n.val.unit}</p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {steps.length === 0 && (
            <p className="text-xs text-gray-400 text-center py-2">No instructions available for this recipe.</p>
          )}

          <p className="text-xs text-gray-300 text-center pt-2 print:hidden">Recipe data by Spoonacular</p>
        </div>
      </div>
    </div>
  );
}

function RecipeApp() {
  const searchParams = useSearchParams();
  const [ingredients, setIngredients] = useState("");
  const [recipes, setRecipes] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [showAll, setShowAll] = useState(false);
  const [searched, setSearched] = useState(false);
  const [history, setHistory] = useState<string[]>([]);
  const [selectedRecipe, setSelectedRecipe] = useState<any | null>(null);
  const [recipeData, setRecipeData] = useState<any | null>(null);
  const [loadingRecipe, setLoadingRecipe] = useState(false);

  useEffect(() => {
    const ing = searchParams.get("ingredients");
    if (ing) {
      setIngredients(ing);
      handleSearch(ing);
    }
  }, []);

  const handleSearch = async (query?: string) => {
    const searchTerm = query || ingredients;
    if (!searchTerm.trim()) return;
    setLoading(true);
    setSearched(true);
    setShowAll(false);
    setIngredients(searchTerm);
    if (!history.includes(searchTerm)) {
      setHistory((prev) => [searchTerm, ...prev].slice(0, 5));
    }
    const res = await fetch("/api/recipes?ingredients=" + searchTerm);
    const data = await res.json();
    if (Array.isArray(data)) setRecipes(data);
    setLoading(false);
  };

  const handleViewRecipe = async (recipe: any) => {
    setSelectedRecipe(recipe);
    setRecipeData(null);
    setLoadingRecipe(true);
    try {
      const res = await fetch("/api/recipes?id=" + recipe.id);
      const data = await res.json();
      setRecipeData(data);
    } catch (e) {
      setRecipeData({});
    }
    setLoadingRecipe(false);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") handleSearch();
  };

  const handleClear = () => {
    setIngredients("");
    setRecipes([]);
    setSearched(false);
    setShowAll(false);
  };

  const inputList = ingredients.split(",").map((i) => i.trim().toLowerCase()).filter(Boolean);

  const isPerfectMatch = (recipe: any) => {
    return inputList.every((ing) =>
      recipe.usedIngredients.some((u: any) => u.name.toLowerCase().includes(ing))
    );
  };

  const filteredRecipes = showAll ? recipes : recipes.filter((recipe) => isPerfectMatch(recipe));

  return (
    <div className="min-h-screen bg-orange-50 flex flex-col">
      {selectedRecipe && (
        loadingRecipe ? (
          <div className="fixed inset-0 bg-black bg-opacity-60 z-50 flex items-center justify-center">
            <div className="w-12 h-12 border-4 border-orange-200 border-t-orange-500 rounded-full animate-spin"></div>
          </div>
        ) : (
          <RecipeModal recipe={selectedRecipe} data={recipeData} onClose={() => setSelectedRecipe(null)} />
        )
      )}

      <header className="bg-white shadow-sm py-5 px-6 print:hidden">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <span className="text-4xl">🍳</span>
          <div>
            <h1 className="text-2xl font-bold text-orange-600">My Recipe Match</h1>
            <p className="text-xs text-gray-400">Find recipes using ingredients you already have</p>
          </div>
        </div>
      </header>

      <main className="flex-1 max-w-4xl mx-auto w-full px-4 py-10 print:hidden">
        <div className="flex gap-2 mb-2">
          <div className="relative flex-1">
            <input
              type="text"
              placeholder="e.g. chicken, rice, eggs"
              className="w-full border-2 border-orange-200 p-3 rounded-xl bg-white pr-10"
              value={ingredients}
              onChange={(e) => setIngredients(e.target.value)}
              onKeyDown={handleKeyDown}
            />
            {ingredients && (
              <button onClick={handleClear} className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 text-xl font-bold">x</button>
            )}
          </div>
          <button onClick={() => handleSearch()} className="bg-orange-500 hover:bg-orange-600 text-white px-6 py-3 rounded-xl font-semibold">
            {loading ? "Searching..." : "Find Recipes"}
          </button>
        </div>

        {history.length > 0 && (
          <div className="flex flex-wrap gap-2 mb-6">
            <span className="text-xs text-gray-400 mt-1">Recent:</span>
            {history.map((item, i) => (
              <button key={i} onClick={() => handleSearch(item)} className="text-xs bg-orange-100 hover:bg-orange-200 text-orange-700 px-3 py-1 rounded-full">{item}</button>
            ))}
          </div>
        )}

        {searched && !loading && (
          <div className="flex items-center justify-between mb-4">
            <p className="text-sm text-gray-500">
              {filteredRecipes.length === 0 ? "No matches found" : "Found " + filteredRecipes.length + " recipe" + (filteredRecipes.length === 1 ? "" : "s")}
            </p>
            {recipes.length > 0 && (
              <button onClick={() => setShowAll(!showAll)} className="text-sm text-orange-600 underline">
                {showAll ? "Show exact matches only" : "Show all partial matches"}
              </button>
            )}
          </div>
        )}

        {loading && (
          <div className="flex justify-center items-center py-12">
            <div className="w-12 h-12 border-4 border-orange-200 border-t-orange-500 rounded-full animate-spin"></div>
          </div>
        )}

        {!loading && searched && filteredRecipes.length === 0 && recipes.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg mb-2">No recipes found for those ingredients.</p>
            <p className="text-gray-400 text-sm">Try different or more common ingredients.</p>
          </div>
        )}

        {!loading && searched && filteredRecipes.length === 0 && recipes.length > 0 && !showAll && (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg mb-2">No exact matches found.</p>
            <button onClick={() => setShowAll(true)} className="text-orange-600 underline text-sm">Show partial matches instead?</button>
          </div>
        )}

        {!loading && (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredRecipes.map((recipe: any) => (
              <div key={recipe.id} className="bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-lg transition-shadow flex flex-col">
                <div className="relative">
                  <img src={recipe.image} alt={recipe.title} className="w-full h-48 object-cover" onError={(e) => { e.currentTarget.src = "https://placehold.co/600x400?text=No+Image"; }} />
                  {isPerfectMatch(recipe) && (
                    <div className="absolute top-2 left-2 bg-green-500 text-white text-xs font-bold px-2 py-1 rounded-full shadow">🎯 Perfect Match</div>
                  )}
                </div>
                <div className="p-4 flex flex-col flex-1">
                  <h2 className="text-lg font-bold text-gray-800 mb-2 leading-tight">{recipe.title}</h2>
                  <p className="text-xs text-green-600 mb-1">Used: {recipe.usedIngredients.map((i: any) => i.name).join(", ")}</p>
                  {recipe.missedIngredients.length > 0 && (
                    <p className="text-xs text-red-400 mb-3">Missing: {recipe.missedIngredients.map((i: any) => i.name).join(", ")}</p>
                  )}
                  <div className="mt-auto">
                    <button onClick={() => handleViewRecipe(recipe)} className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors">
                      View Full Recipe
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>

      <footer className="bg-white border-t border-gray-100 py-4 px-6 text-center text-sm text-gray-400 print:hidden">
        myrecipematch.com · Recipes by Spoonacular · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>
      </footer>
    </div>
  );
}

export default function Home() {
  return (
    <Suspense>
      <RecipeApp />
    </Suspense>
  );
}
