"use client";
import { useState, useEffect } from "react";
import { useSearchParams } from "next/navigation";
import { Suspense } from "react";

function NutritionBar({ label, amount, unit, max, color }: { label: string; amount: number; unit: string; max: number; color: string }) {
  const pct = Math.min(100, Math.round((amount / max) * 100));
  return (
    <div className="mb-2">
      <div className="flex justify-between text-xs mb-0.5">
        <span className="text-gray-600">{label}</span>
        <span className="text-gray-500 font-medium">{Math.round(amount)}{unit}</span>
      </div>
      <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
        <div className={"h-full rounded-full " + color} style={{ width: pct + "%" }}></div>
      </div>
    </div>
  );
}

function SkeletonBlock({ className }: { className: string }) {
  return <div className={"animate-pulse bg-gray-100 rounded-lg " + className}></div>;
}

function RecipeModal({ recipe, onClose }: { recipe: any; onClose: () => void }) {
  const [info, setInfo] = useState<any>(null);
  const [instructions, setInstructions] = useState<any[]>([]);
  const [infoLoading, setInfoLoading] = useState(true);
  const [instrLoading, setInstrLoading] = useState(true);

  useEffect(() => {
    fetch("/api/recipes?id=" + recipe.id + "&type=info")
      .then(r => r.json())
      .then(d => { setInfo(d); setInfoLoading(false); })
      .catch(() => setInfoLoading(false));

    fetch("/api/recipes?id=" + recipe.id + "&type=instructions")
      .then(r => r.json())
      .then(d => { setInstructions(Array.isArray(d) ? d : []); setInstrLoading(false); })
      .catch(() => setInstrLoading(false));
  }, [recipe.id]);

  const nutrients = info?.nutrition?.nutrients || [];
  const cal = nutrients.find((n: any) => n.name === "Calories");
  const protein = nutrients.find((n: any) => n.name === "Protein");
  const fat = nutrients.find((n: any) => n.name === "Fat");
  const carbs = nutrients.find((n: any) => n.name === "Carbohydrates");
  const fiber = nutrients.find((n: any) => n.name === "Fiber");
  const sugar = nutrients.find((n: any) => n.name === "Sugar");
  const sodium = nutrients.find((n: any) => n.name === "Sodium");
  const vitC = nutrients.find((n: any) => n.name === "Vitamin C");
  const calcium = nutrients.find((n: any) => n.name === "Calcium");
  const iron = nutrients.find((n: any) => n.name === "Iron");
  const steps = instructions.length > 0 ? instructions[0].steps || [] : [];
  const equipment = steps.flatMap((s: any) => s.equipment || []).filter((e: any, i: number, arr: any[]) => arr.findIndex((x: any) => x.name === e.name) === i);
  const highResImage = recipe.image ? recipe.image.replace("312x231", "636x393") : null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 print:relative print:inset-auto print:p-0" style={{backgroundColor: "rgba(0,0,0,0.5)"}}>
      <div className="bg-white rounded-2xl w-full max-w-2xl flex flex-col print:rounded-none" style={{maxHeight: "90vh"}}>

        <div className="print:hidden flex items-center justify-between px-5 py-3 border-b border-gray-100 flex-shrink-0">
          <h2 className="text-sm font-bold text-gray-800 pr-4 leading-tight">{recipe.title}</h2>
          <div className="flex gap-2 flex-shrink-0">
            <button onClick={() => window.print()} className="bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-3 py-1.5 rounded-lg text-xs">🖨 Print</button>
            <button onClick={onClose} className="bg-gray-100 hover:bg-gray-200 text-gray-500 font-semibold px-3 py-1.5 rounded-lg text-xs">✕ Close</button>
          </div>
        </div>

        <div className="overflow-y-auto flex-1 print:overflow-visible">
          <div className="hidden print:block p-6 border-b">
            <h1 className="text-2xl font-bold text-gray-800 mb-1">{recipe.title}</h1>
            <p className="text-sm text-gray-400">myrecipematch.com</p>
          </div>

          <img src={highResImage || recipe.image} alt={recipe.title} className="w-full object-cover" style={{height: "220px"}} onError={(e) => { e.currentTarget.src = recipe.image || "https://placehold.co/600x400?text=No+Image"; }} />

          <div className="p-5">
            {infoLoading ? (
              <div className="grid grid-cols-4 gap-2 mb-5">
                {[1,2,3,4].map(i => <SkeletonBlock key={i} className="h-16" />)}
              </div>
            ) : (
              <div className="grid grid-cols-4 gap-2 mb-5">
                {[
                  { label: "Ready In", val: info?.readyInMinutes ? info.readyInMinutes + " min" : null, icon: "⏱" },
                  { label: "Servings", val: info?.servings, icon: "👥" },
                  { label: "Calories", val: cal ? Math.round(cal.amount) + " kcal" : null, icon: "🔥" },
                  { label: "Cost/Serving", val: info?.pricePerServing ? "$" + (info.pricePerServing / 100).toFixed(2) : null, icon: "💰" },
                ].filter(i => i.val).map(item => (
                  <div key={item.label} className="bg-orange-50 rounded-xl p-2 text-center">
                    <div className="text-lg mb-0.5">{item.icon}</div>
                    <p className="text-xs text-gray-400">{item.label}</p>
                    <p className="text-xs font-bold text-gray-700">{item.val}</p>
                  </div>
                ))}
              </div>
            )}

            {infoLoading ? (
              <div className="flex gap-2 mb-5">
                {[1,2,3].map(i => <SkeletonBlock key={i} className="h-6 w-20" />)}
              </div>
            ) : info?.diets && info.diets.length > 0 && (
              <div className="flex flex-wrap gap-1.5 mb-5">
                {info.diets.map((diet: string) => (
                  <span key={diet} className="bg-green-100 text-green-700 text-xs font-medium px-2 py-0.5 rounded-full capitalize">{diet}</span>
                ))}
              </div>
            )}

            {infoLoading ? (
              <div className="mb-5">
                <SkeletonBlock className="h-4 w-24 mb-2" />
                <div className="space-y-1.5">
                  {[1,2,3,4].map(i => <SkeletonBlock key={i} className="h-3" />)}
                </div>
              </div>
            ) : info?.extendedIngredients && info.extendedIngredients.length > 0 && (
              <div className="mb-5">
                <h3 className="text-sm font-bold text-gray-800 mb-2">🥕 Ingredients <span className="text-xs font-normal text-gray-400">({info.extendedIngredients.length})</span></h3>
                <div className="bg-gray-50 rounded-xl p-3">
                  <div className="grid grid-cols-2 gap-x-4 gap-y-1.5">
                    {info.extendedIngredients.map((ing: any, i: number) => (
                      <div key={i} className="flex items-start gap-1.5">
                        <span className="text-orange-400 mt-0.5 flex-shrink-0">•</span>
                        <span className="text-xs text-gray-600">{ing.original}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}

            {instrLoading ? (
              <div className="mb-5">
                <SkeletonBlock className="h-4 w-24 mb-2" />
                <div className="flex gap-2">
                  {[1,2,3].map(i => <SkeletonBlock key={i} className="h-8 w-20" />)}
                </div>
              </div>
            ) : equipment.length > 0 && (
              <div className="mb-5">
                <h3 className="text-sm font-bold text-gray-800 mb-2">🍳 Equipment</h3>
                <div className="flex flex-wrap gap-2">
                  {equipment.map((eq: any) => (
                    <div key={eq.name} className="flex items-center gap-1.5 bg-gray-50 border border-gray-200 rounded-lg px-2.5 py-1.5">
                      {eq.image && <img src={"https://spoonacular.com/cdn/equipment_100x100/" + eq.image} alt={eq.name} className="w-5 h-5 object-contain" onError={(e) => { e.currentTarget.style.display = "none"; }} />}
                      <span className="text-xs text-gray-600 capitalize">{eq.name}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {instrLoading ? (
              <div className="mb-5">
                <SkeletonBlock className="h-4 w-24 mb-3" />
                <div className="space-y-3">
                  {[1,2,3,4].map(i => (
                    <div key={i} className="flex gap-3">
                      <SkeletonBlock className="w-6 h-6 rounded-full flex-shrink-0" />
                      <SkeletonBlock className="h-4 flex-1" />
                    </div>
                  ))}
                </div>
              </div>
            ) : steps.length > 0 && (
              <div className="mb-5">
                <h3 className="text-sm font-bold text-gray-800 mb-2">📋 Instructions</h3>
                <ol className="space-y-3">
                  {steps.map((step: any) => (
                    <li key={step.number} className="flex gap-3">
                      <span className="bg-orange-500 text-white text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center flex-shrink-0 mt-0.5">{step.number}</span>
                      <p className="text-xs text-gray-600 leading-relaxed pt-0.5">{step.step}</p>
                    </li>
                  ))}
                </ol>
              </div>
            )}

            {infoLoading ? (
              <div className="mb-5">
                <SkeletonBlock className="h-4 w-32 mb-3" />
                <div className="grid grid-cols-3 gap-2 mb-3">
                  {[1,2,3].map(i => <SkeletonBlock key={i} className="h-20" />)}
                </div>
                <div className="space-y-2">
                  {[1,2,3,4].map(i => <SkeletonBlock key={i} className="h-4" />)}
                </div>
              </div>
            ) : (protein || fat || carbs) && (
              <div className="mb-4">
                <h3 className="text-sm font-bold text-gray-800 mb-3">📊 Nutrition per serving</h3>
                <div className="grid grid-cols-3 gap-2 mb-3">
                  {[
                    { label: "Protein", n: protein, color: "bg-blue-400" },
                    { label: "Fat", n: fat, color: "bg-yellow-400" },
                    { label: "Carbs", n: carbs, color: "bg-orange-400" },
                  ].filter(x => x.n).map(x => (
                    <div key={x.label} className="text-center bg-gray-50 rounded-xl p-3">
                      <div className={"w-8 h-8 rounded-full mx-auto mb-1 " + x.color}></div>
                      <p className="text-xs font-bold text-gray-700">{Math.round(x.n.amount)}{x.n.unit}</p>
                      <p className="text-xs text-gray-400">{x.label}</p>
                    </div>
                  ))}
                </div>
                <div className="bg-gray-50 rounded-xl p-3 space-y-2">
                  {cal && <NutritionBar label="Calories" amount={cal.amount} unit=" kcal" max={2000} color="bg-red-400" />}
                  {protein && <NutritionBar label="Protein" amount={protein.amount} unit="g" max={50} color="bg-blue-400" />}
                  {fat && <NutritionBar label="Fat" amount={fat.amount} unit="g" max={65} color="bg-yellow-400" />}
                  {carbs && <NutritionBar label="Carbohydrates" amount={carbs.amount} unit="g" max={300} color="bg-orange-400" />}
                  {fiber && <NutritionBar label="Fiber" amount={fiber.amount} unit="g" max={25} color="bg-green-400" />}
                  {sugar && <NutritionBar label="Sugar" amount={sugar.amount} unit="g" max={50} color="bg-pink-400" />}
                  {sodium && <NutritionBar label="Sodium" amount={sodium.amount} unit="mg" max={2300} color="bg-purple-400" />}
                  {vitC && <NutritionBar label="Vitamin C" amount={vitC.amount} unit="mg" max={90} color="bg-teal-400" />}
                  {calcium && <NutritionBar label="Calcium" amount={calcium.amount} unit="mg" max={1000} color="bg-indigo-400" />}
                  {iron && <NutritionBar label="Iron" amount={iron.amount} unit="mg" max={18} color="bg-gray-400" />}
                </div>
              </div>
            )}

            <p className="text-xs text-gray-300 text-center print:hidden">Recipe data by Spoonacular</p>
          </div>
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
    if (Array.isArray(data)) {
      setRecipes(data);
      data.slice(0, 3).forEach((r: any) => {
        fetch("/api/recipes?id=" + r.id + "&type=info").catch(() => {});
        fetch("/api/recipes?id=" + r.id + "&type=instructions").catch(() => {});
      });
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
        <RecipeModal recipe={selectedRecipe} onClose={() => setSelectedRecipe(null)} />
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
                    <button onClick={() => setSelectedRecipe(recipe)} className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors">
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
