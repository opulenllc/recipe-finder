with open('app/recipes/cuisine/[cuisine]/client.tsx', encoding='utf-8') as f:
    content = f.read()

old = '''const navRecipes = [
  { label: "Chicken and Rice", href: "/recipes/chicken-and-rice" },
  { label: "Chicken and Broccoli", href: "/recipes/chicken-and-broccoli" },
  { label: "Beef and Broccoli", href: "/recipes/beef-and-broccoli" },
  { label: "Shrimp and Pasta", href: "/recipes/shrimp-and-pasta" },
  { label: "Eggs and Cheese", href: "/recipes/eggs-and-cheese" },
  { label: "Ground Beef and Rice", href: "/recipes/ground-beef-and-rice" },
  { label: "Salmon and Rice", href: "/recipes/salmon-and-rice" },
  { label: "Pasta and Cheese", href: "/recipes/pasta-and-cheese" },
  { label: "Tuna and Pasta", href: "/recipes/tuna-and-pasta" },
  { label: "Chicken and Pasta", href: "/recipes/chicken-and-pasta" },
];'''

new = '''const navRecipes = [
  { label: "Chicken and Rice", href: "/recipes/chicken-and-rice" },
  { label: "Chicken and Broccoli", href: "/recipes/chicken-and-broccoli" },
  { label: "Chicken Breast and Rice", href: "/recipes/chicken-breast-and-rice" },
  { label: "Chicken and Pasta", href: "/recipes/chicken-and-pasta" },
  { label: "Chicken and Potatoes", href: "/recipes/chicken-and-potatoes" },
  { label: "Chicken and Mushrooms", href: "/recipes/chicken-and-mushrooms" },
  { label: "Chicken and Spinach", href: "/recipes/chicken-and-spinach" },
  { label: "Chicken and Tomatoes", href: "/recipes/chicken-and-tomatoes" },
  { label: "Chicken and Garlic", href: "/recipes/chicken-and-garlic" },
  { label: "Chicken and Lemon", href: "/recipes/chicken-and-lemon" },
  { label: "Beef and Broccoli", href: "/recipes/beef-and-broccoli" },
  { label: "Beef and Potatoes", href: "/recipes/beef-and-potatoes" },
  { label: "Ground Beef and Pasta", href: "/recipes/ground-beef-and-pasta" },
  { label: "Ground Beef and Rice", href: "/recipes/ground-beef-and-rice" },
  { label: "Ground Beef and Potatoes", href: "/recipes/ground-beef-and-potatoes" },
  { label: "Shrimp and Rice", href: "/recipes/shrimp-and-rice" },
  { label: "Shrimp and Pasta", href: "/recipes/shrimp-and-pasta" },
  { label: "Salmon and Rice", href: "/recipes/salmon-and-rice" },
  { label: "Tuna and Pasta", href: "/recipes/tuna-and-pasta" },
  { label: "Pork and Rice", href: "/recipes/pork-and-rice" },
  { label: "Pork and Potatoes", href: "/recipes/pork-and-potatoes" },
  { label: "Eggs and Bread", href: "/recipes/eggs-and-bread" },
  { label: "Eggs and Cheese", href: "/recipes/eggs-and-cheese" },
  { label: "Eggs and Potatoes", href: "/recipes/eggs-and-potatoes" },
  { label: "Pasta and Cheese", href: "/recipes/pasta-and-cheese" },
  { label: "Potatoes and Cheese", href: "/recipes/potatoes-and-cheese" },
];'''

content = content.replace(old, new)

with open('app/recipes/cuisine/[cuisine]/client.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')