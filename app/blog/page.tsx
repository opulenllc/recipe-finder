import type { Metadata } from "next";
import Link from "next/link";
import { posts } from "./posts/index";

export const metadata: Metadata = {
  title: "Blog | My Recipe Match",
  description:
    "Cooking tips, pantry guides, and meal ideas from My Recipe Match. Learn how to cook great meals with whatever ingredients you already have at home.",
};


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
          Practical cooking tips, pantry guides, and meal ideas, all focused
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
