with open("app/blog/page.tsx", "rb") as f:
    content = f.read()

old = b'Read more \xe2\x86\x92\n                </span>\n              </article>'
new = b'Read more \xe2\x86\x92\n                </span>\n                </div>\n              </article>'

if old in content:
    content = content.replace(old, new, 1)
    with open("app/blog/page.tsx", "wb") as f:
        f.write(content)
    print("Fixed!")
else:
    print("Pattern not found")