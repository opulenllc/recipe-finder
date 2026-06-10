import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "About | My Recipe Match",
  description:
    "Learn about My Recipe Match, the free ingredient-based recipe finder that helps you cook great meals with whatever's already in your kitchen.",
};

export default function AboutPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* Hero */}
      <section className="bg-orange-50 py-16 px-6 text-center">
        <p className="text-sm uppercase tracking-widest text-orange-500 font-medium mb-3">
          About Us
        </p>
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          We help you cook with what you&apos;ve got
        </h1>
        <p className="text-lg text-gray-600 max-w-2xl mx-auto leading-relaxed">
          My Recipe Match was built for real kitchens, not perfect ones. Type
          in whatever ingredients you have on hand, and we&apos;ll find recipes
          that actually work.
        </p>
      </section>

      {/* Our Story */}
      <section className="max-w-3xl mx-auto py-14 px-6">
        <p className="text-sm uppercase tracking-widest text-orange-500 font-medium mb-2">
          Our Story
        </p>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">
          Born from a near-empty fridge
        </h2>
        <p className="text-gray-600 leading-relaxed mb-4">
          We got tired of searching for recipes only to realize we were missing
          six of the ten ingredients. Every search seemed to assume you had a
          fully stocked pantry, and most of us simply don&apos;t.
        </p>
        <p className="text-gray-600 leading-relaxed mb-4">
          So we flipped the problem: instead of starting with a recipe and
          hoping you have the ingredients, you start with your ingredients and
          find what you can actually make. My Recipe Match lets you type in
          whatever is sitting in your fridge or cupboard and instantly browse
          hundreds of matching recipes, ranked by how well they fit what you
          already have.
        </p>
        <p className="text-gray-600 leading-relaxed">
          No account required. No paywalls. Just type, match, and cook.
        </p>
      </section>

      {/* How It Works */}
      <section className="bg-gray-50 py-14 px-6">
        <div className="max-w-3xl mx-auto">
          <p className="text-sm uppercase tracking-widest text-orange-500 font-medium mb-2">
            How It Works
          </p>
          <h2 className="text-2xl font-bold text-gray-900 mb-8">
            Three steps to dinner
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              {
                step: "1",
                title: "Enter your ingredients",
                desc: "Type in the ingredients you have: chicken, garlic, lemon, whatever. Separate them with commas.",
              },
              {
                step: "2",
                title: "Browse your matches",
                desc: "We search thousands of recipes and surface the best matches, clearly labeled as perfect or partial matches.",
              },
              {
                step: "3",
                title: "Cook with confidence",
                desc: "Open any recipe for full instructions, a nutrition breakdown, and a print-friendly view.",
              },
            ].map(({ step, title, desc }) => (
              <div
                key={step}
                className="bg-white rounded-xl border border-gray-200 p-6"
              >
                <div className="w-9 h-9 rounded-full bg-orange-100 text-orange-600 font-bold flex items-center justify-center mb-4 text-sm">
                  {step}
                </div>
                <h3 className="font-semibold text-gray-900 mb-2">{title}</h3>
                <p className="text-gray-500 text-sm leading-relaxed">{desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="max-w-3xl mx-auto py-14 px-6">
        <p className="text-sm uppercase tracking-widest text-orange-500 font-medium mb-2">
          Features
        </p>
        <h2 className="text-2xl font-bold text-gray-900 mb-8">
          Everything you need, nothing you don&apos;t
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {[
            {
              icon: "🔍",
              title: "Ingredient-based search",
              desc: "Find recipes by what you already have, not by what a recipe demands.",
            },
            {
              icon: "✅",
              title: "Perfect & partial match badges",
              desc: "Instantly see which recipes use all your ingredients and which need just a couple more.",
            },
            {
              icon: "🌍",
              title: "8 world cuisines",
              desc: "Filter by Italian, Mexican, Chinese, Indian, Japanese, Thai, American, or Mediterranean cooking.",
            },
            {
              icon: "📋",
              title: "Full instructions & nutrition",
              desc: "Every recipe includes step-by-step directions and a complete nutrition facts panel.",
            },
            {
              icon: "🖨️",
              title: "Print-friendly recipes",
              desc: "Print any recipe, complete with instructions, ingredients, and nutrition, all on one clean page.",
            },
            {
              icon: "🕑",
              title: "Search history",
              desc: "Your recent ingredient searches are saved so you can quickly pick up where you left off.",
            },
          ].map(({ icon, title, desc }) => (
            <div
              key={title}
              className="flex gap-4 bg-white rounded-xl border border-gray-200 p-5"
            >
              <span className="text-2xl flex-shrink-0">{icon}</span>
              <div>
                <h3 className="font-semibold text-gray-900 text-sm mb-1">
                  {title}
                </h3>
                <p className="text-gray-500 text-sm leading-relaxed">{desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* By the Numbers */}
      <section className="bg-orange-50 py-14 px-6">
        <div className="max-w-3xl mx-auto text-center">
          <p className="text-sm uppercase tracking-widest text-orange-500 font-medium mb-2">
            By the Numbers
          </p>
          <h2 className="text-2xl font-bold text-gray-900 mb-8">
            Built for home cooks everywhere
          </h2>
          <div className="grid grid-cols-3 gap-6">
            {[
              { num: "50+", label: "Ingredient guides" },
              { num: "8", label: "World cuisines" },
              { num: "1000s", label: "Recipes available" },
            ].map(({ num, label }) => (
              <div key={label}>
                <div className="text-4xl font-bold text-orange-500 mb-1">
                  {num}
                </div>
                <div className="text-sm text-gray-600">{label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Our Commitment */}
      <section className="max-w-3xl mx-auto py-14 px-6">
        <p className="text-sm uppercase tracking-widest text-orange-500 font-medium mb-2">
          Our Commitment
        </p>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">
          Free, fast, and honest
        </h2>
        <p className="text-gray-600 leading-relaxed mb-4">
          My Recipe Match is free to use and always will be. We don&apos;t hide
          recipes behind subscriptions, require you to create an account, or
          make you sit through video ads before showing you the instructions.
        </p>
        <p className="text-gray-600 leading-relaxed mb-4">
          We rely on the{" "}
          <a
            href="https://spoonacular.com/food-api"
            target="_blank"
            rel="noopener noreferrer"
            className="text-orange-500 underline hover:text-orange-600"
          >
            Spoonacular Food API
          </a>{" "}
          to power our recipe database, one of the largest and most reliable
          recipe sources on the web. That means you get accurate ingredient
          lists, nutrition data, and step-by-step instructions for every recipe
          we show.
        </p>
        <p className="text-gray-600 leading-relaxed">
          We&apos;re constantly adding new content: more ingredient combination
          guides, more cuisine filters, and better matching logic, to make My
          Recipe Match even more useful over time.
        </p>
      </section>

      {/* CTA */}
      <section className="bg-gray-900 py-14 px-6 text-center">
        <h2 className="text-2xl font-bold text-white mb-3">
          Ready to find your next meal?
        </h2>
        <p className="text-gray-400 mb-6">
          Enter your ingredients and see what you can make in seconds.
        </p>
        <Link
          href="/"
          className="inline-block bg-orange-500 hover:bg-orange-600 text-white font-semibold px-8 py-3 rounded-full transition-colors"
        >
          Start Searching →
        </Link>
      </section>
    </main>
  );
}
