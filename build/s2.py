import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 2 · Creating a Budget"


def guide():
    d = Doc("template.docx", margins=1.0, footer=FOOT)
    d.h1("Creating a Budget")
    d.p("**Session 2:** A budget that fits your real life", size=13, after=10)

    d.label("In this session, you will:", before=0)
    d.bullets([
        "Share what you learned from tracking your spending",
        "Learn a simple way to plan your money: give every dollar a job",
        "Build your own budget with your real numbers",
        "Think about needs, wants, and what matters most to you",
        "Choose a buddy for the coming week",
    ])
    d.how_to_use("Have your tracker from last week, and any pay stubs or bills you brought, "
                 "ready to use.")

    # 1 -------------------------------------------------------------------
    d.h2("1. Opening Inspiration", 5)
    d.read_aloud([
        "“I am convinced that it is not the amount of money an individual earns that brings "
        "peace of mind as much as it is having *control* of his money. Money can be an obedient "
        "servant but a harsh taskmaster.”",
        "“Many people think a budget robs them of their freedom. On the contrary, successful "
        "people have learned that a budget makes real economic freedom possible.” (N. Eldon "
        "Tanner, “Constancy amid Change,” October 1979 general conference)",
    ])
    d.discuss(["What would “having control of your money” feel like for you?"])

    # 2 -------------------------------------------------------------------
    d.h2("2. Buddy Check-In and Tracking Review", 10)
    d.label("With last week’s buddy (4 minutes)")
    d.bullets([
        "Share one thing you learned from tracking your spending.",
        "Share one thing you’re proud of from the week.",
    ])
    d.label("As a group (6 minutes)")
    d.bullets([
        "How did tracking go? Did you track every day, most days, or some days?",
        "What was the hardest part?",
        "What did you notice about your feelings and your spending?",
        "Look at your Snapshot from Session 1. Which line was most different from what you "
        "tracked?",
    ])
    d.p("**Remember:** Perfect tracking isn’t the goal. Noticing is. If you tracked even one "
        "day, you’ve already started to change.")

    # 3 -------------------------------------------------------------------
    d.h2("3. What a Budget Really Is", 15)
    d.read_aloud([
        "A budget is a plan for your money, made before the money is spent. It isn’t about "
        "cutting out all fun, and you don’t need to be good at math. Adding and subtracting "
        "is enough. A budget matters most when money is tight or when your income changes from "
        "month to month.",
        "The method we’ll use is called **every dollar has a job**. Start with the money you "
        "expect to come in. Then give each dollar a job: rent, food, the electric bill, gas, a "
        "little fun, saving, and giving, until no dollar is left without a job. If you go over in "
        "one area, you haven’t failed. You move money from another job and adjust next month. "
        "A budget is permission to spend on what matters most to you.",
    ], title="Every Dollar Has a Job")
    d.read_aloud([
        "When money comes in, set aside a little for savings before you spend on anything else, "
        "even $5 or the change in your pocket. The habit matters more than the amount. Giving "
        "belongs in a budget too. Many of us give to our church or to people in need, and time "
        "and talents count as giving.",
        "Extra money needs a job too. Before it comes in, from extra hours, a second job, a tax "
        "refund, or a gift, decide what it will do: savings, a debt, or one planned want. Money "
        "without a job tends to disappear. If you work extra hours, count what they cost you, "
        "like childcare, gas, and food on the go, so you know what you really keep.",
    ], title="Save First, and Make Room to Give")
    d.discuss([
        "What has made budgeting hard for you in the past?",
        "Which idea here could make it easier?",
        "What’s one way you already give, with money, time, or talents?",
    ])

    # 4 -------------------------------------------------------------------
    d.h2("4. Build Your Real Life Budget", 25)
    d.h3("On your own", 18, before=2)
    d.p("Turn to the **My Real Life Budget** worksheet. Use your tracker, bills, and pay stubs. "
        "If your income changes from month to month, use a low but typical month. Best guesses "
        "are fine. If you share money with a partner, build it together if you can. If you don’t "
        "finish, that’s OK. You can finish at home.")
    d.h3("With a new buddy", 7)
    d.p("Pair up with someone who wasn’t your buddy last week, or keep the same buddy if you "
        "prefer. (A group of three is fine.) This is your buddy for the coming week, so trade "
        "phone numbers. Then:")
    d.bullets([
        "Share your biggest budget challenge.",
        "Help each other spot anything missing: a yearly bill, school costs, birthdays, or "
        "holidays.",
        "Think of community resources that could help, like a food pantry or utility assistance.",
    ])

    # 5 -------------------------------------------------------------------
    d.h2("5. Needs, Wants, and What Matters", 12)
    d.read_aloud([
        "A **need** is something you must have to live and work: a place to live, basic food, "
        "utilities, and a way to get to work. A **want** makes life better, but you could live "
        "without it. Many things are a little of both. Food is a need, but eating out is "
        "usually a want. A phone may be a need, but the newest phone is a want.",
        "Your needs may be different from someone else’s. And it’s OK to budget for some "
        "wants. A budget with no joy in it rarely lasts. The best question isn’t “Is this "
        "a need?” but “Is this worth it to me right now?”",
    ])
    d.discuss([
        "Need, want, or does it depend? Internet service. Brand-name groceries. New work "
        "clothes when the old ones are worn out. A streaming service. Birthday gifts for family.",
        "Which want matters enough to you to keep in your budget?",
        "Which need could you meet for less, or with help from a community resource?",
    ])

    # 6 -------------------------------------------------------------------
    d.h2("6. Wrap-up and This Week’s Commitment", 8)
    d.label("This week, I will:", before=2)
    d.numbered([
        "Live on my budget, and write down what I spend on the **Weekly Budget Tracker**.",
        "When I go over or under, write down why, to learn and not to judge.",
        "Pick ONE area to focus on, such as groceries or eating out.",
        "Save something first. Start a jar or envelope with any amount, even loose change.",
        "Call or text my buddy at least once to share how it’s going.",
    ])
    d.p("**Want to go further?** The Session 2 take-home worksheets are optional. Do them only if "
        "you have time after your tracker.")
    d.label("Gratitude and giving")
    d.p("A budget helps us see what we already have. Notice one thing in your budget you’re "
        "grateful for. Even a small gift, or time spent helping someone, belongs in a healthy "
        "budget.")
    d.label("Closing circle")
    d.p("What’s one thing about budgeting that feels more doable now than when we started?")
    d.p("**Next week:** We’ll talk about debt: how to pay it down, and how to break the cycle "
        "of borrowing.")

    # Notes ---------------------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Notes", odd=False)
    d.h1("Session 2 Notes")
    d.note("Space for your thoughts during our discussions.")
    for head in ["What I learned from tracking", "Every dollar has a job",
                 "Building my budget", "Needs, wants, and what matters to me"]:
        d.label(head, before=8)
        d.lines(4)

    # Worksheet: real life budget ---------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · My Real Life Budget")
    d.h1("My Real Life Budget")
    d.note("Session 2 · In class. Use your tracker from last week. Give every dollar a job: the "
           "money coming in, minus everything you plan to spend, save, and give, should equal zero.")
    W = (2.75, 0.9)
    d.money_table("Step 1. Money coming in (each month)", [
        "Pay from work (after taxes)",
        "Benefits (SNAP, SSI, etc.)",
        "Child support",
        "Side jobs or gig work",
        "Help from family or others",
        "Other: ________________",
    ], "Total coming in", widths=W, cols=2)
    d.p("**Not paid monthly?** Paid every week: one paycheck × 4.33. Paid every two weeks: one paycheck × 2.17. Paid twice a month: one paycheck × 2.", size=9, before=2, after=2)
    d.money_table("Step 2. Bills that stay about the same", [
        "Rent or mortgage",
        "Renter’s or home insurance",
        "Utilities (average month)",
        "Phone and internet",
        "Car payment",
        "Car insurance",
        "Debt minimum payments",
        "Childcare",
        "Health insurance",
        "Other: ________________",
    ], "Total bills", widths=W, cols=2)
    d.money_table("Step 3. Spending that changes", [
        "Groceries",
        "Eating out and takeout",
        "Gas, bus fare, rides",
        "Personal care and household",
        "Clothing",
        "Medical and prescriptions",
        "Fun and entertainment",
        "Subscriptions",
        "Gifts and holidays",
        "Pets",
        "School costs",
        "Other: ________________",
    ], "Total spending", widths=W, cols=2)
    d.money_table("Step 4. Saving and giving", [
        "Emergency savings (jar, envelope, or account)",
        "Extra debt payments",
        "Giving (church, charity, helping others)",
        "Other goal: ________________",
    ], "Total saving and giving", widths=W, cols=2)
    d.label("Step 5. The reality check", before=6)
    d.grid(["Total coming in", "− Bills", "− Spending", "− Saving & giving",
            "= What’s left"],
           [["$", "$", "$", "$", "$"]], [1.46, 1.46, 1.46, 1.46, 1.46], height=0.34)
    d.bullets([
        "**More than zero?** Give those dollars a job: savings or an extra debt payment.",
        "**Zero?** Every dollar has a job. Well done!",
        "**Less than zero?** You’re not alone. Look at Step 3 for small changes, look for "
        "ways to add income, and use community resources such as food pantries, SNAP, WIC, "
        "school meals, childcare help, utility assistance, or 211. Free tax help (VITA) can "
        "check for tax credits for families. Using help is part of a good plan.",
    ], size=10, after=1)
    d.label("Two changes I could make", before=6)
    d.p("1. I could spend $________ less on ____________________ by _______________________________",
        size=10, after=6)
    d.p("2. I could spend $________ less on ____________________ by _______________________________",
        size=10, after=8)
    d.box([
        "**Quick check (optional): the 50/30/20 target.** One common goal is about half of your "
        "income for needs (50%), some for wants (30%), and the rest for saving, giving, and extra "
        "debt payments (20%). For many people, needs take more than half right now. That’s "
        "common. Treat it as something to work toward, not a test.",
        "My income $________ × 0.50 = $________ for needs     × 0.30 = $________ for wants"
        "     × 0.20 = $________ for saving and giving",
    ])
    d.principle("Give every dollar a job before the month begins, and save a little first, even "
                "$5. A plan you adjust as you go beats no plan at all.")
    d.label("My first step this week", before=8)
    d.lines(2)

    # Homework: weekly tracker --------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Weekly Budget Tracker")
    d.h1("Weekly Budget Tracker")
    d.note("Session 2 · Homework. Write down what you spend this week, then compare it with your "
           "budget at the end of the week. Bring this to Session 3.")
    d.p("Week starting: ______________     My buddy this week: ________________________     "
        "Phone: ________________", size=10, after=2)
    d.p("Check in with your buddy at least once this week. Date we talked: ____________", size=10,
        after=8)
    d.label("What I spent", before=0)
    d.grid(["Day", "What I bought", "Budget area", "Amount"],
           [[""] * 4 for _ in range(19)], [1.0, 3.3, 2.0, 1.0], height=0.3)
    d.page_break()
    d.label("End of the week: how did I do?", before=0)
    d.note("For each area, use one week of your budget: the monthly amount ÷ 4.3 (a month is about 4.3 weeks).", after=3)
    d.grid(["Budget area", "Budget for the week", "What I spent", "Over or under", "Why?"], [
        ["Groceries", "$", "$", "", ""],
        ["Eating out", "$", "$", "", ""],
        ["Gas, bus fare, rides", "$", "$", "", ""],
        ["Personal and household", "$", "$", "", ""],
        ["Fun", "$", "$", "", ""],
        ["Other: ____________", "$", "$", "", ""],
    ], [1.9, 1.3, 1.2, 1.1, 1.8], height=0.3)
    d.p("Did I save something first this week?   ☐ Yes, $________     ☐ Not yet", size=10,
        before=4, after=4)
    d.question(1, "Where did I stay on track? What helped?", 2, size=10)
    d.question(2, "What will I change in my budget for next week?", 2, size=10)
    d.question(3, "What am I proud of this week?", 2, size=10)

    d.save(OUT)


if __name__ == "__main__":
    guide()
