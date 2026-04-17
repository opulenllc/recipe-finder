with open('app/page.tsx', encoding='utf-8') as f:
    content = f.read()

# Remove duplicate referrerPage state
content = content.replace(
    '  const [referrerPage, setReferrerPage] = useState<string | null>(null);\n  const [referrerPage, setReferrerPage] = useState<string | null>(null);',
    '  const [referrerPage, setReferrerPage] = useState<string | null>(null);'
)

# Remove duplicate referrer detection
content = content.replace(
    '    const referrer = searchParams.get("from");\n    if (referrer) setReferrerPage(decodeURIComponent(referrer));\n    const referrer = searchParams.get("from");\n    if (referrer) setReferrerPage(decodeURIComponent(referrer));',
    '    const referrer = searchParams.get("from");\n    if (referrer) setReferrerPage(decodeURIComponent(referrer));'
)

with open('app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')