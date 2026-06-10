import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Blog | My Recipe Match",
  description:
    "Cooking tips, pantry guides, and meal ideas from My Recipe Match. Learn how to cook great meals with whatever ingredients you already have at home.",
};

const posts = [
  {
    slug: "ingredient-combos-that-make-amazing-meals",
    title: "10 Ingredient Combos That Make Amazing Meals (No Recipe Needed)",
    date: "June 1, 2026",
    excerpt:
      "Some ingredient pairings are so natural they barely need a recipe. Here are 10 combinations that reliably produce delicious meals with minimal effort.",
    readTime: "6 min read",
  },
  {
    slug: "clean-out-your-fridge-before-grocery-day",
    title: "How to Clean Out Your Fridge Before Grocery Day",
    date: "May 25, 2026",
    excerpt:
      "Grocery day is coming and your fridge is a mystery. Here is a practical, stress-free approach to using up what you have before buying more.",
    readTime: "5 min read",
  },
  {
    slug: "cooking-with-what-you-have-saves-more-than-you-think",
    title: "Why Cooking With What You Have Saves More Than You Think",
    date: "May 18, 2026",
    excerpt:
      "The average household throws away hundreds of dollars of food each year. Ingredient-first cooking is one of the simplest ways to stop the waste.",
    readTime: "5 min read",
  },
  {
    slug: "pantry-staples-that-go-with-almost-everything",
    title: "The 5 Pantry Staples That Go With Almost Everything",
    date: "May 10, 2026",
    excerpt:
      "Stock these five ingredients and you will always have the foundation for a great meal, no matter what else is in your fridge.",
    readTime: "4 min read",
  },
  {
    slug: "what-to-cook-with-20-minutes-and-random-ingredients",
    title: "What to Cook When You Only Have 20 Minutes and Random Ingredients",
    date: "May 3, 2026",
    excerpt:
      "It is 6pm, you are tired, and dinner needs to happen. Here is how to turn whatever is in your kitchen into something genuinely good in under 20 minutes.",
    readTime: "5 min read",
  },
];

export default function BlogPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* Hero */}
      <section className="bg-orange-50 py-14 px-6 text-center">
        <p className="text-sm uppercase tracking-widest text-orange-500 font-medium mb-3">
          The My Recipe Match Blog
        </p>
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Cook smarter with what you have
        </h1>
        <p className="text-lg text-gray-600 max-w-xl mx-auto leading-relaxed">
          Practical cooking tips, pantry guides, and meal ideas — all focused
          on making the most of the ingredients you already own.
        </p>
      </section>

      {/* Post list */}
      <section className="max-w-3xl mx-auto py-14 px-6">
        <div className="space-y-8">
          {posts.map((post) => (
            <Link
              key={post.slug}
              href={"/blog/" + post.slug}
              className="block group"
            >
              <article className="border border-gray-200 rounded-2xl overflow-hidden hover:border-orange-300 hover:shadow-md transition-all">
                <img src={post.image} alt={post.title} className="w-full h-48 object-cover" />
                <div className="p-6">
                <div className="flex items-center gap-3 mb-3">
                  <span className="text-xs text-gray-400">{post.date}</span>
                  <span className="text-gray-300">·</span>
                  <span className="text-xs text-gray-400">{post.readTime}</span>
                </div>
                <h2 className="text-xl font-bold text-gray-900 mb-2 group-hover:text-orange-600 transition-colors leading-snug">
                  {post.title}
                </h2>
                <p className="text-gray-500 text-sm leading-relaxed">
                  {post.excerpt}
                </p>
                <span className="inline-block mt-4 text-sm font-semibold text-orange-500 group-hover:text-orange-600">
                  Read more →
                </span>
                </div>
              </article>
            </Link>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="bg-gray-900 py-12 px-6 text-center">
        <h2 className="text-2xl font-bold text-white mb-3">
          Ready to find recipes from your ingredients?
        </h2>
        <p className="text-gray-400 mb-6">
          Type in what you have and discover what you can make.
        </p>
        <Link
          href="/"
          className="inline-block bg-orange-500 hover:bg-orange-600 text-white font-semibold px-8 py-3 rounded-full transition-colors"
        >
          Search Recipes →
        </Link>
      </section>
    </main>
  );
}
