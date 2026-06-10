with open("app/blog/[slug]/page.tsx", "rb") as f:
    content = f.read()

content = content.replace(
    b'from "../posts/index"',
    b'from "@/app/blog/posts/index"'
)

with open("app/blog/[slug]/page.tsx", "wb") as f:
    f.write(content)

print("Done")