import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 3 · Breaking the Debt Cycle"


def guide():
    d = Doc("template.docx", margins=1.0, footer=FOOT)
    d.h1("Breaking the Debt Cycle")
    d.p("**Session 3:** A plan to pay down what you owe, and stay out of new debt", size=13,
        after=10)

    d.label("In this session, you will:", before=0)
    d.bullets([
        "See how interest makes debt cost more the longer it lasts",
        "Learn two simple ways to pay down debt",
        "Make a plan for your own debts",
        "Learn your rights with debt collectors, and how to ask for help",
        "Choose a buddy for the coming week",
    ])
    d.how_to_use("Have your budget from last week, and any bills or statements for money you "
                 "owe, ready to use.")

    # 1 -------------------------------------------------------------------
    d.h2("1. Opening Inspiration", 5)
    d.read_aloud([
        "“Interest never sleeps nor sickens nor dies; it never goes to the hospital; it works "
        "on Sundays and holidays; it never takes a vacation. … Once in debt, interest is your "
        "companion every minute of the day and night; …” (J. Reuben Clark Jr., quoted by Joseph B. "
        "Wirthlin, “Earthly Debts, Heavenly Debts,” April 2004 general conference)",
        "“When we make purchases on credit, they give us only an illusion of prosperity. We think "
        "we own things, but the reality is, our things own us.” (Joseph B. Wirthlin, same talk)",
    ])
    d.discuss(["What would it feel like to have one less payment each month?"])

    # 2 -------------------------------------------------------------------
    d.h2("2. Buddy Check-In and Budget Review", 10)
    d.label("With last week’s buddy (4 minutes)")
    d.bullets([
        "Share one way your budget helped you this week.",
        "Share one place where it was hard to stick to.",
    ])
    d.label("As a group (6 minutes)")
    d.bullets([
        "Where did your budget work? Where did it surprise you?",
        "Did anything come up this week that you hadn’t planned for? How did you pay for it?",
    ])
    d.p("**Remember:** Many of us reach for a credit card, a loan, or a friend when something "
        "unexpected happens. That’s how debt grows. Today is about breaking that cycle, one "
        "step at a time.")

    # 3 -------------------------------------------------------------------
    d.h2("3. The True Cost of Debt", 15)
    d.read_aloud([
        "Debt is money you owe. It can be a credit card, a store card, or a car loan. It can be "
        "a payday loan, a title loan, or a medical bill. It can be “buy now, pay later,” "
        "rent-to-own, back rent, or money from family. Having debt doesn’t make you a bad "
        "person. Most of the time, life cost more than you had, and you did what you had to do.",
        "Most debt also has **interest**. Interest is a fee for borrowing. It is added every "
        "month until you pay the debt off. Here is what happens with $3,000 on a credit card "
        "at 22% interest:",
    ], title="How Interest Works Against You")
    d.grid(["If you pay each month", "Time to pay it off", "Total you pay", "Interest alone"], [
        ["$75", "6 years, 1 month", "about $5,460", "about $2,460"],
        ["$150", "2 years, 2 months", "about $3,770", "about $770"],
    ], [1.9, 1.6, 1.5, 1.5], height=0.3, size=11)
    d.p("Paying $75 more each month saves almost four years and about $1,690. Even an extra "
        "$10 or $20 helps. Paying only the minimum takes even longer, because the minimum "
        "shrinks as you pay the balance down. Payday loans, title loans, and rent-to-own often cost far more than "
        "a credit card, so they are worth paying off first or avoiding when you can.")
    d.discuss([
        "What surprises you about these numbers?",
        "What kinds of debt are most common for people you know?",
        "What would you do with the money you now spend on interest?",
    ])

    # 4 -------------------------------------------------------------------
    d.h2("4. Make Your Debt Plan", 25)
    d.read_aloud([
        "First, keep up with the bills that keep your family safe: housing, utilities, food, and "
        "getting to work. Then pay at least the minimum on every debt. Any extra money goes to "
        "**one debt at a time**. Choose which one in one of two ways:",
    ], title="Two Ways to Pay It Down", bullets=[
        "**Snowball:** Pay off the smallest balance first. You get a quick win, and that keeps "
        "you going.",
        "**Avalanche:** Pay off the debt with the highest interest rate first. This saves the "
        "most money.",
    ], after_bullets=[
        "When one debt is paid off, add its payment to the next one. Your payment grows like a "
        "snowball rolling downhill. The best method is the one you’ll stick with.",
    ])
    d.p("**Example:** A credit card for $1,200 at 24%, a store card for $300 at 18%, and a "
        "medical bill for $600 at 0%. With the snowball, you pay the store card first. With the "
        "avalanche, you pay the credit card first. Either way, you pay the minimum on the rest.")
    d.h3("On your own", 15, before=2)
    d.p("Turn to the **My Debt Plan** worksheet. List what you owe, choose a method, and find "
        "even a small extra amount in your budget. If you don’t know an interest rate, leave it "
        "blank and find it on a statement this week. If you have no debt, use the time to plan how "
        "to stay that way, or help your buddy.")
    d.h3("With a new buddy", 7)
    d.p("Pair up with someone new, or keep your buddy if you prefer. Trade phone numbers. Then:")
    d.bullets([
        "Share which method you chose, and why.",
        "Talk about what could get in the way, and what would help.",
    ])

    # 5 -------------------------------------------------------------------
    d.h2("5. Know Your Rights and Ask for Help", 12)
    d.read_aloud([
        "Debt collectors must follow the law. They can’t call before 8 a.m. or after 9 p.m., "
        "threaten you, or lie to you. You can ask them in writing to prove you owe the debt, and "
        "to contact you only in writing. Never pay a debt you don’t recognize until it’s proven.",
        "You can also call the people you owe and ask for help: a lower interest rate, a smaller "
        "payment, a payment plan, or a late fee removed. Many will say yes, especially if you "
        "call before you fall behind. Get any agreement in writing, and never promise a payment "
        "you can’t make. A **nonprofit credit counselor** can also help for free or at low cost. "
        "Be careful of companies that charge big fees up front to “settle” your debt.",
    ], title="You Have More Power Than You Think")
    d.label("Practice with your buddy")
    d.p("Take turns reading this aloud, as if you were on the phone:")
    d.p("“Hi, I’m calling about my account ending in ____. I want to pay what I owe, but "
        "money is tight right now. Is there any way you can help me with a lower interest rate, a "
        "lower payment, or a payment plan?”", italic=True)
    d.discuss([
        "How did it feel to say that out loud?",
        "Who in your life could you call for help or advice about debt?",
    ])

    # 6 -------------------------------------------------------------------
    d.h2("6. Wrap-up and This Week’s Commitment", 8)
    d.label("This week, I will:", before=2)
    d.numbered([
        "Pay at least the minimum on each debt, on time, and mark it on the **Weekly Debt "
        "Tracker**.",
        "Put any extra money, even $5, toward my first debt.",
        "Avoid new debt. If I’m tempted, I’ll wait a day or call my buddy first.",
        "Find any missing balances or interest rates on my statements, or by calling.",
        "Keep saving something first, even loose change.",
        "Call or text my buddy at least once.",
    ])
    d.p("**Want to go further?** The Session 3 take-home worksheets are optional. Do them only if "
        "you have time after your tracker.")
    d.label("Gratitude and giving")
    d.p("Every debt we pay off frees up money for our families and for helping others. Notice "
        "one thing you already own outright, and be grateful for it.")
    d.label("Closing circle")
    d.p("What’s one thing you’ll do differently about debt starting today?")
    d.p("**Next week:** We’ll build a safety net, a small cushion of savings so surprises don’t "
        "push us back into debt.")

    # Notes ---------------------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Notes", odd=False)
    d.h1("Session 3 Notes")
    d.note("Space for your thoughts during our discussions.")
    for head in ["How interest works against me", "My debt plan",
                 "My rights, and who can help", "Things I want to remember"]:
        d.label(head, before=8)
        d.lines(4)

    # Worksheet: debt plan --------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · My Debt Plan")
    d.h1("My Debt Plan")
    d.note("Session 3 · In class. Use your bills and statements. Best guesses are fine. Include "
           "everything you owe, even money owed to family or overdue bills. This page is private.")
    d.label("Step 1. What I owe", before=2)
    d.grid(["Who I owe", "Balance", "Interest rate", "Minimum payment", "Due date",
            "Behind?"],
           [[""] * 6 for _ in range(6)] + [["Totals", "$", "", "$", "", ""]],
           [2.2, 1.1, 1.0, 1.2, 0.9, 0.9], height=0.3, bold_rows=(6,), shade_rows=(6,))
    d.label("Step 2. Choose my method", before=6)
    d.p("☐ **Snowball:** smallest balance first     ☐ **Avalanche:** highest interest first"
        "     ☐ A mix of both", size=10, after=4)
    d.p("My debts in the order I’ll pay them off:", size=10, after=2)
    d.grid(["Order", "Who I owe", "Balance"], [
        ["1st (my target)", "", "$"],
        ["2nd", "", "$"],
        ["3rd", "", "$"],
    ], [1.6, 4.0, 1.7], height=0.28)
    d.label("Step 3. Find a little extra", before=6)
    d.p("Each month, I can put an extra $________ toward my target debt. It will come from:",
        size=10, after=2)
    d.p("     ☐ Spending less on ________________     ☐ Money left at month’s end     "
        "☐ Tax refunds, gifts, or extra hours", size=10, after=4)
    d.label("Step 4. Keep it rolling", before=6)
    d.p("When my first debt is paid off, I’ll add its payment to my next debt. I’ll celebrate "
        "by (something free or small): ______________________________________", size=10)
    d.box([
        "**If I can’t make all my minimum payments:** First keep up with housing, utilities, "
        "food, and getting to work. Then call the people I owe before I fall behind, and ask for "
        "a lower payment or a payment plan. A nonprofit credit counselor can help too. "
        "Calling 211 can connect me with local help.",
    ])
    d.page_break()
    d.h2("Seeing the Finish Line")
    d.note("The back of your debt plan. If time runs short in class, finish this at home.")
    d.p("A rough way to see when a debt will be paid off: divide the balance by what you pay "
        "each month. Interest adds a little more time, but you’ll see that there is an end.",
        size=10, after=4)
    d.box([
        "**Example (the snowball, from the guide):** The store card is $300. Pay the $25 minimum "
        "plus $25 extra, $50 a month: $300 ÷ $50 = about 6 months (a little more with interest).",
        "Then **roll it**: the medical bill’s $20 minimum plus the $50 you were paying on the "
        "store card makes $70 a month. By then the bill is down to about $480: $480 ÷ $70 = "
        "about 7 more months. Each payoff makes the next one faster.",
    ])
    d.label("My debts, in the order I’ll pay them off", before=6)
    d.grid(["Debt", "Balance", "Monthly payment", "Months to pay off (balance ÷ payment)"], [
        ["1st: ", "$", "$", ""],
        ["2nd: ", "$", "$", ""],
        ["3rd: ", "$", "$", ""],
    ], [2.2, 1.2, 1.4, 2.5], height=0.32)
    d.p("For each new target, the monthly payment = its own minimum + everything you were "
        "paying on the debt you just finished.", size=9, after=6)
    d.p("About when my first debt will be paid off: ________________   I’ll tell: "
        "________________", size=10, after=4)
    d.p("When I’m tempted to borrow again, I will: ________________________________________",
        size=10, after=6)
    d.principle("Focus on one debt at a time, and roll each finished payment into the next. "
                "Every payoff speeds up the next one. Avoid new debt while you do.")
    d.label("My first step this week", before=8)
    d.lines(2)

    # Homework: weekly tracker -----------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Weekly Debt Tracker")
    d.h1("Weekly Debt Tracker")
    d.note("Session 3 · Homework. Write down each payment you make this week, and keep using your "
           "budget. Bring this to Session 4.")
    d.p("Week starting: ______________     My buddy this week: ________________________     "
        "Phone: ________________", size=10, after=2)
    d.p("Check in with your buddy at least once this week. Date we talked: ____________", size=10,
        after=8)
    d.label("Payments I made", before=0)
    d.grid(["Date", "Who I paid", "Amount", "Extra?", "New balance"],
           [[""] * 5 for _ in range(7)], [1.0, 2.8, 1.1, 0.9, 1.5], height=0.3)
    d.label("This week I…", before=6)
    d.checks([
        "Paid every minimum on time",
        "Put extra money toward my target debt: $________",
        "Called someone I owe to ask for help (who: ________________)",
        "Saved something first: $________",
    ], size=10, after=1)
    d.p("Did I take on any new debt?   ☐ No     ☐ Yes: ______________________  Why? "
        "__________________________", size=10, before=4, after=4)
    d.question(1, "What helped me stick to my plan?", 2, size=10)
    d.question(2, "What got in the way, and what will I try next week?", 2, size=10)
    d.question(3, "What am I proud of this week?", 2, size=10)

    d.save(OUT)


if __name__ == "__main__":
    guide()
