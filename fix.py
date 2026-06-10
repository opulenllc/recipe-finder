with open("app/blog/[slug]/page.tsx", "rb") as f:
    content = f.read()

old = b'type Props = { params: { slug: string } };\nexport async function generateStaticParams() {\n  return posts.map((p) => ({ slug: p.slug }));\n}\nexport async function generateMetadata({ params }: Props): Promise<Metadata> {\n  const post = posts.find((p) => p.slug === params.slug);\n  if (!post) return {};\n  return {\n    title: post.title + " | My Recipe Match Blog",\n    description: post.excerpt,\n  };\n}\nexport default function BlogPostPage({ params }: Props) {\n  const post = posts.find((p) => p.slug === params.slug);\n  if (!post) notFound();'

new = b'type Props = { params: Promise<{ slug: string }> };\nexport async function generateStaticParams() {\n  return posts.map((p) => ({ slug: p.slug }));\n}\nexport async function generateMetadata({ params }: Props): Promise<Metadata> {\n  const { slug } = await params;\n  const post = posts.find((p) => p.slug === slug);\n  if (!post) return {};\n  return {\n    title: post.title + " | My Recipe Match Blog",\n    description: post.excerpt,\n  };\n}\nexport default async function BlogPostPage({ params }: Props) {\n  const { slug } = await params;\n  const post = posts.find((p) => p.slug === slug);\n  if (!post) notFound();'

if old in content:
    content = content.replace(old, new, 1)
    with open("app/blog/[slug]/page.tsx", "wb") as f:
        f.write(content)
    print("Fixed!")
else:
    print("Pattern not found")