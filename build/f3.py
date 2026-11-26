import sys

from pflib import Doc

OUT = sys.argv[1]
S = 11


def build():
    d = Doc("template.docx", margins=0.8, footer="Session 3 · Facilitator Notes")
    d.h1("Session 3 Facilitator Notes")
    d.p("**Breaking the Debt Cycle.** Use with the Session 3 guide, which you and the group read "
        "together.", size=S, after=4)

    d.h2("Session goals")
    d.p("By the end of the session, each person should:", size=S, after=2)
    d.bullets([
        "See debt as a problem with a solution, not a personal failing",
        "Understand how interest makes debt cost more over time",
        "Know the snowball and avalanche methods, and have chosen one",
        "Have started **My Debt Plan** with their own debts",
        "Know their basic rights with collectors, and where to find free help",
        "Have a buddy, and know how to use the **Weekly Debt Tracker**",
    ], size=S, after=1)
    d.p("Some people have no debt, and some owe a great deal. Both are welcome. The aim is a first "
        "step, not a finished plan.", size=S, after=4)

    d.h2("Your role")
    d.p("As before, you guide the council rather than teach it. Keep time, invite every voice, "
        "and let the group help each other. Ask for volunteers to read; never call on anyone. "
        "Keep the math simple and the tone hopeful. You don’t need to be a debt expert. Your job "
        "is to help people take one step and to point them to real help.", size=S, after=4)

    d.h2("How to prepare")
    d.bullets([
        "Fill out My Debt Plan, front and back, yourself or for a made-up person. The back, "
        "**Seeing the Finish Line**, ends with the principle and a first step. People can finish it at home, but read the principle aloud before moving on.",
        "Find the nearest **nonprofit credit counseling** agency (members of the National "
        "Foundation for Credit Counseling, nfcc.org) and add it to your resource list, along "
        "with any local free legal aid.",
        "Bring guides, pens, calculators, the resource list, and a flipchart or whiteboard.",
        "Practice the phone script once out loud, so you can model it calmly.",
    ], size=S, after=1)

    d.h2("Timing")
    d.p("The plan below uses 75 minutes, leaving about 15 for a late start, a break, and "
        "conversation.", size=S, after=4, keep_next=True)
    d.grid(["Part", "Minutes", "If you're running behind"], [
        ["1. Opening Inspiration", "5", "Read the first quote only."],
        ["2. Buddy Check-In and Budget Review", "10", "Use one group question."],
        ["3. The True Cost of Debt", "15", "Read the box and table; use one question."],
        ["4. Make Your Debt Plan", "25", "Protect this time. Never go below 15 minutes on "
         "the worksheet, and don’t skip choosing buddies."],
        ["5. Know Your Rights and Ask for Help", "12", "Read the box; skip the practice."],
        ["6. Wrap-up and Commitment", "8", "Never skip the homework and the closing circle."],
        ["Total", "75", ""],
    ], [3.0, 0.75, 3.15], height=0.26, size=10, bold_rows=(6,), shade_rows=(6,),
           keep_together=True)

    d.h2("Handling emotions and issues")
    for head, text in [
        ("Debt shame.", "Many people have never told anyone what they owe. Say clearly that debt "
         "usually means life cost more than people had. Never ask anyone to share amounts."),
        ("Overwhelm.", "If the total feels too big, help them focus on one debt, the first "
         "one, and on the next payment only."),
        ("Can’t make the minimums.", "Point to the box on the worksheet: housing, utilities, "
         "food, and transportation come first. Then call creditors and a nonprofit credit "
         "counselor. Don’t give legal advice about bankruptcy; refer them to legal aid."),
        ("Payday loans and other costly debt.", "Don’t shame anyone for using them. They "
         "often feel like the only choice. Talk about what could replace them next time."),
        ("No debt, or no extra money.", "People without debt can plan to stay that way and "
         "help their buddy. If there’s no extra money, $5 or simply avoiding new debt is a real "
         "step."),
        ("Collectors, scams, and fear.", "If someone is being harassed or threatened, help "
         "them privately with the rights list and the CFPB complaint site. Warn against "
         "companies that charge big fees to “settle” debt."),
        ("Money and abuse.", "If someone mentions a partner controlling money or running up debt "
         "in their name, talk privately and share the domestic violence hotline "
         "(1-800-799-7233) and local resources."),
        ("Advice-giving.", "Steer toward “what worked for me” rather than “what you "
         "should do.”"),
    ]:
        d.p(f"**{head}** {text}", size=S, after=4)
    d.save(OUT)


if __name__ == "__main__":
    build()
