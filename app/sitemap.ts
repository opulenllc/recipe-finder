import { MetadataRoute } from "next";

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = "https://www.myrecipematch.com";
  const cuisines = ["italian", "mexican", "chinese", "indian", "japanese", "thai", "american", "mediterranean"];

  return [
    { url: baseUrl, lastModified: new Date(), changeFrequency: "daily", priority: 1 },
    { url: baseUrl + "/privacy", lastModified: new Date(), changeFrequency: "monthly", priority: 0.3 },
    { url: baseUrl + "/terms", lastModified: new Date(), changeFrequency: "monthly", priority: 0.3 },
    ...cuisines.map((cuisine) => ({
      url: baseUrl + "/recipes/cuisine/" + cuisine,
      lastModified: new Date(),
      changeFrequency: "weekly" as const,
      priority: 0.8,
    })),
  ];
}
