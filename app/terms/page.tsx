export default function TermsOfService() {
  return (
    <div className="min-h-screen bg-orange-50 flex flex-col">
      <header className="bg-white shadow-sm py-5 px-6">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <a href="/">
            <div className="flex items-center gap-3">
              <span className="text-4xl">🍳</span>
              <div>
                <h1 className="text-2xl font-bold text-orange-600">My Recipe Match</h1>
                <p className="text-xs text-gray-400">Find recipes using ingredients you already have</p>
              </div>
            </div>
          </a>
        </div>
      </header>

      <main className="flex-1 max-w-3xl mx-auto w-full px-4 py-10">
        <h2 className="text-3xl font-bold text-gray-800 mb-2">Terms of Service</h2>
        <p className="text-sm text-gray-400 mb-8">Last updated: April 5, 2026</p>

        <div className="bg-white rounded-2xl shadow-sm p-8 space-y-6 text-gray-600">

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">1. Acceptance of Terms</h3>
            <p>By accessing and using My Recipe Match at myrecipematch.com, you accept and agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use our service.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">2. Use of Service</h3>
            <p>My Recipe Match is a free tool that helps users find recipes based on ingredients they have available. You agree to use this service only for lawful purposes and in a way that does not infringe the rights of others.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">3. Disclaimer of Warranties</h3>
            <p>My Recipe Match is provided "as is" without any warranties of any kind, either express or implied. We do not guarantee that the service will be uninterrupted, error-free, or that recipes returned will be accurate or suitable for your dietary needs.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">4. Recipe Content</h3>
            <p>All recipe data is provided by Spoonacular. We are not responsible for the accuracy, completeness, or suitability of any recipe content. Always verify ingredients and cooking instructions before preparing any meal, especially if you have dietary restrictions or allergies.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">5. Limitation of Liability</h3>
            <p>To the fullest extent permitted by law, My Recipe Match shall not be liable for any indirect, incidental, special, consequential, or punitive damages arising from your use of the service.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">6. Third Party Links</h3>
            <p>Our service may contain links to third party websites including Spoonacular recipe pages. We are not responsible for the content or practices of any third party websites.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">7. Advertising</h3>
            <p>My Recipe Match may display advertisements served by Google AdSense. These ads are subject to Google's terms and privacy policies. We are not responsible for the content of any advertisements displayed on our site.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">8. Changes to Terms</h3>
            <p>We reserve the right to modify these Terms of Service at any time. Changes will be effective immediately upon posting to the website. Your continued use of the service after any changes constitutes your acceptance of the new terms.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">9. Governing Law</h3>
            <p>These Terms of Service shall be governed by and construed in accordance with the laws of the United States, without regard to its conflict of law provisions.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-800 mb-2">10. Contact Us</h3>
            <p>If you have any questions about these Terms of Service, please contact us at: <a href="mailto:legal@myrecipematch.com" className="text-orange-500 underline">legal@myrecipematch.com</a></p>
          </section>

        </div>
      </main>

      <footer className="bg-white border-t border-gray-100 py-4 px-6 text-center text-sm text-gray-400">
        myrecipematch.com · Recipes by Spoonacular · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>
      </footer>
    </div>
  );
}
