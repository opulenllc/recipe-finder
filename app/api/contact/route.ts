import { NextRequest, NextResponse } from "next/server";
import nodemailer from "nodemailer";

export async function POST(req: NextRequest) {
  try {
    const { name, email, message } = await req.json();

    if (!name || !email || !message) {
      return NextResponse.json({ error: "All fields are required." }, { status: 400 });
    }

    // TEMP DEBUG LOGGING - masked for safety
    const user = process.env.YAHOO_USER || "";
    const receiver = process.env.CONTACT_RECEIVER || "";
    console.log("DEBUG user length:", user.length, "first2:", user.slice(0,2), "last4:", user.slice(-4));
    console.log("DEBUG receiver length:", receiver.length, "first2:", receiver.slice(0,2), "last4:", receiver.slice(-4));
    console.log("DEBUG receiver full (TEMP):", JSON.stringify(receiver));

    const transporter = nodemailer.createTransport({
      host: "smtp.mail.yahoo.com",
      port: 587,
      secure: false,
      requireTLS: true,
      auth: {
        user: process.env.YAHOO_USER,
        pass: process.env.YAHOO_APP_PASSWORD,
      },
    });

    await transporter.sendMail({
      from: process.env.YAHOO_USER,
      to: process.env.CONTACT_RECEIVER,
      replyTo: email,
      subject: `New contact from ${name} - My Recipe Match`,
      text: `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`,
      html: `
        <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto;">
          <h2 style="color: #ea580c;">New Contact Form Submission</h2>
          <p><strong>Name:</strong> ${name}</p>
          <p><strong>Email:</strong> <a href="mailto:${email}">${email}</a></p>
          <p><strong>Message:</strong></p>
          <div style="background: #f9fafb; padding: 16px; border-radius: 8px; margin-top: 8px;">
            ${message.replace(/\n/g, "<br>")}
          </div>
          <p style="color: #9ca3af; font-size: 12px; margin-top: 24px;">Sent from myrecipematch.com contact form</p>
        </div>
      `,
    });

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error("Contact form error:", error);
    return NextResponse.json({ error: "Failed to send message. Please try again." }, { status: 500 });
  }
}
