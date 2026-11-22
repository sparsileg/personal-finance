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
     "My Financial Snapshot", "7-Day Money & Emotion Tracker",
     "Money Messages from My Past; What Leads Me to Spend; The Future I Want"),
    ("2", "Creating a Budget", "A budget that fits your real life",
     "Using what they learned from tracking, participants build a budget with their real "
     "numbers, using one simple method: every dollar has a job. They save first, make room to "
     "give, and sort needs from wants by asking what matters most to them.",
     ["Opening Inspiration (5)", "Buddy Check-In and Tracking Review (10)",
      "What a Budget Really Is (15)", "Build Your Real Life Budget (25)",
      "Needs, Wants, and What Matters (12)", "Wrap-up and This Week’s Commitment (8)"],
     "My Real Life Budget", "Weekly Budget Tracker",
     "Needs, Wants, or It Depends?; My Budget Success Plan; Budget Problem-Solving"),
    ("3", "Breaking the Debt Cycle", "A plan to pay down what you owe, and stay out of new debt",
     "Participants see what interest really costs, list everything they owe, and choose a "
     "payoff order (snowball or avalanche). They learn which bills to protect first, their "
     "rights with debt collectors, and where to find free, trustworthy help.",
     ["Opening Inspiration (5)", "Buddy Check-In and Budget Review (10)",
      "The True Cost of Debt (15)", "Make Your Debt Plan (25)",
      "Know Your Rights and Ask for Help (12)", "Wrap-up and This Week’s Commitment (8)"],
     "My Debt Plan", "Weekly Debt Tracker",
     "What Leads Me into Debt; Calling Someone I Owe; The Day My Debt Is Paid"),
    ("4", "Financial Safety Net", "A cushion for life’s surprises, starting small",
     "Participants see that most “emergencies” are surprises they can plan for, and set a "
     "first savings goal, even $1 a week. They also look at the other safety nets in their "
     "lives: insurance, community programs, and people.",
     ["Opening Inspiration (5)", "Buddy Check-In and Debt Progress (10)",
      "Surprises We Can Plan For (15)", "Build Your Safety Net Plan (25)",
      "Other Safety Nets (12)", "Wrap-up and This Week’s Commitment (8)"],
     "My Safety Net Plan", "Weekly Safety Net Tracker",
     "My Surprise Expenses; Finding Money to Save; Insurance and Other Safety Nets"),
    ("5", "Building Wealth (optional)",
     "Small, steady steps toward a secure and meaningful future",
     "Here “wealth” means enough, with peace of mind and room to help others. Participants "
     "celebrate their progress, see how time helps small amounts grow, learn the difference "
     "between saving and investing, learn to spot scams, and plan their next steps with a "
     "buddy for the months after the course.",
     ["Opening Inspiration (5)", "Check-In and Looking Back (12)",
      "Time Is Your Best Friend (15)", "Growing Money for Later (13)",
      "My Next Steps (20)", "Celebration and Closing (10)"],
     "My Next Steps Plan", "Monthly Check-In (for three months after the course)",
     "The Power of Starting Now; Saving or Investing?; Looking Back, Looking Ahead"),
]


def build():
    d = Doc("template.docx", margins=1.0, footer="Course Overview")
    d.h1("Personal Finance Survival Course")
    d.p("**Course overview:** four weekly sessions, plus an optional fifth", size=13, after=10)

    d.h2("Who it’s for")
    d.p("People receiving support through a community organization, food pantry, or church. "
        "Most have had little chance to learn about money. Some have little or no work; others "
        "have steady jobs but haven’t been able to save or plan ahead. The materials use plain "
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
        "**Length.** Each session takes about 90 minutes. The guide plans 75, leaving time for a "
        "late start, a break, and good conversation.",
        "**A council, not a class.** There is no teacher or expert. A facilitator keeps time and "
        "invites every voice. The group reads the session guide together, and volunteers read "
        "the Read Aloud boxes. Reading aloud is always optional.",
        "**The same pattern each week.** An opening thought, a buddy check-in, a few key ideas, "
        "a hands-on worksheet with real numbers, discussion, and a wrap-up with a commitment, "
        "a moment of gratitude, and a closing circle.",
        "**Opening thoughts.** Each session opens with a short quote from a general conference "
        "address, chosen for simple guidance toward a happy, meaningful life.",
        "**Buddies.** Members pair up in class and check in with each other at least once "
        "during the week. They can switch buddies each week.",
        "**Homework.** One weekly tracker, plus optional take-home worksheets for those who "
        "want to go further.",
        "**Tone.** Positive and free of shame, grateful for what people already have, and "
        "encouraging them to give back to family, church, friends, and community.",
    ], size=S, after=1)

    d.h2("The materials for each session")
    d.grid(["Document", "Who uses it", "What’s in it"], [
        ["Session guide, such as “3 - Breaking the Debt Cycle”", "Everyone",
         "The session plan with minutes for each part, Read Aloud boxes, and discussion "
         "questions, followed by the in-class worksheet, the homework tracker, and a notes "
         "page, each on its own page"],
        ["Facilitator Notes", "The facilitator",
         "Two pages: goals, the facilitator’s role, how to prepare, timing and what to "
         "shorten, and handling emotions and issues"],
        ["Take-Home Worksheets", "Anyone who wants more",
         "Three optional worksheets that go deeper into the week’s topic"],
    ], [2.1, 1.4, 3.0], height=0.3, size=10)

    d.h2("Before the course begins")
    d.bullets([
        "Make a **local resource list**: 211, food pantries, utility and rent help, free tax help "
        "(VITA), a nonprofit credit counselor, and banks or credit unions with low-cost accounts. "
        "Bring copies every week.",
        "Print a session guide for each person, and the facilitator notes for yourself.",
        "Bring pens, calculators, and something to write on that the whole group can see.",
    ], size=S, after=1)

    d.page_break()
    d.h2("The sessions")
    d.grid(["Session", "In-class worksheet", "Homework"],
           [[f"{n}. {title}", ws, hw] for n, title, _, _, _, ws, hw, _ in SESSIONS],
           [2.6, 1.9, 2.0], height=0.3, size=10)
    for n, title, sub, focus, parts, ws, hw, th in SESSIONS:
        d.h3(f"Session {n}: {title}", before=10)
        d.p(sub, italic=True, size=S, after=2, keep_next=True)
        d.p(focus, size=S, after=2, keep_next=True)
        d.p("**Parts (minutes):** " + "; ".join(parts) + ".", size=10, after=2)
        d.p(f"**Take-home (optional):** {th}.", size=10, after=4)
    d.save(OUT)


if __name__ == "__main__":
    build()
