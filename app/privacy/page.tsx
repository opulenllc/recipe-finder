export default function PrivacyPolicy() {
  return (
    <div className="min-h-screen bg-orange-50 flex flex-col">
      <header className="bg-white shadow-sm py-5 px-6">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <a href="/" className="flex items-center gap-3">
            <span className="text-4xl">🍳</span>
            <div>
              <h1 className="text-2xl font-bold text-orange-600">My Recipe Match</h1>
              <p className="text-xs text-gray-400">Find recipes using ingredients you already have</p>
            </div>
          </a>
        </div>
      </header>

      <main className="flex-1 max-w-3xl mx-auto w-full px-4 py-10">
        <h2 className="text-3xl font-bold text-gray-800 mb-2">Privacy Policy</h2>
        <p className="text-sm text-gray-400 mb-8">Last updated: April 5, 2026</p>

        <div className="bg-white rounded-2xl shadow-sm p-8 space-y-6 text-gray-600">

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">1. Introduction</h3>
            <p>Welcome to My Recipe Match ("we", "our", or "us"). We are committed to protecting your privacy. This Privacy Policy explains how we collect, use, and safeguard information when you visit myrecipematch.com.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">2. Information We Collect</h3>
            <p>We do not require you to create an account or provide personal information to use My Recipe Match. The only information processed is the ingredients you enter into the search box, which are sent to the Spoonacular API to retrieve recipe results. We do not store your search queries.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">3. Cookies and Tracking</h3>
            <p>We may use cookies and similar tracking technologies to serve advertisements through Google AdSense. Google may use cookies to serve ads based on your prior visits to our website or other websites. You can opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" className="text-orange-500 underline">Google Ads Settings</a>.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">4. Third Party Services</h3>
            <p>We use the following third party services:</p>
            <ul className="list-disc ml-6 mt-2 space-y-1">
              <li><strong>Spoonacular API</strong> — to retrieve recipe data based on your ingredient searches</li>
              <li><strong>Google AdSense</strong> — to display advertisements</li>
              <li><strong>Vercel</strong> — to host and serve our website</li>
            </ul>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">5. Data Security</h3>
            <p>We take reasonable measures to protect your information. However, no method of transmission over the internet is 100% secure and we cannot guarantee absolute security.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">6. Children Privacy</h3>
            <p>Our service is not directed to children under 13. We do not knowingly collect personal information from children under 13.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">7. Changes to This Policy</h3>
            <p>We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new policy on this page with an updated date.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">8. Contact Us</h3>
            <p>If you have any questions about this Privacy Policy, please contact us at: <a href="mailto:privacy@myrecipematch.com" className="text-orange-500 underline">privacy@myrecipematch.com</a></p>
          </section>

        </div>
      </main>

      <footer className="bg-white border-t border-gray-100 py-4 px-6 text-center text-sm text-gray-400">
        myrecipematch.com · Recipes by Spoonacular
      </footer>
    </div>
  );
}
