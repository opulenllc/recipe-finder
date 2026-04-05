import os

os.makedirs("app/recipes/cuisine/[cuisine]", exist_ok=True)

cuisine_page = """import { Metadata } from "next";

type CuisineMeta = {
  label: string;
  headline: string;
  description: string;
  commonIngredients: string[];
  keywords: string[];
};

const cuisineMeta: Record<string, CuisineMeta> = {
  italian: { label: "Italian", headline: "Italian Recipes by Ingredient", description: "Enter ingredients like pasta, tomatoes, or mozzarella and find authentic Italian recipes you can cook tonight.", commonIngredients: ["pasta", "tomatoes", "garlic", "olive oil", "basil"], keywords: ["Italian recipes by ingredient", "pasta recipes", "easy Italian dinner ideas"] },
  mexican: { label: "Mexican", headline: "Mexican Recipes by Ingredient", description: "Have chicken, beans, or tortillas on hand? Find Mexican recipes that use exactly what is in your kitchen.", commonIngredients: ["chicken", "black beans", "tortillas", "cumin", "lime"], keywords: ["Mexican recipes by ingredient", "taco recipes", "easy Mexican dinner ideas"] },
  chinese: { label: "Chinese", headline: "Chinese Recipes by Ingredient", description: "Soy sauce, ginger, rice - search your pantry and find Chinese recipes ready in minutes.", commonIngredients: ["soy sauce", "ginger", "garlic", "rice", "sesame oil"], keywords: ["Chinese recipes by ingredient", "stir fry recipes", "easy Chinese dinner ideas"] },
  indian: { label: "Indian", headline: "Indian Recipes by Ingredient", description: "Got lentils, chickpeas, or spices? Discover Indian recipes that transform everyday ingredients into flavourful curries.", commonIngredients: ["lentils", "chickpeas", "cumin", "turmeric", "garam masala"], keywords: ["Indian recipes by ingredient", "curry recipes", "easy Indian dinner ideas"] },
  japanese: { label: "Japanese", headline: "Japanese Recipes by Ingredient", description: "Miso, rice, and soy sauce open up a world of Japanese cooking. Find ramen, donburi, teriyaki, and more.", commonIngredients: ["miso", "soy sauce", "rice", "dashi", "mirin"], keywords: ["Japanese recipes by ingredient", "ramen recipes", "easy Japanese dinner ideas"] },
  thai: { label: "Thai", headline: "Thai Recipes by Ingredient", description: "Fish sauce, coconut milk, and lime leaves can take you far in Thai cooking. Find Thai recipes from your pantry.", commonIngredients: ["fish sauce", "coconut milk", "lemongrass", "lime", "chilli"], keywords: ["Thai recipes by ingredient", "Thai curry recipes", "easy Thai dinner ideas"] },
  american: { label: "American", headline: "American Recipes by Ingredient", description: "Ground beef, potatoes, cheese - classic American cooking starts in the pantry. Find comfort food recipes.", commonIngredients: ["ground beef", "potatoes", "cheddar cheese", "bacon", "onion"], keywords: ["American recipes by ingredient", "comfort food recipes", "easy American dinner ideas"] },
  mediterranean: { label: "Mediterranean", headline: "Mediterranean Recipes by Ingredient", description: "Olive oil, feta, chickpeas, and fresh vegetables define Mediterranean cooking. Find healthy vibrant dishes.", commonIngredients: ["olive oil", "feta", "chickpeas", "cucumber", "lemon"], keywords: ["Mediterranean recipes by ingredient", "Greek recipes", "easy Mediterranean dinner ideas"] },
};

export async function generateMetadata({ params }: { params: Promise<{ cuisine: string }> }): Promise<Metadata> {
  const { cuisine } = await params;
  const meta = cuisineMeta[cuisine];
  if (!meta) return { title: "Cuisine Recipes | My Recipe Match" };
  return {
    title: meta.headline + " - My Recipe Match",
    description: meta.description,
    keywords: meta.keywords,
    alternates: { canonical: "https://www.myrecipematch.com/recipes/cuisine/" + cuisine },
  };
}

export function generateStaticParams() {
  return ["italian","mexican","chinese","indian","japanese","thai","american","mediterranean"].map((c) => ({ cuisine: c }));
}

export default async function CuisinePage({ params }: { params: Promise<{ cuisine: string }> }) {
  const { cuisine } = await params;
  const meta = cuisineMeta[cuisine];
  if (!meta) return <p>Cuisine not found.</p>;

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
}
"""

with open("app/recipes/cuisine/[cuisine]/page.tsx", "w", encoding="utf-8") as f:
    f.write(cuisine_page)
print("cuisine page done!")
print("All done!")
