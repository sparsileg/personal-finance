import sys

from pflib import Doc

OUT = sys.argv[1]
S = 11


def build():
    d = Doc("template.docx", margins=0.8, footer="Session 5 · Facilitator Notes")
    d.h1("Session 5 Facilitator Notes")
    d.p("**Building Wealth (optional session).** Use with the Session 5 guide, which you and the "
        "group read together.", size=S, after=4)

    d.h2("Is this session right for your group?")
    d.p("Session 5 is optional, and Sessions 1–4 make a complete course without it. Decide "
        "with the host whether your group will benefit from learning about investing. It "
        "fits best when most people have a working budget and have started a safety net. You "
        "can hold it the week after Session 4, or a few months later as a reunion.",
        size=S, after=4)

    d.h2("Session goals")
    d.p("By the end of the session, each person should:", size=S, after=2)
    d.bullets([
        "Understand that time helps small amounts grow, and that it’s never too late to start",
        "Know the difference between saving and investing",
        "Know why low-fee index funds, not single stocks, are a good way to start",
        "Expect the market to drop at times, and know not to sell in fear",
        "Know the difference between retirement accounts and regular investment accounts, "
        "the value of a job match, and why not to cash out when changing jobs",
        "Know that Social Security is most people’s main retirement income",
        "Know the warning signs of scams",
        "Leave with **My Plan for Later** and a next step, even if that step is their safety net",
    ], size=S, after=1)
    d.p("If people leave knowing their next step and feeling it’s within reach, the session "
        "worked.", size=S, after=4)

    d.h2("Your role")
    d.p("As before, you guide the council rather than teach it. Ask for volunteers to read; never "
        "call on anyone. **Don’t give investment advice** or name specific companies, funds, or "
        "products. You can explain what an index fund is, but not which one to buy. Keep it "
        "simple: safety net first, costly debt next, then saving for later, and always get a "
        "job match. For detailed questions, point people to their job’s HR office, free tax "
        "help (VITA), or a fee-only advisor.", size=S, after=4)

    d.h2("How to prepare")
    d.bullets([
        "Read the guide, and practice explaining the $25-a-month table and the difference "
        "between a stock and an index fund in your own words. Fill out My Plan for Later, front "
        "and back. Read the principle aloud in class, even if people finish it at home.",
        "Find the nearest free tax help site (VITA) and add it to the resource list.",
        "Bring guides, pencils, blank paper, calculators, and the resource list.",
    ], size=S, after=1)

    d.h2("Timing")
    d.p("This session runs about 105 minutes. The plan uses 90, leaving about 15 for a late "
        "start, a break, and questions.", size=S, after=4, keep_next=True)
    d.grid(["Part", "Minutes", "If you're running behind"], [
        ["1. Opening Inspiration", "5", "Take one or two answers."],
        ["2. Buddy Check-In", "8", "Use one group question."],
        ["3. Time Is Your Best Friend", "12", "Read the box and table; use one question."],
        ["4. Saving and Investing", "15", "Read the box; use one question."],
        ["5. When the Market Drops", "8", "Read the box; use one question."],
        ["6. Retirement and Other Long-Term Investing", "20", "Read the box and scam signs; "
         "skip the questions."],
        ["7. My Plan for Later", "15", "Protect this time. People can finish the back at home."],
        ["8. Wrap-up and Closing", "7", "Never skip the closing circle."],
        ["Total", "90", ""],
    ], [3.0, 0.75, 3.15], height=0.26, size=10, bold_rows=(8,), shade_rows=(8,),
           keep_together=True)

    d.h2("Handling emotions and issues")
    for head, text in [
        ("“Investing is for rich people.”", "Point to the $10 and $25 examples. The goal is "
         "a habit and some security, not getting rich."),
        ("“I’m too old to start.”", "Starting now is better than not starting. Even a few "
         "years of saving, plus a safety net, makes later life easier."),
        ("Nothing left to save.", "Many people won’t be ready to invest. That’s fine. Their "
         "next steps are their safety net and debt plan. Celebrate those."),
        ("Fear of losing money.", "Acknowledge it. Investing is only for money that can stay "
         "put for years. Point to the Ups and Downs box: past drops "
         "in the whole market came back over time, and selling in fear locked in the loss."),
        ("A hot stock or crypto tip.", "If someone mentions a “sure thing” or a stock a "
         "friend is buying, don’t argue. Point back to **One Company, or Many?**: one company can fall a lot, "
         "and an index fund spreads the risk. Use the scam warning signs gently, without "
         "embarrassing anyone."),
        ("Detailed tax or account questions.", "Which kind is right for me, how much to put "
         "in, which fund: say it’s a good question for HR, free tax help (VITA), or a "
         "fee-only advisor."),
        ("Benefits and savings limits.", "Rules vary. Don’t guess; refer people to their caseworker."),
    ]:
        d.p(f"**{head}** {text}", size=S, after=4)
    d.save(OUT)


if __name__ == "__main__":
    build()
