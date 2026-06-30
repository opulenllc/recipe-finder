with open("app/api/contact/route.ts", "rb") as f:
    content = f.read()

old = b'from: `"My Recipe Match Contact" <${process.env.YAHOO_USER}>`,'
new = b'from: process.env.YAHOO_USER,'

if old in content:
    content = content.replace(old, new, 1)
    with open("app/api/contact/route.ts", "wb") as f:
        f.write(content)
    print("Fixed!")
else:
    print("Pattern not found")