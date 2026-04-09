import os

os.makedirs("app/recipes/[slug]", exist_ok=True)

page = """import { Metadata } from "next";

const slugData: Record<string, { title: string; heading: string; intro: string; ingredients: string; keywords: string[] }> = {
  "chicken-and-rice": {
    title: "Recipes with Chicken and Rice",
    heading: "Easy Recipes with Chicken and Rice",
    intro: "Have chicken and rice at home? You are already halfway to a delicious meal. From classic chicken fried rice to hearty casseroles, these recipes use simple ingredients you likely already have in your kitchen.",
    ingredients: "chicken,rice",
    keywords: ["recipes with chicken and rice", "easy chicken and rice recipe", "simple chicken and rice recipes"],
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
  "chicken-and-pasta": {
    title: "Recipes with Chicken and Pasta",
    heading: "Easy Recipes with Chicken and Pasta",
    intro: "Chicken and pasta is a classic combination that never gets old. From creamy alfredo to light lemon pasta, these recipes are quick, satisfying, and perfect for busy weeknights.",
    ingredients: "chicken,pasta",
    keywords: ["recipes with chicken and pasta", "easy chicken pasta recipes", "quick chicken and pasta dinner"],
  },
  "eggs-and-cheese": {
    title: "Recipes with Eggs and Cheese",
    heading: "Easy Recipes with Eggs and Cheese",
    intro: "Eggs and cheese are a dream team in the kitchen. Whether you are making a quick omelette, frittata, or baked egg dish, these recipes are simple, delicious, and ready in minutes.",
    ingredients: "eggs,cheese",
    keywords: ["recipes with eggs and cheese", "easy egg and cheese recipes", "what to make with eggs and cheese"],
  },
  "ground-beef-and-rice": {
    title: "Recipes with Ground Beef and Rice",
    heading: "Easy Recipes with Ground Beef and Rice",
    intro: "Ground beef and rice make a budget-friendly, filling meal that the whole family will love. These easy recipes come together quickly with ingredients you already have on hand.",
    ingredients: "ground beef,rice",
    keywords: ["recipes with ground beef and rice", "ground beef rice recipes", "easy ground beef and rice dinner"],
  },
  "chicken-and-potatoes": {
    title: "Recipes with Chicken and Potatoes",
    heading: "Easy Recipes with Chicken and Potatoes",
    intro: "Chicken and potatoes is the ultimate comfort food combination. Roasted, baked, or in a hearty stew, these recipes are simple, satisfying, and perfect for any night of the week.",
    ingredients: "chicken,potatoes",
    keywords: ["recipes with chicken and potatoes", "chicken and potato recipes", "easy chicken potatoes dinner"],
  },
  "tuna-and-pasta": {
    title: "Recipes with Tuna and Pasta",
    heading: "Easy Recipes with Tuna and Pasta",
    intro: "Tuna and pasta is a quick, budget-friendly meal that comes together in under 20 minutes. Stock your pantry with these two ingredients and you are always one step away from a great meal.",
    ingredients: "tuna,pasta",
    keywords: ["recipes with tuna and pasta", "tuna pasta recipes", "easy tuna and pasta dinner"],
  },
  "beef-and-broccoli": {
    title: "Beef and Broccoli Recipes",
    heading: "Easy Beef and Broccoli Recipes",
    intro: "Beef and broccoli is a takeout favorite you can easily make at home. These recipes are quick, flavorful, and use simple ingredients you likely already have in your kitchen.",
    ingredients: "beef,broccoli",
    keywords: ["beef and broccoli recipes", "easy beef broccoli stir fry", "homemade beef and broccoli"],
  },
  "shrimp-and-rice": {
    title: "Recipes with Shrimp and Rice",
    heading: "Easy Recipes with Shrimp and Rice",
    intro: "Shrimp and rice is a light, flavorful combination perfect for a quick weeknight dinner. From fried rice to shrimp bowls, these recipes are ready in 30 minutes or less.",
    ingredients: "shrimp,rice",
    keywords: ["recipes with shrimp and rice", "shrimp rice recipes", "easy shrimp and rice dinner"],
  },
  "pork-and-potatoes": {
    title: "Recipes with Pork and Potatoes",
    heading: "Easy Recipes with Pork and Potatoes",
    intro: "Pork and potatoes are a hearty, satisfying combination that works for any meal. From roasted pork chops to stews and casseroles, these recipes are simple and delicious.",
    ingredients: "pork,potatoes",
    keywords: ["recipes with pork and potatoes", "pork and potato recipes", "easy pork potatoes dinner"],
  },
  "salmon-and-rice": {
    title: "Recipes with Salmon and Rice",
    heading: "Easy Recipes with Salmon and Rice",
    intro: "Salmon and rice is a healthy, protein-rich meal that is as easy to make as it is delicious. These recipes are perfect for a nutritious weeknight dinner the whole family will enjoy.",
    ingredients: "salmon,rice",
    keywords: ["recipes with salmon and rice", "salmon rice recipes", "easy salmon and rice dinner"],
  },
  "chicken-and-mushrooms": {
    title: "Recipes with Chicken and Mushrooms",
    heading: "Easy Recipes with Chicken and Mushrooms",
    intro: "Chicken and mushrooms are a classic flavor pairing that works in so many dishes. From creamy pasta to savory stir fries, these recipes are simple and incredibly satisfying.",
    ingredients: "chicken,mushrooms",
    keywords: ["recipes with chicken and mushrooms", "chicken mushroom recipes", "easy chicken and mushroom dinner"],
  },
  "eggs-and-potatoes": {
    title: "Recipes with Eggs and Potatoes",
    heading: "Easy Recipes with Eggs and Potatoes",
    intro: "Eggs and potatoes are the ultimate budget-friendly combination. From breakfast hash to frittatas and casseroles, these recipes are hearty, filling, and incredibly easy to make.",
    ingredients: "eggs,potatoes",
    keywords: ["recipes with eggs and potatoes", "egg and potato recipes", "easy eggs and potatoes dinner"],
  },
  "chicken-and-spinach": {
    title: "Recipes with Chicken and Spinach",
    heading: "Easy Recipes with Chicken and Spinach",
    intro: "Chicken and spinach is a healthy, nutritious combination perfect for clean eating. These recipes are light, flavorful, and come together quickly for a satisfying weeknight meal.",
    ingredients: "chicken,spinach",
    keywords: ["recipes with chicken and spinach", "chicken spinach recipes", "easy chicken and spinach dinner"],
  },
  "ground-beef-and-potatoes": {
    title: "Recipes with Ground Beef and Potatoes",
    heading: "Easy Recipes with Ground Beef and Potatoes",
    intro: "Ground beef and potatoes make a hearty, filling meal that the whole family will love. These budget-friendly recipes are simple to prepare and packed with flavor.",
    ingredients: "ground beef,potatoes",
    keywords: ["recipes with ground beef and potatoes", "ground beef potato recipes", "easy ground beef and potatoes"],
  },
  "chicken-and-tomatoes": {
    title: "Recipes with Chicken and Tomatoes",
    heading: "Easy Recipes with Chicken and Tomatoes",
    intro: "Chicken and tomatoes are a classic Mediterranean combination that works in countless dishes. From baked chicken to pasta sauces and soups, these recipes are bright, flavorful, and easy.",
    ingredients: "chicken,tomatoes",
    keywords: ["recipes with chicken and tomatoes", "chicken tomato recipes", "easy chicken and tomato dinner"],
  },
  "pasta-and-cheese": {
    title: "Recipes with Pasta and Cheese",
    heading: "Easy Recipes with Pasta and Cheese",
    intro: "Pasta and cheese is comfort food at its finest. From classic mac and cheese to baked pasta dishes, these simple recipes are crowd-pleasers that come together in no time.",
    ingredients: "pasta,cheese",
    keywords: ["recipes with pasta and cheese", "pasta cheese recipes", "easy pasta and cheese dinner"],
  },
  "chicken-and-garlic": {
    title: "Recipes with Chicken and Garlic",
    heading: "Easy Recipes with Chicken and Garlic",
    intro: "Chicken and garlic are a flavor match made in heaven. These aromatic, savory recipes transform simple ingredients into restaurant-quality meals you can make at home.",
    ingredients: "chicken,garlic",
    keywords: ["recipes with chicken and garlic", "garlic chicken recipes", "easy chicken and garlic dinner"],
  },
  "beef-and-potatoes": {
    title: "Recipes with Beef and Potatoes",
    heading: "Easy Recipes with Beef and Potatoes",
    intro: "Beef and potatoes are a timeless combination perfect for hearty, satisfying meals. From beef stew to roasted dinners, these recipes are comforting, filling, and easy to make.",
    ingredients: "beef,potatoes",
    keywords: ["recipes with beef and potatoes", "beef and potato recipes", "easy beef and potatoes dinner"],
  },
  "chicken-and-lemon": {
    title: "Recipes with Chicken and Lemon",
    heading: "Easy Recipes with Chicken and Lemon",
    intro: "Chicken and lemon is a bright, fresh combination that elevates any dish. These recipes are light, flavorful, and perfect for anyone looking for a simple but impressive weeknight meal.",
    ingredients: "chicken,lemon",
    keywords: ["recipes with chicken and lemon", "lemon chicken recipes", "easy chicken and lemon dinner"],
  },
  "pork-and-rice": {
    title: "Recipes with Pork and Rice",
    heading: "Easy Recipes with Pork and Rice",
    intro: "Pork and rice is a versatile, satisfying combination enjoyed in cuisines around the world. These easy recipes are perfect for a quick weeknight dinner with minimal ingredients.",
    ingredients: "pork,rice",
    keywords: ["recipes with pork and rice", "pork rice recipes", "easy pork and rice dinner"],
  },
  "shrimp-and-pasta": {
    title: "Recipes with Shrimp and Pasta",
    heading: "Easy Recipes with Shrimp and Pasta",
    intro: "Shrimp and pasta is an elegant yet easy combination perfect for weeknight dinners or special occasions. These recipes come together in under 30 minutes and taste like restaurant quality.",
    ingredients: "shrimp,pasta",
    keywords: ["recipes with shrimp and pasta", "shrimp pasta recipes", "easy shrimp and pasta dinner"],
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
                />
                <div className="p-4 flex flex-col flex-1">
                  <h3 className="text-base font-bold text-gray-800 mb-2 leading-tight">{recipe.title}</h3>
                  {recipe.usedIngredients && recipe.usedIngredients.length > 0 && (
                    <p className="text-xs text-green-600 mb-1">Uses: {recipe.usedIngredients.map((i: any) => i.name).join(", ")}</p>
                  )}
                  {recipe.missedIngredients && recipe.missedIngredients.length > 0 && (
                    <p className="text-xs text-red-400 mb-3">Also needs: {recipe.missedIngredients.slice(0, 3).map((i: any) => i.name).join(", ")}</p>
                  )}
                  <div className="mt-auto flex flex-col gap-2">
                    <a href={"/?recipeId=" + recipe.id + "&recipeTitle=" + encodeURIComponent(recipe.title) + "&recipeImage=" + encodeURIComponent(recipe.image || "") + "&ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-500 hover:bg-orange-600 text-white font-semibold px-4 py-2 rounded-lg transition-colors text-sm">View Full Recipe</a>
                    <a href={"/?ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors text-sm">Find Similar Recipes</a>
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
"""

with open("app/recipes/[slug]/page.tsx", "w", encoding="utf-8") as f:
    f.write(page)
print("Done!")