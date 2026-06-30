import { MetadataRoute } from "next";

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = "https://www.myrecipematch.com";

  const cuisines = ["italian", "mexican", "chinese", "indian", "japanese", "thai", "american", "mediterranean"];

  const slugs = [
    "chicken-and-rice",
    "chicken-and-broccoli",
    "chicken-breast-and-rice",
    "eggs-and-bread",
    "ground-beef-and-pasta",
    "potatoes-and-cheese",
    "chicken-and-rice-soup",
    "chicken-stir-fry-with-rice",
    "baked-chicken-and-rice",
    "healthy-chicken-and-rice",
    "chicken-and-pasta",
    "eggs-and-cheese",
    "ground-beef-and-rice",
    "chicken-and-potatoes",
    "tuna-and-pasta",
    "beef-and-broccoli",
    "shrimp-and-rice",
    "pork-and-potatoes",
    "salmon-and-rice",
    "chicken-and-mushrooms",
    "eggs-and-potatoes",
    "chicken-and-spinach",
    "ground-beef-and-potatoes",
    "chicken-and-tomatoes",
    "pasta-and-cheese",
    "chicken-and-garlic",
    "beef-and-potatoes",
    "chicken-and-lemon",
    "pork-and-rice",
    "shrimp-and-pasta",
    "chicken-and-zucchini",
    "chicken-and-sweet-potato",
    "ground-beef-and-onions",
    "shrimp-and-garlic",
    "salmon-and-potatoes",
    "pasta-and-tomatoes",
    "eggs-and-spinach",
    "chicken-and-carrots",
    "beef-and-mushrooms",
    "tuna-and-rice",
    "chicken-and-corn",
    "shrimp-and-broccoli",
    "ground-beef-and-tomatoes",
    "pasta-and-mushrooms",
    "chicken-and-beans",
    "eggs-and-mushrooms",
    "salmon-and-lemon",
    "beef-and-carrots",
    "chicken-and-avocado",
  ];

  const blogSlugs = [
    "ingredient-combos-that-make-amazing-meals",
    "clean-out-your-fridge-before-grocery-day",
    "cooking-with-what-you-have-saves-more-than-you-think",
    "pantry-staples-that-go-with-almost-everything",
    "what-to-cook-with-20-minutes-and-random-ingredients",
    "beginners-guide-to-cooking-chicken-without-drying-it-out",
    "how-to-turn-leftovers-into-a-completely-different-meal",
    "10-things-you-can-make-with-a-can-of-chickpeas",
    "why-meal-prepping-one-ingredient-beats-prepping-full-meals",
    "best-spice-combinations-every-home-cook-should-know",
  ];

  return [
    { url: baseUrl, lastModified: new Date(), changeFrequency: "daily", priority: 1 },
    { url: baseUrl + "/about", lastModified: new Date(), changeFrequency: "monthly" as const, priority: 0.6 },
    { url: baseUrl + "/blog", lastModified: new Date(), changeFrequency: "weekly" as const, priority: 0.7 },
    { url: baseUrl + "/privacy", lastModified: new Date(), changeFrequency: "monthly" as const, priority: 0.3 },
    { url: baseUrl + "/terms", lastModified: new Date(), changeFrequency: "monthly" as const, priority: 0.3 },
    ...blogSlugs.map((slug) => ({
      url: baseUrl + "/blog/" + slug,
      lastModified: new Date(),
      changeFrequency: "monthly" as const,
      priority: 0.6,
    })),
    ...cuisines.map((cuisine) => ({
      url: baseUrl + "/recipes/cuisine/" + cuisine,
      lastModified: new Date(),
      changeFrequency: "weekly" as const,
      priority: 0.7,
    })),
    ...slugs.map((slug) => ({
      url: baseUrl + "/recipes/" + slug,
      lastModified: new Date(),
      changeFrequency: "weekly" as const,
      priority: 0.8,
    })),
  ];
}
