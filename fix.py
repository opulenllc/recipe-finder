with open("app/recipes/cuisine/[cuisine]/client.tsx", "rb") as f:
    content = f.read()

old = b'">About</a>\r\n      </div>\r\n    </nav>'
new = b'">About</a>\r\n        <a href="/blog" className="text-xs font-semibold text-gray-600 hover:text-orange-600 px-3 py-1 rounded-lg hover:bg-orange-50 transition-colors">Blog</a>\r\n      </div>\r\n    </nav>'

if old in content:
    content = content.replace(old, new, 1)
    with open("app/recipes/cuisine/[cuisine]/client.tsx", "wb") as f:
        f.write(content)
    print("Fixed!")
else:
    print("Pattern not found")