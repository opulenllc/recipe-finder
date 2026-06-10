path = "app/blog/page.tsx"

with open(path, "rb") as f:
    content = f.read()

# Replace the local posts array with an import from the shared index
old = b'import Link from "next/link";\n\nexport const metadata'
new = b'import Link from "next/link";\nimport { posts } from "./posts/index";\n\nexport const metadata'

fixed1 = False
if old in content:
    content = content.replace(old, new, 1)
    fixed1 = True

# Remove the local hardcoded posts array (from "const posts = [" to the closing "];" before the export)
import re
content = re.sub(b'\r?\nconst posts = \[.*?\];\n\nexport default', b'\n\nexport default', content, flags=re.DOTALL)

with open(path, "wb") as f:
    f.write(content)

print(f"import added: {fixed1}")
print("Done!")