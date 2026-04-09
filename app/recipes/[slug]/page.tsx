import { Metadata } from "next";

const slugData: Record<string, { title: string; heading: string; intro: string; ingredients: string; keywords: string[] }> = {
  "chicken-and-rice": {
    title: "Recipes with Chicken and Rice",
    heading: "Easy Recipes with Chicken and Rice",
    intro: "Have chicken and rice at home? You are already halfway to a delicious meal. From classic chicken fried rice to hearty casseroles, these recipes use simple ingredients you likely already have in your kitchen.",
    ingredients: "chicken,rice",
    keywords: ["recipes with chicken and rice", "easy chicken and rice recipe", "simple chicken and rice recipes", "quick and easy chicken and rice recipes"],
  },
  "chicken-and-broccoli": {
    title: "Recipes with Chicken and Broccoli",
    heading: "Easy Recipes with Chicken and Broccoli",
    intro: "Chicken and broccoli make one of the most popular ingredient combinations in the kitchen. Whether you are looking for a stir fry, casserole, or baked dish, these recipes have you covered.",
    ingredients: "chicken,broccoli",
    keywords: ["recipes with chicken and broccoli", "chicken broccoli recipes", "easy chicken and broccoli dinner"],
  },
  "chicken-breast-and-rice": {
    title: "Chicken Breast and Rice Recipes",
    heading: "Easy Chicken Breast and Rice Recipes",
    intro: "Chicken breast and rice is a healthy, protein-packed combination perfect for weeknight dinners. These recipes are simple, filling, and use ingredients you already have at home.",
    ingredients: "chicken breast,rice",
    keywords: ["chicken breast and rice recipes", "easy chicken breast and rice", "healthy chicken breast rice dinner"],
  },
  "eggs-and-bread": {
    title: "Recipes with Eggs and Bread",
    heading: "Easy Recipes with Eggs and Bread",
    intro: "Eggs and bread are pantry staples that can turn into so much more than toast. From French toast to savory egg dishes, discover delicious meals using just these two simple ingredients.",
    ingredients: "eggs,bread",
    keywords: ["recipes with eggs and bread", "easy egg and bread recipes", "what to make with eggs and bread"],
  },
  "ground-beef-and-pasta": {
    title: "Recipes with Ground Beef and Pasta",
    heading: "Easy Recipes with Ground Beef and Pasta",
    intro: "Ground beef and pasta are a match made in heaven. These hearty, budget-friendly recipes are perfect for feeding a family on a weeknight without spending hours in the kitchen.",
    ingredients: "ground beef,pasta",
    keywords: ["recipes with ground beef and pasta", "ground beef pasta recipes", "easy ground beef and pasta dinner"],
  },
  "potatoes-and-cheese": {
    title: "Recipes with Potatoes and Cheese",
    heading: "Easy Recipes with Potatoes and Cheese",
    intro: "Potatoes and cheese are comfort food at its finest. From cheesy baked potatoes to casseroles and soups, these recipes transform simple ingredients into satisfying meals.",
    ingredients: "potatoes,cheese",
    keywords: ["recipes with potatoes and cheese", "cheesy potato recipes", "easy potato and cheese dinner"],
  },
  "chicken-and-rice-soup": {
    title: "Chicken and Rice Soup Recipe",
    heading: "Easy Chicken and Rice Soup Recipes",
    intro: "Nothing beats a warm bowl of chicken and rice soup. It is comforting, nourishing, and incredibly easy to make with ingredients you probably already have at home.",
    ingredients: "chicken,rice",
    keywords: ["chicken and rice soup recipe", "easy chicken rice soup", "homemade chicken and rice soup"],
  },
  "chicken-stir-fry-with-rice": {
    title: "Chicken Stir Fry with Rice Recipes",
    heading: "Easy Chicken Stir Fry with Rice",
    intro: "Chicken stir fry with rice is one of the quickest and most satisfying meals you can make. Ready in under 30 minutes with simple pantry ingredients.",
    ingredients: "chicken,rice,soy sauce",
    keywords: ["chicken stir fry with rice", "easy chicken stir fry rice recipe", "quick chicken stir fry"],
  },
  "baked-chicken-and-rice": {
    title: "Baked Chicken and Rice Recipes",
    heading: "Easy Baked Chicken and Rice Recipes",
    intro: "Baked chicken and rice is the ultimate one-pan dinner. Simply combine your ingredients, pop it in the oven, and come back to a perfectly cooked meal with minimal cleanup.",
    ingredients: "chicken,rice",
    keywords: ["baked chicken and rice", "easy baked chicken rice recipe", "oven baked chicken and rice"],
  },
  "healthy-chicken-and-rice": {
    title: "Healthy Chicken and Rice Recipes",
    heading: "Healthy Chicken and Rice Recipes",
    intro: "Looking for healthy dinner ideas using chicken and rice? These nutritious, protein-packed recipes are perfect for anyone eating clean without sacrificing flavor.",
    ingredients: "chicken,rice",
    keywords: ["healthy chicken and rice recipes", "clean eating chicken rice", "low calorie chicken and rice"],
  },
};

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const data = slugData[slug];
  if (!data) return { title: "Recipes | My Recipe Match" };
  return {
    title: data.title + " - My Recipe Match",
    description: data.intro,
    keywords: data.keywords,
    alternates: { canonical: "https://www.myrecipematch.com/recipes/" + slug },
    openGraph: {
      title: data.title + " - My Recipe Match",
      description: data.intro,
      url: "https://www.myrecipematch.com/recipes/" + slug,
      type: "website",
    },
  };
}

