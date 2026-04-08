export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const ingredients = searchParams.get("ingredients");
  const id = searchParams.get("id");
  const apiKey = "6b6dd0f982c448f7adef501f6ca84f88";

  if (id) {
    try {
      const res = await fetch("https://api.spoonacular.com/recipes/" + id + "/analyzedInstructions?apiKey=" + apiKey);
      const data = await res.json();
      return Response.json(data);
    } catch (error) {
      return Response.json([], { status: 500 });
    }
  }

  try {
    const res = await fetch("https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + ingredients + "&number=9&apiKey=" + apiKey);
    const data = await res.json();
    return Response.json(data);
  } catch (error) {
    return Response.json({ error: "Failed to fetch recipes" }, { status: 500 });
  }
}
