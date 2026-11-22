import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 4 · Financial Safety Net"


def guide():
    d = Doc("template.docx", margins=1.0, footer=FOOT)
    d.h1("Financial Safety Net")
    d.p("**Session 4:** A cushion for life’s surprises, starting small", size=13, after=10)

    d.label("In this session, you will:", before=0)
    d.bullets([
        "See that most “emergencies” can be planned for",
        "Learn why a small cushion of savings matters, even while you pay off debt",
        "Make a plan to start or grow your own safety net",
        "Learn about other safety nets: insurance, community help, and each other",
        "Choose a buddy for the coming week",
    ])
    d.p("As before, a volunteer reads each **Read Aloud** box, and reading is always optional. "
        "Your worksheets are at the end of this guide. Have your budget and your debt plan ready "
        "to use.")

    # 1 -------------------------------------------------------------------
    d.h2("1. Opening Inspiration", 5)
    d.read_aloud([
        "“We ought to have a little money laid aside in case of a rainy day.” (Gordon B. "
        "Hinckley, “If Ye Are Prepared Ye Shall Not Fear,” October 2005 general conference)",
        "“They should save some money, if only a few coins each week. This modest approach will "
        "soon enable them to have several months’ reserve.” (Keith B. McMullin, “Lay Up in "
        "Store,” April 2007 general conference)",
    ])
    d.discuss(["What would even a small cushion of savings change for you?"])

    # 2 -------------------------------------------------------------------
    d.h2("2. Buddy Check-In and Debt Progress", 10)
    d.label("With last week’s buddy (4 minutes)")
    d.bullets([
        "Share one step you took on your debt plan, however small.",
        "Share one thing that made it hard.",
    ])
    d.label("As a group (6 minutes)")
    d.bullets([
        "What step are you proud of this week?",
        "Did a surprise expense come up? How did you handle it?",
    ])
    d.p("**Remember:** Every payment and every dollar saved counts, even when it doesn’t feel "
        "like much.")

    # 3 -------------------------------------------------------------------
    d.h2("3. Surprises We Can Plan For", 15)
    d.read_aloud([
        "The car breaks down. A child needs new shoes. The rent goes up, a tooth aches, or work "
        "hours get cut. These feel like emergencies, but they happen to almost everyone, again "
        "and again. We don’t know when they’ll come, but we know they will come.",
        "Without savings, each surprise becomes new debt: a credit card, a payday loan, or a "
        "late bill. That’s how the debt cycle keeps turning. A **safety net**, even a small one, "
        "breaks the cycle. If you have $100 set aside, a $100 surprise is an inconvenience, not "
        "a crisis.",
    ], title="Emergencies Aren’t Really Surprises")
    d.label("As a group")
    d.p("Name the surprises that have come up for people you know in the past year. The "
        "facilitator lists them on the board, with a rough cost for each.")
    d.discuss([
        "Which of these happen most often? About how much do they usually cost?",
        "How did people pay for them? What happened next?",
        "Which ones could you plan for, at least a little?",
    ])

    # 4 -------------------------------------------------------------------
    d.h2("4. Build Your Safety Net Plan", 25)
    d.read_aloud([
        "You don’t need thousands of dollars to start. Build your safety net in steps:",
    ], title="Start Small, Then Grow", bullets=[
        "**Step 1:** A first goal of $100, then $500. This is enough for many small surprises.",
        "**Step 2:** One month of must-pay expenses: housing, utilities, food, getting to work, "
        "and minimum payments.",
        "**Step 3:** Over time, three months or more of must-pay expenses.",
    ], after_bullets=[
        "Save first, a little at a time, even while you pay off debt. Keep the money where it’s "
        "easy to reach but not too easy to spend: an envelope at home, a separate savings "
        "account, or a credit union. Use it only for real emergencies, then refill it.",
    ])
    d.h3("On your own", 15, before=2)
    d.p("Turn to the **My Safety Net Plan** worksheet. Use your budget to find your must-pay "
        "expenses, then choose a first goal and a weekly amount. If saving anything feels "
        "impossible right now, start with $1 a week or the change in your pocket. That counts.")
    d.h3("With a new buddy", 7)
    d.p("Pair up with someone new, or keep your buddy if you prefer. Trade phone numbers. Then:")
    d.bullets([
        "Share your first goal and where you’ll keep the money.",
        "Trade one idea for finding a few extra dollars to save.",
    ])

    # 5 -------------------------------------------------------------------
    d.h2("5. Other Safety Nets", 12)
    d.read_aloud([
        "Savings is one safety net, but not the only one. **Insurance** protects against costs "
        "too big to save for. Health coverage comes first; Medicaid or CHIP may cover you or your "
        "children at low or no cost. Renter’s insurance often costs just a few dollars a week. "
        "Check what your job offers, such as life or disability insurance.",
        "**Community help** is a safety net too: food pantries, utility and rent assistance, and "
        "programs you can find by calling 211. Using them when you need them is wise, not "
        "shameful. And **people** are a safety net: family, friends, neighbors, your church, and "
        "the buddies in this room. One day you’ll be part of someone else’s safety net.",
    ], title="More Than Savings")
    d.discuss([
        "Who is in your safety net? Whose safety net are you part of?",
        "What’s one kind of coverage or help you’d like to learn more about?",
    ])

    # 6 -------------------------------------------------------------------
    d.h2("6. Wrap-up and This Week’s Commitment", 8)
    d.label("This week, I will:", before=2)
    d.numbered([
        "Choose a place for my safety net: an envelope, a jar, or a separate account.",
        "Save something every week, even $1, and write it on the **Weekly Safety Net Tracker**.",
        "Use my safety net only for real emergencies.",
        "Keep up with my budget and my debt plan.",
        "Look into one other safety net, such as health coverage, renter’s insurance, or a "
        "community program.",
        "Call or text my buddy at least once.",
    ])
    d.p("**Want to go further?** The Session 4 take-home worksheets are optional. Do them only if "
        "you have time after your tracker.")
    d.label("Gratitude and giving")
    d.p("Think of someone who has been part of your safety net. This week, thank them, or find "
        "a small way to be part of someone else’s.")
    d.label("Closing circle")
    d.p("Finish this sentence: “When I have $100 set aside, I’ll feel …”")
    d.p("**Next week (optional session):** We’ll look at small, steady ways to build a secure "
        "future.")

    # Worksheet: safety net plan --------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · My Safety Net Plan")
    d.h1("My Safety Net Plan")
    d.note("Session 4 · In class. Use your budget from Session 2. Best guesses are fine. This page "
           "is private.")
    d.money_table("Step 1. My must-pay expenses (each month)", [
        "Rent or mortgage",
        "Utilities",
        "Groceries",
        "Phone",
        "Gas, bus fare, rides",
        "Car payment and insurance",
        "Minimum debt payments",
        "Childcare",
        "Medicine and health coverage",
        "Other must-pay: ____________",
    ], "One month of must-pays", widths=(2.75, 0.9), cols=2)
    d.label("Step 2. My goals", before=6)
    d.grid(["Goal", "Amount", "By about when"], [
        ["First goal: $100 (or my own first step)", "$", ""],
        ["Starter safety net: $500", "$500", ""],
        ["One month of must-pays (from Step 1)", "$", ""],
        ["Three months of must-pays (Step 1 × 3)", "$", ""],
    ], [4.0, 1.3, 2.0], height=0.3)
    d.label("Step 3. How I’ll get there", before=6)
    d.p("I’ll save $________ each week, on ______________ (day). I have $________ saved now.",
        size=10, after=4)
    d.p("I’ll keep it in:   ☐ An envelope or jar at home   ☐ A separate savings account   "
        "☐ A credit union   ☐ Other: __________", size=10, after=4)
    d.p("Where the money will come from (check any):", size=10, after=1)
    d.p("     ☐ Saving first, before spending   ☐ Loose change and $1 bills   ☐ Selling things I "
        "don’t use", size=10, after=1)
    d.p("     ☐ Part of a tax refund or gift   ☐ Spending less on ______________   ☐ Extra hours "
        "or a side job", size=10, after=4)
    d.box([
        "**My safety net rules.** Before I use it, I ask: Is it **unexpected**? Is it "
        "**necessary**? Is it **urgent**? If all three are yes, it’s an emergency. Sales, "
        "vacations, gifts, and bills I forgot to budget for are not. When I use it, I start "
        "refilling it right away.",
    ])

    # Homework: weekly tracker -------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Weekly Safety Net Tracker")
    d.h1("Weekly Safety Net Tracker")
    d.note("Session 4 · Homework. Write down every amount you add to (or take from) your safety "
           "net, and keep using your budget and debt plan. Bring this to Session 5.")
    d.p("Week starting: ______________     My buddy this week: ________________________     "
        "Phone: ________________", size=10, after=2)
    d.p("Check in with your buddy at least once this week. Date we talked: ____________", size=10,
        after=8)
    d.p("My safety net at the start of the week: $__________     My first goal: $__________",
        size=10, after=6)
    d.grid(["Date", "Where it came from (or what I used it for)", "Added", "Taken out"],
           [[""] * 4 for _ in range(7)] + [["Totals", "", "$", "$"]],
           [1.0, 4.0, 1.15, 1.15], height=0.3, bold_rows=(7,), shade_rows=(7,))
    d.p("My safety net at the end of the week: $__________", size=10, before=4, after=4)
    d.label("This week I…", before=4)
    d.checks([
        "Saved first, before spending",
        "Kept up with my budget and my debt payments",
        "Used my safety net only for a real emergency (or didn’t need it)",
        "Learned about one other safety net: ______________________",
    ], size=10, after=1)
    d.question(1, "What helped me save this week?", 2, size=10)
    d.question(2, "What will I try next week?", 1, size=10)
    d.question(3, "What am I proud of this week?", 1, size=10)

    # Notes ---------------------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Notes")
    d.h1("Session 4 Notes")
    d.note("Space for your thoughts during our discussions.")
    for head in ["Surprises I can plan for", "My safety net plan",
                 "Other safety nets I want to look into", "Things I want to remember"]:
        d.label(head, before=8)
        d.lines(4)
    d.save(OUT)


if __name__ == "__main__":
    guide()
