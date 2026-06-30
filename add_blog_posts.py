path = "app/blog/posts/index.ts"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

new_posts = '''  {
    slug: "beginners-guide-to-cooking-chicken-without-drying-it-out",
    image: "https://images.unsplash.com/photo-1604503468506-a8da13d11d36?w=800&q=80",
    title: "The Beginner's Guide to Cooking Chicken Without Drying It Out",
    date: "June 8, 2026",
    readTime: "6 min read",
    excerpt:
      "Dry, rubbery chicken is one of the most common cooking frustrations. Here is exactly why it happens and how to fix it for good.",
    content: `
      <p>Dry chicken is one of the most discouraging things that can happen in a home kitchen. You follow the recipe, you cook it through, and somehow you still end up with something that tastes like sawdust. The good news is that dry chicken is almost always caused by one of a handful of fixable mistakes — and once you understand them, you will never make them again.</p>

      <h2>Why Chicken Dries Out</h2>
      <p>Chicken dries out for one fundamental reason: it has been cooked past the point where its proteins can retain moisture. Chicken breast is particularly unforgiving because it is very lean — there is almost no fat to compensate for overcooking. When the internal temperature goes past about 165F, the muscle fibers contract aggressively and squeeze out the moisture they were holding. The result is dry, chalky meat.</p>
      <p>The problem is compounded by the fact that chicken looks done before it actually is — the outside browns and firms up long before the inside reaches a safe temperature. This tempts cooks to pull it early, then leave it on heat "just a little longer" to be sure, which pushes it past the point of no return.</p>

      <h2>The Most Important Tool You Can Own</h2>
      <p>A meat thermometer costs less than ten dollars and completely solves the overcooking problem. Insert it into the thickest part of the chicken, away from bone, and pull the chicken when it reads 160F. Carry-over cooking will bring it to 165F as it rests. This single habit eliminates dry chicken almost entirely.</p>
      <p>If you do not have a thermometer yet, the visual test is to cut into the thickest part — the juices should run clear and the meat should be white with no pink, but still look moist rather than chalky. The moment it looks dry inside, it is already overcooked.</p>

      <h2>Pound Chicken Breasts Flat</h2>
      <p>Chicken breasts are thicker at one end than the other, which means the thin end overcooks by the time the thick end is done. Placing the breast in a zip-lock bag and pounding it to an even thickness with a rolling pin or heavy pan takes about 30 seconds and solves this completely. Even thickness means even cooking throughout.</p>
      <p>Alternatively, butterfly the breast by cutting it horizontally almost all the way through and opening it like a book. This halves the cooking time and dramatically reduces the chance of drying out.</p>

      <h2>Brine for Insurance</h2>
      <p>Brining is the process of soaking chicken in salted water before cooking. The salt causes the muscle fibers to absorb and retain more water, which gives you a buffer against overcooking. A simple brine is just one tablespoon of salt dissolved in one cup of water. Submerge the chicken for 15 to 30 minutes, rinse, pat dry, and cook as normal.</p>
      <p>Even a quick 15-minute brine makes a noticeable difference in how juicy the final result is. If you have time for nothing else, this one step will improve your chicken more than anything except a thermometer.</p>

      <h2>Let It Rest</h2>
      <p>Cutting into chicken immediately after cooking lets the juices run out onto the cutting board instead of staying in the meat. Resting the chicken for five minutes after cooking allows the juices to redistribute back into the muscle fibers. Cover it loosely with foil and leave it alone. The difference in juiciness between rested and immediately cut chicken is significant and requires no extra skill — just patience.</p>

      <h2>Choose the Right Cut</h2>
      <p>Chicken thighs are far more forgiving than breasts. They have more fat and connective tissue, which means they stay moist even if you cook them slightly past the ideal temperature. If you consistently struggle with dry chicken, switching to thighs solves the problem immediately. They are also cheaper, more flavorful, and work in virtually every recipe that calls for chicken breast.</p>

      <h2>Cooking Methods That Protect Moisture</h2>
      <p>Some cooking methods are more forgiving than others. Braising — cooking chicken in liquid in a covered pot — makes it almost impossible to dry out because the steam keeps the meat moist throughout. Poaching in barely simmering water or broth produces the most tender, juicy chicken possible, though without any browning. Roasting at moderate heat (375F) is more forgiving than high-heat methods. Pan searing on high heat is fast and delicious but the least forgiving — it requires a thermometer and attentive timing.</p>

      <p>Once you internalize these principles — even thickness, a thermometer, a brief rest — dry chicken becomes a thing of the past. It is one of those cooking problems that feels mysterious until you understand the cause, and then becomes completely straightforward to prevent.</p>
    `,
  },
  {
    slug: "how-to-turn-leftovers-into-a-completely-different-meal",
    image: "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=800&q=80",
    title: "How to Turn Leftovers Into a Completely Different Meal",
    date: "June 15, 2026",
    readTime: "5 min read",
    excerpt:
      "Eating the same meal twice is fine. Transforming last night's dinner into something completely new is better. Here is how to do it consistently.",
    content: `
      <p>Leftovers have a reputation problem. The word itself implies something lesser — food that was not good enough to finish the first time. But the best home cooks think about leftovers differently. They cook with the second meal in mind, intentionally making more than they need so that tomorrow's dinner is already halfway done.</p>

      <p>The key is transformation — not reheating the same dish, but using the components of one meal as the starting point for something that tastes completely different.</p>

      <h2>The Components Mindset</h2>
      <p>Most meals are made of components: a protein, a starch or grain, and some vegetables. When you think about leftovers at the component level rather than the dish level, the possibilities multiply dramatically.</p>
      <p>Last night's roast chicken is not just leftover roast chicken — it is cooked chicken, which can become tacos, chicken salad, soup, fried rice, pasta, or a grain bowl. Last night's roasted vegetables are not just reheated sides — they are already-cooked vegetables that can go into an omelette, a frittata, a sandwich, or a sauce. Thinking in components rather than dishes is the fundamental shift that makes leftover transformation natural.</p>

      <h2>The Best Leftover Transformations</h2>

      <p><strong>Cooked rice → Fried rice.</strong> Day-old rice is actually better for fried rice than freshly cooked rice because it has dried out slightly and fries rather than steams. Heat oil in a wok or large pan until very hot, add the rice and press it flat, let it sit for a minute to develop some char, then toss with soy sauce, a scrambled egg, and whatever protein and vegetables you have. This is one of the fastest and most satisfying leftover transformations possible.</p>

      <p><strong>Roasted vegetables → Frittata or omelette.</strong> Already-cooked vegetables go directly into eggs without any prep. Scatter them in an oven-safe pan, pour beaten eggs over the top, cook on the stovetop until the edges set, then finish under the broiler for two minutes. Add cheese if you have it. A frittata made from leftover roasted vegetables is genuinely better than one made from raw vegetables because the flavors have already concentrated.</p>

      <p><strong>Cooked chicken → Tacos or grain bowls.</strong> Shred any cooked chicken with two forks. Season with cumin, lime juice, and salt for tacos, or with soy sauce and sesame oil for an Asian-style grain bowl. Cooked chicken absorbs new seasonings very well, which is why it transforms so easily into dishes with completely different flavor profiles.</p>

      <p><strong>Leftover soup or stew → Pasta sauce.</strong> Many soups and stews reduce beautifully into pasta sauces. Simmer the leftovers in a pan until thickened, taste and adjust seasoning, toss with cooked pasta. A leftover lentil soup becomes a hearty pasta sauce. A beef stew becomes a rich Bolognese-style topping for pappardelle.</p>

      <p><strong>Cooked grains → Salad base.</strong> Leftover quinoa, farro, barley, or rice make excellent bases for grain salads. Toss with olive oil, lemon juice, whatever vegetables are in the fridge, fresh herbs, and a handful of nuts or cheese. Grain salads are served at room temperature, which means the leftovers do not need to be reheated at all.</p>

      <h2>The Flavor Reset Technique</h2>
      <p>The reason transformed leftovers can taste completely different from the original dish is that you are applying a new flavor profile over a neutral base. The trick is to use enough of the new seasoning to genuinely override the original. A squeeze of lime and a spoonful of fish sauce will make yesterday's plain rice taste completely Southeast Asian. A generous amount of cumin, smoked paprika, and garlic will make leftover chicken taste like it was always destined for tacos.</p>
      <p>Do not be shy with seasoning when transforming leftovers. The original dish's flavors need to be redirected, not just supplemented.</p>

      <h2>Plan for It</h2>
      <p>The most effective approach is to cook extra intentionally. When you make rice, make double. When you roast vegetables, fill the pan. When you cook chicken, cook two extra pieces. This costs almost no extra effort and gives you a meaningful head start on the next day's meal. Ingredient-first cooking and leftover transformation work together — they are both about making the most of what you already have.</p>
    `,
  },
  {
    slug: "10-things-you-can-make-with-a-can-of-chickpeas",
    image: "https://images.unsplash.com/photo-1515543237350-b3eea1ec8082?w=800&q=80",
    title: "10 Things You Can Make With a Can of Chickpeas",
    date: "June 22, 2026",
    readTime: "5 min read",
    excerpt:
      "A can of chickpeas is one of the most versatile things in your pantry. Here are 10 genuinely different meals you can make with one.",
    content: `
      <p>A can of chickpeas costs less than a dollar, lasts years in the pantry, and is one of the most nutritionally complete foods you can eat — high in protein, fiber, and complex carbohydrates. It is also remarkably versatile. Here are ten genuinely different things you can make with a single can.</p>

      <h2>1. Hummus</h2>
      <p>Drain and rinse the chickpeas, blend with tahini, lemon juice, garlic, olive oil, and a pinch of salt until smooth. Add a tablespoon or two of ice water while blending for a creamier texture. Homemade hummus takes five minutes and tastes dramatically better than store-bought. Serve with bread, vegetables, or crackers.</p>

      <h2>2. Roasted Chickpeas</h2>
      <p>Drain, rinse, and dry the chickpeas thoroughly. Toss with olive oil, salt, and whatever spice you like — smoked paprika, cumin, curry powder, or garlic powder all work well. Roast at 400F for 25 to 30 minutes, shaking the pan halfway, until crispy. Eat as a snack or use as a crunchy salad topping instead of croutons.</p>

      <h2>3. Chickpea Curry</h2>
      <p>Saute onion and garlic in oil, add curry powder or paste and cook one minute, add the drained chickpeas and a can of crushed tomatoes or coconut milk, simmer 15 minutes. Serve over rice with fresh cilantro. This is one of the fastest and most satisfying vegetarian dinners possible from pantry ingredients alone.</p>

      <h2>4. Chickpea and Spinach Stew</h2>
      <p>Cook garlic and cumin in olive oil, add the chickpeas and enough broth to cover, simmer five minutes, add several large handfuls of spinach and stir until wilted. Season with lemon juice and salt. This Mediterranean-inspired stew comes together in 15 minutes and is nutritionally exceptional.</p>

      <h2>5. Chickpea Salad</h2>
      <p>Combine drained chickpeas with diced cucumber, cherry tomatoes, red onion, feta cheese, and fresh herbs. Dress with olive oil, lemon juice, salt, and pepper. This is a complete, protein-rich meal that requires zero cooking and comes together in five minutes.</p>

      <h2>6. Pasta e Ceci</h2>
      <p>This classic Italian dish — pasta with chickpeas — is one of the great peasant dishes of Rome. Saute garlic in olive oil, add chickpeas and mash about a third of them against the pan to thicken the sauce, add broth and bring to a simmer, cook small pasta directly in the broth until tender. Finish with olive oil and parmesan. It is hearty, inexpensive, and deeply satisfying.</p>

      <h2>7. Chickpea Tacos</h2>
      <p>Drain chickpeas and cook in a hot pan with cumin, chili powder, garlic powder, and a splash of lime juice until slightly crispy. Serve in warm tortillas with avocado, salsa, and shredded cabbage. These are a genuinely good vegetarian taco that even committed meat eaters tend to enjoy.</p>

      <h2>8. Shakshuka with Chickpeas</h2>
      <p>Add drained chickpeas to a spiced tomato sauce alongside the eggs in classic shakshuka. The chickpeas absorb the tomato flavor beautifully and make the dish substantially more filling. This is an excellent way to turn a breakfast dish into a complete dinner.</p>

      <h2>9. Chickpea Soup</h2>
      <p>Saute onion, carrot, and celery in olive oil until soft, add garlic, add chickpeas and enough broth to cover generously, simmer 20 minutes. Blend half the soup for a creamy-chunky texture, or leave it fully chunky. Add a rind of parmesan while it simmers for remarkable depth of flavor. Serve with crusty bread.</p>

      <h2>10. Aquafaba Meringues</h2>
      <p>Do not throw away the liquid from the can. Aquafaba — the starchy liquid chickpeas are canned in — whips into stiff peaks just like egg whites and can be used to make meringues, mousses, and even macarons. Three tablespoons of aquafaba equals one egg white. It is one of the most surprising and useful cooking discoveries of the last decade.</p>

      <p>One can of chickpeas. Ten completely different directions. Keep a few cans in your pantry at all times and you will always have the foundation for a nutritious, satisfying meal.</p>
    `,
  },
  {
    slug: "why-meal-prepping-one-ingredient-beats-prepping-full-meals",
    image: "https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=800&q=80",
    title: "Why Meal Prepping One Ingredient Beats Prepping Full Meals",
    date: "June 29, 2026",
    readTime: "5 min read",
    excerpt:
      "Full meal prep sounds efficient but often leads to food fatigue by Wednesday. Prepping one versatile ingredient gives you more flexibility with less effort.",
    content: `
      <p>Meal prep culture has a problem. The standard advice — spend Sunday cooking five identical lunches and five identical dinners, portion them into containers, eat the same thing every day — works for about two days before food fatigue sets in. By Wednesday, you are staring at your fourth consecutive chicken and rice bowl wondering why you even bothered.</p>

      <p>There is a better approach: prep one highly versatile ingredient instead of complete meals. It takes less time, produces more variety, and actually gets eaten.</p>

      <h2>What Is Single-Ingredient Prep?</h2>
      <p>Instead of cooking complete dishes on Sunday, you cook one foundational ingredient in a large batch and then use it in different ways throughout the week. The ingredient you choose should be versatile enough to work in multiple different flavor contexts — so that Tuesday's use feels completely different from Monday's.</p>
      <p>The best candidates are proteins and grains, because they absorb new flavors easily and work as the base for countless different dishes.</p>

      <h2>The Best Ingredients to Batch Cook</h2>

      <p><strong>Chicken thighs.</strong> Roast a full tray of bone-in, skin-on chicken thighs with just salt, pepper, and olive oil. Once cooked, the meat shreds easily and can go into tacos on Monday, a grain bowl on Tuesday, soup on Wednesday, and pasta on Thursday. Each meal tastes completely different because the chicken is a neutral protein that takes on whatever flavors you apply to it.</p>

      <p><strong>Grains.</strong> A large pot of cooked grains — rice, quinoa, farro, or barley — takes 20 to 45 minutes of mostly hands-off cooking and lasts five days in the fridge. Use it as a base for bowls, stir it into soups, fry it with eggs and vegetables, or serve it alongside whatever protein you cook fresh each night. Having cooked grains in the fridge cuts 20 minutes off every weeknight dinner.</p>

      <p><strong>Hard boiled eggs.</strong> Cook a dozen eggs at the start of the week. They last seven days in the fridge, require zero reheating, and can be eaten as a snack, sliced over salads, used in sandwiches, turned into egg salad, or served alongside whatever else you are eating. They are the ultimate low-effort, high-return prep ingredient.</p>

      <p><strong>Roasted vegetables.</strong> Roast two or three sheet pans of mixed vegetables — whatever needs to be used up. Already-cooked vegetables can go into omelettes, grain bowls, sandwiches, soups, and pasta dishes throughout the week. They take about 25 minutes of active oven time and make every subsequent meal faster.</p>

      <h2>Why This Works Better Than Full Meal Prep</h2>
      <p>Full meal prep locks you into specific dishes for the entire week. If your plans change, if you are hungrier or less hungry than expected, or if you simply stop wanting to eat that particular thing, you are stuck. Single-ingredient prep gives you components that can be assembled differently each day depending on what sounds good in the moment.</p>
      <p>It also requires significantly less cooking time. Roasting a tray of chicken thighs takes 35 minutes. Cooking a pot of rice takes 20 minutes. That is under an hour of actual cooking to set yourself up for a full week of faster dinners — compared to the two or three hours that full meal prep typically requires.</p>

      <h2>How to Apply This</h2>
      <p>Pick one protein and one grain each week. Cook them simply and store them in the fridge. Then, each evening, combine them with whatever fresh vegetables you have, apply a different flavor profile — Italian herbs and olive oil one night, soy sauce and ginger the next, cumin and lime the night after — and you have a genuinely different meal each time from the same two base ingredients.</p>
      <p>This is ingredient-first cooking applied to meal planning. Start with what you have, build flexibility into the system, and let the week's meals evolve naturally rather than locking yourself into a rigid schedule that falls apart by midweek.</p>
    `,
  },
  {
    slug: "best-spice-combinations-every-home-cook-should-know",
    image: "https://images.unsplash.com/photo-1532336414038-cf19250c5757?w=800&q=80",
    title: "The Best Spice Combinations Every Home Cook Should Know",
    date: "July 6, 2026",
    readTime: "6 min read",
    excerpt:
      "Knowing five spice combinations by heart is more useful than owning fifty spices. Here are the combinations that unlock entire cuisines.",
    content: `
      <p>Most home cooks have a drawer or cabinet full of spices they do not fully use. They buy a jar of something for a specific recipe, use a teaspoon, and then the jar sits there for two years. The result is a large collection of aging spices and a persistent feeling that something is missing from home-cooked food.</p>

      <p>The problem is not the number of spices — it is not knowing which ones to combine. A handful of spice combinations, memorized and applied consistently, will transform your everyday cooking more than any individual spice ever could.</p>

      <h2>Italian: Garlic + Oregano + Basil</h2>
      <p>This is the flavor base of Italian-American cooking. Garlic provides the savory foundation, dried oregano adds a slightly bitter herbal note, and basil — fresh if available, dried otherwise — contributes sweetness and aroma. Use this combination in pasta sauces, on pizza, with roasted chicken, or in any dish where you want an Italian flavor profile. Add a pinch of red pepper flakes for heat and a drizzle of olive oil as a finishing touch.</p>
      <p>The ratio: equal parts oregano and basil, with garlic used more generously than both.</p>

      <h2>Mexican: Cumin + Chili Powder + Smoked Paprika</h2>
      <p>Cumin is the dominant flavor in most Mexican and Tex-Mex cooking — earthy, warm, and slightly nutty. Chili powder adds heat and complexity. Smoked paprika contributes a subtle smokiness that mimics the flavor of dried chiles without requiring specialty ingredients. Together they create the flavor profile of tacos, enchiladas, fajitas, and chili.</p>
      <p>Use this combination on chicken, ground beef, beans, or roasted vegetables. Add garlic powder and a squeeze of lime to complete the flavor. The ratio: two parts cumin to one part chili powder to one part smoked paprika.</p>

      <h2>Indian: Cumin + Coriander + Turmeric</h2>
      <p>This trio is the base of countless Indian dishes, from simple dal to complex curries. Cumin provides warmth, coriander adds a citrusy brightness, and turmeric gives the characteristic golden color and a mild earthy bitterness. Bloom these spices in hot oil for 30 seconds before adding other ingredients — this step, called tempering, dramatically intensifies their flavor.</p>
      <p>Add garam masala at the end of cooking for depth and complexity. Fresh ginger and garlic complete the base. The ratio: equal parts cumin and coriander, with turmeric used more sparingly — about half as much as the others.</p>

      <h2>Middle Eastern: Za'atar + Sumac</h2>
      <p>Za'atar is a blend of dried thyme, sesame seeds, and sumac that is used across Lebanese, Israeli, and Syrian cooking. Sumac on its own — a deep red berry ground into a tart powder — adds a lemony acidity that brightens any dish. Together they transform roasted chicken, grilled vegetables, eggs, and flatbread into something that tastes distinctly of the eastern Mediterranean.</p>
      <p>Both are increasingly available in mainstream supermarkets. Mix za'atar with olive oil to make a paste for marinating chicken or spreading on bread before toasting.</p>

      <h2>Chinese Five Spice: Star Anise + Cloves + Cinnamon + Sichuan Pepper + Fennel</h2>
      <p>Five spice powder is one of the great flavor shortcuts in Chinese cooking — a single jar that contains the complex, warming spice profile used in red-braised pork, Peking duck, and countless other dishes. It is intensely flavored, so use it sparingly — a quarter teaspoon is often enough to transform an entire dish. Use it in marinades for pork or duck, add a pinch to stir fry sauces, or mix with soy sauce and honey for a quick glaze.</p>

      <h2>How to Apply This Knowledge</h2>
      <p>Memorize these five combinations and you have unlocked five completely different culinary traditions using ingredients that are available in any grocery store. When you look at what is in your fridge and cannot decide what to make, the question becomes: which of these flavor profiles fits what I have? Chicken can go Italian, Mexican, Indian, Middle Eastern, or Chinese depending entirely on which spice combination you reach for.</p>
      <p>That is the real power of knowing your spice combinations — they give you a framework for improvising confidently with whatever ingredients you already have.</p>
    `,
  },'''

# Insert before the closing bracket of the posts array
marker = "];\n"
last_idx = content.rfind(marker)

if last_idx != -1:
    content = content[:last_idx] + new_posts + "\n" + content[last_idx:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done! 5 new posts added.")
else:
    print("Marker not found")
