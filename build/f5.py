import sys

from pflib import Doc

OUT = sys.argv[1]
S = 11


def build():
    d = Doc("template.docx", margins=0.8, footer="Session 5 · Facilitator Notes")
    d.h1("Session 5 Facilitator Notes")
    d.p("**Building Wealth (optional session).** Use with the Session 5 guide, which you and the "
        "group read together.", size=S, after=4)

    d.h2("Session goals")
    d.p("By the end of the session, each person should:", size=S, after=2)
    d.bullets([
        "Recognize and celebrate the progress they’ve made",
        "See “wealth” as enough, with peace of mind and room to help others, not riches",
        "Understand that time helps small amounts grow, and that it’s never too late to start",
        "Know the difference between saving and investing, and the value of a job match",
        "Know the warning signs of scams",
        "Leave with a **My Next Steps Plan** and a buddy to check in with monthly",
    ], size=S, after=1)
    d.p("This is a celebration as much as a lesson. If people leave hopeful and connected, the "
        "session worked.", size=S, after=4)

    d.h2("Your role")
    d.p("As before, you guide the council rather than teach it. Ask for volunteers to read; never "
        "call on anyone. **Don’t give investment advice** or recommend specific companies or "
        "products. Keep it simple: safety net first, costly debt next, then saving for later, "
        "and always get a job match. For detailed questions, point people to their job’s HR "
        "office, free tax help (VITA), or a fee-only advisor.", size=S, after=4)

    d.h2("How to prepare")
    d.bullets([
        "Read the guide and practice explaining the $25-a-month table in your own words.",
        "Find the nearest free tax help site (VITA) and add it to the resource list.",
        "Bring guides, pens, the resource list, and, if you like, simple certificates of "
        "completion with each person’s name.",
        "Consider light refreshments to celebrate, and think about planning a reunion about "
        "three months from now.",
    ], size=S, after=1)

    d.h2("Timing")
    d.p("The plan below uses 75 minutes, leaving about 15 for a late start, a break, and "
        "celebration.", size=S, after=4, keep_next=True)
    d.grid(["Part", "Minutes", "If you're running behind"], [
        ["1. Opening Inspiration", "5", "Take one or two answers."],
        ["2. Check-In and Looking Back", "12", "Use one group question."],
        ["3. Time Is Your Best Friend", "15", "Read the box and table; use one question."],
        ["4. Growing Money for Later", "13", "Read both boxes; use one question."],
        ["5. My Next Steps", "20", "Protect this time, especially choosing a buddy for "
         "the months ahead."],
        ["6. Celebration and Closing", "10", "Never skip the closing circle."],
        ["Total", "75", ""],
    ], [3.0, 0.75, 3.15], height=0.26, size=10, bold_rows=(6,), shade_rows=(6,),
           keep_together=True)

    d.h2("Handling emotions and issues")
    for head, text in [
        ("“Investing is for rich people.”", "Point to the $10 and $25 examples. The goal is "
         "a habit and some security, not getting rich."),
        ("“I’m too old to start.”", "Starting now is better than not starting. Even a few "
         "years of saving, plus a safety net, makes later life easier."),
        ("Nothing left to save.", "Many people won’t be ready to invest. That’s fine. Their "
         "next steps are their safety net and debt plan. Celebrate those."),
        ("Fear of losing money.", "Acknowledge it. Savings is for money needed soon; investing "
         "is only for money that can stay put for years."),
        ("Get-rich-quick ideas.", "If someone mentions a “sure thing,” crypto tip, or "
         "high-pressure offer, use the warning signs in the guide, gently and without "
         "embarrassing them."),
        ("Sadness that the course is ending.", "Plan the monthly buddy check-ins together, "
         "and consider a reunion. Remind people they can keep meeting on their own."),
        ("Feeling behind others.", "Everyone started in a different place. Celebrate each "
         "person’s progress against their own starting point, not anyone else’s."),
    ]:
        d.p(f"**{head}** {text}", size=S, after=4)
    d.save(OUT)


if __name__ == "__main__":
    build()
