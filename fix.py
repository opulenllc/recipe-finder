with open('app/recipes/[slug]/page.tsx', encoding='utf-8') as f:
    lines = f.readlines()

lines[171] = '                    <a\n'
lines[172] = '                      href={"/?ingredients=" + data.ingredients}\n'
lines[173] = '                      className="inline-block w-full text-center bg-orange-100 hover:bg-orange-200 text-orange-700 font-semibold px-4 py-2 rounded-lg transition-colors text-sm"\n'
lines[174] = '                    >\n'

with open('app/recipes/[slug]/page.tsx', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Done!')