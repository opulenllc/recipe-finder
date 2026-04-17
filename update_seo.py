import os

os.makedirs("app/recipes/[slug]", exist_ok=True)

page = """import { Metadata } from "next";

type SlugEntry = {
  title: string;
  heading: string;
  intro: string;
  ingredients: string;
  keywords: string[];
  tips: string[];
  variations: string[];
  faqs: { q: string; a: string }[];
};

const slugData: Record<string, SlugEntry> = {
  "chicken-and-rice": {
    title: "7 Easy Recipes with Chicken and Rice (No Grocery Trip Needed)",
    heading: "7 Easy Recipes with Chicken and Rice",
    intro: "If you have chicken and rice in your kitchen, you are already halfway to a delicious, satisfying meal. These two pantry staples are the foundation of countless dishes across dozens of cuisines — from classic American casseroles to Asian-inspired fried rice and hearty soups. The best part? You do not need a long shopping list or hours in the kitchen. Whether you have fresh chicken breasts, leftover rotisserie, or frozen thighs, paired with any type of rice, these recipes will get dinner on the table fast. We have put together the best easy chicken and rice recipes you can make tonight using ingredients you likely already have at home.",
    ingredients: "chicken,rice",
    keywords: ["recipes with chicken and rice", "easy chicken and rice recipe", "simple chicken and rice recipes", "quick chicken and rice dinner", "chicken and rice meals"],
    tips: [
      "Use long-grain white rice for the best texture in most recipes — it stays fluffy and does not clump.",
      "Leftover or rotisserie chicken works perfectly in rice dishes and saves significant cooking time.",
      "Toast your rice in a dry pan for 2 minutes before adding liquid for a nuttier, more complex flavor.",
      "Always let your rice rest covered for 5 minutes after cooking — this makes it significantly fluffier.",
      "Add a bay leaf or garlic clove to your cooking liquid for extra depth of flavor.",
    ],
    variations: [
      "Healthy version: Use brown rice and skinless chicken breast, add extra vegetables like broccoli or spinach.",
      "Quick version: Use a rice cooker and pre-cooked rotisserie chicken for a meal in under 15 minutes.",
      "Budget version: Stretch the dish with canned beans or frozen vegetables to feed more people.",
      "Casserole version: Mix cooked chicken and rice with cream of mushroom soup, top with breadcrumbs, and bake at 375F for 25 minutes.",
      "Soup version: Add chicken broth, carrots, and celery to transform basic chicken and rice into a comforting soup.",
    ],
    faqs: [
      { q: "What is the best rice to use with chicken?", a: "Long-grain white rice is the most versatile and works well in most chicken and rice recipes. Jasmine rice adds a slightly floral aroma, basmati works great for pilafs, and brown rice is the healthiest option though it takes longer to cook." },
      { q: "Can I use frozen chicken for chicken and rice recipes?", a: "Yes, but thaw it completely first for even cooking. Pat it dry before cooking to get a better sear. Alternatively, you can cook frozen chicken directly in a slow cooker or instant pot with rice." },
      { q: "How do I keep chicken and rice from drying out?", a: "The key is using enough liquid and not overcooking. Use a 1.5 to 2 ratio of liquid to rice, cover tightly while cooking, and let it rest off heat for 5 minutes before serving." },
      { q: "How long does chicken and rice last in the fridge?", a: "Properly stored in an airtight container, chicken and rice will last 3 to 4 days in the refrigerator. Reheat with a splash of water or broth to restore moisture." },
    ],
  },
  "chicken-and-broccoli": {
    title: "6 Easy Recipes with Chicken and Broccoli (Quick Weeknight Dinners)",
    heading: "6 Easy Recipes with Chicken and Broccoli",
    intro: "Chicken and broccoli is one of the most popular ingredient combinations for a reason — it is healthy, quick, and incredibly versatile. Whether you are craving a Chinese-inspired stir fry, a creamy casserole, or a simple sheet pan dinner, this dynamic duo delivers every time. Both ingredients cook quickly, making them perfect for busy weeknights when you need dinner on the table fast. Plus, they are packed with protein and nutrients, so you can feel good about what you are eating. Here are the best easy chicken and broccoli recipes you can make tonight.",
    ingredients: "chicken,broccoli",
    keywords: ["recipes with chicken and broccoli", "chicken broccoli recipes", "easy chicken and broccoli dinner", "chicken broccoli stir fry", "healthy chicken broccoli meals"],
    tips: [
      "Cut chicken into even-sized pieces so it cooks at the same rate as the broccoli.",
      "Do not overcook broccoli — it should be bright green and slightly crisp, not mushy.",
      "Blanch broccoli for 2 minutes in boiling water before stir frying for the perfect texture.",
      "Marinate chicken for at least 15 minutes before cooking for significantly more flavor.",
      "Use high heat when stir frying to get a proper sear on the chicken rather than steaming it.",
    ],
    variations: [
      "Stir fry version: Toss with soy sauce, garlic, ginger, and sesame oil for a classic Chinese takeout style dish.",
      "Casserole version: Mix with cream of chicken soup and cheddar cheese, bake at 350F for 30 minutes.",
      "Sheet pan version: Season with olive oil, garlic, and lemon, roast everything together at 425F for 20 minutes.",
      "Pasta version: Add cooked pasta and a light cream sauce for a complete one-pan meal.",
      "Low carb version: Skip the rice or pasta and serve over cauliflower rice for a keto-friendly meal.",
    ],
    faqs: [
      { q: "Should I use fresh or frozen broccoli?", a: "Fresh broccoli gives the best texture and flavor, especially for stir fries. Frozen broccoli works well in casseroles and soups where texture matters less. If using frozen, do not thaw first — add it directly to the pan." },
      { q: "How do I make chicken and broccoli stir fry sauce?", a: "A basic stir fry sauce combines soy sauce, garlic, ginger, a little sugar, and cornstarch mixed with water. Add sesame oil at the end for authentic flavor." },
      { q: "Can I meal prep chicken and broccoli?", a: "Absolutely. Cook a large batch and store in airtight containers in the fridge for up to 4 days. It reheats well in the microwave with a splash of water or broth." },
      { q: "What goes well with chicken and broccoli?", a: "Rice is the classic pairing, but noodles, quinoa, mashed potatoes, or cauliflower rice all work great. A simple side salad also complements the dish nicely." },
    ],
  },
  "chicken-breast-and-rice": {
    title: "6 Easy Chicken Breast and Rice Recipes (Healthy Weeknight Dinners)",
    heading: "6 Easy Chicken Breast and Rice Recipes",
    intro: "Chicken breast and rice is one of the healthiest and most satisfying meal combinations you can make. High in protein and low in fat, chicken breast paired with rice gives you a complete, balanced meal that keeps you full for hours. The challenge many cooks face is keeping chicken breast moist and flavorful — but with the right techniques, it is easy to achieve restaurant-quality results at home. These recipes cover everything from baked chicken and rice to quick stovetop meals and hearty soups, all designed for busy weeknights.",
    ingredients: "chicken breast,rice",
    keywords: ["chicken breast and rice recipes", "easy chicken breast and rice", "healthy chicken breast rice dinner", "baked chicken breast and rice", "simple chicken breast meals"],
    tips: [
      "Pound chicken breasts to an even thickness before cooking to ensure they cook evenly.",
      "Brine chicken breasts in salted water for 30 minutes before cooking to keep them juicy.",
      "Use a meat thermometer — chicken breast is done at 165F internal temperature.",
      "Let chicken rest for 5 minutes after cooking before cutting to retain its juices.",
      "Season generously — chicken breast benefits from bold seasonings like garlic, paprika, and herbs.",
    ],
    variations: [
      "Baked version: Season with garlic, paprika, and olive oil, bake at 400F for 20-25 minutes over a bed of rice.",
      "Stovetop version: Slice thin, cook in a skillet with butter and herbs, serve over fluffy white rice.",
      "Healthy version: Use brown rice and add steamed vegetables for a nutritious balanced meal.",
      "Mediterranean version: Season with lemon, oregano, and olives for a bright, fresh flavor profile.",
      "Asian version: Marinate in soy sauce, ginger, and garlic, serve over jasmine rice with sesame seeds.",
    ],
    faqs: [
      { q: "How do I keep chicken breast from drying out?", a: "The key is not overcooking. Use a meat thermometer and remove from heat at 165F. Brining beforehand, cooking at the right temperature, and letting it rest before cutting all help retain moisture." },
      { q: "How long does it take to bake chicken breast with rice?", a: "At 375F, chicken breast typically takes 25-30 minutes. If baking over rice, the rice needs about 45 minutes total, so add the chicken partway through or par-cook the rice first." },
      { q: "Is chicken breast and rice good for weight loss?", a: "Yes — it is high in lean protein and complex carbohydrates, keeping you full while staying relatively low in calories. Use brown rice for added fiber and nutrients." },
      { q: "Can I use chicken thighs instead of breasts?", a: "Absolutely. Chicken thighs are more forgiving and stay moist more easily than breasts. They take slightly longer to cook but deliver more flavor." },
    ],
  },
  "eggs-and-bread": {
    title: "7 Easy Recipes with Eggs and Bread (Quick Meals Any Time of Day)",
    heading: "7 Easy Recipes with Eggs and Bread",
    intro: "Eggs and bread are the ultimate pantry duo — humble, affordable, and endlessly versatile. From a simple egg on toast to elegant French toast and hearty breakfast casseroles, these two ingredients can produce dozens of satisfying meals any time of day. Whether you are making breakfast, lunch, or a quick dinner, eggs and bread come together in minutes and never disappoint. These recipes celebrate the simplicity of cooking with what you have, proving that you do not need fancy ingredients to eat well.",
    ingredients: "eggs,bread",
    keywords: ["recipes with eggs and bread", "easy egg and bread recipes", "what to make with eggs and bread", "egg toast recipes", "quick egg meals"],
    tips: [
      "Use day-old or slightly stale bread for French toast — it absorbs the egg mixture better without falling apart.",
      "For perfectly fried eggs, start with a cold pan and heat gradually for whites that set without browning.",
      "Whisk eggs thoroughly with a fork before scrambling for a more uniform, fluffy result.",
      "Sourdough or thick-cut bread holds up best in egg-based recipes and adds more flavor.",
      "Add a splash of milk or cream to scrambled eggs before cooking for a creamier texture.",
    ],
    variations: [
      "Sweet version: French toast with cinnamon, vanilla, and maple syrup for a classic breakfast treat.",
      "Savory version: Egg in a hole — cut a circle from bread, fry the egg inside the hole for a fun presentation.",
      "Casserole version: Layer bread and eggs with cheese and vegetables in a baking dish for an overnight breakfast casserole.",
      "Sandwich version: Scrambled or fried eggs with cheese and hot sauce between toasted bread slices.",
      "Crouton version: Cube stale bread and bake until crispy, top a soft boiled egg salad for texture contrast.",
    ],
    faqs: [
      { q: "What is the best bread for egg recipes?", a: "Thick-cut white bread or brioche works best for French toast. Sourdough is great for savory egg dishes. Any sturdy bread works well — avoid very thin sandwich bread as it can fall apart." },
      { q: "How do I make perfect scrambled eggs?", a: "Use medium-low heat, stir constantly, and remove from heat while still slightly wet — residual heat will finish cooking them. Add butter at the end for extra richness." },
      { q: "Can I make egg and bread recipes ahead of time?", a: "Breakfast casseroles are perfect for making ahead — assemble the night before, refrigerate, and bake in the morning. French toast batter can also be made ahead and stored overnight." },
      { q: "What can I add to egg and bread recipes for more nutrition?", a: "Spinach, tomatoes, mushrooms, onions, and bell peppers all pair beautifully with eggs. Add cheese for protein, or avocado for healthy fats." },
    ],
  },
  "ground-beef-and-pasta": {
    title: "6 Easy Recipes with Ground Beef and Pasta (Hearty Family Dinners)",
    heading: "6 Easy Recipes with Ground Beef and Pasta",
    intro: "Ground beef and pasta is the ultimate comfort food combination — hearty, satisfying, and loved by the whole family. From classic bolognese to simple hamburger helper style dishes, this pair delivers big flavor without big effort. Ground beef cooks quickly and pairs perfectly with virtually any pasta shape, making it one of the most versatile weeknight dinner options available. These recipes range from quick 20-minute meals to slow-simmered sauces that fill your kitchen with incredible aromas.",
    ingredients: "ground beef,pasta",
    keywords: ["recipes with ground beef and pasta", "ground beef pasta recipes", "easy ground beef and pasta dinner", "hamburger pasta recipes", "quick beef pasta meals"],
    tips: [
      "Brown ground beef in batches without stirring too much to get a proper sear and more flavor.",
      "Drain excess fat after browning but leave a little for flavor — about a tablespoon is ideal.",
      "Season ground beef while browning, not after, for better flavor penetration.",
      "Reserve a cup of pasta water before draining — the starchy water helps bind sauce to pasta.",
      "Cook pasta just to al dente since it will continue cooking when combined with hot sauce.",
    ],
    variations: [
      "Bolognese version: Slow simmer with tomatoes, wine, and herbs for a rich, authentic Italian meat sauce.",
      "Quick version: Brown beef with jarred marinara and toss with any pasta shape for dinner in 20 minutes.",
      "Baked version: Layer with pasta, beef sauce, and mozzarella for a simple baked pasta dish.",
      "Creamy version: Add cream cheese or heavy cream to the beef sauce for a rich, indulgent twist.",
      "Healthy version: Use whole wheat pasta and add spinach or zucchini to boost nutrition.",
    ],
    faqs: [
      { q: "What pasta shape works best with ground beef?", a: "Chunky shapes like rigatoni, penne, and shells hold meat sauce well. Spaghetti and fettuccine work great for bolognese. Elbow macaroni is classic for hamburger pasta dishes." },
      { q: "How do I make ground beef pasta sauce from scratch?", a: "Brown the beef, add diced onion and garlic, cook until soft, add crushed tomatoes and Italian seasoning, simmer for 20 minutes. Season with salt, pepper, and a pinch of sugar to balance acidity." },
      { q: "Can I freeze ground beef pasta dishes?", a: "Yes — most ground beef pasta dishes freeze very well for up to 3 months. Store in airtight containers and thaw overnight in the fridge before reheating." },
      { q: "What percentage fat ground beef is best for pasta?", a: "80/20 ground beef gives the best flavor. Leaner beef like 90/10 can be used for a healthier option but may be slightly less flavorful. Drain excess fat after browning regardless." },
    ],
  },
  "potatoes-and-cheese": {
    title: "6 Easy Recipes with Potatoes and Cheese (Ultimate Comfort Food)",
    heading: "6 Easy Recipes with Potatoes and Cheese",
    intro: "Potatoes and cheese are comfort food royalty. Few combinations are as universally loved or as satisfying as these two simple ingredients coming together in a hot, bubbling dish. From classic scalloped potatoes to loaded baked potatoes, cheesy potato soup, and crispy potato gratins, the possibilities are almost endless. Both ingredients are affordable, widely available, and shelf-stable, making this combination a reliable go-to whenever you need a satisfying meal without a grocery run.",
    ingredients: "potatoes,cheese",
    keywords: ["recipes with potatoes and cheese", "cheesy potato recipes", "easy potato and cheese dinner", "potato cheese casserole", "loaded potato recipes"],
    tips: [
      "Slice potatoes evenly for casseroles and gratins — a mandoline slicer makes this much faster.",
      "Parboil potatoes for 5 minutes before baking to significantly reduce overall cooking time.",
      "Sharp cheddar, gruyere, and fontina melt the best and provide the most flavor in potato dishes.",
      "Add a pinch of nutmeg to cheesy potato dishes — it enhances the flavor in a subtle but noticeable way.",
      "Let cheesy potato dishes rest for 10 minutes before serving so they set and are easier to serve.",
    ],
    variations: [
      "Gratin version: Layer thinly sliced potatoes with cream and gruyere, bake at 375F for 45 minutes until golden.",
      "Loaded version: Bake whole potatoes, top with cheddar, sour cream, bacon, and chives.",
      "Soup version: Simmer diced potatoes in broth, mash partially, stir in cheddar for a thick, creamy soup.",
      "Casserole version: Mix cubed potatoes with cream of mushroom soup and cheddar, bake until bubbly.",
      "Hash version: Pan fry diced potatoes until crispy, melt cheese on top for a quick breakfast or dinner.",
    ],
    faqs: [
      { q: "What potatoes work best with cheese?", a: "Russet potatoes are best for baking and mashing. Yukon Gold potatoes have a naturally buttery flavor that pairs beautifully with cheese. Red potatoes hold their shape well in casseroles and soups." },
      { q: "What cheese melts best on potatoes?", a: "Cheddar is the classic choice. Gruyere, fontina, and gouda melt smoothly and add sophistication. Mozzarella gives a stretchy, mild melt. Avoid pre-shredded cheese when possible as it contains anti-caking agents that prevent smooth melting." },
      { q: "How do I make cheesy potatoes not watery?", a: "Dry potatoes thoroughly after washing. If making a casserole, avoid covering tightly which traps steam. Use a roux-based sauce rather than adding liquid cheese directly to prevent separation." },
      { q: "Can I make cheesy potatoes ahead of time?", a: "Yes — assemble the dish, cover, and refrigerate up to 24 hours before baking. Add 10-15 extra minutes to the baking time if cooking straight from the fridge." },
    ],
  },
  "chicken-and-pasta": {
    title: "6 Easy Recipes with Chicken and Pasta (Quick Weeknight Dinners)",
    heading: "6 Easy Recipes with Chicken and Pasta",
    intro: "Chicken and pasta is a combination that never goes out of style. Whether you are craving something creamy and indulgent like chicken alfredo, bright and lemony, or hearty with a tomato sauce, chicken and pasta delivers every single time. Both ingredients cook relatively quickly, making them perfect for weeknights when time is short but you still want something satisfying and homemade. These recipes cover the full range from light and healthy to rich and comforting.",
    ingredients: "chicken,pasta",
    keywords: ["recipes with chicken and pasta", "easy chicken pasta recipes", "quick chicken and pasta dinner", "chicken pasta meals", "simple chicken noodle dishes"],
    tips: [
      "Pound chicken to even thickness before cooking for consistent results and faster cooking time.",
      "Always salt your pasta water generously — it should taste like the sea for properly seasoned pasta.",
      "Reserve pasta water before draining to use in your sauce for better consistency.",
      "Let chicken rest before slicing to keep it juicy and prevent the juices from running out.",
      "Finish pasta in the sauce pan with a splash of pasta water for the best coating.",
    ],
    variations: [
      "Alfredo version: Toss with butter, heavy cream, and parmesan for a classic creamy indulgent dish.",
      "Tomato version: Simmer with crushed tomatoes, garlic, and basil for a light, bright sauce.",
      "Lemon version: Brighten with lemon juice, zest, and capers for a fresh Mediterranean flavor.",
      "Pesto version: Toss with store-bought or homemade pesto for an incredibly fast weeknight dinner.",
      "Soup version: Add broth, vegetables, and egg noodles for a comforting chicken noodle soup.",
    ],
    faqs: [
      { q: "What pasta shape works best with chicken?", a: "Penne and rigatoni work great with chunky chicken pieces and thick sauces. Fettuccine and linguine pair well with creamy sauces. Spaghetti works for lighter tomato-based dishes." },
      { q: "How do I make chicken pasta not dry?", a: "Do not overcook the chicken and always add enough sauce. Finishing the pasta in the sauce pan with pasta water helps coat every piece. A drizzle of good olive oil at the end adds richness." },
      { q: "Can I use rotisserie chicken in pasta recipes?", a: "Absolutely — rotisserie chicken is perfect for pasta dishes. It saves significant time and adds great flavor. Just shred or chop and add at the end of cooking to heat through." },
      { q: "How do I make a simple chicken pasta sauce from scratch?", a: "Saute garlic in olive oil, add diced tomatoes or cream, season with salt, pepper, and Italian herbs. Add cooked chicken, toss with pasta and pasta water, finish with parmesan." },
    ],
  },
  "eggs-and-cheese": {
    title: "6 Easy Recipes with Eggs and Cheese (Quick Meals Any Time)",
    heading: "6 Easy Recipes with Eggs and Cheese",
    intro: "Eggs and cheese are one of the most natural and delicious pairings in all of cooking. Together they create rich, satisfying dishes that work for breakfast, lunch, or dinner. From a simple cheesy omelette to a baked frittata, quiche, or egg casserole, this combination is endlessly flexible and comes together in minutes. Both ingredients are protein-rich, making egg and cheese recipes not just delicious but genuinely nutritious and filling.",
    ingredients: "eggs,cheese",
    keywords: ["recipes with eggs and cheese", "easy egg and cheese recipes", "what to make with eggs and cheese", "cheesy egg dishes", "egg cheese breakfast ideas"],
    tips: [
      "Bring eggs to room temperature before cooking for more even, consistent results.",
      "Use freshly grated cheese rather than pre-shredded for better melting and superior flavor.",
      "For omelettes, use medium-low heat and do not rush — patience produces a silkier result.",
      "Add cheese at the very end of cooking scrambled eggs and fold it in off the heat.",
      "Gruyere, cheddar, and feta are the best cheeses for egg dishes due to their strong flavors.",
    ],
    variations: [
      "Omelette version: Beat eggs with a fork, cook in butter, fill with any cheese for a classic French omelette.",
      "Frittata version: Cook eggs with cheese and vegetables in an oven-safe pan, finish under the broiler.",
      "Quiche version: Pour egg and cheese custard into a pastry shell, bake at 350F for 35 minutes.",
      "Scramble version: Soft scramble eggs with cream cheese folded in at the end for an ultra-creamy result.",
      "Baked version: Crack eggs into individual ramekins, top with cheese, bake at 375F for 12 minutes.",
    ],
    faqs: [
      { q: "What cheese goes best with eggs?", a: "Cheddar is the most popular for everyday egg dishes. Gruyere adds sophistication and melts beautifully. Feta adds a salty, tangy punch. Brie and goat cheese make for an elegant, creamy filling in omelettes." },
      { q: "How do I make a perfect cheesy omelette?", a: "Use 2-3 eggs per omelette, beat well, cook in butter over medium heat, add cheese when the eggs are just set but still slightly wet on top, fold and serve immediately." },
      { q: "Can I meal prep egg and cheese dishes?", a: "Frittatas and egg casseroles meal prep very well — make on Sunday and portion for the week. Individual egg cups baked in a muffin tin are also perfect for grab-and-go breakfasts." },
      { q: "How many eggs per person for egg recipes?", a: "For a main dish, plan on 2-3 eggs per person. For a frittata or casserole serving 4, use 6-8 eggs total. Adjust based on what other ingredients you are including." },
    ],
  },
  "ground-beef-and-rice": {
    title: "6 Easy Recipes with Ground Beef and Rice (Budget-Friendly Dinners)",
    heading: "6 Easy Recipes with Ground Beef and Rice",
    intro: "Ground beef and rice is one of the most budget-friendly meal combinations you can make, and it is incredibly versatile. From Korean-inspired beef bowls to classic stuffed peppers and hearty one-pot meals, this combination delivers big flavor without straining your grocery budget. Ground beef cooks in minutes and pairs beautifully with rice in cuisines from around the world. These recipes prove that eating well does not have to be expensive.",
    ingredients: "ground beef,rice",
    keywords: ["recipes with ground beef and rice", "ground beef rice recipes", "easy ground beef and rice dinner", "beef rice bowl recipes", "budget beef and rice meals"],
    tips: [
      "Brown ground beef in a hot, dry pan without crowding for the best caramelization and flavor.",
      "Add aromatics like onion and garlic after browning the beef for maximum flavor development.",
      "Use beef broth instead of water to cook your rice for a richer, more savory base.",
      "Season in layers — add salt and pepper to the beef while browning, then adjust at the end.",
      "A splash of soy sauce or Worcestershire sauce adds incredible depth to beef and rice dishes.",
    ],
    variations: [
      "Korean bowl version: Season with soy sauce, sesame oil, garlic, and ginger, serve over rice with a fried egg.",
      "Stuffed pepper version: Mix cooked beef and rice with tomato sauce, stuff into bell peppers, bake at 375F.",
      "One pot version: Brown beef, add rice and broth directly to the pan, simmer until rice is cooked.",
      "Mexican version: Season with cumin, chili powder, and salsa for a quick taco rice bowl.",
      "Fried rice version: Use day-old rice, stir fry with beef, soy sauce, and vegetables for a complete meal.",
    ],
    faqs: [
      { q: "What rice works best with ground beef?", a: "Long-grain white rice is the most versatile. Jasmine rice adds a subtle floral note that pairs well with Asian-inspired beef dishes. Brown rice adds nutrition and a nutty flavor. Day-old rice works best for fried rice dishes." },
      { q: "How do I make ground beef and rice more flavorful?", a: "Brown the beef properly for the best flavor base. Use beef broth instead of water for the rice. Add aromatics like onion, garlic, and ginger. Season boldly with soy sauce, Worcestershire, or your favorite spice blend." },
      { q: "Is ground beef and rice healthy?", a: "It can be very healthy. Use lean ground beef (90/10), choose brown rice for added fiber, and load up on vegetables. A typical serving provides a good balance of protein, carbohydrates, and healthy fats." },
      { q: "How much ground beef per person for rice dishes?", a: "Plan on about 4-6 ounces of ground beef per person for a main dish. Combined with rice, this creates a satisfying, filling meal for most adults." },
    ],
  },
  "chicken-and-potatoes": {
    title: "6 Easy Recipes with Chicken and Potatoes (One-Pan Comfort Food)",
    heading: "6 Easy Recipes with Chicken and Potatoes",
    intro: "Chicken and potatoes is the ultimate one-pan comfort food combination. These two humble ingredients have been feeding families for generations, and for good reason — they are affordable, filling, and absolutely delicious together. Whether you roast them in the oven, cook them in a skillet, or simmer them in a hearty stew, chicken and potatoes deliver a satisfying meal that requires minimal cleanup and effort. These recipes make the most of this classic combination.",
    ingredients: "chicken,potatoes",
    keywords: ["recipes with chicken and potatoes", "chicken and potato recipes", "easy chicken potatoes dinner", "roasted chicken and potatoes", "one pan chicken potato meals"],
    tips: [
      "Cut potatoes into similar-sized pieces as the chicken for even cooking times.",
      "Parboil potatoes for 5 minutes before roasting for crispier results in less time.",
      "Season both the chicken and potatoes separately before combining for even flavor distribution.",
      "Use a high oven temperature (425F) for roasting to get crispy potatoes and golden chicken skin.",
      "Add garlic and fresh herbs like rosemary or thyme for a classic, fragrant flavor combination.",
    ],
    variations: [
      "Roasted version: Toss with olive oil, garlic, and herbs, roast at 425F for 35-40 minutes on one pan.",
      "Stew version: Simmer chicken thighs and cubed potatoes in broth with vegetables for a hearty dinner.",
      "Skillet version: Brown chicken and potatoes together in a cast iron pan for a quick stovetop meal.",
      "Greek version: Season with lemon, oregano, and olive oil for a bright Mediterranean flavor profile.",
      "Slow cooker version: Set and forget — cook on low for 6-8 hours for fall-apart tender results.",
    ],
    faqs: [
      { q: "What potatoes are best with chicken?", a: "Baby potatoes and Yukon Gold potatoes are ideal — they roast beautifully, have a creamy texture, and do not need peeling. Russet potatoes work well in stews as they absorb flavors well." },
      { q: "How do I get crispy potatoes when roasting with chicken?", a: "Make sure potatoes are completely dry before seasoning. Use high heat (425F), do not overcrowd the pan, and parboil for 5 minutes before roasting for maximum crispiness." },
      { q: "Should I use bone-in or boneless chicken with potatoes?", a: "Bone-in chicken thighs are ideal for roasting with potatoes — they take similar amounts of time and stay moist and flavorful. Boneless chicken breasts cook faster, so add them later in the cooking process." },
      { q: "What herbs go best with chicken and potatoes?", a: "Rosemary, thyme, and garlic are the classic combination. Paprika adds color and mild smokiness. Oregano gives a Mediterranean flavor. Fresh parsley added at the end brightens the whole dish." },
    ],
  },
  "tuna-and-pasta": {
    title: "6 Easy Recipes with Tuna and Pasta (Quick Budget Meals)",
    heading: "6 Easy Recipes with Tuna and Pasta",
    intro: "Tuna and pasta is one of the quickest, most affordable meals you can make. With just a can of tuna and some pasta, you can have a satisfying dinner on the table in under 20 minutes. This combination is popular across Mediterranean Europe and for good reason — it is simple, protein-rich, and incredibly flavorful when seasoned well. These recipes range from light and lemony to creamy and indulgent, all built around pantry staples you likely already have.",
    ingredients: "tuna,pasta",
    keywords: ["recipes with tuna and pasta", "tuna pasta recipes", "easy tuna and pasta dinner", "canned tuna pasta", "quick tuna noodle dishes"],
    tips: [
      "Drain tuna thoroughly and pat dry to prevent excess liquid from diluting your sauce.",
      "Oil-packed tuna has significantly more flavor than water-packed — worth the slight price difference.",
      "Add tuna at the very end of cooking to prevent it from becoming dry and crumbly.",
      "Capers, olives, and lemon juice complement tuna pasta beautifully and add brightness.",
      "Fresh or dried chili flakes add a welcome kick that elevates simple tuna pasta dishes.",
    ],
    variations: [
      "Mediterranean version: Toss with olive oil, capers, olives, cherry tomatoes, and lemon for a light summery dish.",
      "Creamy version: Mix with cream cheese or canned cream of mushroom soup for a quick tuna noodle casserole.",
      "Baked version: Top pasta and tuna with breadcrumbs and cheese, bake until golden and bubbly.",
      "Cold version: Toss chilled pasta with tuna, mayo, celery, and lemon for a refreshing pasta salad.",
      "Spicy version: Add chili flakes, garlic, and capers for an Italian-inspired puttanesca style dish.",
    ],
    faqs: [
      { q: "What pasta shape works best with tuna?", a: "Spaghetti and linguine work beautifully with light oil-based tuna sauces. Penne and rigatoni are better for chunkier sauces. Egg noodles are traditional in American tuna noodle casserole." },
      { q: "Is canned tuna healthy?", a: "Yes — canned tuna is an excellent source of lean protein and omega-3 fatty acids. Light tuna in water is the lowest calorie option. Limit to 2-3 servings per week due to mercury content." },
      { q: "How do I make tuna pasta more flavorful?", a: "Use oil-packed tuna, do not skip the garlic, add lemon juice and zest, use capers or olives, and finish with fresh parsley. A pinch of chili flakes wakes up the whole dish." },
      { q: "Can I make tuna pasta ahead of time?", a: "Light tuna pasta dishes are best served fresh. Creamy tuna noodle casserole can be assembled ahead and baked when needed. Cold tuna pasta salad actually improves after a few hours in the fridge." },
    ],
  },
  "beef-and-broccoli": {
    title: "6 Easy Beef and Broccoli Recipes (Better Than Takeout)",
    heading: "6 Easy Beef and Broccoli Recipes",
    intro: "Beef and broccoli is one of the most beloved Chinese-American dishes, and making it at home is much easier than most people think. The key is a flavorful sauce and high heat cooking. Once you master the basic technique, you will never need to order takeout again. Beyond the classic stir fry, beef and broccoli works beautifully in noodle dishes, rice bowls, and even sheet pan dinners. These recipes bring restaurant-quality results to your home kitchen.",
    ingredients: "beef,broccoli",
    keywords: ["beef and broccoli recipes", "easy beef broccoli stir fry", "homemade beef and broccoli", "better than takeout beef broccoli", "quick beef broccoli dinner"],
    tips: [
      "Slice beef against the grain and as thin as possible for the most tender results.",
      "Freeze beef for 20 minutes before slicing — it firms up and makes thin slicing much easier.",
      "Velveting beef with baking soda for 15 minutes before cooking produces restaurant-quality tenderness.",
      "Use high heat and cook in small batches so the beef sears rather than steams.",
      "Make the sauce before you start cooking — the stir fry moves fast and you will not have time.",
    ],
    variations: [
      "Classic stir fry version: Thin beef strips with oyster sauce, soy sauce, and garlic over steamed rice.",
      "Noodle version: Toss beef and broccoli with cooked lo mein or udon noodles and stir fry sauce.",
      "Sheet pan version: Roast beef strips and broccoli florets with a soy-sesame glaze at 425F.",
      "Slow cooker version: Cook beef in sauce on low for 6 hours, add blanched broccoli at the end.",
      "Healthy version: Use lean sirloin, reduce sauce sugar, add extra broccoli and serve over cauliflower rice.",
    ],
    faqs: [
      { q: "What cut of beef is best for beef and broccoli?", a: "Flank steak is the traditional choice — it is affordable and becomes very tender when sliced thin against the grain. Sirloin, skirt steak, and flat iron steak also work well. Avoid thick, tough cuts like chuck." },
      { q: "How do I make beef and broccoli sauce?", a: "Combine soy sauce, oyster sauce, brown sugar, sesame oil, garlic, ginger, and cornstarch mixed with water. This creates a glossy, savory sauce that coats everything perfectly." },
      { q: "How do I make beef tender for stir fry?", a: "Slice thin against the grain, marinate briefly in soy sauce and cornstarch, and optionally velvet with baking soda. Cook in a very hot pan in small batches for maximum tenderness." },
      { q: "Can I use frozen broccoli for beef and broccoli?", a: "Yes — thaw and pat very dry before using to prevent steaming instead of stir frying. Fresh broccoli will give you better texture, but frozen works in a pinch." },
    ],
  },
  "shrimp-and-rice": {
    title: "6 Easy Recipes with Shrimp and Rice (Quick Elegant Dinners)",
    heading: "6 Easy Recipes with Shrimp and Rice",
    intro: "Shrimp and rice might be the fastest path to an impressive, restaurant-worthy dinner at home. Shrimp cook in just 2-3 minutes, making this one of the quickest protein and grain combinations available. From classic shrimp fried rice to Cajun shrimp bowls and coconut shrimp curry, the flavor possibilities are enormous. Whether you use fresh or frozen shrimp, these recipes deliver big flavor with minimal effort.",
    ingredients: "shrimp,rice",
    keywords: ["recipes with shrimp and rice", "shrimp rice recipes", "easy shrimp and rice dinner", "shrimp fried rice recipe", "quick shrimp rice bowls"],
    tips: [
      "Pat shrimp completely dry before cooking — moisture prevents proper searing.",
      "Do not overcook shrimp — they are done the moment they curl into a C shape and turn pink.",
      "Season shrimp just before cooking, not ahead of time, to prevent the salt from drawing out moisture.",
      "Use day-old rice for fried rice — freshly cooked rice is too moist and will not fry properly.",
      "Cook shrimp last when combining with rice to prevent overcooking while other elements heat up.",
    ],
    variations: [
      "Fried rice version: Stir fry day-old rice with shrimp, soy sauce, eggs, and vegetables for a classic dish.",
      "Cajun version: Season with Cajun spices, sear quickly, serve over white rice with lemon butter.",
      "Coconut curry version: Simmer shrimp in coconut milk with curry paste, serve over jasmine rice.",
      "Garlic butter version: Cook shrimp in garlic butter, serve over rice with fresh parsley and lemon.",
      "Bowl version: Layer rice with seasoned shrimp, avocado, cucumber, and a drizzle of sriracha mayo.",
    ],
    faqs: [
      { q: "Fresh or frozen shrimp — which is better?", a: "For most home cooks, frozen shrimp is actually fresher than what is sold as fresh at the counter, which is often previously frozen and thawed. Buy frozen and thaw yourself for the best quality and value." },
      { q: "How do I thaw shrimp quickly?", a: "Place frozen shrimp in a colander under cold running water for 5 minutes. Never thaw in warm water or the microwave as this begins cooking the shrimp unevenly." },
      { q: "What size shrimp is best for rice dishes?", a: "Medium to large shrimp (21/25 count per pound) work best in rice dishes — they cook quickly but are substantial enough to be satisfying. Extra large shrimp work well for showier presentations." },
      { q: "How do I know when shrimp are cooked?", a: "Shrimp are done when they turn pink and opaque and curl into a loose C shape. If they curl into a tight O shape, they are overcooked. This happens very quickly — usually just 1-2 minutes per side." },
    ],
  },
  "pork-and-potatoes": {
    title: "6 Easy Recipes with Pork and Potatoes (Hearty Comfort Dinners)",
    heading: "6 Easy Recipes with Pork and Potatoes",
    intro: "Pork and potatoes is a classic combination that has sustained families for centuries. Affordable, filling, and deeply satisfying, this pairing works across dozens of cooking styles — from simple roasted pork chops with potatoes to hearty stews and crispy hash. Pork has incredible versatility and pairs naturally with the starchy richness of potatoes, creating meals that feel substantial and comforting without requiring advanced cooking skills.",
    ingredients: "pork,potatoes",
    keywords: ["recipes with pork and potatoes", "pork and potato recipes", "easy pork potatoes dinner", "pork chops and potatoes", "roasted pork potato meals"],
    tips: [
      "Bring pork chops to room temperature for 20 minutes before cooking for more even results.",
      "Sear pork in a very hot pan before finishing in the oven for the best crust and juiciness.",
      "Use a meat thermometer — pork is safe and perfectly juicy at 145F internal temperature.",
      "Parboil potatoes before adding to the pan with pork so everything finishes at the same time.",
      "Let pork rest for 5 minutes after cooking to redistribute juices before cutting.",
    ],
    variations: [
      "Roasted version: Season pork chops and potatoes with garlic and herbs, roast together at 400F.",
      "Stew version: Braise pork shoulder with cubed potatoes in broth until fork tender.",
      "Skillet version: Pan fry pork chops, make a pan sauce, add parboiled potatoes to finish together.",
      "Sheet pan version: Arrange pork tenderloin and halved baby potatoes on one pan, roast at 425F.",
      "Slow cooker version: Cook pork with potatoes and vegetables on low for 8 hours for a hands-off dinner.",
    ],
    faqs: [
      { q: "What cut of pork works best with potatoes?", a: "Pork chops are the quickest option. Pork shoulder and pork butt become incredibly tender in slow braises with potatoes. Pork tenderloin is the leanest option and roasts beautifully with potatoes." },
      { q: "How do I keep pork chops from drying out?", a: "Do not overcook — use a meat thermometer and pull at 145F. Brine the chops in salted water for 30 minutes before cooking. Bone-in chops stay juicier than boneless. Let them rest before cutting." },
      { q: "What seasonings go best with pork and potatoes?", a: "Garlic, rosemary, thyme, and sage are classic pairings. Smoked paprika adds depth. Mustard-based marinades pair beautifully with both pork and potatoes. Apple and fennel also complement pork wonderfully." },
      { q: "Can I cook pork and potatoes together from raw?", a: "Yes — in a slow cooker or oven roast they cook together beautifully. For stovetop cooking, parboil potatoes first since pork chops cook much faster than raw potatoes." },
    ],
  },
  "salmon-and-rice": {
    title: "6 Easy Recipes with Salmon and Rice (Healthy Elegant Dinners)",
    heading: "6 Easy Recipes with Salmon and Rice",
    intro: "Salmon and rice is one of the healthiest, most elegant meals you can prepare at home. Rich in omega-3 fatty acids, high-quality protein, and essential nutrients, salmon paired with rice creates a nutritionally complete meal that also happens to taste incredible. From simple baked salmon over white rice to sophisticated sushi bowls and teriyaki glazed fillets, these recipes cover the full range of what this outstanding combination can achieve.",
    ingredients: "salmon,rice",
    keywords: ["recipes with salmon and rice", "salmon rice recipes", "easy salmon and rice dinner", "baked salmon and rice", "healthy salmon rice bowls"],
    tips: [
      "Bring salmon to room temperature for 15 minutes before cooking for more even results.",
      "Pat salmon skin completely dry before cooking for the crispiest skin possible.",
      "Cook salmon skin-side down first on high heat, then flip for just 1-2 minutes to finish.",
      "Do not move salmon while cooking — let it release naturally from the pan for the best crust.",
      "A simple glaze of soy sauce, honey, and garlic transforms basic salmon into something spectacular.",
    ],
    variations: [
      "Teriyaki version: Glaze with soy sauce, mirin, and honey, serve over steamed rice with sesame seeds.",
      "Bowl version: Flake baked salmon over rice with avocado, cucumber, edamame, and sriracha mayo.",
      "Baked version: Season with lemon, dill, and garlic, bake at 400F for 12-15 minutes, serve over rice.",
      "Fried rice version: Flake leftover salmon into fried rice with soy sauce and vegetables.",
      "Curry version: Simmer salmon in a light coconut curry sauce, serve over fragrant jasmine rice.",
    ],
    faqs: [
      { q: "What rice pairs best with salmon?", a: "Jasmine rice is the most popular pairing — its subtle fragrance complements salmon beautifully. Sushi rice works for bowls. Brown rice adds nutrition. Wild rice adds a nutty, earthy flavor that pairs well with richer salmon preparations." },
      { q: "How do I know when salmon is cooked?", a: "Salmon is done when it flakes easily with a fork and the flesh has changed from translucent to opaque. For the juiciest result, cook to an internal temperature of 125-130F for medium, or 145F for well done." },
      { q: "Should I eat the salmon skin?", a: "Salmon skin is edible and actually contains concentrated omega-3 fatty acids. When cooked crispy, it is delicious. If you prefer not to eat it, it removes easily after cooking." },
      { q: "Can I use canned salmon instead of fresh?", a: "Yes — canned salmon works well in salmon fried rice, salmon bowls, and salmon patties served over rice. It is significantly cheaper and still provides excellent nutrition." },
    ],
  },
  "chicken-and-mushrooms": {
    title: "6 Easy Recipes with Chicken and Mushrooms (Rich Savory Dinners)",
    heading: "6 Easy Recipes with Chicken and Mushrooms",
    intro: "Chicken and mushrooms are a flavor pairing that has stood the test of time in virtually every culinary tradition. Mushrooms bring an earthy, umami-rich depth that elevates chicken from simple to sublime. Together they create sauces, stews, and skillet dishes with a richness that tastes like you spent hours cooking, even when dinner comes together in 30 minutes. These recipes make the most of this outstanding combination.",
    ingredients: "chicken,mushrooms",
    keywords: ["recipes with chicken and mushrooms", "chicken mushroom recipes", "easy chicken and mushroom dinner", "creamy chicken mushroom", "chicken mushroom skillet"],
    tips: [
      "Do not crowd mushrooms in the pan — cook in batches so they brown rather than steam.",
      "Let mushrooms sit undisturbed in the hot pan for 2-3 minutes before stirring for best browning.",
      "Add a splash of white wine or sherry after browning mushrooms to deglaze and add depth.",
      "Season mushrooms with salt only after they have browned — early salting draws out moisture.",
      "Dried mushrooms rehydrated in warm water add intense flavor to sauces and stews.",
    ],
    variations: [
      "Creamy version: Make a rich cream sauce with garlic and thyme, pour over seared chicken and mushrooms.",
      "Marsala version: Deglaze with Marsala wine for a classic Italian-American restaurant dish at home.",
      "Stir fry version: Slice thin and stir fry with soy sauce, ginger, and sesame oil over rice.",
      "Soup version: Simmer with broth, herbs, and cream for a hearty chicken and mushroom soup.",
      "Baked version: Layer in a baking dish with cream of mushroom soup, bake covered at 350F for 45 minutes.",
    ],
    faqs: [
      { q: "What mushrooms work best with chicken?", a: "Cremini and button mushrooms are the most accessible and work well in any preparation. Shiitake add deep umami flavor. Oyster mushrooms have a delicate texture. Portobello mushrooms are meaty and substantial." },
      { q: "How do I get mushrooms to brown properly?", a: "Use a hot, dry pan. Do not add oil until the pan is very hot. Cook in small batches without crowding. Do not stir too early — let them sit and develop color before moving." },
      { q: "Can I use canned mushrooms instead of fresh?", a: "Fresh mushrooms will always give better texture and flavor. Canned mushrooms work in soups and sauces where texture matters less. Drain and pat dry thoroughly before using canned mushrooms." },
      { q: "What herbs go best with chicken and mushrooms?", a: "Thyme is the classic pairing. Rosemary adds piney depth. Tarragon gives a French bistro character. Fresh parsley added at the end brightens the whole dish. Sage works particularly well in fall preparations." },
    ],
  },
  "eggs-and-potatoes": {
    title: "6 Easy Recipes with Eggs and Potatoes (Hearty Any-Time Meals)",
    heading: "6 Easy Recipes with Eggs and Potatoes",
    intro: "Eggs and potatoes are a combination beloved across cultures for a simple reason — they are delicious together. Whether you are making a classic American breakfast hash, a Spanish tortilla, or a hearty frittata, eggs and potatoes create filling, satisfying meals that work any time of day. Both are economical, widely available, and packed with nutrients, making this one of the best budget-friendly meal combinations available.",
    ingredients: "eggs,potatoes",
    keywords: ["recipes with eggs and potatoes", "egg and potato recipes", "easy eggs and potatoes dinner", "potato egg hash recipes", "Spanish tortilla recipe"],
    tips: [
      "Par-cook potatoes before combining with eggs so both elements finish at the same time.",
      "Use a well-seasoned cast iron or non-stick pan for the best results with potato and egg dishes.",
      "Dice potatoes uniformly so they cook evenly — larger pieces for roasting, smaller for hash.",
      "Season potatoes generously with salt and pepper before cooking for the most flavorful result.",
      "For frittatas, finish under the broiler rather than flipping for a perfectly set top without risk.",
    ],
    variations: [
      "Hash version: Crispy diced potatoes topped with fried or poached eggs for a classic brunch dish.",
      "Frittata version: Layer sliced cooked potatoes with eggs and cheese, finish under the broiler.",
      "Spanish tortilla version: Slowly cook sliced potatoes in olive oil, combine with eggs, cook on both sides.",
      "Baked version: Nest eggs in a bed of roasted seasoned potatoes, bake until whites are just set.",
      "Scrambled version: Soft scramble eggs with diced sauteed potatoes and onions for a simple meal.",
    ],
    faqs: [
      { q: "How do I make crispy potato hash?", a: "Start with dry, diced potatoes. Cook in a hot pan with oil without stirring for 4-5 minutes to develop a crust, then stir and repeat. Season well and finish with butter for extra flavor." },
      { q: "What is a Spanish tortilla?", a: "A Spanish tortilla is a thick egg and potato omelette cooked slowly in olive oil. Unlike a French omelette, it is flipped and served at room temperature. It is one of the most popular dishes in Spain." },
      { q: "Can eggs and potatoes be meal prepped?", a: "Frittatas and egg casseroles with potatoes meal prep beautifully — make on Sunday and reheat portions throughout the week. Hash is best made fresh as potatoes lose their crispiness when reheated." },
      { q: "What goes well with egg and potato dishes?", a: "Hot sauce, salsa, and ketchup are classic accompaniments. Sour cream pairs wonderfully with potato-forward dishes. A simple green salad balances the richness nicely." },
    ],
  },
  "chicken-and-spinach": {
    title: "6 Easy Recipes with Chicken and Spinach (Healthy Quick Dinners)",
    heading: "6 Easy Recipes with Chicken and Spinach",
    intro: "Chicken and spinach is a powerhouse combination for anyone focused on eating healthily without sacrificing flavor. Spinach wilts quickly and integrates seamlessly into countless dishes, adding nutrition without overwhelming other flavors. Together with chicken, you get a protein and iron-rich meal that comes together quickly and tastes genuinely delicious. These recipes range from simple stuffed chicken to creamy pasta and vibrant salads.",
    ingredients: "chicken,spinach",
    keywords: ["recipes with chicken and spinach", "chicken spinach recipes", "easy chicken and spinach dinner", "healthy chicken spinach meals", "stuffed chicken spinach"],
    tips: [
      "Fresh spinach wilts down dramatically — what looks like a lot will reduce to a small amount.",
      "Add spinach at the very end of cooking to preserve its bright color and nutritional value.",
      "Squeeze excess moisture from thawed frozen spinach before using in stuffed chicken or casseroles.",
      "Baby spinach is more tender and has a milder flavor than mature spinach — better for most recipes.",
      "Garlic and spinach are natural partners — saute garlic first before adding spinach for maximum flavor.",
    ],
    variations: [
      "Stuffed version: Fill chicken breasts with spinach, feta, and garlic, bake at 375F for 25 minutes.",
      "Creamy pasta version: Toss with cream sauce, cooked pasta, and wilted spinach for a one-pan meal.",
      "Salad version: Slice grilled chicken over fresh spinach with your favorite dressing and toppings.",
      "Soup version: Add spinach to chicken broth with diced chicken, white beans, and Italian seasoning.",
      "Stir fry version: Quick cook with garlic, soy sauce, and sesame oil for a light, healthy dinner.",
    ],
    faqs: [
      { q: "Fresh or frozen spinach — which should I use?", a: "Fresh baby spinach is best for salads, stir fries, and dishes where texture matters. Frozen spinach works well in stuffed chicken, casseroles, and soups where it will be cooked down. Always squeeze frozen spinach dry before using." },
      { q: "How do I prevent spinach from getting slimy?", a: "Add spinach at the very end of cooking over high heat. Do not overcook — spinach should just wilt, not stew. Pat dry before adding to hot pans and avoid covering the pan which traps steam." },
      { q: "Is chicken and spinach good for weight loss?", a: "It is an excellent weight loss meal — very high in protein and low in calories. Spinach is extremely nutrient-dense while being almost calorie-free. Together they create a filling, satisfying meal." },
      { q: "What cheese pairs well with chicken and spinach?", a: "Feta is the classic choice — its saltiness and tanginess complement both chicken and spinach perfectly. Parmesan adds savory depth. Ricotta creates a creamy, mild filling in stuffed chicken preparations." },
    ],
  },
  "ground-beef-and-potatoes": {
    title: "6 Easy Recipes with Ground Beef and Potatoes (Hearty Budget Meals)",
    heading: "6 Easy Recipes with Ground Beef and Potatoes",
    intro: "Ground beef and potatoes might be the ultimate budget-friendly comfort food combination. From shepherd's pie to hearty hash and simple one-pot dinners, these two affordable ingredients create meals that are filling, satisfying, and loved by the whole family. Ground beef cooks quickly, potatoes are filling and versatile, and together they create dinners that feel far more substantial than their cost suggests.",
    ingredients: "ground beef,potatoes",
    keywords: ["recipes with ground beef and potatoes", "ground beef potato recipes", "easy ground beef and potatoes", "beef potato dinner", "shepherd pie recipe"],
    tips: [
      "Brown ground beef in batches without crowding for proper caramelization and more flavor.",
      "Pre-cook potatoes partially before combining with beef so both elements finish at the same time.",
      "Drain excess fat from ground beef but leave a tablespoon for flavor when sauteing aromatics.",
      "Season both the beef and potatoes separately for more even, well-distributed flavor.",
      "A splash of Worcestershire sauce adds deep savory flavor to any ground beef and potato dish.",
    ],
    variations: [
      "Shepherd's pie version: Brown beef with vegetables, top with mashed potatoes, bake until golden.",
      "Hash version: Cook diced potatoes until crispy, add seasoned ground beef, serve with eggs.",
      "One pot version: Brown beef, add diced potatoes and broth, simmer until potatoes are tender.",
      "Stuffed potato version: Fill baked potatoes with seasoned ground beef, cheese, and sour cream.",
      "Skillet version: Layer sliced potatoes with ground beef and cheese in a cast iron skillet, bake until bubbly.",
    ],
    faqs: [
      { q: "What is the best way to cook ground beef and potatoes together?", a: "Brown the beef first, remove it, cook the potatoes in the same pan using the rendered fat for flavor, then combine. This ensures both elements are properly cooked without one being over or undercooked." },
      { q: "How do I make shepherd's pie?", a: "Brown ground beef with onions, carrots, and peas. Season with Worcestershire sauce and thyme. Transfer to a baking dish, top with mashed potatoes, brush with butter, and bake at 400F until golden." },
      { q: "What potatoes work best with ground beef?", a: "Russet potatoes are best for mashed potato toppings. Yukon Gold has a naturally buttery flavor. Red potatoes hold their shape well in hashes. All varieties work in one-pot dishes." },
      { q: "How do I make ground beef and potatoes more interesting?", a: "Season boldly with garlic, onion, paprika, and cumin. Add Worcestershire sauce for depth. Include vegetables like peppers and peas. Top with cheese and sour cream. A splash of hot sauce elevates the whole dish." },
    ],
  },
  "chicken-and-tomatoes": {
    title: "6 Easy Recipes with Chicken and Tomatoes (Mediterranean Inspired Dinners)",
    heading: "6 Easy Recipes with Chicken and Tomatoes",
    intro: "Chicken and tomatoes is a classic Mediterranean combination that produces some of the most vibrant, flavorful meals in the culinary world. The acidity of tomatoes tenderizes chicken while adding brightness and depth to any dish. From simple skillet chicken in tomato sauce to baked chicken provencal and hearty stews, this combination works beautifully across cooking methods and cuisine styles. These recipes bring the flavors of the Mediterranean to your weeknight dinner table.",
    ingredients: "chicken,tomatoes",
    keywords: ["recipes with chicken and tomatoes", "chicken tomato recipes", "easy chicken and tomato dinner", "Mediterranean chicken recipes", "Italian chicken tomato sauce"],
    tips: [
      "Use a mix of fresh and canned tomatoes for the best balance of brightness and depth.",
      "Brown chicken well before adding tomatoes — proper searing builds the flavor base for the sauce.",
      "Add a pinch of sugar to tomato-based chicken dishes to balance acidity if needed.",
      "Fresh basil added at the very end of cooking preserves its bright flavor and aroma.",
      "Deglaze the pan with white wine before adding tomatoes to capture all the browned bits.",
    ],
    variations: [
      "Cacciatore version: Braise with tomatoes, olives, capers, and herbs for a classic Italian hunter's stew.",
      "Provencal version: Bake with tomatoes, garlic, olives, and thyme for a French countryside flavor.",
      "Quick skillet version: Saute chicken with cherry tomatoes, garlic, and basil for a 20-minute dinner.",
      "Shakshuka version: Poach eggs in spiced tomato sauce with chicken for a North African inspired dish.",
      "Baked version: Roast chicken thighs over a bed of tomatoes, garlic, and herbs until caramelized.",
    ],
    faqs: [
      { q: "Fresh or canned tomatoes for chicken dishes?", a: "Canned whole or crushed tomatoes are often better for sauces and braises as they are picked and processed at peak ripeness. Fresh tomatoes shine in quick sautes and dishes where they are lightly cooked." },
      { q: "How do I make chicken in tomato sauce?", a: "Brown chicken pieces in olive oil, remove and saute garlic and onion, add crushed tomatoes and herbs, return chicken and simmer covered for 25-30 minutes until tender and sauce has thickened." },
      { q: "What herbs go best with chicken and tomatoes?", a: "Basil is the classic pairing. Oregano and thyme add Mediterranean character. Rosemary works well in roasted preparations. Bay leaves add depth to slow-cooked dishes. Parsley brightens any preparation at the end." },
      { q: "Can I freeze chicken and tomato dishes?", a: "Yes — tomato-based chicken dishes freeze exceptionally well for up to 3 months. The tomato sauce actually improves after freezing as flavors meld together. Thaw overnight in the fridge and reheat gently." },
    ],
  },
  "pasta-and-cheese": {
    title: "6 Easy Recipes with Pasta and Cheese (Ultimate Comfort Food)",
    heading: "6 Easy Recipes with Pasta and Cheese",
    intro: "Pasta and cheese is arguably the greatest comfort food combination ever created. From the creamy indulgence of homemade mac and cheese to elegant cacio e pepe and satisfying baked ziti, these two ingredients together create meals that are universally loved and endlessly satisfying. The beauty of pasta and cheese is its simplicity — with good quality ingredients and the right technique, you can create genuinely spectacular dishes from just a few basic components.",
    ingredients: "pasta,cheese",
    keywords: ["recipes with pasta and cheese", "pasta cheese recipes", "easy pasta and cheese dinner", "mac and cheese recipe", "baked pasta cheese dishes"],
    tips: [
      "Always grate cheese freshly — pre-shredded cheese contains anti-caking agents that prevent smooth melting.",
      "Add cheese off the heat or over very low heat to prevent it from becoming grainy and clumping.",
      "Use starchy pasta water to create silky, emulsified sauces — reserve at least a cup before draining.",
      "A combination of cheeses almost always beats a single cheese for complexity and better melting.",
      "Season pasta water generously with salt — this is your only opportunity to season the pasta itself.",
    ],
    variations: [
      "Mac and cheese version: Make a bechamel, melt cheddar, toss with cooked macaroni, bake with breadcrumbs.",
      "Cacio e pepe version: Toss hot pasta with pecorino romano, black pepper, and pasta water for a Roman classic.",
      "Baked ziti version: Layer pasta with ricotta, mozzarella, and marinara, bake until bubbly and golden.",
      "Carbonara version: Toss pasta with eggs, parmesan, and pancetta for a silky Roman sauce.",
      "Four cheese version: Combine parmesan, gruyere, fontina, and gorgonzola for a decadent pasta dish.",
    ],
    faqs: [
      { q: "What cheese melts best in pasta?", a: "Gruyere, fontina, and young cheddar melt the most smoothly. Parmesan and pecorino add flavor but do not melt as smoothly — combine with a melting cheese for best results. Avoid pre-shredded cheese which contains anti-caking agents." },
      { q: "How do I make mac and cheese from scratch?", a: "Make a bechamel (butter, flour, milk), melt sharp cheddar into it, season with mustard and cayenne, toss with cooked macaroni. Bake with breadcrumbs and more cheese for a crispy top." },
      { q: "Why does my cheese sauce become grainy?", a: "Cheese was added to sauce that was too hot. Always add cheese off the heat or over very low heat, stirring constantly. Adding a teaspoon of cornstarch to shredded cheese before adding helps prevent graining." },
      { q: "What pasta shapes work best with cheese sauces?", a: "Short tubular shapes like penne, rigatoni, and ziti trap cheese sauce inside. Elbow macaroni is classic for mac and cheese. Spaghetti and rigatoni work for cacio e pepe. Wide noodles suit bechamel-based sauces." },
    ],
  },
  "chicken-and-garlic": {
    title: "6 Easy Recipes with Chicken and Garlic (Aromatic Weeknight Dinners)",
    heading: "6 Easy Recipes with Chicken and Garlic",
    intro: "Chicken and garlic is one of the most fundamentally satisfying flavor combinations in all of cooking. The pungent, aromatic quality of garlic transforms simple chicken into something deeply flavorful and memorable. From 40-clove garlic chicken to quick garlic butter pan sauces and roasted garlic dishes, these recipes prove that sometimes the most powerful ingredient in your kitchen is the humble garlic bulb. These are recipes that will fill your kitchen with the most inviting aromas imaginable.",
    ingredients: "chicken,garlic",
    keywords: ["recipes with chicken and garlic", "garlic chicken recipes", "easy chicken and garlic dinner", "roasted garlic chicken", "garlic butter chicken"],
    tips: [
      "Whole roasted garlic cloves become sweet and mellow — very different from raw or quickly cooked garlic.",
      "Mince garlic finely for sauces, slice for stir fries, and use whole cloves for roasting.",
      "Add garlic after browning meat so it does not burn — garlic burns quickly and becomes bitter.",
      "Garlic infused olive oil is a simple way to add garlic flavor without pieces that might burn.",
      "Fresh garlic is always significantly better than pre-minced jarred garlic for these recipes.",
    ],
    variations: [
      "40-clove version: Braise chicken with 40 whole garlic cloves until sweet and tender — a classic French dish.",
      "Garlic butter version: Pan sear chicken, make a quick garlic butter sauce, serve immediately.",
      "Roasted version: Rub chicken with garlic paste and herbs, roast until golden and fragrant.",
      "Lemon garlic version: Brighten with lemon juice and zest for a fresh, vibrant preparation.",
      "Asian version: Marinate with garlic, soy sauce, and ginger for an Asian-inspired preparation.",
    ],
    faqs: [
      { q: "How much garlic should I use with chicken?", a: "For most recipes, 3-6 cloves is a good starting point. For garlic-forward dishes like 40-clove chicken, you can use an entire head. Adjust based on your personal preference — garlic lovers can always add more." },
      { q: "How do I prevent garlic from burning?", a: "Add garlic to a pan that is warm but not smoking hot. Keep the heat at medium and stir frequently. Adding garlic after your protein is browned reduces the risk. Whole cloves and slices are less likely to burn than minced." },
      { q: "What is the easiest garlic chicken recipe?", a: "Pat chicken dry, season with salt and pepper, sear in butter until golden, add minced garlic and more butter, baste the chicken with the garlic butter for 2 minutes, serve immediately. Done in under 20 minutes." },
      { q: "Can I use garlic powder instead of fresh garlic?", a: "Garlic powder works as a substitute but delivers a different, less complex flavor. Use about a quarter teaspoon of garlic powder per garlic clove. For the best results in these recipes, fresh garlic is strongly recommended." },
    ],
  },
  "beef-and-potatoes": {
    title: "6 Easy Recipes with Beef and Potatoes (Hearty Classic Dinners)",
    heading: "6 Easy Recipes with Beef and Potatoes",
    intro: "Beef and potatoes is one of the most classic and universally beloved combinations in home cooking. This hearty pairing appears in virtually every culinary tradition around the world — from American pot roast to Irish beef stew and French beef bourguignon. Both ingredients are filling, nutritious, and become remarkably tender and flavorful when cooked together over time. These recipes celebrate the simple power of beef and potatoes to create deeply satisfying meals.",
    ingredients: "beef,potatoes",
    keywords: ["recipes with beef and potatoes", "beef and potato recipes", "easy beef and potatoes dinner", "beef stew with potatoes", "pot roast with potatoes"],
    tips: [
      "Brown beef in small batches over high heat for the best crust and flavor development.",
      "Cut potatoes into larger chunks for stews so they hold together during long cooking times.",
      "Deglaze the pan with red wine or beef broth after browning beef to capture all the flavor.",
      "Add potatoes in the last 45 minutes of stew cooking so they do not become mushy.",
      "Use tougher, cheaper cuts of beef for stews — they become tender and flavorful with slow cooking.",
    ],
    variations: [
      "Stew version: Braise beef chunks with potatoes, carrots, and onions in beef broth for 2 hours.",
      "Pot roast version: Slow cook a beef chuck roast with whole potatoes and vegetables until fork tender.",
      "Skillet version: Sear thin beef slices with cubed potatoes in a hot pan for a quick dinner.",
      "Slow cooker version: Set and forget — cook on low for 8 hours for incredibly tender results.",
      "Sheet pan version: Roast beef strips and cubed potatoes with garlic and herbs at 425F.",
    ],
    faqs: [
      { q: "What cut of beef is best for beef and potato dishes?", a: "Chuck roast and beef stew meat are ideal for slow-cooked dishes — they become incredibly tender. Sirloin works for quick skillet meals. Short ribs add incredible richness to braised potato dishes." },
      { q: "How do I make beef and potato stew?", a: "Brown beef chunks in batches, saute onions and garlic, add broth, tomato paste, and herbs, return beef, simmer 1 hour, add potatoes and carrots, continue simmering 45 minutes until everything is tender." },
      { q: "How long does beef and potato stew take?", a: "On the stovetop, plan on 2-2.5 hours total for the most tender results. In a slow cooker, 8 hours on low. In a pressure cooker or instant pot, about 45 minutes with natural pressure release." },
      { q: "Can I freeze beef and potato stew?", a: "Yes, but potatoes can become mealy after freezing. For best results, make the stew without potatoes to freeze, then add freshly cooked potatoes when reheating. Alternatively, use waxy potatoes which freeze better than russets." },
    ],
  },
  "chicken-and-lemon": {
    title: "6 Easy Recipes with Chicken and Lemon (Bright Fresh Weeknight Dinners)",
    heading: "6 Easy Recipes with Chicken and Lemon",
    intro: "Chicken and lemon is a combination that instantly elevates any dish from ordinary to extraordinary. The brightness and acidity of lemon cuts through the richness of chicken, creating a fresh, vibrant flavor profile that never feels heavy. From simple pan-seared lemon chicken to roasted lemon herb preparations and light pasta dishes, lemon transforms chicken into something that feels special and restaurant-worthy even on a weeknight.",
    ingredients: "chicken,lemon",
    keywords: ["recipes with chicken and lemon", "lemon chicken recipes", "easy chicken and lemon dinner", "lemon herb chicken", "quick lemon chicken meals"],
    tips: [
      "Use both lemon juice AND zest — the zest contains the most intensely flavored lemon oils.",
      "Add lemon juice at the end of cooking to preserve its bright, fresh flavor — heat dulls it.",
      "Rub lemon zest under chicken skin before roasting for the most intensely flavored result.",
      "Slice lemons and roast alongside chicken — they caramelize and create an incredible pan sauce.",
      "Balance lemon with butter or olive oil — a little fat softens the acidity for a more rounded flavor.",
    ],
    variations: [
      "Pan sauce version: Sear chicken, deglaze with lemon juice and white wine, finish with butter.",
      "Roasted version: Stuff with lemon halves and herbs, roast until golden and fragrant.",
      "Piccata version: Pound thin, dredge in flour, sear quickly, make a lemon caper butter sauce.",
      "Greek version: Marinate with lemon, olive oil, and oregano, grill or bake until tender.",
      "Pasta version: Toss seared chicken with pasta, lemon butter sauce, and parmesan.",
    ],
    faqs: [
      { q: "How much lemon is too much in chicken dishes?", a: "Start with the juice of one lemon and taste before adding more. Too much lemon makes dishes unpleasantly sour. Balance with butter, olive oil, or a pinch of sugar. The zest adds flavor without as much acidity as juice." },
      { q: "Should I marinate chicken in lemon juice?", a: "Limit lemon juice marinades to 30-60 minutes maximum. The acid begins cooking the chicken protein, making the texture chalky if left too long. For longer marinating, use lemon zest with oil rather than juice." },
      { q: "What herbs pair best with chicken and lemon?", a: "Thyme and lemon are a classic combination. Oregano gives a Greek character. Rosemary works well in roasted preparations. Tarragon adds an elegant French bistro quality. Fresh parsley brightens any lemon chicken dish." },
      { q: "How do I make lemon chicken without it being too sour?", a: "Balance the lemon with plenty of fat (butter or olive oil), season generously with salt which rounds out acidity, add a small pinch of sugar if needed, and use lemon zest as the primary flavoring rather than juice." },
    ],
  },
  "pork-and-rice": {
    title: "6 Easy Recipes with Pork and Rice (Global Comfort Food)",
    heading: "6 Easy Recipes with Pork and Rice",
    intro: "Pork and rice is a combination celebrated in cuisines across Asia, Latin America, and Europe for its incredible versatility and satisfying nature. From Filipino adobo to Chinese pork fried rice, Cuban-style pork bowls, and simple pork chops over steamed rice, this combination works beautifully across dozens of flavor profiles. Pork is particularly compatible with rice because its rich fat content creates natural sauces that coat each grain beautifully.",
    ingredients: "pork,rice",
    keywords: ["recipes with pork and rice", "pork rice recipes", "easy pork and rice dinner", "pork fried rice recipe", "pork rice bowls"],
    tips: [
      "Use day-old rice for fried rice — freshly cooked rice contains too much moisture.",
      "Pork shoulder becomes incredibly tender and flavorful after 2+ hours of braising over rice.",
      "Pork belly fat renders beautifully and creates natural sauces that coat rice perfectly.",
      "Season pork with soy sauce, garlic, and ginger for the most versatile Asian-inspired preparations.",
      "Let pork rest before slicing or shredding to prevent moisture loss and maintain juiciness.",
    ],
    variations: [
      "Fried rice version: Stir fry day-old rice with diced pork, soy sauce, eggs, and vegetables.",
      "Adobo version: Braise pork in soy sauce, vinegar, and garlic, serve over steamed white rice.",
      "Bowl version: Slice roasted pork over rice with pickled vegetables and a drizzle of hoisin.",
      "Soup version: Simmer pork ribs or shoulder with rice in broth for a nourishing congee.",
      "One pot version: Brown pork chops, add rice and broth directly, simmer until rice absorbs liquid.",
    ],
    faqs: [
      { q: "What cut of pork works best with rice?", a: "Ground pork is quickest for fried rice and bowls. Pork tenderloin is lean and cooks fast. Pork shoulder becomes wonderfully tender when braised. Pork belly is rich and pairs beautifully with plain steamed rice." },
      { q: "How do I make pork fried rice?", a: "Use day-old rice and very high heat. Stir fry diced pork until cooked, push to the side, scramble eggs, add cold rice and break up any clumps, add soy sauce and sesame oil, toss everything together." },
      { q: "What flavors go best with pork and rice?", a: "Soy sauce, garlic, and ginger are the classic Asian combination. For Latin-inspired dishes, try cumin, oregano, and citrus. Apple and sage create a wonderful European preparation. Fish sauce adds incredible depth." },
      { q: "Can I use any rice with pork?", a: "White rice is the most universal pairing. Jasmine rice works beautifully with Asian pork preparations. Brown rice adds nutrition. Sticky or glutinous rice is traditional with many Southeast Asian pork dishes." },
    ],
  },
  "shrimp-and-pasta": {
    title: "6 Easy Recipes with Shrimp and Pasta (Quick Elegant Dinners)",
    heading: "6 Easy Recipes with Shrimp and Pasta",
    intro: "Shrimp and pasta might be the most impressive quick dinner you can make. Shrimp cook in just 2-3 minutes, meaning the entire dish can be on the table in under 20 minutes. Despite the speed, shrimp and pasta dishes look and taste elegant — perfect for impressing guests or treating yourself on a weeknight. From classic shrimp scampi to spicy arrabbiata and light lemon pasta, these recipes cover the full range of what this outstanding combination can achieve.",
    ingredients: "shrimp,pasta",
    keywords: ["recipes with shrimp and pasta", "shrimp pasta recipes", "easy shrimp and pasta dinner", "shrimp scampi recipe", "quick shrimp noodle dishes"],
    tips: [
      "Do not overcook shrimp — they are done when pink and curled into a C shape, usually 1-2 minutes per side.",
      "Cook shrimp separately and add to pasta at the very end to prevent overcooking while sauce reduces.",
      "Use the shrimp shells to make a quick stock for pasta cooking water — adds incredible flavor.",
      "Pat shrimp dry before cooking for better searing and more flavor development.",
      "Reserve pasta water — the starchy liquid is essential for creating silky, coating sauces.",
    ],
    variations: [
      "Scampi version: Saute shrimp in garlic butter with white wine and lemon, toss with linguine.",
      "Arrabbiata version: Cook shrimp in spicy tomato sauce with plenty of garlic and red pepper flakes.",
      "Creamy version: Toss with a light cream sauce, sun-dried tomatoes, and fresh basil.",
      "Pesto version: Toss simply with basil pesto, cherry tomatoes, and parmesan for speed.",
      "Mediterranean version: Combine with olives, capers, feta, and cherry tomatoes for brightness.",
    ],
    faqs: [
      { q: "What pasta shape works best with shrimp?", a: "Linguine and spaghetti are classic with shrimp scampi and light sauces. Penne and rigatoni work well with chunkier tomato sauces. Angel hair cooks extremely fast and pairs well with delicate shrimp and butter sauces." },
      { q: "Should I use fresh or frozen shrimp for pasta?", a: "Frozen shrimp that you thaw yourself is often fresher than fresh shrimp at the counter which may have been previously frozen. Buy frozen, thaw under cold running water, and pat completely dry before cooking." },
      { q: "How do I make shrimp scampi?", a: "Saute minced garlic in butter and olive oil, add white wine and lemon juice, cook shrimp until pink, toss with cooked linguine and pasta water, finish with parsley and parmesan. Ready in 15 minutes." },
      { q: "How do I prevent shrimp pasta from being watery?", a: "Pat shrimp very dry before cooking. Cook shrimp separately so their liquid does not water down the sauce. Reduce sauce properly before adding pasta. Use pasta water sparingly to adjust consistency." },
    ],
  },
};

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const data = slugData[slug];
  if (!data) return { title: "Recipes | My Recipe Match" };
  return {
    title: data.title + " - My Recipe Match",
    description: data.intro.slice(0, 160),
    keywords: data.keywords,
    alternates: { canonical: "https://www.myrecipematch.com/recipes/" + slug },
    openGraph: {
      title: data.title,
      description: data.intro.slice(0, 160),
      url: "https://www.myrecipematch.com/recipes/" + slug,
      type: "website",
    },
  };
}

export function generateStaticParams() {
  return Object.keys(slugData).map((slug) => ({ slug }));
}

export default async function RecipePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const data = slugData[slug];
  if (!data) return <p>Page not found.</p>;

  let recipes: any[] = [];
  try {
    const apiKey = process.env.SPOONACULAR_API_KEY;
    const res = await fetch(
      "https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + data.ingredients + "&number=6&apiKey=" + apiKey,
      { next: { revalidate: 86400 } }
    );
    recipes = await res.json();
    if (!Array.isArray(recipes)) recipes = [];
  } catch (e) {
    recipes = [];
  }

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    name: data.title,
    description: data.intro.slice(0, 160),
    url: "https://www.myrecipematch.com/recipes/" + slug,
  };

  return (
    <div className="min-h-screen bg-orange-50 flex flex-col">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
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

      <main className="flex-1 max-w-4xl mx-auto w-full px-4 py-10">
        <h2 className="text-3xl font-bold text-gray-800 mb-3">{data.heading}</h2>
        <p className="text-gray-600 mb-6 leading-relaxed">{data.intro}</p>

        <div className="bg-orange-100 border border-orange-200 rounded-2xl p-5 mb-8 flex flex-col sm:flex-row items-center gap-4">
          <div className="flex-1">
            <p className="font-semibold text-orange-800 mb-1">Have different ingredients?</p>
            <p className="text-sm text-orange-700">Enter what you have and instantly find matching recipes.</p>
          </div>
          <a href="/" className="bg-orange-500 hover:bg-orange-600 text-white font-semibold px-6 py-3 rounded-xl text-sm flex-shrink-0">
            Search Your Ingredients
          </a>
        </div>

        {recipes.length > 0 ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
            {recipes.map((recipe: any) => (
              <div key={recipe.id} className="bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-lg transition-shadow flex flex-col">
                <img src={recipe.image} alt={recipe.title} className="w-full h-48 object-cover" />
                <div className="p-4 flex flex-col flex-1">
                  <h3 className="text-base font-bold text-gray-800 mb-2 leading-tight">{recipe.title}</h3>
                  {recipe.usedIngredients && recipe.usedIngredients.length > 0 && (
                    <p className="text-xs text-green-600 mb-1">Uses: {recipe.usedIngredients.map((i: any) => i.name).join(", ")}</p>
                  )}
                  {recipe.missedIngredients && recipe.missedIngredients.length > 0 && (
                    <p className="text-xs text-red-400 mb-3">Also needs: {recipe.missedIngredients.slice(0, 3).map((i: any) => i.name).join(", ")}</p>
                  )}
                  <div className="mt-auto flex flex-col gap-2">
                    <a href={"/?recipeId=" + recipe.id + "&recipeTitle=" + encodeURIComponent(recipe.title) + "&recipeImage=" + encodeURIComponent(recipe.image || "") + "&ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-500 hover:bg-orange-600 text-white font-semibold px-4 py-2 rounded-lg transition-colors text-sm">View Full Recipe</a>
                    <a href={"/?ingredients=" + data.ingredients} className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors text-sm">Find Similar Recipes</a>
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-12 mb-8">
            <p className="text-gray-400">No recipes found. Try searching with your own ingredients!</p>
          </div>
        )}

        <div className="bg-white rounded-2xl shadow-sm p-6 mb-8">
          <h3 className="text-xl font-bold text-gray-800 mb-4">Tips for Cooking {data.heading.replace("Easy Recipes with ", "").replace("Easy ", "").replace(" Recipes", "")}</h3>
          <ul className="space-y-3">
            {data.tips.map((tip, i) => (
              <li key={i} className="flex items-start gap-3">
                <span className="bg-orange-500 text-white text-xs font-bold rounded-full w-5 h-5 flex items-center justify-center flex-shrink-0 mt-0.5">{i + 1}</span>
                <p className="text-sm text-gray-600 leading-relaxed">{tip}</p>
              </li>
            ))}
          </ul>
        </div>

        <div className="bg-white rounded-2xl shadow-sm p-6 mb-8">
          <h3 className="text-xl font-bold text-gray-800 mb-4">Variations to Try</h3>
          <div className="space-y-3">
            {data.variations.map((variation, i) => (
              <div key={i} className="flex items-start gap-3 p-3 bg-orange-50 rounded-xl">
                <span className="text-orange-500 font-bold text-sm flex-shrink-0">→</span>
                <p className="text-sm text-gray-600">{variation}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white rounded-2xl shadow-sm p-6 mb-8">
          <h3 className="text-xl font-bold text-gray-800 mb-4">Frequently Asked Questions</h3>
          <div className="space-y-4">
            {data.faqs.map((faq, i) => (
              <div key={i} className="border-b border-gray-100 pb-4 last:border-0 last:pb-0">
                <h4 className="text-sm font-bold text-gray-800 mb-2">{faq.q}</h4>
                <p className="text-sm text-gray-600 leading-relaxed">{faq.a}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-orange-500 rounded-2xl p-6 mb-8 text-center">
          <h3 className="text-xl font-bold text-white mb-2">Find Recipes With Your Ingredients</h3>
          <p className="text-orange-100 text-sm mb-4">Enter whatever you have at home and instantly find matching recipes — no shopping needed.</p>
          <a href="/" className="inline-block bg-white text-orange-600 font-bold px-8 py-3 rounded-xl hover:bg-orange-50 transition-colors">
            Try My Recipe Match Free
          </a>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
          <p className="col-span-full text-sm font-semibold text-gray-500 mb-1">Browse more recipes:</p>
          {Object.entries(slugData).filter(([s]) => s !== slug).slice(0, 6).map(([s, d]) => (
            <a key={s} href={"/recipes/" + s} className="bg-white hover:bg-orange-50 border border-gray-100 rounded-xl px-3 py-2 text-xs text-gray-600 hover:text-orange-600 transition-colors">
              {d.title.split(" - ")[0]}
            </a>
          ))}
        </div>
      </main>

      <footer className="bg-white border-t border-gray-100 py-4 px-6 text-center text-sm text-gray-400">
        myrecipematch.com · Recipes by Spoonacular · <a href="/privacy" className="hover:text-orange-400">Privacy Policy</a> · <a href="/terms" className="hover:text-orange-400">Terms of Service</a>
      </footer>
    </div>
  );
}
"""

with open("app/recipes/[slug]/page.tsx", "w", encoding="utf-8") as f:
    f.write(page)
print("Done!")