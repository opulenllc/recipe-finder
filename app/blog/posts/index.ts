export type BlogPost = {
  slug: string;
  title: string;
  date: string;
  readTime: string;
  excerpt: string;
  content: string;
};

export const posts: BlogPost[] = [
  {
    slug: "ingredient-combos-that-make-amazing-meals",
    title: "10 Ingredient Combos That Make Amazing Meals (No Recipe Needed)",
    date: "June 1, 2026",
    readTime: "6 min read",
    excerpt:
      "Some ingredient pairings are so natural they barely need a recipe. Here are 10 combinations that reliably produce delicious meals with minimal effort.",
    content: `
      <p>Some ingredients just belong together. Not because a cookbook told you so, but because they share flavors, textures, and cooking times that naturally produce great results. If you understand a handful of these pairings, you can walk to your fridge with almost nothing and still put together something genuinely delicious.</p>

      <p>Here are ten ingredient combinations that work every time — no formal recipe required.</p>

      <h2>1. Chicken + Garlic + Lemon</h2>
      <p>This trio is the foundation of dozens of Mediterranean and Italian dishes. The acid in lemon brightens the richness of chicken while garlic adds depth. Sear chicken in a pan, add sliced garlic, squeeze in lemon juice, and you have a complete dish in 20 minutes. Add herbs if you have them, but they are not essential.</p>

      <h2>2. Eggs + Butter + Fresh Herbs</h2>
      <p>Scrambled eggs cooked slowly in butter with whatever fresh herbs you have — chives, parsley, tarragon — is one of the most underrated meals you can make. The key is low heat and patience. Rushing eggs robs them of their creamy texture. Take five extra minutes and the result is completely different.</p>

      <h2>3. Pasta + Olive Oil + Parmesan</h2>
      <p>The Roman classic aglio e olio proves that great food does not require many ingredients. Cook pasta, reserve some starchy pasta water, saute garlic in olive oil until golden, toss everything together with parmesan. The pasta water emulsifies the oil into a silky sauce. Add chili flakes if you like heat.</p>

      <h2>4. Ground Beef + Onion + Tomatoes</h2>
      <p>This is the base of Bolognese, taco filling, chili, shepherd's pie, and dozens of other dishes. Brown the beef, cook down the onions until sweet, add tomatoes and season generously. From here you can go in any direction depending on what else you have — Italian herbs for pasta, cumin and chili powder for tacos, or beans and broth for chili.</p>

      <h2>5. Rice + Soy Sauce + Egg</h2>
      <p>Fried rice is one of the best ways to use leftover rice. Day-old rice fries better than fresh because it has dried out slightly. Heat oil in a pan until very hot, add rice and let it sit without stirring for a minute to develop some char, push to the side, scramble in an egg, combine and season with soy sauce. Add whatever vegetables or protein you have.</p>

      <h2>6. Potatoes + Rosemary + Olive Oil</h2>
      <p>Roasted potatoes with rosemary are one of life's simple pleasures. Cut potatoes into chunks, toss with olive oil, salt, and fresh or dried rosemary, roast at 425F until golden and crispy. They go with almost any protein and most people will eat them by the handful straight from the pan.</p>

      <h2>7. Shrimp + Garlic + Butter</h2>
      <p>Shrimp cooks in under five minutes, which makes it the perfect weeknight protein. Melt butter in a hot pan, add minced garlic, cook 30 seconds until fragrant, add shrimp and cook two minutes per side. Finish with lemon juice and parsley. Serve over rice, pasta, or with crusty bread to soak up the sauce.</p>

      <h2>8. Salmon + Lemon + Dill</h2>
      <p>Salmon has enough natural flavor that it needs very little help. Lemon and dill are its classic companions for good reason — they complement rather than compete. Season the fillet, roast at 400F for 12 minutes, squeeze lemon over the top, and scatter fresh dill. Simple, healthy, and ready faster than takeout.</p>

      <h2>9. Chickpeas + Spinach + Cumin</h2>
      <p>This vegetarian combination is hearty, satisfying, and comes together in about 15 minutes. Saute garlic and cumin in olive oil, add a can of drained chickpeas and let them crisp slightly, then wilt in spinach and season with salt and lemon. Serve over rice or with flatbread. It punches well above its weight in flavor.</p>

      <h2>10. Banana + Peanut Butter + Oats</h2>
      <p>Not every great combo is a dinner. Mashed banana, peanut butter, and oats baked together make three-ingredient cookies that are genuinely satisfying. Or blend them into a smoothie with milk. Or just eat them as overnight oats. The natural sweetness of banana means you rarely need added sugar.</p>

      <h2>The Underlying Principle</h2>
      <p>What all ten of these combinations share is balance — between rich and bright, heavy and light, savory and aromatic. Once you start to see those patterns, you can start improvising with confidence. You do not need a recipe for every meal. You just need to understand why certain flavors work together.</p>

      <p>That is the whole idea behind ingredient-first cooking — start with what you have, understand the combinations that work, and let that guide you rather than a shopping list.</p>
    `,
  },
  {
    slug: "clean-out-your-fridge-before-grocery-day",
    title: "How to Clean Out Your Fridge Before Grocery Day",
    date: "May 25, 2026",
    readTime: "5 min read",
    excerpt:
      "Grocery day is coming and your fridge is a mystery. Here is a practical, stress-free approach to using up what you have before buying more.",
    content: `
      <p>The day before grocery shopping is one of the most creative cooking opportunities of the week — if you approach it the right way. Instead of ordering takeout because "there is nothing to eat," a quick audit of your fridge and pantry almost always reveals enough for at least one solid meal, often two.</p>

      <p>Here is a practical approach to cleaning out your fridge before grocery day without wasting food or making cooking feel like a chore.</p>

      <h2>Step 1: Do a Full Audit First</h2>
      <p>Pull everything out of the fridge and lay it on the counter. Yes, everything. This sounds excessive but it takes less than five minutes and completely changes how you cook. When ingredients are buried behind other things, your brain does not register them as options. When they are all visible at once, you start to see combinations.</p>
      <p>Group items by type — proteins, vegetables, dairy, condiments, leftovers. Now you can actually see what you are working with.</p>

      <h2>Step 2: Identify What Needs to Go First</h2>
      <p>Some items are more urgent than others. Fresh proteins like chicken, fish, and ground beef should be used first if they are approaching their use-by date. Wilting vegetables can usually be saved by cooking — heat transforms a limp carrot or a slightly soft pepper into something perfectly fine. Leftovers from earlier in the week should be prioritized over fresh items that still have a few days left.</p>
      <p>Make a mental note of your priority order: urgent items first, followed by things that are fine but should not sit another week.</p>

      <h2>Step 3: Build Around Your Protein</h2>
      <p>The easiest way to plan a fridge-clearing meal is to start with whatever protein needs to be used and build everything else around it. If you have chicken thighs that need cooking today, those become the anchor. Now look at your vegetables — whatever you have goes into the pan alongside or underneath the chicken. Whatever grains or starches you have (rice, pasta, potatoes, bread) become the base.</p>
      <p>This approach works because protein drives the cooking method and timing. Everything else is flexible.</p>

      <h2>Step 4: Use Your Condiments and Sauces</h2>
      <p>The door of your fridge is probably full of condiments you forgot about. Soy sauce, hot sauce, mustard, miso paste, fish sauce, tahini, and sriracha are all flavor powerhouses that can transform basic ingredients into something memorable. A plain chicken and vegetable stir fry becomes completely different depending on whether you finish it with soy sauce and sesame oil or fish sauce and lime.</p>
      <p>Before you start cooking, look at your condiment collection. One of those bottles is probably the missing piece that pulls everything together.</p>

      <h2>Step 5: Make One Big Meal, Not Several Small Ones</h2>
      <p>When you are trying to clear out the fridge, resist the urge to make multiple separate dishes. Instead, make one larger meal that uses as many ingredients as possible. A frittata can absorb almost any combination of vegetables and cheese. A fried rice can incorporate any protein and vegetable in the fridge. A soup or stew can take virtually anything.</p>
      <p>These flexible, everything-goes formats are designed for exactly this situation.</p>

      <h2>Step 6: Know What Can Be Frozen</h2>
      <p>If you genuinely cannot use everything before it goes bad, know what can be frozen. Raw meat and fish freeze very well. Cooked grains like rice and pasta freeze fine. Most soups and stews freeze beautifully. Hard cheeses can be frozen and used later in cooking. Bread freezes well and toasts from frozen without any issues.</p>
      <p>Freezing is not failure — it is smart food management. A labeled bag of frozen cooked rice or portioned chicken is a future meal that costs nothing extra.</p>

      <h2>The Bigger Picture</h2>
      <p>Doing this consistently — clearing the fridge before each grocery trip — gradually reduces food waste and grocery spending without requiring much effort. You start to buy less because you waste less. You get better at improvising because you practice it regularly. And you stop feeling that low-grade guilt of throwing away food that never got used.</p>
      <p>The fridge audit before grocery day is one of the simplest habits that makes a real difference.</p>
    `,
  },
  {
    slug: "cooking-with-what-you-have-saves-more-than-you-think",
    title: "Why Cooking With What You Have Saves More Than You Think",
    date: "May 18, 2026",
    readTime: "5 min read",
    excerpt:
      "The average household throws away hundreds of dollars of food each year. Ingredient-first cooking is one of the simplest ways to stop the waste.",
    content: `
      <p>Most people know they waste food. Fewer people realize how much it costs them. Studies consistently show that the average American household throws away between $1,500 and $1,800 worth of food every year. That is not a rounding error — it is a car payment, a vacation, or several months of groceries.</p>

      <p>The waste happens quietly. A bunch of cilantro bought for one recipe, used once, forgotten. A head of lettuce that went soft before it was finished. Leftovers that got pushed to the back of the fridge. A chicken breast that was going to be dinner until it was not.</p>

      <p>Ingredient-first cooking — deciding what to make based on what you already have — is one of the most effective ways to close that gap. Here is why it works.</p>

      <h2>It Changes the Direction of the Decision</h2>
      <p>Recipe-first cooking starts with a dish and works backward to the shopping list. If you want to make chicken tikka masala, you need a specific set of ingredients. If you do not have them, you buy them. Some of those ingredients — a bunch of fresh fenugreek, a can of coconut cream — may only be used partially before they are forgotten.</p>
      <p>Ingredient-first cooking reverses that process. You start with what is already in your kitchen and find recipes that match. The shopping list shrinks because you are already working with what you have. Waste drops because ingredients are used before they expire.</p>

      <h2>It Reduces Impulse Grocery Spending</h2>
      <p>Grocery stores are designed to encourage impulse buying. If you walk in without a clear plan, you will almost certainly leave with things you did not intend to buy. Cooking from your existing inventory reduces how often you need to go to the store, which directly reduces how much you spend.</p>
      <p>People who cook ingredient-first typically find that their grocery trips become more intentional. They go less often and buy with more purpose because they are only shopping for genuine gaps, not ingredients for meals they might make someday.</p>

      <h2>It Gets Better With Practice</h2>
      <p>The first few times you try to cook from whatever is in the fridge, it feels uncertain. You are not sure what goes together. You do not know if the combination will work. That uncertainty fades quickly with experience.</p>
      <p>After a few weeks of ingredient-first cooking, most people develop a strong intuition for what flavors work together, what cooking methods suit different proteins, and how to build a satisfying meal from imperfect starting materials. That skill does not go away. It compounds over time and makes you a more confident, efficient cook.</p>

      <h2>It Produces Surprisingly Good Food</h2>
      <p>Constraint is one of the oldest creative forces in cooking. Many of the world's most beloved dishes were invented as ways to use up leftovers or make the most of scarce ingredients. Fried rice exists because day-old rice fries better than fresh. Frittatas exist as a way to use up vegetable scraps and cheese rinds. French onion soup was born from a need to make something rich and satisfying from very little.</p>
      <p>When you cook from what you have, you often discover combinations you would never have tried if you had started from a recipe. Some of those combinations become favorites.</p>

      <h2>Simple Ways to Start</h2>
      <p>You do not need to overhaul your cooking habits overnight. Start small. Designate one meal per week as a fridge-clearing meal — use up whatever is closest to going bad and find a recipe that fits those ingredients. Use a tool like My Recipe Match to search by ingredients rather than by dish name. Build the habit gradually and let it grow from there.</p>
      <p>The savings and the reduced waste will follow naturally once the habit is in place.</p>
    `,
  },
  {
    slug: "pantry-staples-that-go-with-almost-everything",
    title: "The 5 Pantry Staples That Go With Almost Everything",
    date: "May 10, 2026",
    readTime: "4 min read",
    excerpt:
      "Stock these five ingredients and you will always have the foundation for a great meal, no matter what else is in your fridge.",
    content: `
      <p>A well-stocked pantry is not about having hundreds of ingredients. It is about having the right ones — the ingredients that are versatile enough to work with almost anything else, that have long shelf lives, and that can transform simple proteins and vegetables into complete, satisfying meals.</p>

      <p>Here are five pantry staples that earn their place in any kitchen and that we rely on constantly when building recipes around whatever is already in the fridge.</p>

      <h2>1. Olive Oil</h2>
      <p>Olive oil is the most versatile cooking fat in existence. It works as a cooking medium for sauteing, roasting, and pan frying. It works as a finishing oil drizzled over soups, pastas, and salads. It emulsifies into dressings and sauces. It carries and amplifies other flavors rather than competing with them.</p>
      <p>Keep a larger bottle of regular olive oil for cooking and a smaller bottle of good extra virgin for finishing. The difference in cost is small. The difference in flavor is significant.</p>

      <h2>2. Garlic</h2>
      <p>Garlic is the most widely used flavoring ingredient in the world, and for good reason. It makes almost everything taste better. A few cloves of garlic sauteed in olive oil before adding any protein or vegetable immediately adds depth and aroma that elevates the entire dish.</p>
      <p>Fresh garlic keeps for weeks on the counter and is far superior to garlic powder in most applications. Buy a full head each week and use it freely. You will rarely regret having added garlic to something. You will frequently regret not having added it.</p>

      <h2>3. Canned Tomatoes</h2>
      <p>A can of crushed or diced tomatoes is the foundation of pasta sauces, braises, soups, stews, curries, and countless other dishes. Good quality canned tomatoes — San Marzano if available — have rich, balanced flavor and provide both liquid and body to any dish they are added to.</p>
      <p>Keep at least four cans in your pantry at all times. They have a shelf life of two years, cost very little, and transform a pan of browned meat and vegetables into something that tastes like it cooked for hours.</p>

      <h2>4. Soy Sauce</h2>
      <p>Soy sauce is one of the most efficient flavor tools in cooking. A small amount added to almost anything — soups, stir fries, marinades, braises, even salad dressings — adds a deep, savory umami quality that is difficult to achieve any other way. It works in Asian-inspired dishes obviously, but also in Western ones where you would not necessarily expect it.</p>
      <p>A splash of soy sauce added to a beef stew or a roasting pan of chicken amplifies the savory quality of the meat without tasting distinctly Asian. It is one of those ingredients that chefs use quietly across cuisines to deepen flavor without drawing attention to itself.</p>

      <h2>5. Dried Pasta</h2>
      <p>Dried pasta has an essentially infinite shelf life, costs almost nothing, and can be the base of hundreds of different meals depending on what you pair it with. It absorbs sauces beautifully, fills people up reliably, and goes from dry to dinner in twelve minutes.</p>
      <p>Keep at least three different shapes — a long pasta like spaghetti or linguine, a short pasta like penne or rigatoni, and a small pasta like orzo or ditalini for soups. Different shapes suit different sauces, and having variety gives you more options when you are building a meal around whatever protein and vegetables you have.</p>

      <h2>What These Five Have in Common</h2>
      <p>Every one of these staples shares the same qualities: long shelf life, low cost, high versatility, and the ability to make other ingredients taste better. They are not the stars of the meal — they are the supporting cast that makes the stars shine. With these five items in your pantry, you can take almost any protein or vegetable from the fridge and turn it into a complete, satisfying dinner.</p>
      <p>Build your pantry around ingredients like these, and you will find yourself needing to grocery shop less while eating better.</p>
    `,
  },
  {
    slug: "what-to-cook-with-20-minutes-and-random-ingredients",
    title: "What to Cook When You Only Have 20 Minutes and Random Ingredients",
    date: "May 3, 2026",
    readTime: "5 min read",
    excerpt:
      "It is 6pm, you are tired, and dinner needs to happen. Here is how to turn whatever is in your kitchen into something genuinely good in under 20 minutes.",
    content: `
      <p>Six o'clock on a weeknight. You are tired, possibly hungry already, and the last thing you want to do is spend 45 minutes cooking. You open the fridge and see a loosely related collection of ingredients that do not obviously go together. Takeout is tempting.</p>

      <p>But here is the thing: almost any combination of protein, vegetable, and starch can be turned into a genuinely satisfying meal in 20 minutes or less if you know the right approach. The key is not having the perfect ingredients — it is knowing which cooking methods are fast and which flavor combinations work reliably.</p>

      <h2>The 20-Minute Framework</h2>
      <p>Start by identifying what you have in three categories: protein, vegetable, and base. You do not need all three — two is often enough. But knowing which category each ingredient falls into helps you decide how to cook it and how long it will take.</p>
      <p>Proteins: eggs, chicken breast or thighs, shrimp, ground beef, canned tuna, tofu, leftover cooked meat. Vegetables: anything in the fridge — peppers, zucchini, spinach, broccoli, carrots, tomatoes, onions. Base: pasta, rice (especially leftover rice), bread, potatoes, noodles.</p>

      <h2>The Fastest Cooking Methods</h2>
      <p>When time is short, your cooking method matters more than your ingredients. These four methods are fast, require minimal cleanup, and work with almost any combination of ingredients.</p>

      <p><strong>The hot pan saute.</strong> Heat oil in a pan until very hot. Add protein, cook without moving for two minutes to develop a sear, flip, cook two more minutes. Remove. Add vegetables to the same pan, cook three to four minutes. Season everything generously, combine, serve. Total time: 12 to 15 minutes.</p>

      <p><strong>The sheet pan roast.</strong> Preheat oven to 425F. Toss protein and vegetables with olive oil and salt on a sheet pan. Roast for 20 minutes. This is the most hands-off method and produces great results with almost any combination. The high heat caramelizes everything and concentrates flavor.</p>

      <p><strong>The egg rescue.</strong> When you genuinely have nothing else, eggs are always the answer. A frittata, a scramble with whatever vegetables are in the fridge, or eggs fried in butter and served over toast — any of these takes under ten minutes and is more satisfying than it sounds.</p>

      <p><strong>The fried rice method.</strong> If you have leftover rice in the fridge (and you should always try to have some), fried rice comes together in eight minutes. High heat, oil, rice pressed flat in the pan, soy sauce, whatever protein and vegetable you have, an egg scrambled in at the end. Done.</p>

      <h2>The Flavor Shortcuts</h2>
      <p>The difference between a meal that tastes thrown together and one that tastes intentional is usually seasoning and finish. These three shortcuts do most of the work.</p>
      <p>Acid at the end — a squeeze of lemon or lime, a splash of vinegar — brightens everything and makes it taste complete. Fat as a finish — a knob of butter stirred in at the end, a drizzle of good olive oil — adds richness and rounds out sharp edges. One bold seasoning — a spoonful of soy sauce, a teaspoon of fish sauce, a spoonful of miso stirred into a sauce — adds the kind of savory depth that makes a meal taste like it took longer than it did.</p>

      <h2>Stop Waiting for the Right Ingredients</h2>
      <p>The biggest obstacle to cooking on busy weeknights is not actually time — it is the feeling that you do not have the right things. That feeling is almost always wrong. The ingredients sitting in your fridge right now can almost certainly be turned into something good in 20 minutes if you approach them with a method rather than a recipe.</p>
      <p>Use My Recipe Match to search by whatever you have. Pick the fastest result. Cook it. Dinner is done before the delivery estimate would have updated.</p>
    `,
  },
];
