import sys

from pflib import Doc

OUT = sys.argv[1]
S = 11

SESSIONS = [
    ("1", "Understanding Your Money Story", "Where you are today, and how you got here",
     "Participants meet the group, look at the money messages they grew up with, and get an "
     "honest, judgment-free picture of the money coming in and going out each month. They "
     "also notice what feelings lead them to spend.",
     ["Opening Inspiration (5)", "Welcome and Getting Started (15)",
      "Money Messages from Growing Up (12)", "Your Money Snapshot (25)",
      "What Leads Us to Spend (10)", "Wrap-up and This Week’s Commitment (8)"],
     "My Financial Snapshot (back: What My Snapshot Tells Me)", "7-Day Money & Emotion Tracker",
     "Money Messages from My Past; What Leads Me to Spend; The Future I Want"),
    ("2", "Creating a Budget", "A budget that fits your real life",
     "Using what they learned from tracking, participants build a budget with their real "
     "numbers, using one simple method: every dollar has a job. They save first, make room to "
     "give, and sort needs from wants by asking what matters most to them.",
     ["Opening Inspiration (5)", "Buddy Check-In and Tracking Review (10)",
      "What a Budget Really Is (15)", "Build Your Real Life Budget (25)",
      "Needs, Wants, and What Matters (12)", "Wrap-up and This Week’s Commitment (8)"],
     "My Real Life Budget (front and back)", "Weekly Budget Tracker",
     "Which Paycheck Pays What; My Budget Success Plan; Budget Problem-Solving"),
    ("3", "Breaking the Debt Cycle", "A plan to pay down what you owe, and stay out of new debt",
     "Participants see what interest really costs, list everything they owe, and choose a "
     "payoff order (snowball or avalanche). They learn which bills to protect first, their "
     "rights with debt collectors, and where to find free, trustworthy help.",
     ["Opening Inspiration (5)", "Buddy Check-In and Budget Review (10)",
      "The True Cost of Debt (15)", "Make Your Debt Plan (25)",
      "Know Your Rights and Ask for Help (12)", "Wrap-up and This Week’s Commitment (8)"],
     "My Debt Plan (back: Seeing the Finish Line)", "Weekly Debt Tracker",
     "What Leads Me into Debt; Calling Someone I Owe; The Day My Debt Is Paid"),
    ("4", "Financial Safety Net", "A cushion for life’s surprises, starting small",
     "Participants see that most “emergencies” are surprises they can plan for, and set a "
     "first savings goal, even $1 a week. They also look at the other safety nets in their "
     "lives: insurance, community programs, and people, and plan what to do when life knocks "
     "them off course. As the last session, it closes the course: participants look back at "
     "how far they’ve come and choose a buddy to check in with monthly after the course.",
     ["Opening Inspiration (5)", "Buddy Check-In and Debt Progress (10)",
      "Surprises We Can Plan For (12)", "Build Your Safety Net Plan (25)",
      "Other Safety Nets (10)", "When Life Knocks You Off Course (10)",
      "Looking Back and Keeping It Going (18)"],
     "My Safety Net Plan (back: Putting My Safety Net to Work)",
     "Weekly Safety Net Tracker (back: Keeping It Going, a monthly check-in for after the course)",
     "My Surprise Expenses; Finding Money to Save; Insurance and Other Safety Nets; Looking "
     "Back, Looking Ahead"),
    ("5", "Building Wealth (optional)",
     "Small, steady steps toward a secure and meaningful future",
     "For groups ready to think about investing. Here “wealth” means enough, with peace of "
     "mind and room to help others. Building on Sessions 1–4, participants see how time helps "
     "small amounts grow, learn why low-fee index funds are a better start than single stocks "
     "and why not to sell when the market drops, learn the difference between retirement "
     "accounts and other long-term investing, how Social Security fits in, and why not to "
     "cash out when changing jobs, learn to spot scams, and choose a next step.",
     ["Opening Inspiration (5)", "Buddy Check-In (8)",
      "Time Is Your Best Friend (12)", "Saving and Investing (15)",
      "When the Market Drops (8)", "Retirement and Other Long-Term Investing (20)",
      "My Plan for Later (15)", "Wrap-up and Closing (7)"],
     "My Plan for Later (back: One Company, or Many?)", "Finding Out",
     "The Power of Starting Now; Saving or Investing?; What Fees Cost"),
]


PRINCIPLES = {
    "1": "You can’t change what you don’t look at. Knowing your numbers, without judging "
         "them, is the first step to changing them.",
    "2": "Give every dollar a job before the month begins, and save a little first, even $5. "
         "A plan you adjust as you go beats no plan at all.",
    "3": "Focus on one debt at a time, and roll each finished payment into the next. Every "
         "payoff speeds up the next one. Avoid new debt while you do.",
    "4": "Save first, start small, and keep it for real emergencies. Even $100 set aside turns "
         "many crises into inconveniences, and keeps you out of new debt.",
    "5": "Build your safety net first. Then invest a little, steadily, in low-fee funds that "
         "own many companies, and give it time to grow.",
}


