"use client";
import { useState, useEffect, useRef } from "react";
import { useSearchParams } from "next/navigation";
import { Suspense } from "react";

const funMessages = [
  "Consulting the chef... 👨‍🍳",
  "Taste-testing in progress... 😋",
  "Sharpening the knives... 🔪",
  "Preheating the oven... 🔥",
  "Chopping the veggies... 🥦",
  "Checking the pantry... 🫙",
  "Asking Grandma for tips... 👵",
  "Stirring the pot... 🥄",
  "Sniffing the spices... 🌶️",
  "Tasting for seasoning... 🧂",
  "Hunting for recipes... 🗺️",
  "Whisking things up... 🥚",
  "Marinating the ideas... 🍗",
  "Reading the recipe twice... 📖",
  "Negotiating with the garlic... 🧄",
];

function FunLoader({ label }: { label?: string }) {
  const [msgIndex, setMsgIndex] = useState(Math.floor(Math.random() * funMessages.length));
  useEffect(() => {
    const interval = setInterval(() => {
      setMsgIndex((prev) => (prev + 1) % funMessages.length);
    }, 1800);
    return () => clearInterval(interval);
  }, []);
  return (
    <div className="flex flex-col items-center justify-center py-6 gap-2">
      <div className="w-7 h-7 border-orange-200 border-t-orange-500 rounded-full animate-spin" style={{borderWidth: "3px", borderStyle: "solid"}}></div>
      <p className="text-xs text-orange-500 font-medium text-center">{funMessages[msgIndex]}</p>
      {label && <p className="text-xs text-gray-400">{label}</p>}
    </div>
  );
}

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

