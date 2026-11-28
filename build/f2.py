import sys

from pflib import Doc

OUT = sys.argv[1]
S = 11


def build():
    d = Doc("template.docx", margins=0.8, footer="Session 2 · Facilitator Notes")
    d.h1("Session 2 Facilitator Notes")
    d.p("**Creating a Budget.** Use with the Session 2 guide, which you and the group read "
        "together.", size=S, after=4)

    d.h2("Session goals")
    d.p("By the end of the session, each person should:", size=S, after=2)
    d.bullets([
        "See a budget as a plan and a permission, not a punishment",
        "Understand “every dollar has a job” and “save first”",
        "Have a first draft of **My Real Life Budget** with their own numbers",
        "Have room in their budget for a little saving, giving, and fun, even small amounts",
        "Have a buddy for the week, and know how to use the **Weekly Budget Tracker**",
    ], size=S, after=1)
    d.p("A rough budget that people will use beats a perfect one they won’t. Unfinished "
        "worksheets are fine.", size=S, after=4)

    d.h2("Your role")
    d.p("As in Session 1, you guide the council rather than teach it. Keep time, draw out quieter "
        "people, and let the group help each other. Ask for volunteers to read; never call on "
        "anyone. During the budget worksheet, move around the room and help people who are "
        "stuck, without looking over shoulders uninvited.", size=S, after=4)

    d.h2("How to prepare")
    d.bullets([
        "Fill out My Real Life Budget yourself, or for a made-up family with a low or irregular "
        "income, so you can show an example on the flipchart. Its second side ends with the "
        "principle and a first step. People can finish it at home, but read the principle aloud before moving on.",
        "Bring the **local resource list** again, plus spare copies of the Session 1 tracker for "
        "anyone who didn’t bring theirs.",
        "Bring guides, pencils, blank paper, calculators (phones work too), and a flipchart or "
        "whiteboard.",
        "Think of a time a budget didn’t work for you, and what you learned. A short, honest "
        "story helps people feel normal.",
    ], size=S, after=1)

    d.h2("Timing")
    d.p("The plan below uses 75 minutes, leaving about 15 for a late start, a break, and "
        "conversation.", size=S, after=4, keep_next=True)
    d.grid(["Part", "Minutes", "If you're running behind"], [
        ["1. Opening Inspiration", "5", "Take one or two answers."],
        ["2. Buddy Check-In and Tracking Review", "10", "Use the first two group questions."],
        ["3. What a Budget Really Is", "15", "Read both boxes; use one question."],
        ["4. Build Your Real Life Budget", "25", "Protect this time. Never go below 15 minutes "
         "on the worksheet, and don’t skip choosing buddies."],
        ["5. Needs, Wants, and What Matters", "12", "Sort two or three items aloud."],
        ["6. Wrap-up and Commitment", "8", "Never skip the homework and the closing circle."],
        ["Total", "75", ""],
    ], [3.0, 0.75, 3.15], height=0.26, size=10, bold_rows=(6,), shade_rows=(6,),
           keep_together=True)

    d.h2("Handling emotions and issues")
    for head, text in [
        ("Income doesn’t cover needs.", "For some people, no amount of cutting will balance "
         "the budget. Don’t press for cuts that aren’t possible. Point them to the "
         "resource list, and treat that help as part of the plan, not a failure."),
        ("Didn’t track last week.", "Welcome them warmly. They can build the budget from "
         "their Snapshot and best guesses, and start tracking this week."),
        ("Irregular or no income.", "Budget on a low, typical month. Anything extra goes to "
         "savings or debt. If there is no income right now, plan the money and help that do come "
         "in."),
        ("No bank account or credit card.", "Cash and envelopes work well. Never assume "
         "anyone has an account, an app, or a credit card."),
        ("Discouragement or shame.", "Some people will see a negative number for the first time. "
         "Acknowledge how hard that is, and remind them that knowing is the first step."),
        ("“I’ve tried budgeting and failed.”", "Most people try more than once. Ask "
         "what didn’t work, and suggest starting with just a few big areas."),
        ("Couples.", "Partners may see money differently. Encourage shared goals, even if each "
         "keeps track in their own way."),
        ("Advice-giving.", "Steer the group toward “what worked for me” rather than "
         "“what you should do.”"),
    ]:
        d.p(f"**{head}** {text}", size=S, after=4)
    d.save(OUT)


if __name__ == "__main__":
    build()
