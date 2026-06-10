import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { posts } from "../posts/index";

type Props = { params: { slug: string } };

export async function generateStaticParams() {
  return posts.map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const post = posts.find((p) => p.slug === params.slug);
  if (!post) return {};
  return {
    title: post.title + " | My Recipe Match Blog",
    description: post.excerpt,
  };
}

export default function BlogPostPage({ params }: Props) {
  const post = posts.find((p) => p.slug === params.slug);
  if (!post) notFound();

  return (
    <main className="min-h-screen bg-white">
      {/* Header */}
      <section className="bg-orange-50 py-12 px-6">
        <div className="max-w-2xl mx-auto">
          <Link
            href="/blog"
            className="text-sm text-orange-500 hover:text-orange-600 font-medium mb-6 inline-block"
          >
            ← Back to Blog
          </Link>
          <div className="flex items-center gap-3 mb-4">
            <span className="text-xs text-gray-400">{post.date}</span>
            <span className="text-gray-300">·</span>
            <span className="text-xs text-gray-400">{post.readTime}</span>
          </div>
          <h1 className="text-3xl font-bold text-gray-900 leading-snug">
            {post.title}
          </h1>
        </div>
      </section>

      {/* Content */}
      <article className="max-w-2xl mx-auto px-6 py-12">
        <div
          className="prose prose-orange prose-lg max-w-none"
          dangerouslySetInnerHTML={{ __html: post.content }}
        />
      </article>

      {/* CTA */}
      <section className="max-w-2xl mx-auto px-6 pb-16">
        <div className="bg-orange-50 rounded-2xl p-8 text-center">
          <h2 className="text-xl font-bold text-gray-900 mb-2">
            Find recipes from your ingredients
          </h2>
          <p className="text-gray-500 text-sm mb-5">
            Type in what you have and instantly discover meals you can make right now.
          </p>
          <Link
            href="/"
            className="inline-block bg-orange-500 hover:bg-orange-600 text-white font-semibold px-6 py-2.5 rounded-full text-sm transition-colors"
          >
            Search Recipes →
          </Link>
        </div>
      </section>
    </main>
  );
}
