nav_component = '''
function NavBar() {
  const cuisines = [
    { label: "Italian", href: "/recipes/cuisine/italian" },
    { label: "Mexican", href: "/recipes/cuisine/mexican" },
    { label: "Chinese", href: "/recipes/cuisine/chinese" },
    { label: "Indian", href: "/recipes/cuisine/indian" },
    { label: "Japanese", href: "/recipes/cuisine/japanese" },
    { label: "Thai", href: "/recipes/cuisine/thai" },
    { label: "American", href: "/recipes/cuisine/american" },
    { label: "Mediterranean", href: "/recipes/cuisine/mediterranean" },
  ];

  const recipes = [
    { label: "Chicken and Rice", href: "/recipes/chicken-and-rice" },
    { label: "Chicken and Pasta", href: "/recipes/chicken-and-pasta" },
    { label: "Beef and Broccoli", href: "/recipes/beef-and-broccoli" },
    { label: "Shrimp and Pasta", href: "/recipes/shrimp-and-pasta" },
    { label: "Eggs and Cheese", href: "/recipes/eggs-and-cheese" },
    { label: "Ground Beef and Rice", href: "/recipes/ground-beef-and-rice" },
    { label: "Salmon and Rice", href: "/recipes/salmon-and-rice" },
    { label: "Chicken and Broccoli", href: "/recipes/chicken-and-broccoli" },
    { label: "Pasta and Cheese", href: "/recipes/pasta-and-cheese" },
    { label: "Tuna and Pasta", href: "/recipes/tuna-and-pasta" },
  ];

  return (
    <nav className="bg-white border-b border-gray-100 px-6">
      <div className="max-w-4xl mx-auto flex items-center gap-1 h-10">
        <a href="/" className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors">
          Home
        </a>
        <div className="group relative">
          <button className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors flex items-center gap-1">
            Cuisines <span className="text-gray-400">▼</span>
          </button>
          <div className="hidden group-hover:block absolute top-full left-0 bg-white border border-gray-100 rounded-xl shadow-lg z-50 py-2 min-w-40">
            {cuisines.map(c => (
              <a key={c.href} href={c.href} className="block px-4 py-1.5 text-xs text-gray-600 hover:text-orange-600 hover:bg-orange-50">
                {c.label}
              </a>
            ))}
          </div>
        </div>
        <div className="group relative">
          <button className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors flex items-center gap-1">
            Recipes <span className="text-gray-400">▼</span>
          </button>
          <div className="hidden group-hover:block absolute top-full left-0 bg-white border border-gray-100 rounded-xl shadow-lg z-50 py-2 min-w-48">
            {recipes.map(r => (
              <a key={r.href} href={r.href} className="block px-4 py-1.5 text-xs text-gray-600 hover:text-orange-600 hover:bg-orange-50">
                {r.label}
              </a>
            ))}
          </div>
        </div>
      </div>
    </nav>
  );
}

'''

with open('app/recipes/[slug]/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Add NavBar before the default export
content = content.replace(
    'export default async function RecipePage',
    nav_component + 'export default async function RecipePage'
)

# Add NavBar after header in the page
content = content.replace(
    '</header>\n\n      <main',
    '</header>\n      <NavBar />\n\n      <main'
)

with open('app/recipes/[slug]/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')