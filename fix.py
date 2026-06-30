with open("app/page.tsx", "rb") as f:
    content = f.read()

old = b'transition-colors">About</a>\r\n        <a href="/blog"'
new = b'transition-colors">About</a>\r\n        <a href="/contact" className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors">Contact</a>\r\n        <a href="/blog"'

if old in content:
    content = content.replace(old, new, 1)
    with open("app/page.tsx", "wb") as f:
        f.write(content)
    print("Fixed!")
else:
    print("Pattern not found")