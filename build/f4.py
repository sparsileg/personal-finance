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
        "Know what to do when a setback hits: no shame, call a buddy, restart smaller",
        "Recognize and celebrate the progress they’ve made in the course",
        "Leave with a buddy and a plan to check in monthly, using **Keeping It Going**",
    ], size=S, after=1)
    d.p("This is the last session, so it is a celebration as much as a lesson. A person who "
        "leaves having saved their first dollar, or knowing where it will go, and with a buddy "
        "to keep going, has succeeded.", size=S, after=4)

    d.h2("Your role")
    d.p("As before, you guide the council rather than teach it. Keep time, invite every voice, "
        "and let the group share ideas with each other. Ask for volunteers to read; never call on "
        "anyone. Celebrate a $5 safety net as warmly as a $500 one.", size=S, after=4)

    d.h2("How to prepare")
    d.bullets([
        "Fill out My Safety Net Plan, front and back, yourself or for a made-up person on a tight "
        "income. Read the principle on the back aloud in class, even if people finish it at "
        "home.",
        "Update the **local resource list**: 211, food pantries, utility and rent help, Medicaid "
        "and CHIP offices, free tax help (VITA), and credit unions or banks with low-cost "
        "accounts.",
        "Bring guides, pencils, blank paper, calculators, a flipchart or whiteboard for listing "
        "surprise expenses, and, if you like, plain envelopes people can label “Safety Net” "
        "and simple certificates of completion with each person’s name. Consider light "
        "refreshments at the end to celebrate, if the host can provide them.",
        "Think of a time a small amount of savings, or someone’s help, got you through a "
        "surprise. Consider planning a reunion about three months from now.",
        "If you and the host plan to hold the optional Session 5, invite people at the end. "
        "The Session 4 materials don’t mention it.",
    ], size=S, after=1)

    d.h2("Timing")
    d.p("This session runs about 105 minutes. The plan uses 90, leaving about 15 for a late "
        "start, a break, and refreshments.", size=S, after=4, keep_next=True)
    d.grid(["Part", "Minutes", "If you're running behind"], [
        ["1. Opening Inspiration", "5", "Take one or two answers."],
        ["2. Buddy Check-In and Debt Progress", "10", "Use one group question."],
        ["3. Surprises We Can Plan For", "12", "List five surprises; use one question."],
        ["4. Build Your Safety Net Plan", "25", "Protect this time. Never go below 15 minutes "
         "on the worksheet, and don’t skip choosing buddies for the months ahead."],
        ["5. Other Safety Nets", "10", "Read the box; use the first question."],
        ["6. When Life Knocks You Off Course", "10", "Read the five steps; use one "
         "question."],
        ["7. Looking Back and Keeping It Going", "18", "Never skip the box, the monthly "
         "check-in plan, and the closing circle."],
        ["Total", "90", ""],
    ], [3.0, 0.75, 3.15], height=0.26, size=10, bold_rows=(7,), shade_rows=(7,),
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
        ("Pride about accepting help.", "Remind the group that community programs exist for "
         "times like this, and that they may one day help others in return."),
        ("Sadness that the course is ending.", "Plan the monthly buddy check-ins together, "
         "and consider a reunion. Celebrate each person’s progress from their own start."),
    ]:
        d.p(f"**{head}** {text}", size=S, after=4)
    d.save(OUT)


if __name__ == "__main__":
    build()
