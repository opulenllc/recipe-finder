"use client";
import { useState, useEffect } from "react";
import { useSearchParams } from "next/navigation";
import { Suspense } from "react";

function RecipeApp() {
  const searchParams = useSearchParams();
  const [ingredients, setIngredients] = useState("");
  const [recipes, setRecipes] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [showAll, setShowAll] = useState(false);
  const [searched, setSearched] = useState(false);
  const [history, setHistory] = useState<string[]>([]);
  const [expandedId, setExpandedId] = useState<number | null>(null);

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
    setExpandedId(null);
    setIngredients(searchTerm);
    if (!history.includes(searchTerm)) {
      setHistory((prev) => [searchTerm, ...prev].slice(0, 5));
    }
    const res = await fetch("/api/recipes?ingredients=" + searchTerm);
    const data = await res.json();
    if (Array.isArray(data)) {
      setRecipes(data);
    }
    setLoading(false);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") handleSearch();
  };

  const handleClear = () => {
    setIngredients("");
    setRecipes([]);
    setSearched(false);
    setShowAll(false);
    setExpandedId(null);
  };

  const inputList = ingredients.split(",").map((i) => i.trim().toLowerCase()).filter(Boolean);

  const isPerfectMatch = (recipe: any) => {
    return inputList.every((ing) =>
      recipe.usedIngredients.some((u: any) => u.name.toLowerCase().includes(ing))
    );
  };

  const filteredRecipes = showAll ? recipes : recipes.filter((recipe) => isPerfectMatch(recipe));

  const getSteps = (recipe: any) => {
    if (recipe.analyzedInstructions && recipe.analyzedInstructions.length > 0) {
      return recipe.analyzedInstructions[0].steps || [];
    }
    return [];
  };

  return (
    <div className="min-h-screen bg-orange-50 flex flex-col">
      <header className="bg-white shadow-sm py-5 px-6">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <span className="text-4xl">🍳</span>
          <div>
            <h1 className="text-2xl font-bold text-orange-600">My Recipe Match</h1>
            <p className="text-xs text-gray-400">Find recipes using ingredients you already have</p>
          </div>
        </div>
      </header>

      <main className="flex-1 max-w-4xl mx-auto w-full px-4 py-10">
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
            {filteredRecipes.map((recipe: any) => {
              const steps = getSteps(recipe);
              const isExpanded = expandedId === recipe.id;
              return (
                <div key={recipe.id} className="bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-lg transition-shadow flex flex-col">
                  <div className="relative">
                    <img src={recipe.image} alt={recipe.title} className="w-full h-48 object-cover" onError={(e) => { e.currentTarget.src = "https://placehold.co/600x400?text=No+Image"; }} />
                    {isPerfectMatch(recipe) && (
                      <div className="absolute top-2 left-2 bg-green-500 text-white text-xs font-bold px-2 py-1 rounded-full shadow">🎯 Perfect Match</div>
                    )}
                    {recipe.readyInMinutes && (
                      <div className="absolute top-2 right-2 bg-black bg-opacity-60 text-white text-xs px-2 py-1 rounded-full">⏱ {recipe.readyInMinutes} min</div>
                    )}
                  </div>
                  <div className="p-4 flex flex-col flex-1">
                    <h2 className="text-lg font-bold text-gray-800 mb-2 leading-tight">{recipe.title}</h2>
                    {recipe.servings && (
                      <p className="text-xs text-gray-400 mb-1">Serves {recipe.servings}</p>
                    )}
                    <p className="text-xs text-green-600 mb-1">Used: {recipe.usedIngredients.map((i: any) => i.name).join(", ")}</p>
                    {recipe.missedIngredients.length > 0 && (
                      <p className="text-xs text-red-400 mb-3">Missing: {recipe.missedIngredients.map((i: any) => i.name).join(", ")}</p>
                    )}
                    <div className="mt-auto">
                      {steps.length > 0 ? (
                        <button
                          onClick={() => setExpandedId(isExpanded ? null : recipe.id)}
                          className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors"
                        >
                          {isExpanded ? "Hide Instructions" : "View Full Recipe"}
                        </button>
                      ) : recipe.sourceUrl ? (
                        <a href={recipe.sourceUrl} target="_blank" className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors">
                          View Full Recipe
                        </a>
                      ) : (
                        <a href={"https://spoonacular.com/recipes/" + recipe.title.replaceAll(" ", "-").toLowerCase() + "-" + recipe.id} target="_blank" className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors">
                          View Full Recipe
                        </a>
                      )}
                    </div>
                    {isExpanded && steps.length > 0 && (
                      <div className="mt-4 border-t border-orange-100 pt-4">
                        <h3 className="text-sm font-bold text-gray-700 mb-3">Instructions</h3>
                        <ol className="space-y-3">
                          {steps.map((step: any) => (
                            <li key={step.number} className="flex gap-2">
                              <span className="bg-orange-500 text-white text-xs font-bold rounded-full w-5 h-5 flex items-center justify-center flex-shrink-0 mt-0.5">{step.number}</span>
                              <p className="text-xs text-gray-600 leading-relaxed">{step.step}</p>
                            </li>
                          ))}
                        </ol>
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </main>

      <footer className="bg-white border-t border-gray-100 py-4 px-6 text-center text-sm text-gray-400">
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
