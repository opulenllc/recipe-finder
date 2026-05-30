with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Remove the pre-fetching code
old = '''      setRecipes(data);
      data.slice(0, 3).forEach((r: any) => {
        fetch("/api/recipes?id=" + r.id + "&type=info").catch(() => {});
        fetch("/api/recipes?id=" + r.id + "&type=instructions").catch(() => {});
      });'''
new = '      setRecipes(data);'

content = content.replace(old, new)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')