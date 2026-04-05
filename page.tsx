"use client";
import { useState } from "react";

interface Ingredient {
  name: string;
}

interface Recipe {
  id: number;
  title: string;
  image: string;
  usedIngredients: Ingredient[];
}

export default function Home() {
  const [ingredients, setIngredients] = useState("");
  const [recipes, setRecipes] = useState<Recipe[]>([]);

  const handleSearch = async () => {
    const res = await fetch("/api/recipes?ingredients=" + ingredients);
    const data = await res.json();
    setRecipes(data);
  };

  return (
    <main className="min-h-screen p-6 bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Recipe Finder</h1>
      <input
        type="text"
        placeholder="Enter ingredients e.g. chicken rice eggs"
        className="border p-2 w-full mb-4 rounded"
        value={ingredients}
        onChange={(e) => setIngredients(e.target.value)}
      />
      <button
        onClick={handleSearch}
        className="bg-black text-white px-4 py-2 rounded mb-6"
      >
        Find Recipes
      </button>
      <div className="grid gap-4">
        {recipes.map((recipe) => (
          <div key={recipe.id} className="bg-white p-4 rounded shadow">
            <h2 className="text-xl font-semibold">{recipe.title}</h2>
            <img
              src={recipe.image}
              alt={recipe.title}
              className="w-full h-48 object-cover my-2 rounded"
            />
            <p className="text-sm">
              Ingredients: {recipe.usedIngredients.map((i) => i.name).join(", ")}
            </p>
            
              href={"https://spoonacular.com/recipes/" + recipe.title.replaceAll(" ", "-").toLowerCase() + "-" + recipe.id}
              target="_blank"
              className="text-blue-600 underline mt-2 block"
            >
              View Recipe
            </a>
          </div>
        ))}
      </div>
    </main>
  );
}
