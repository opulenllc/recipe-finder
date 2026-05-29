with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Add a hero/landing section that shows when no search has been done yet
old = '        {loading && ('
new = '''        {!searched && !loading && (
          <div>
            <div className="text-center mb-10">
              <h2 className="text-3xl font-bold text-gray-800 mb-3">Find Recipes Using Ingredients You Already Have</h2>
              <p className="text-gray-500 max-w-xl mx-auto text-sm leading-relaxed">Stop staring at your fridge wondering what to cook. Type in whatever ingredients you have at home and instantly discover delicious recipes you can make right now — no extra shopping needed.</p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-10">
              {[
                { icon: "🥕", title: "Enter Your Ingredients", desc: "Type in whatever you have at home — chicken, rice, eggs, anything." },
                { icon: "🔍", title: "Instant Recipe Matches", desc: "We search thousands of recipes and find the best matches for your ingredients." },
                { icon: "🍳", title: "Cook With Confidence", desc: "See full instructions, nutrition info, and what ingredients you are missing." },
              ].map(item => (
                <div key={item.title} className="bg-white rounded-2xl p-5 text-center shadow-sm">
                  <div className="text-4xl mb-3">{item.icon}</div>
                  <h3 className="font-bold text-gray-800 mb-1 text-sm">{item.title}</h3>
                  <p className="text-xs text-gray-500 leading-relaxed">{item.desc}</p>
                </div>
              ))}
            </div>

            <div className="bg-white rounded-2xl shadow-sm p-6 mb-6">
              <h3 className="text-lg font-bold text-gray-800 mb-4">Popular Ingredient Combinations</h3>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                {[
                  { label: "Chicken + Rice", search: "chicken,rice" },
                  { label: "Eggs + Cheese", search: "eggs,cheese" },
                  { label: "Ground Beef + Pasta", search: "ground beef,pasta" },
                  { label: "Shrimp + Rice", search: "shrimp,rice" },
                  { label: "Chicken + Broccoli", search: "chicken,broccoli" },
                  { label: "Salmon + Rice", search: "salmon,rice" },
                  { label: "Pasta + Cheese", search: "pasta,cheese" },
                  { label: "Beef + Potatoes", search: "beef,potatoes" },
                  { label: "Chicken + Pasta", search: "chicken,pasta" },
                ].map(item => (
                  <button
                    key={item.search}
                    onClick={() => { setIngredients(item.search); handleSearch(item.search); }}
                    className="bg-orange-50 hover:bg-orange-100 text-orange-700 text-xs font-medium px-3 py-2.5 rounded-xl text-left transition-colors border border-orange-100"
                  >
                    🍽️ {item.label}
                  </button>
                ))}
              </div>
            </div>

            <div className="bg-white rounded-2xl shadow-sm p-6 mb-6">
              <h3 className="text-lg font-bold text-gray-800 mb-4">Browse by Cuisine</h3>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                {[
                  { label: "🍝 Italian", href: "/recipes/cuisine/italian" },
                  { label: "🌮 Mexican", href: "/recipes/cuisine/mexican" },
                  { label: "🥢 Chinese", href: "/recipes/cuisine/chinese" },
                  { label: "🍛 Indian", href: "/recipes/cuisine/indian" },
                  { label: "🍱 Japanese", href: "/recipes/cuisine/japanese" },
                  { label: "🌶️ Thai", href: "/recipes/cuisine/thai" },
                  { label: "🍔 American", href: "/recipes/cuisine/american" },
                  { label: "🫒 Mediterranean", href: "/recipes/cuisine/mediterranean" },
                ].map(item => (
                  <a key={item.href} href={item.href} className="bg-gray-50 hover:bg-orange-50 text-gray-700 hover:text-orange-600 text-xs font-medium px-3 py-2.5 rounded-xl text-center transition-colors border border-gray-100">
                    {item.label}
                  </a>
                ))}
              </div>
            </div>

            <div className="bg-white rounded-2xl shadow-sm p-6 mb-6">
              <h3 className="text-lg font-bold text-gray-800 mb-4">Featured Recipe Pages</h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  { title: "7 Easy Recipes with Chicken and Rice", href: "/recipes/chicken-and-rice", desc: "Quick weeknight dinners using pantry staples." },
                  { title: "6 Easy Beef and Broccoli Recipes", href: "/recipes/beef-and-broccoli", desc: "Better than takeout and ready in 30 minutes." },
                  { title: "6 Easy Recipes with Shrimp and Pasta", href: "/recipes/shrimp-and-pasta", desc: "Elegant dinners that come together fast." },
                  { title: "6 Easy Recipes with Eggs and Cheese", href: "/recipes/eggs-and-cheese", desc: "Quick meals any time of day." },
                ].map(item => (
                  <a key={item.href} href={item.href} className="flex items-start gap-3 p-4 bg-orange-50 hover:bg-orange-100 rounded-xl transition-colors border border-orange-100">
                    <span className="text-2xl flex-shrink-0">📖</span>
                    <div>
                      <p className="text-sm font-bold text-gray-800 leading-tight mb-1">{item.title}</p>
                      <p className="text-xs text-gray-500">{item.desc}</p>
                    </div>
                  </a>
                ))}
              </div>
            </div>

            <div className="bg-white rounded-2xl shadow-sm p-6">
              <h3 className="text-lg font-bold text-gray-800 mb-3">Why My Recipe Match?</h3>
              <div className="space-y-3">
                {[
                  { icon: "🎯", title: "Perfect Match Technology", desc: "Our tool identifies which recipes use ALL of your ingredients so you never have to buy anything extra." },
                  { icon: "🥦", title: "Reduce Food Waste", desc: "Use up ingredients before they go bad. My Recipe Match helps you cook smarter and waste less." },
                  { icon: "💰", title: "Save Money on Groceries", desc: "Cook with what you have instead of buying new ingredients every night. Thousands of recipes, zero extra shopping." },
                  { icon: "⚡", title: "Results in Seconds", desc: "No browsing through endless recipe blogs. Enter your ingredients and get matched recipes instantly." },
                ].map(item => (
                  <div key={item.title} className="flex items-start gap-3">
                    <span className="text-xl flex-shrink-0">{item.icon}</span>
                    <div>
                      <p className="text-sm font-bold text-gray-700">{item.title}</p>
                      <p className="text-xs text-gray-500 leading-relaxed">{item.desc}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {loading && ('''

content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')