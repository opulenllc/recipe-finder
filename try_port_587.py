path = "app/api/contact/route.ts"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''    const transporter = nodemailer.createTransport({
      host: "smtp.mail.yahoo.com",
      port: 465,
      secure: true,
      auth: {
        user: process.env.YAHOO_USER,
        pass: process.env.YAHOO_APP_PASSWORD,
      },
    });'''

new = '''    const transporter = nodemailer.createTransport({
      host: "smtp.mail.yahoo.com",
      port: 587,
      secure: false,
      requireTLS: true,
      auth: {
        user: process.env.YAHOO_USER,
        pass: process.env.YAHOO_APP_PASSWORD,
      },
    });'''

if old in content:
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Switched to port 587 STARTTLS")
else:
    print("Pattern not found")
