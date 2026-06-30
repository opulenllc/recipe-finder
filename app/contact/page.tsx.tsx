"use client";
import { useState } from "react";
import Link from "next/link";

export default function ContactPage() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [status, setStatus] = useState<"idle" | "sending" | "success" | "error">("idle");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus("sending");

    try {
      const res = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, message }),
      });

      if (res.ok) {
        setStatus("success");
        setName("");
        setEmail("");
        setMessage("");
      } else {
        setStatus("error");
      }
    } catch {
      setStatus("error");
    }
  };

  return (
    <main className="min-h-screen bg-white">
      {/* Hero */}
      <section className="bg-orange-50 py-14 px-6 text-center">
        <p className="text-sm uppercase tracking-widest text-orange-500 font-medium mb-3">
          Contact Us
        </p>
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Get in touch
        </h1>
        <p className="text-lg text-gray-600 max-w-xl mx-auto leading-relaxed">
          Have a suggestion, found a bug, or just want to say hi? Send us a
          message and we will get back to you as soon as we can.
        </p>
      </section>

      {/* Form */}
      <section className="max-w-xl mx-auto py-14 px-6">
        {status === "success" ? (
          <div className="text-center py-12">
            <div className="text-5xl mb-4">✅</div>
            <h2 className="text-2xl font-bold text-gray-900 mb-2">
              Message sent!
            </h2>
            <p className="text-gray-500 mb-6">
              Thanks for reaching out. We will get back to you shortly.
            </p>
            <Link
              href="/"
              className="inline-block bg-orange-500 hover:bg-orange-600 text-white font-semibold px-6 py-2.5 rounded-full text-sm transition-colors"
            >
              Back to Home
            </Link>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label
                htmlFor="name"
                className="block text-sm font-medium text-gray-700 mb-1"
              >
                Your name
              </label>
              <input
                id="name"
                type="text"
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Jane Smith"
                className="w-full border-2 border-gray-200 focus:border-orange-400 rounded-xl px-4 py-3 text-sm outline-none transition-colors"
              />
            </div>

            <div>
              <label
                htmlFor="email"
                className="block text-sm font-medium text-gray-700 mb-1"
              >
                Your email
              </label>
              <input
                id="email"
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="jane@example.com"
                className="w-full border-2 border-gray-200 focus:border-orange-400 rounded-xl px-4 py-3 text-sm outline-none transition-colors"
              />
            </div>

            <div>
              <label
                htmlFor="message"
                className="block text-sm font-medium text-gray-700 mb-1"
              >
                Message
              </label>
              <textarea
                id="message"
                required
                rows={6}
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Tell us what's on your mind..."
                className="w-full border-2 border-gray-200 focus:border-orange-400 rounded-xl px-4 py-3 text-sm outline-none transition-colors resize-none"
              />
            </div>

            {status === "error" && (
              <p className="text-red-500 text-sm">
                Something went wrong. Please try again.
              </p>
            )}

            <button
              type="submit"
              disabled={status === "sending"}
              className="w-full bg-orange-500 hover:bg-orange-600 disabled:bg-orange-300 text-white font-semibold py-3 rounded-xl transition-colors text-sm"
            >
              {status === "sending" ? "Sending..." : "Send Message"}
            </button>
          </form>
        )}
      </section>

      {/* Bottom links */}
      <section className="border-t border-gray-100 py-10 px-6">
        <div className="max-w-xl mx-auto grid grid-cols-1 sm:grid-cols-3 gap-6 text-center">
          {[
            { icon: "🏠", label: "Homepage", href: "/" },
            { icon: "📖", label: "About Us", href: "/about" },
            { icon: "🔒", label: "Privacy Policy", href: "/privacy" },
          ].map(({ icon, label, href }) => (
            <Link
              key={href}
              href={href}
              className="flex flex-col items-center gap-2 text-gray-400 hover:text-orange-500 transition-colors"
            >
              <span className="text-2xl">{icon}</span>
              <span className="text-sm font-medium">{label}</span>
            </Link>
          ))}
        </div>
      </section>
    </main>
  );
}
