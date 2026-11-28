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
        "Plan what to do when life knocks you off course",
        "Look back at how far you’ve come",
        "Choose a buddy to keep in touch with after the course",
    ])
    d.how_to_use("Have your budget and your debt plan ready to use.")

    # 1 -------------------------------------------------------------------
    d.h2("1. Opening Inspiration", 5)
    d.read_aloud([
        "“The time to repair the roof is when the sun is shining.” (John F. Kennedy, State of "
        "the Union address, January 11, 1962)",
    ])
    d.p("A safety net is easiest to build before the storm, a little at a time.")
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
    d.h2("3. Surprises We Can Plan For", 12)
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
        "**Step 1:** A first goal of $100, then $500. This is enough for many surprises.",
        "**Step 2:** One month of must-pay expenses: housing, utilities, food, getting to work, "
        "and minimum payments.",
        "**Step 3:** Over time, three months or more of must-pay expenses.",
    ], after_bullets=[
        "Save first, a little at a time, even while you pay off debt. Keep the money where it’s "
        "easy to reach but not too easy to spend: an envelope at home, a separate savings "
        "account, or a credit union. Use it only for real emergencies, then refill it.",
        "Move the money on payday, before you spend, or set up an automatic transfer if you "
        "have an account. When extra money comes in, like a refund or extra hours, decide "
        "ahead of time how much goes to your safety net.",
    ])
    d.p("**Keeping it safe.** Money in a bank or credit union marked “FDIC” or “NCUA” is "
        "insured by the government. Cash at home is easier to lose or spend. If you open an "
        "account, ask about monthly and overdraft fees. Many credit unions and “Bank On” "
        "certified accounts have low or no fees.")
    d.h3("On your own", 15, before=2)
    d.p("Turn to the **My Safety Net Plan** worksheet. Use your budget to find your must-pay "
        "expenses, then choose a first goal and a weekly amount. If saving anything feels "
        "impossible right now, start with $1 a week or the change in your pocket. That counts.")
    d.h3("Choose a buddy for the months ahead", 7)
    d.p("This is the last session, but your plans keep going. Choose a buddy to keep in touch "
        "with after the course: someone from any week, or your buddy now. Trade phone numbers. "
        "Then:")
    d.bullets([
        "Share your first goal and where you’ll keep the money.",
        "Trade one idea for finding a few extra dollars to save.",
    ])

    # 5 -------------------------------------------------------------------
    d.h2("5. Other Safety Nets", 10)
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
    d.h2("6. When Life Knocks You Off Course", 10)
    d.p("Some months, the plan won’t work. A surprise empties your safety net. Work hours get "
        "cut. A bill comes in bigger than you expected. This happens to everyone who makes a "
        "plan. What matters is what you do next:")
    d.bullets([
        "**No shame.** A setback isn’t a failure. If your safety net softened the blow, it did "
        "its job.",
        "**Call your buddy.** Say what happened to someone who’s on your side.",
        "**Reach for help before costly debt.** Call 211, a food pantry, or a utility or rent "
        "program before a payday loan. Ask the people you owe for a payment plan.",
        "**Restart smaller.** If $10 a week is too much right now, save $2. Make a new budget "
        "for the month you’re really having.",
        "**Refill your safety net** a little at a time, as soon as you can.",
    ])
    d.discuss([
        "What knocks your plans off course? What helps you get back on track?",
        "After a setback, what would you want your buddy to say to you?",
    ])

    # 7 -------------------------------------------------------------------
    d.h2("7. Looking Back and Keeping It Going", 18)
    d.read_aloud([
        "Four weeks ago, many of us felt worried or stuck about money. Since then, we’ve looked "
        "honestly at our numbers, built a budget, made a plan for debt, and started a safety "
        "net, even a small one. Most of all, we’ve learned that we don’t have to do this alone.",
        "This isn’t the end. It’s a beginning. Keep tracking, keep saving first, keep giving, "
        "and keep encouraging each other. Small, steady steps change lives.",
    ], title="Look How Far You’ve Come")
    d.label("With your buddy for the months ahead (7 minutes)")
    d.p("Turn to the **Keeping It Going** sheet. Check the habits you’ll keep, and agree on a "
        "day each month when you’ll talk.")
    d.label("In the weeks ahead, I will:", before=6)
    d.numbered([
        "Save something every week, even $1, and write it on the **Weekly Safety Net Tracker**.",
        "Use my safety net only for real emergencies, and refill it when I use it.",
        "If something knocks me off course, call my buddy and restart smaller.",
        "Make a new budget each month, and keep up with my debt plan.",
        "Look into one other safety net, like health coverage or renter’s insurance.",
        "Talk with my buddy once a month, using the **Monthly Check-In**.",
    ])
    d.p("**Want to go further?** Try the take-home **Looking Back, Looking Ahead**.")
    d.label("Gratitude and giving")
    d.p("Think of someone who has been part of your safety net, and thank them this week. "
        "Then think of one way to share what you’ve learned with someone else.")
    d.label("Closing circle")
    d.p("Think back to your “money in one word” from Session 1. Share the word you’d choose "
        "now, and one thing you’re grateful for from our time together.")

    # Notes ---------------------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Notes", odd=False)
    d.h1("Session 4 Notes")
    d.note("Space for your thoughts during our discussions.")
    for head in ["Surprises I can plan for", "My safety net plan",
                 "Other safety nets I want to look into", "Looking back, and what comes next"]:
        d.label(head, before=8)
        d.lines(4)

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
    d.page_break()
    d.h2("Putting My Safety Net to Work")
    d.note("The back of your safety net plan. If time runs short in class, finish this at home.")
    d.label("1. How long to my first goal?", before=4)
    d.p("My first goal $________ − what I have now $________ = $________ to go", size=10,
        after=4)
    d.p("$________ to go ÷ $________ a week = about ________ weeks", size=10, after=2)
    d.p("Example: a $100 goal, with $10 saved now and $5 a week: $90 ÷ $5 = 18 weeks, about "
        "four months. Saving a little more, or adding a gift or refund, gets you there sooner.",
        size=9, italic=True, after=6)
    d.label("2. Emergency or not? Use the three questions: unexpected, necessary, urgent.")
    d.grid(["Situation", "Emergency", "Not an emergency"], [
        ["The car you need to get to work breaks down", "☐", "☐"],
        ["A big sale on a TV you’ve wanted", "☐", "☐"],
        ["A child’s birthday next month", "☐", "☐"],
        ["An urgent-care co-pay for a sick child", "☐", "☐"],
        ["The rent, due on the 1st as usual", "☐", "☐"],
        ["Your hours are cut at work this month", "☐", "☐"],
    ], [4.5, 1.4, 1.4], height=0.3, size=10)
    d.p("Answers: the car, the co-pay, and the cut hours are emergencies. The sale is a want, and "
        "the birthday and rent are expected, so they belong in the budget.", size=9,
        italic=True, after=6)
    d.label("3. If I have to use my safety net, I’ll refill it by:")
    d.lines(1)
    d.principle("Save first, start small, and keep it for real emergencies. Even $100 set aside "
                "turns many crises into inconveniences, and keeps you out of new debt.")
    d.label("My first step this week", before=8)
    d.lines(2)

    # Homework: weekly tracker -------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Weekly Safety Net Tracker")
    d.h1("Weekly Safety Net Tracker")
    d.note("Session 4 · For the weeks ahead. Write down every amount you add to (or take from) "
           "your safety net, and keep using your budget and debt plan. Need more weeks? Use a "
           "fresh copy or a notebook. The back is your plan for the months after the course.")
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
    d.page_break()
    d.h2("Keeping It Going")
    d.note("The back of your tracker. Keep it with your plans, and talk with your buddy once a "
           "month for the next three months.")
    d.label("The habits I’ll keep (check all that apply)", before=2)
    d.checks([
        "Write down what I spend, at least for a few days each month",
        "Make a budget before each month begins, on a fresh copy of **My Real Life Budget**",
        "Save something first, and put a little extra toward one debt at a time",
        "Use my safety net only for real emergencies, and refill it",
        "Give some time, talents, or money to others",
    ], size=10, after=1)
    d.p("My buddy: ______________________________   Phone: ____________________   We’ll talk "
        "on the ______ of each month.", size=10, before=6, after=4)
    d.label("Monthly Check-In", before=2)
    d.grid(["", "Month 1", "Month 2", "Month 3"], [
        ["Date we talked", "", "", ""],
        ["Did I use my budget?", "☐ Yes ☐ Some ☐ No", "☐ Yes ☐ Some ☐ No", "☐ Yes ☐ Some ☐ No"],
        ["Safety net now", "$", "$", "$"],
        ["What I owe now", "$", "$", "$"],
        ["One thing that went well", "", "", ""],
        ["One thing that was hard", "", "", ""],
        ["How I gave or helped someone", "", "", ""],
        ["My goal for next month", "", "", ""],
    ], [2.2, 1.7, 1.7, 1.7], height=0.42)
    d.label("Questions to ask each other", before=6)
    d.bullets([
        "What are you proud of this month?",
        "What’s getting in the way, and what could help?",
        "Did anything knock you off course? What’s your restart step?",
        "How can I encourage you before we talk next?",
    ], size=10, after=1)

    d.save(OUT)


if __name__ == "__main__":
    guide()
