import sys

from pflib import Doc

OUT = sys.argv[1]
S = 11


def build():
    d = Doc("template.docx", margins=0.8, footer="Session 4 · Facilitator Notes")
    d.h1("Session 4 Facilitator Notes")
    d.p("**Financial Safety Net.** Use with the Session 4 guide, which you and the group read "
        "together.", size=S, after=4)

    d.h2("Session goals")
    d.p("By the end of the session, each person should:", size=S, after=2)
    d.bullets([
        "See that most “emergencies” are surprises we can plan for",
        "Understand why a small safety net breaks the debt cycle, even while paying debt",
        "Have a first savings goal, a weekly amount, and a place to keep the money",
        "Know about other safety nets: insurance, community help, and people",
        "Have a buddy, and know how to use the **Weekly Safety Net Tracker**",
    ], size=S, after=1)
    d.p("A person who leaves having saved their first dollar, or knowing where it will go, has "
        "succeeded.", size=S, after=4)

    d.h2("Your role")
    d.p("As before, you guide the council rather than teach it. Keep time, invite every voice, "
        "and let the group share ideas with each other. Ask for volunteers to read; never call on "
        "anyone. Celebrate a $5 safety net as warmly as a $500 one. Keep insurance simple: the "
        "goal is awareness, not expert advice.", size=S, after=4)

    d.h2("How to prepare")
    d.bullets([
        "Fill out My Safety Net Plan, front and back, yourself or for a made-up person on a tight "
        "income. The back, **Putting My Safety Net to Work**, ends with the principle and a "
        "first step. People can finish it at home, but read the principle aloud before moving on.",
        "Update the **local resource list**: 211, food pantries, utility and rent help, Medicaid "
        "and CHIP offices, free tax help (VITA), and credit unions or banks with low-cost "
        "accounts.",
        "Bring guides, pens, calculators, a flipchart or whiteboard for listing surprise "
        "expenses, and, if you like, plain envelopes people can label “Safety Net.”",
        "Think of a time a small amount of savings, or someone’s help, got you through a "
        "surprise.",
    ], size=S, after=1)

    d.h2("Timing")
    d.p("The plan below uses 75 minutes, leaving about 15 for a late start, a break, and "
        "conversation.", size=S, after=4, keep_next=True)
    d.grid(["Part", "Minutes", "If you're running behind"], [
        ["1. Opening Inspiration", "5", "Take one or two answers."],
        ["2. Buddy Check-In and Debt Progress", "10", "Use one group question."],
        ["3. Surprises We Can Plan For", "15", "List five surprises; use one question."],
        ["4. Build Your Safety Net Plan", "25", "Protect this time. Never go below 15 minutes "
         "on the worksheet, and don’t skip choosing buddies."],
        ["5. Other Safety Nets", "12", "Read the box; use the first question."],
        ["6. Wrap-up and Commitment", "8", "Never skip the homework and the closing circle."],
        ["Total", "75", ""],
    ], [3.0, 0.75, 3.15], height=0.26, size=10, bold_rows=(6,), shade_rows=(6,),
           keep_together=True)

    d.h2("Handling emotions and issues")
    for head, text in [
        ("“Save while I’m in debt?”", "Many will feel torn. Explain that a small safety net "
         "keeps the next surprise from becoming new debt. Start with $100, then keep paying "
         "down debt."),
        ("“I can’t save anything.”", "Believe them. Start with $1 a week, loose change, or "
         "part of a tax refund. If even that isn’t possible, focus on community help and "
         "people as their safety net for now."),
        ("A crisis right now.", "If someone faces eviction, a shut-off, or no food, talk with them "
         "privately after the session and give them the resource list. Don’t try to solve it "
         "in the group."),
        ("No bank account.", "An envelope works. If they want an account, credit unions and "
         "low-cost bank accounts are options. Never assume anyone has one."),
        ("Spending the safety net.", "Most people dip into it at first. Review the three "
         "questions (unexpected, necessary, urgent), and encourage them to refill it."),
        ("Insurance questions.", "Don’t recommend specific policies or companies. Point "
         "people to their job, HealthCare.gov, 211, or a licensed agent."),
        ("Pride about accepting help.", "Some people feel ashamed to use community programs. "
         "Remind the group that these programs exist for times like this, and that they may "
         "one day help others in return."),
    ]:
        d.p(f"**{head}** {text}", size=S, after=4)
    d.save(OUT)


if __name__ == "__main__":
    build()
