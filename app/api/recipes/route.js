export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const ingredients = searchParams.get("ingredients");
  const url = "https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + ingredients + "&number=9&apiKey=6b6dd0f982c448f7adef501f6ca84f88";
  try {
    const res = await fetch(url);
    const data = await res.json();
    return Response.json(data);
  } catch (error) {
    return Response.json({ error: "Failed" }, { status: 500 });
  }
}