export function generateStaticParams() {
  return Object.keys(slugData).map((slug) => ({ slug }));
}

export default async function RecipePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const data = slugData[slug];
  if (!data) return <p>Page not found.</p>;

  let recipes: any[] = [];
  try {
    const apiKey = process.env.SPOONACULAR_API_KEY;
    const res = await fetch(
      "https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + data.ingredients + "&number=6&apiKey=" + apiKey,
      { next: { revalidate: 86400 } }
    );
    recipes = await res.json();
    if (!Array.isArray(recipes)) recipes = [];
  } catch (e) {
    recipes = [];
  }

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    name: data.title,
    description: data.intro,
    url: "https://www.myrecipematch.com/recipes/" + slug,
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
        <h2 className="text-3xl font-bold text-gray-800 mb-3">{data.heading}</h2>
        <p className="text-gray-600 mb-6 leading-relaxed">{data.intro}</p>

        <div className="bg-orange-100 border border-orange-200 rounded-2xl p-5 mb-8 flex flex-col sm:flex-row items-center gap-4">
          <div className="flex-1">
            <p className="font-semibold text-orange-800 mb-1">Have different ingredients?</p>
            <p className="text-sm text-orange-700">Enter what you have and instantly find matching recipes.</p>
          </div>
          <a href="/" className="bg-orange-500 hover:bg-orange-600 text-white font-semibold px-6 py-3 rounded-xl text-sm flex-shrink-0">
            Search Your Ingredients
          </a>
        </div>

        {recipes.length > 0 ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
            {recipes.map((recipe: any) => (
              <div key={recipe.id} className="bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-lg transition-shadow flex flex-col">
                <img
                  src={recipe.image}
                  alt={recipe.title}
                  className="w-full h-48 object-cover"
                  onError={() => {}}
                />
                <div className="p-4 flex flex-col flex-1">
                  <h3 className="text-base font-bold text-gray-800 mb-2 leading-tight">{recipe.title}</h3>
                  {recipe.usedIngredients && recipe.usedIngredients.length > 0 && (
                    <p className="text-xs text-green-600 mb-1">Uses: {recipe.usedIngredients.map((i: any) => i.name).join(", ")}</p>
                  )}
                  {recipe.missedIngredients && recipe.missedIngredients.length > 0 && (
                    <p className="text-xs text-red-400 mb-3">Also needs: {recipe.missedIngredients.slice(0, 3).map((i: any) => i.name).join(", ")}</p>
                  )}
                  <div className="mt-auto">
                    <a
                      href={"/?ingredients=" + data.ingredients}
                      className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors text-sm"
                    >
                      Find Similar Recipes
                    </a>
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-12 mb-8">
            <p className="text-gray-400">No recipes found. Try searching with your own ingredients!</p>
          </div>
        )}

        <div className="bg-white rounded-2xl shadow-sm p-6 mb-6">
          <h3 className="text-lg font-bold text-gray-800 mb-2">Find More Recipes</h3>
          <p className="text-gray-600 text-sm mb-4">My Recipe Match finds recipes based on exactly what you have at home. No wasted ingredients, no extra shopping trips.</p>
          <a href="/" className="inline-block bg-orange-500 hover:bg-orange-600 text-white font-semibold px-6 py-3 rounded-xl">
            Try My Recipe Match Free
          </a>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
          <p className="col-span-full text-sm font-semibold text-gray-500 mb-1">Browse more recipes:</p>
          {Object.entries(slugData).filter(([s]) => s !== slug).slice(0, 6).map(([s, d]) => (
            <a key={s} href={"/recipes/" + s} className="bg-white hover:bg-orange-50 border border-gray-100 rounded-xl px-3 py-2 text-xs text-gray-600 hover:text-orange-600 transition-colors">
              {d.title}
            </a>
          ))}
        </div>
      </main>

      <footer className="bg-white border-t border-gray-100 py-4 px-6 text-center text-sm text-gray-400">
        myrecipematch.com · Recipes by Spoonacular · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>
      </footer>
    </div>
  );
}
