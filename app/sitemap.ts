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
  ];

  return [
    { url: baseUrl, lastModified: new Date(), changeFrequency: "daily", priority: 1 },
    { url: baseUrl + "/privacy", lastModified: new Date(), changeFrequency: "monthly", priority: 0.3 },
    { url: baseUrl + "/terms", lastModified: new Date(), changeFrequency: "monthly", priority: 0.3 },
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