function RecipeModal({ recipe, onClose }: { recipe: any; onClose: () => void }) {
  const [info, setInfo] = useState<any>(null);
  const [instructions, setInstructions] = useState<any[]>([]);
  const [infoLoading, setInfoLoading] = useState(true);
  const [instrLoading, setInstrLoading] = useState(true);
  const [activeTab, setActiveTab] = useState("loading");
  const firstTabSet = useRef(false);

  useEffect(() => {
    fetch("/api/recipes?id=" + recipe.id + "&type=instructions")
      .then(r => r.json())
      .then(d => {
        setInstructions(Array.isArray(d) ? d : []);
        setInstrLoading(false);
        if (!firstTabSet.current) {
          firstTabSet.current = true;
          setActiveTab("instructions");
        }
      })
      .catch(() => { setInstrLoading(false); });

    fetch("/api/recipes?id=" + recipe.id + "&type=info")
      .then(r => r.json())
      .then(d => {
        setInfo(d);
        setInfoLoading(false);
        if (!firstTabSet.current) {
          firstTabSet.current = true;
          setActiveTab("overview");
        }
      })
      .catch(() => { setInfoLoading(false); });
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

  const tabs = [
    { id: "overview", label: "Overview", loading: infoLoading },
    { id: "instructions", label: "Instructions", loading: instrLoading },
    { id: "nutrition", label: "Nutrition", loading: infoLoading },
  ];

  const handlePrint = () => {
    if (infoLoading || instrLoading) {
      alert("Please wait for all recipe data to finish loading before printing.");
      return;
    }
    window.print();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 print:relative print:inset-auto print:p-0 print:block" style={{backgroundColor: "rgba(0,0,0,0.5)"}}>
      <div className="bg-white rounded-2xl w-full max-w-2xl flex flex-col print:rounded-none print:max-w-none print:max-h-none print:w-full" style={{maxHeight: "90vh"}}>

        <div className="print:hidden flex items-center justify-between px-5 py-3 border-b border-gray-100 flex-shrink-0">
          <h2 className="text-sm font-bold text-gray-800 pr-4 leading-tight line-clamp-1">{recipe.title}</h2>
          <div className="flex gap-2 flex-shrink-0">
            <button onClick={handlePrint} className="bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-3 py-1.5 rounded-lg text-xs">🖨 Print</button>
            <button onClick={onClose} className="bg-gray-100 hover:bg-gray-200 text-gray-500 font-semibold px-3 py-1.5 rounded-lg text-xs">✕ Close</button>
          </div>
        </div>

        <div className="print:hidden flex border-b border-gray-100 flex-shrink-0">
          {tabs.map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={"flex-1 py-2.5 text-xs font-semibold transition-colors " + (activeTab === tab.id ? "text-orange-600 border-b-2 border-orange-500" : "text-gray-400 hover:text-gray-600")}
            >
              {tab.label}
              {tab.loading && <span className="ml-1 inline-block w-1.5 h-1.5 bg-orange-300 rounded-full animate-pulse"></span>}
            </button>
          ))}
        </div>

        <div className="overflow-y-auto flex-1 print:overflow-visible">
          <div className="hidden print:block p-6 border-b">
            <h1 className="text-2xl font-bold text-gray-800 mb-1">{recipe.title}</h1>
            <p className="text-sm text-gray-400">myrecipematch.com</p>
          </div>

          <img src={highResImage || recipe.image} alt={recipe.title} className="w-full object-cover print:h-48" style={{height: "200px"}} onError={(e) => { e.currentTarget.src = recipe.image || "https://placehold.co/600x400?text=No+Image"; }} />

          <div className="p-5 print:p-6">
            {activeTab === "loading" && <FunLoader label="Loading recipe..." />}

            <div className="print:hidden">
              {activeTab === "overview" && (
                <>
                  {infoLoading ? <FunLoader label="Loading recipe details..." /> : (
                    <>
                      <div className="grid grid-cols-4 gap-2 mb-4">
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
                      {info?.diets && info.diets.length > 0 && (
                        <div className="flex flex-wrap gap-1.5 mb-4">
                          {info.diets.map((diet: string) => (
                            <span key={diet} className="bg-green-100 text-green-700 text-xs font-medium px-2 py-0.5 rounded-full capitalize">{diet}</span>
                          ))}
                        </div>
                      )}
                      {info?.extendedIngredients && info.extendedIngredients.length > 0 && (
                        <div className="mb-4">
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
                      {equipment.length > 0 && (
                        <div className="mb-4">
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
                      <div className="flex gap-2 mt-2">
                        <button onClick={() => setActiveTab("instructions")} className="flex-1 bg-orange-500 hover:bg-orange-600 text-white font-semibold py-2 rounded-xl text-xs">📋 View Instructions</button>
                        <button onClick={() => setActiveTab("nutrition")} className="flex-1 bg-gray-100 hover:bg-gray-200 text-gray-600 font-semibold py-2 rounded-xl text-xs">📊 View Nutrition</button>
                      </div>
                    </>
                  )}
                </>
              )}

              {activeTab === "instructions" && (
                <>
                  {instrLoading ? <FunLoader label="Loading instructions..." /> : steps.length > 0 ? (
                    <ol className="space-y-4">
                      {steps.map((step: any) => (
                        <li key={step.number} className="flex gap-3">
                          <span className="bg-orange-500 text-white text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center flex-shrink-0 mt-0.5">{step.number}</span>
                          <p className="text-sm text-gray-600 leading-relaxed pt-0.5">{step.step}</p>
                        </li>
                      ))}
                    </ol>
                  ) : (
                    <div className="text-center py-8">
                      <p className="text-gray-400 text-sm">No instructions available for this recipe.</p>
                    </div>
                  )}
                </>
              )}

              {activeTab === "nutrition" && (
                <>
                  {infoLoading ? <FunLoader label="Calculating nutrition..." /> : (protein || fat || carbs) ? (
                    <>
                      <div className="grid grid-cols-3 gap-2 mb-4">
                        {[
                          { label: "Protein", n: protein, color: "bg-blue-400" },
                          { label: "Fat", n: fat, color: "bg-yellow-400" },
                          { label: "Carbs", n: carbs, color: "bg-orange-400" },
                        ].filter(x => x.n).map(x => (
                          <div key={x.label} className="text-center bg-gray-50 rounded-xl p-3">
                            <div className={"w-10 h-10 rounded-full mx-auto mb-2 " + x.color}></div>
                            <p className="text-sm font-bold text-gray-700">{Math.round(x.n.amount)}{x.n.unit}</p>
                            <p className="text-xs text-gray-400">{x.label}</p>
                          </div>
                        ))}
                      </div>
                      <div className="bg-gray-50 rounded-xl p-4 space-y-2.5">
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
                    </>
                  ) : (
                    <div className="text-center py-8">
                      <p className="text-gray-400 text-sm">No nutrition data available for this recipe.</p>
                    </div>
                  )}
                </>
              )}
            </div>

            <div className="hidden print:block">
              <div className="grid grid-cols-4 gap-2 mb-4">
                {[
                  { label: "Ready In", val: info?.readyInMinutes ? info.readyInMinutes + " min" : null, icon: "⏱" },
                  { label: "Servings", val: info?.servings, icon: "👥" },
                  { label: "Calories", val: cal ? Math.round(cal.amount) + " kcal" : null, icon: "🔥" },
                  { label: "Cost/Serving", val: info?.pricePerServing ? "$" + (info.pricePerServing / 100).toFixed(2) : null, icon: "💰" },
                ].filter(i => i.val).map(item => (
                  <div key={item.label} className="bg-orange-50 rounded-xl p-2 text-center">
                    <p className="text-xs text-gray-400">{item.label}</p>
                    <p className="text-xs font-bold text-gray-700">{item.val}</p>
                  </div>
                ))}
              </div>
              {info?.diets && info.diets.length > 0 && (
                <div className="flex flex-wrap gap-1.5 mb-4">
                  {info.diets.map((diet: string) => (
                    <span key={diet} className="bg-green-100 text-green-700 text-xs font-medium px-2 py-0.5 rounded-full capitalize">{diet}</span>
                  ))}
                </div>
              )}
              {info?.extendedIngredients && info.extendedIngredients.length > 0 && (
                <div className="mb-5">
                  <h3 className="text-sm font-bold text-gray-800 mb-2">Ingredients</h3>
                  <div className="grid grid-cols-2 gap-x-4 gap-y-1.5">
                    {info.extendedIngredients.map((ing: any, i: number) => (
                      <div key={i} className="flex items-start gap-1.5">
                        <span className="text-orange-400 mt-0.5 flex-shrink-0">•</span>
                        <span className="text-xs text-gray-600">{ing.original}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
              {equipment.length > 0 && (
                <div className="mb-5">
                  <h3 className="text-sm font-bold text-gray-800 mb-2">Equipment</h3>
                  <div className="flex flex-wrap gap-2">
                    {equipment.map((eq: any) => (
                      <span key={eq.name} className="text-xs text-gray-600 bg-gray-100 px-2 py-1 rounded capitalize">{eq.name}</span>
                    ))}
                  </div>
                </div>
              )}
              {steps.length > 0 && (
                <div className="mb-5">
                  <h3 className="text-sm font-bold text-gray-800 mb-3">Instructions</h3>
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
              {(protein || fat || carbs) && (
                <div className="mb-4">
                  <h3 className="text-sm font-bold text-gray-800 mb-3">Nutrition per serving</h3>
                  <div className="space-y-2">
                    {cal && <NutritionBar label="Calories" amount={cal.amount} unit=" kcal" max={2000} color="bg-red-400" />}
                    {protein && <NutritionBar label="Protein" amount={protein.amount} unit="g" max={50} color="bg-blue-400" />}
                    {fat && <NutritionBar label="Fat" amount={fat.amount} unit="g" max={65} color="bg-yellow-400" />}
                    {carbs && <NutritionBar label="Carbohydrates" amount={carbs.amount} unit="g" max={300} color="bg-orange-400" />}
                    {fiber && <NutritionBar label="Fiber" amount={fiber.amount} unit="g" max={25} color="bg-green-400" />}
                    {sugar && <NutritionBar label="Sugar" amount={sugar.amount} unit="g" max={50} color="bg-pink-400" />}
                    {sodium && <NutritionBar label="Sodium" amount={sodium.amount} unit="mg" max={2300} color="bg-purple-400" />}
                  </div>
                </div>
              )}
              <p className="text-xs text-gray-300 text-center mt-4">Recipe data by Spoonacular · myrecipematch.com</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}


function NavBar() {
  const [cuisinesOpen, setCuisinesOpen] = useState(false);
  const [recipesOpen, setRecipesOpen] = useState(false);

  const cuisines = [
    { label: "Italian", href: "/recipes/cuisine/italian" },
    { label: "Mexican", href: "/recipes/cuisine/mexican" },
    { label: "Chinese", href: "/recipes/cuisine/chinese" },
    { label: "Indian", href: "/recipes/cuisine/indian" },
    { label: "Japanese", href: "/recipes/cuisine/japanese" },
    { label: "Thai", href: "/recipes/cuisine/thai" },
    { label: "American", href: "/recipes/cuisine/american" },
    { label: "Mediterranean", href: "/recipes/cuisine/mediterranean" },
  ];

  const recipes = [
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

  return (
    <nav className="bg-white border-b border-gray-100 px-6 print:hidden">
      <div className="max-w-4xl mx-auto flex items-center gap-1 h-10">
        <a href="/" className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors">
          Home
        </a>
        <div className="relative">
          <button
            onClick={() => { setCuisinesOpen(!cuisinesOpen); setRecipesOpen(false); }}
            className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors flex items-center gap-1"
          >
            Cuisines <span className="text-gray-400">{cuisinesOpen ? "▲" : "▼"}</span>
          </button>
          {cuisinesOpen && (
            <div className="absolute top-full left-0 bg-white border border-gray-100 rounded-xl shadow-lg z-50 py-2 min-w-40">
              {cuisines.map(c => (
                <a key={c.href} href={c.href} className="block px-4 py-1.5 text-xs text-gray-600 hover:text-orange-600 hover:bg-orange-50">
                  {c.label}
                </a>
              ))}
            </div>
          )}
        </div>
        <div className="relative">
          <button
            onClick={() => { setRecipesOpen(!recipesOpen); setCuisinesOpen(false); }}
            className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors flex items-center gap-1"
          >
            Recipes <span className="text-gray-400">{recipesOpen ? "▲" : "▼"}</span>
          </button>
          {recipesOpen && (
            <div className="absolute top-full left-0 bg-white border border-gray-100 rounded-xl shadow-lg z-50 py-2 min-w-48">
              {recipes.map(r => (
                <a key={r.href} href={r.href} className="block px-4 py-1.5 text-xs text-gray-600 hover:text-orange-600 hover:bg-orange-50">
                  {r.label}
                </a>
              ))}
            </div>
          )}
        </div>
      </div>
    </nav>
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
  const [searchMode, setSearchMode] = useState<"ingredients" | "name">("ingredients");
  const [referrerPage, setReferrerPage] = useState<string | null>(null);

  useEffect(() => {
    const referrer = searchParams.get("from");
    if (referrer) setReferrerPage(decodeURIComponent(referrer));
    const ing = searchParams.get("ingredients");
    const recipeId = searchParams.get("recipeId");
    const recipeTitle = searchParams.get("recipeTitle");
    const recipeImage = searchParams.get("recipeImage");

    if (ing) {
      setIngredients(ing);
      handleSearch(ing, "ingredients").then((results: any[]) => {
        if (recipeId && results) {
          const found = results.find((r: any) => String(r.id) === String(recipeId));
          if (found) {
            setSelectedRecipe(found);
          } else if (recipeTitle) {
            setSelectedRecipe({ id: recipeId, title: decodeURIComponent(recipeTitle), image: recipeImage ? decodeURIComponent(recipeImage) : null, usedIngredients: [], missedIngredients: [] });
          }
        }
      });
    } else if (recipeId && recipeTitle) {
      setSelectedRecipe({ id: recipeId, title: decodeURIComponent(recipeTitle), image: recipeImage ? decodeURIComponent(recipeImage) : null, usedIngredients: [], missedIngredients: [] });
    }
  }, []);

  const handleSearch = async (query?: string, mode?: "ingredients" | "name"): Promise<any[]> => {
    const searchTerm = query || ingredients;
    const currentMode = mode || searchMode;
    if (!searchTerm.trim()) return [];
    setLoading(true);
    setSearched(true);
    setShowAll(false);
    setIngredients(searchTerm);
    if (!history.includes(searchTerm)) {
      setHistory((prev) => [searchTerm, ...prev].slice(0, 5));
    }

    const url = currentMode === "name"
      ? "/api/recipes?query=" + encodeURIComponent(searchTerm)
      : "/api/recipes?ingredients=" + searchTerm;

    const res = await fetch(url);
    const data = await res.json();
    if (Array.isArray(data)) {
      setRecipes(data);
      data.slice(0, 3).forEach((r: any) => {
        fetch("/api/recipes?id=" + r.id + "&type=info").catch(() => {});
        fetch("/api/recipes?id=" + r.id + "&type=instructions").catch(() => {});
      });
      setLoading(false);
      return data;
    }
    setLoading(false);
    return [];
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

  const handleModeSwitch = (mode: "ingredients" | "name") => {
    setSearchMode(mode);
    setIngredients("");
    setRecipes([]);
    setSearched(false);
    setShowAll(false);
  };

  const inputList = ingredients.split(",").map((i) => i.trim().toLowerCase()).filter(Boolean);

  const isPerfectMatch = (recipe: any) => {
    if (recipe.isNameSearch) return false;
    return inputList.every((ing) =>
      recipe.usedIngredients.some((u: any) => u.name.toLowerCase().includes(ing))
    );
  };

  const filteredRecipes = showAll || searchMode === "name"
    ? recipes
    : recipes.filter((recipe) => isPerfectMatch(recipe));

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
      <NavBar />

      <main className="flex-1 max-w-4xl mx-auto w-full px-4 py-10 print:hidden">
        {referrerPage && (
          <a href={referrerPage} className="inline-flex items-center gap-2 text-sm text-orange-600 hover:text-orange-700 font-medium mb-4 bg-white px-4 py-2 rounded-xl shadow-sm border border-orange-100">
            ← Back to {referrerPage.split("/recipes/")[1] ? referrerPage.split("/recipes/")[1].split("-").map((w: string) => w.charAt(0).toUpperCase() + w.slice(1)).join(" ") + " Recipes" : "Recipes"}
          </a>
        )}
        {referrerPage && (
          <a href={referrerPage} className="inline-flex items-center gap-2 text-sm text-orange-600 hover:text-orange-700 font-medium mb-4 bg-white px-4 py-2 rounded-xl shadow-sm border border-orange-100">
            ← Back to {referrerPage.split("/recipes/")[1] ? referrerPage.split("/recipes/")[1].split("-").map((w: string) => w.charAt(0).toUpperCase() + w.slice(1)).join(" ") + " Recipes" : "Recipes"}
          </a>
        )}

        <div className="flex gap-2 mb-3 bg-white rounded-xl p-1 border-2 border-orange-100 w-fit">
          <button
            onClick={() => handleModeSwitch("ingredients")}
            className={"px-4 py-2 rounded-lg text-sm font-semibold transition-colors " + (searchMode === "ingredients" ? "bg-orange-500 text-white" : "text-gray-400 hover:text-gray-600")}
          >
            🥕 By Ingredients
          </button>
          <button
            onClick={() => handleModeSwitch("name")}
            className={"px-4 py-2 rounded-lg text-sm font-semibold transition-colors " + (searchMode === "name" ? "bg-orange-500 text-white" : "text-gray-400 hover:text-gray-600")}
          >
            🍽️ By Recipe Name
          </button>
        </div>

        <div className="flex gap-2 mb-2">
          <div className="relative flex-1">
            <input
              type="text"
              placeholder={searchMode === "ingredients" ? "e.g. chicken, rice, eggs" : "e.g. chicken parmesan, beef tacos..."}
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

        {searchMode === "ingredients" && (
          <p className="text-xs text-gray-400 mb-4">Separate ingredients with commas</p>
        )}

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
            {searchMode === "ingredients" && recipes.length > 0 && (
              <button onClick={() => setShowAll(!showAll)} className="text-sm text-orange-600 underline">
                {showAll ? "Show exact matches only" : "Show all partial matches"}
              </button>
            )}
          </div>
        )}

        {loading && (
          <div className="flex flex-col items-center justify-center py-12">
            <FunLoader />
          </div>
        )}

        {!loading && searched && filteredRecipes.length === 0 && recipes.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg mb-2">No recipes found.</p>
            <p className="text-gray-400 text-sm">Try different {searchMode === "ingredients" ? "ingredients" : "recipe name"}.</p>
          </div>
        )}

        {!loading && searched && filteredRecipes.length === 0 && recipes.length > 0 && !showAll && searchMode === "ingredients" && (
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
                  {recipe.isNameSearch && (
                    <div className="absolute top-2 left-2 bg-orange-500 text-white text-xs font-bold px-2 py-1 rounded-full shadow">🍽️ Recipe</div>
                  )}
                </div>
                <div className="p-4 flex flex-col flex-1">
                  <h2 className="text-lg font-bold text-gray-800 mb-2 leading-tight">{recipe.title}</h2>
                  {!recipe.isNameSearch && (
                    <>
                      <p className="text-xs text-green-600 mb-1">Used: {recipe.usedIngredients.map((i: any) => i.name).join(", ")}</p>
                      {recipe.missedIngredients.length > 0 && (
                        <p className="text-xs text-red-400 mb-3">Missing: {recipe.missedIngredients.map((i: any) => i.name).join(", ")}</p>
                      )}
                    </>
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
