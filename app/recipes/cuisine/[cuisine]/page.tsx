import { Metadata } from "next";
import CuisineClient from "./client";

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
    <CuisineClient
      cuisine={cuisine}
      label={meta.label}
      headline={meta.headline}
      description={meta.description}
      commonIngredients={meta.commonIngredients}
    />
  );
}