def build():
    d = Doc("template.docx", margins=1.0, footer="Course Overview")
    d.h1("Personal Finance Survival Course")
    d.p("**Course overview:** four weekly sessions, plus an optional fifth", size=13, after=10)

    d.h2("Who it’s for")
    d.p("Anyone who wants to learn a few things about understanding and managing their income, "
        "expenses, and savings, whether they’re starting from scratch or just want a refresher. "
        "People come from all kinds of situations: some have little or no work, some have steady "
        "jobs but haven’t been able to save or plan ahead, and some are doing fine and want to "
        "sharpen their skills. The materials use plain "
        "language and examples that fit tight or irregular incomes, and they never assume "
        "spare money, a bank account, or good credit.", size=S)

    d.h2("What each person leaves with")
    d.bullets([
        "A clear picture of their money today",
        "A simple budget that works for their real life",
        "A plan for paying down debt and avoiding new debt",
        "A first step toward a safety net, even a very small one",
        "Knowledge of the community resources available to them",
        "A buddy who keeps them going after the course ends",
    ], size=S, after=1)

    d.h2("How the course works")
    d.bullets([
        "**Length.** Sessions 1–3 take about 90 minutes; the guide plans 75, leaving time for "
        "a late start, a break, and good conversation. Session 4, and the optional Session 5, "
        "take about 105 minutes, with 90 planned, for more discussion and, in Session 4, a "
        "closing celebration with light refreshments if the host can provide them.",
        "**A council, not a class.** There is no teacher or expert. A facilitator keeps time and "
        "invites every voice. The group reads the session guide together, and volunteers read "
        "the Read Aloud boxes. Reading aloud is always optional. The guide also works for "
        "someone reading on their own, such as a member who missed a session.",
        "**The same pattern each week.** An opening thought, a buddy check-in, a few key ideas, "
        "a hands-on worksheet with real numbers, discussion, and a wrap-up with a commitment, "
        "a moment of gratitude, and a closing circle.",
        "**Worksheets that change something.** Each in-class worksheet is printed front and "
        "back. The front uses each person’s real numbers. The back puts them to work with a "
        "short exercise, then ends with the principle behind it and a first step for the "
        "week. Anything left unfinished in class can be finished at home.",
        "**Opening thoughts.** Each session opens with a short, well-known quote tied to the "
        "week’s topic, chosen for simple guidance toward a happy, meaningful life.",
        "**Buddies.** Members pair up in class and check in with each other at least once "
        "during the week. They can switch buddies each week.",
        "**Homework.** One weekly tracker, plus optional take-home worksheets for those who "
        "want to go further.",
        "**An optional fifth session.** Session 4 closes the course, and Sessions 1–4 are "
        "complete on their own; their materials don’t mention Session 5. Session 5, Building "
        "Wealth, covers investing for later. It isn’t right for every group, so the "
        "facilitator and host decide whether to hold it, either the week after Session 4 or "
        "a few months later as a reunion.",
        "**Tone.** Positive and free of shame, grateful for what people already have, and "
        "encouraging them to give back to family, church, friends, and community.",
    ], size=S, after=1)

    d.h2("The materials for each session")
    d.grid(["Document", "Who uses it", "What’s in it"], [
        ["Session guide, such as “3 - Breaking the Debt Cycle”", "Everyone",
         "The session plan with minutes for each part, Read Aloud boxes, and discussion "
         "questions, followed by a notes page. Then come the in-class worksheet (front and "
         "back) and the homework tracker, each starting on its own sheet of paper"],
        ["Facilitator Notes", "The facilitator",
         "Two pages: goals, the facilitator’s role, how to prepare, timing and what to "
         "shorten, and handling emotions and issues"],
        ["Take-Home Worksheets", "Anyone who wants more",
         "Three or four optional worksheets that go deeper into the week’s topic"],
    ], [2.1, 1.4, 3.0], height=0.3, size=10)

    d.h2("Before the course begins")
    d.bullets([
        "Make a **local resource list**: 211, food pantries, utility and rent help, free tax help "
        "(VITA), a nonprofit credit counselor, and banks or credit unions with low-cost accounts. "
        "Bring copies every week.",
        "Print a session guide for each person, and the facilitator notes for yourself. Print "
        "double-sided: each worksheet starts on its own sheet (the files include a blank page "
        "where needed), so worksheets can be pulled out or printed separately.",
        "Bring pencils with erasers (not pens, so mistakes erase easily), blank paper, "
        "calculators, and something to write on that the whole group can see. Set up tables in "
        "a square or rectangle so everyone faces each other and has a hard surface to write on.",
    ], size=S, after=1)

    d.h2("The sessions")
    d.grid(["Session", "In-class worksheet", "Homework"],
           [[f"{n}. {title}", ws, hw] for n, title, _, _, _, ws, hw, _ in SESSIONS],
           [2.0, 2.6, 1.9], height=0.3, size=10)
    for n, title, sub, focus, parts, ws, hw, th in SESSIONS:
        d.h3(f"Session {n}: {title}", before=6)
        d.p(sub, italic=True, size=S, after=2, keep_next=True)
        d.p(focus, size=10, after=2, keep_next=True)
        d.p("**Parts (minutes):** " + "; ".join(parts) + ".", size=10, after=2)
        d.p(f"**The principle:** {PRINCIPLES[n]}", size=10, after=2)
        d.p(f"**Take-home (optional):** {th}.", size=10, after=4)
    d.save(OUT)


if __name__ == "__main__":
    build()
