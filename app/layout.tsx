import type { Metadata } from "next";
import { Geist } from "next/font/google";
import "./globals.css";
import Script from "next/script";

const geist = Geist({ subsets: ["latin"] });

export const metadata: Metadata = {
  metadataBase: new URL("https://www.myrecipematch.com"),
  title: {
    default: "My Recipe Match - Find Recipes From Ingredients You Have",
    template: "%s | My Recipe Match",
  },
  description: "Type in the ingredients you have on hand and instantly find recipes you can make right now. Thousands of recipes across every cuisine - powered by Spoonacular.",
  keywords: ["recipes by ingredients", "what can I make with", "ingredient search recipes", "use up leftovers recipes", "recipes from ingredients I have", "cook with what you have", "leftover ingredient recipes", "meal ideas from pantry"],
  robots: { index: true, follow: true },
  alternates: { canonical: "https://www.myrecipematch.com" },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <script
          async
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3869654865137233"
          crossOrigin="anonymous"
        />
      </head>
      <body className={geist.className}>
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-TNPMQSS9L2"
          strategy="afterInteractive"
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-TNPMQSS9L2');
          `}
        </Script>
        {children}
      </body>
    </html>
  );
}
