import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 5 · Building Wealth"


def guide():
    d = Doc("template.docx", margins=1.0, footer=FOOT)
    d.h1("Building Wealth")
    d.p("**Session 5 (optional):** Small, steady steps toward a secure and meaningful future",
        size=13, after=10)

    d.p("This optional session builds on the first four. It’s for when your budget is "
        "working, your safety net has started, and you’re ready to think about growing money "
        "for the long run. “Wealth” here doesn’t mean being rich. It means having enough, "
        "with peace of mind, and room to help others.")
    d.label("In this session, you will:", before=0)
    d.bullets([
        "Check in on how your plans are going",
        "See how time helps even small amounts grow",
        "Learn the difference between one company’s stock and an index fund",
        "Learn what to do when the market drops",
        "Learn the difference between retirement accounts and other investing, and how "
        "Social Security fits in",
        "Learn how to spot scams",
        "Make a plan for saving for later",
    ])
    d.how_to_use("Have your budget, debt plan, safety net plan, and Keeping It Going sheet "
                 "ready to use.")

    # 1 -------------------------------------------------------------------
    d.h2("1. Opening Inspiration", 5)
    d.read_aloud([
        "“The best time to plant a tree was 20 years ago. The second best time is now.” "
        "(A proverb)",
    ])
    d.discuss(["What “tree” would you like to plant for your future, or for your family’s?"])

    # 2 -------------------------------------------------------------------
    d.h2("2. Buddy Check-In", 8)
    d.label("With your buddy (3 minutes)")
    d.bullets([
        "Share how your safety net is going, even if it’s just a few dollars.",
        "Share one habit from the course you’ve kept.",
    ])
    d.label("As a group (5 minutes)")
    d.bullets([
        "What has changed in how you handle money since Session 1?",
        "What would you want in place before you start saving for later?",
    ])

    # 3 -------------------------------------------------------------------
    d.h2("3. Time Is Your Best Friend", 12)
    d.read_aloud([
        "When you save or invest money for a long time, it can earn money, and then that money "
        "earns money too. This is called **compound growth**. The longer you leave it, the "
        "faster it grows. Here is what $25 a month could become if it grew about 7% a year. "
        "(Real growth goes up and down, and isn’t guaranteed.)",
    ], title="How Small Amounts Grow")
    d.grid(["$25 a month for…", "You put in", "It could grow to about"], [
        ["10 years", "$3,000", "$4,300"],
        ["20 years", "$6,000", "$13,000"],
        ["30 years", "$9,000", "$30,500"],
    ], [2.2, 2.0, 2.3], height=0.3, size=11)
    d.p("**Joanne and Mike:** Joanne saves $50 a month from age 25 to 35, then stops. Mike saves "
        "$50 a month from age 35 to 65. Joanne puts in $6,000; Mike puts in $18,000. At 65, "
        "Joanne has about $70,000 and Mike about $61,000. Starting early helps most, but "
        "starting now, at any age, is always better than waiting.")
    d.discuss([
        "What surprises you about these numbers?",
        "What has kept you, or people you know, from saving for the future?",
    ])

    # 4 -------------------------------------------------------------------
    d.h2("4. Saving and Investing", 15)
    d.p("**Saving** is for money you’ll need in the next few years, like your safety net. Keep it "
        "safe and easy to reach. **Investing** is for money you won’t need for five years or "
        "more. It goes up and down, but over many years it usually grows more. Build your "
        "safety net and pay down costly debt first.")
    d.read_aloud([
        "A **stock** is a small piece of one company. If the company does well, the stock can "
        "go up. If it does badly, the stock can fall a lot, or become worthless. Picking which "
        "companies will do well is hard, even for experts. That’s why buying single stocks is "
        "not a good way to start investing.",
        "An **index fund** is a kind of mutual fund that buys a small piece of hundreds or "
        "thousands of companies at once. It follows a list, called an index, such as the 500 "
        "largest companies in the U.S. Its benefits:",
    ], title="One Company, or Many?", bullets=[
        "**Spread out.** If one company fails, it’s only a tiny part of what you own. "
        "This is called being **diversified**.",
        "**Low cost.** No one is paid to pick stocks, so fees are low, often less than 10¢ a "
        "year for every $100.",
        "**Simple.** You don’t have to choose companies or follow the news.",
        "**Hard to beat.** Over many years, most professionals who pick stocks do worse than a "
        "simple index fund, mostly because of their higher fees.",
    ], after_bullets=[
        "Fees matter more than they look. $50 a month for 30 years could grow to about $60,000 "
        "in a low-fee index fund, but only about $50,000 in a fund that charges 1% a year. A "
        "**target-date fund** is one simple choice: a mix of funds, often index funds, that "
        "gets safer as the year you plan to retire gets closer. Check that its fee is low.",
    ])
    d.discuss([
        "Why might one company’s stock feel exciting? Why is it risky?",
        "What questions would you ask about a fund before putting money in it?",
    ])

    # 5 -------------------------------------------------------------------
    d.h2("5. When the Market Drops", 8)
    d.read_aloud([
        "Investments go up and down, sometimes a lot. In 2008 and 2009, U.S. stock prices fell "
        "by about half, and took about five years to get back to where they had been. In 2020, "
        "they fell by about a third in a month, then came back in about six months. No one "
        "knows when the next drop will come, but one will.",
        "The people hurt most were often those who sold in fear while prices were low. That "
        "turned a drop on paper into a real loss. People who held on, and kept putting in a "
        "little each month, bought at low prices and came out ahead when prices recovered.",
        "That’s why investing is only for money you won’t need for five years or more, and why "
        "your safety net stays in savings. When the market drops, don’t panic. Leave it alone, "
        "and keep going.",
    ], title="Ups and Downs")
    d.discuss([
        "How might you feel if your account dropped by a third? What would help you hold on?",
        "Why does a safety net make it easier to leave your investments alone?",
    ])

    # 6 -------------------------------------------------------------------
    d.h2("6. Retirement and Other Long-Term Investing", 20)
    d.read_aloud([
        "A **retirement account** gives you a tax break for saving for later in life. At work "
        "it may be called a 401(k) or 403(b). Many jobs add a **match**: your job adds money "
        "when you save, often 50¢ or $1 for each $1 you put in, up to a limit. It’s free "
        "money, so put in at least enough to get the full match. Without a plan at work, you "
        "can open an IRA (Individual Retirement Account) of your own at a bank, credit union, or "
        "investment company. Retirement money is meant to stay put until about age 59½. Taking "
        "it out early usually means paying taxes plus a 10% penalty.",
        "A **regular investment account** has no tax break and no yearly limit, and you can take "
        "money out whenever you choose, though you may owe tax on what it earned. It’s for "
        "long-term goals other than retirement, at least five years away, like a down payment "
        "on a home. In either kind of account, low-fee index funds are a good choice.",
        "A good order: your safety net, then costly debt, then the full job match, then more "
        "for retirement, then other long-term goals. If your income is modest, you may also get "
        "a tax credit for saving for retirement. Free tax help (VITA, Volunteer Income Tax "
        "Assistance) can tell you.",
    ], title="Two Kinds of Accounts")
    d.p("**Roth or traditional?** Many retirement accounts come in two kinds. With a "
        "**traditional** account, you get the tax break now and pay tax when you take the money "
        "out. With a **Roth** account, you pay tax now, and the money comes out tax-free in "
        "retirement. You can also take out what you put in to a Roth IRA, but not what it "
        "earned, without a penalty. If your taxes are low now, a Roth is often a good choice. "
        "Free tax help (VITA) can help you decide.")
    d.p("**When you change jobs,** don’t cash out your retirement plan. You’d lose taxes plus "
        "the 10% penalty, and the years of growth. Leave it where it is, move it to your new "
        "job’s plan, or move it to an IRA. Ask for a **direct rollover**, so the money goes "
        "straight from one account to the other.")
    d.p("**Social Security** will be the main retirement income for most of us. Work that’s "
        "reported, where Social Security tax comes out of your pay, earns you credit toward it. "
        "You can start your checks at 62, but they’ll be smaller for life. Waiting until your "
        "full retirement age (67 for most people working today), or until 70, makes each check "
        "bigger. Look up your own estimate at ssa.gov/myaccount.")
    d.p("**If you get benefits** like SSI or Medicaid, savings over a set limit can affect "
        "them, and retirement accounts may count. Ask your caseworker before saving larger "
        "amounts. If you have a disability, an **ABLE account** may let you save without losing "
        "benefits.")
    d.label("Protect what you build")
    d.p("Watch out for scams. Be careful if someone:", after=2)
    d.bullets([
        "Promises big, quick, or sure profits",
        "Pushes you to decide right now",
        "Wants you to pay with a gift card, a wire transfer, or crypto",
        "Sells something you can’t explain in your own words",
    ])
    d.p("If it sounds too good to be true, it is. Talk to someone you trust before you sign "
        "anything.")
    d.discuss([
        "Does your job, or a family member’s, offer a retirement plan? How could you find out?",
        "Who could you talk to before making a money decision?",
    ])

    # 7 -------------------------------------------------------------------
    d.h2("7. My Plan for Later", 15)
    d.h3("On your own", 10, before=2)
    d.p("Turn to the **My Plan for Later** worksheet. Check where you are, then choose your "
        "next step. If you aren’t ready to invest yet, that’s fine: your next step is your "
        "safety net or your debt plan.")
    d.h3("With your buddy", 5)
    d.bullets([
        "Share your next step.",
        "Agree on who will find out what before your next monthly check-in, using the **Finding "
        "Out** sheet.",
    ])

    # 8 -------------------------------------------------------------------
    d.h2("8. Wrap-up and Closing", 7)
    d.label("In the weeks ahead, I will:", before=2)
    d.numbered([
        "Find out about the retirement plan at my job, or where I could open an IRA, using the "
        "**Finding Out** sheet.",
        "Look up my Social Security estimate at ssa.gov/myaccount, if I’ve worked.",
        "Keep saving something first, and keep my safety net for real emergencies.",
        "Talk with my buddy at our monthly check-in.",
    ])
    d.p("**Want to go further?** The Session 5 take-home worksheets are optional. Do them "
        "whenever you have time.")
    d.label("Gratitude and giving")
    d.p("Growing money for later isn’t only for us. It’s also a way to care for our families "
        "and to have more to share. Think of one person you could share an idea from today with.")
    d.label("Closing circle")
    d.p("Finish this sentence: “The tree I’m planting for my future is …”")

    # Notes ---------------------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Notes", odd=False)
    d.h1("Session 5 Notes")
    d.note("Space for your thoughts during our discussions.")
    for head in ["How small amounts grow", "Stocks, index funds, and ups and downs",
                 "Retirement, Social Security, and other investing",
                 "Things I want to remember"]:
        d.label(head, before=8)
        d.lines(4)

    # Worksheet: plan for later ---------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · My Plan for Later")
    d.h1("My Plan for Later")
    d.note("Session 5 · In class. Best guesses are fine. This page is private.")
    d.label("Step 1. Am I ready to invest? (Check what’s true today.)", before=4)
    d.checks([
        "My budget works most months.",
        "I have a starter safety net ($500, or my own first goal).",
        "I’ve paid off costly debt, like payday loans and high-interest cards, or I have a plan "
        "for it.",
        "I have some money I won’t need for at least five years.",
    ], size=10, after=1)
    d.p("Not all checked yet? That’s fine. My next step is the first box I haven’t checked.",
        size=10, before=2, after=6)
    d.label("Step 2. Where my money for later could go")
    d.grid(["Account", "Do I have one?", "Each month"], [
        ["Retirement plan at work (401(k), 403(b)) with a match", "☐ Yes ☐ No ☐ Not sure",
         "$"],
        ["IRA of my own (if there’s no plan at work)", "☐ Yes ☐ No ☐ Not sure", "$"],
        ["Regular investment account (long-term goals)", "☐ Yes ☐ No ☐ Not sure", "$"],
        ["Savings (goals less than five years away)", "☐ Yes ☐ No ☐ Not sure", "$"],
    ], [3.7, 2.2, 1.4], height=0.34, size=10)
    d.p("If my job matches, it adds up to ______% of my pay. To get the full match, I need to "
        "put in ______%.", size=10, before=4, after=6)
    d.label("Step 3. What I’ll choose inside the account")
    d.p("☐ A low-fee target-date fund     ☐ A low-fee index fund     ☐ Not sure yet: I’ll ask "
        "______________", size=10, after=4)
    d.p("The yearly fee I’ll look for: less than ______% (many index funds charge less than "
        "0.1%)", size=10, after=6)
    d.label("Where to go with questions")
    d.p("☐ My buddy   ☐ My job’s HR office   ☐ Free tax help (VITA)   ☐ A fee-only advisor   "
        "☐ Social Security (ssa.gov)   ☐ Other: ______________", size=10)
    d.page_break()
    d.h2("One Company, or Many?")
    d.note("The back of your plan. If time runs short in class, finish this at home.")
    d.label("1. Stock or index fund? Check which one each sentence describes.", before=4)
    d.grid(["", "One company’s stock", "Index fund"], [
        ["Owns a small piece of hundreds of companies", "☐", "☐"],
        ["One bad year for one company can wipe out much of it", "☐", "☐"],
        ["Usually has very low fees", "☐", "☐"],
        ["You have to pick the winners yourself", "☐", "☐"],
        ["A good first choice for most people", "☐", "☐"],
    ], [4.3, 1.5, 1.5], height=0.3, size=10)
    d.p("Answers: the index fund owns many companies, has low fees, and is a good first choice. "
        "A single stock can lose much of its value, and you have to pick it yourself.", size=9,
        italic=True, after=6)
    d.label("2. Which account fits each goal?")
    d.grid(["Goal", "Savings", "Retirement account", "Regular investment account"], [
        ["Retirement in 30 years", "☐", "☐", "☐"],
        ["New tires next year", "☐", "☐", "☐"],
        ["A down payment on a home in 8 years", "☐", "☐", "☐"],
        ["My safety net", "☐", "☐", "☐"],
    ], [2.9, 1.1, 1.5, 1.8], height=0.3, size=10)
    d.p("Answers: retirement goes in a retirement account; the tires and your safety net go in "
        "savings; the home in 8 years could go in a regular investment account.", size=9,
        italic=True, after=6)
    d.label("3. My first step toward investing (or toward being ready):")
    d.lines(1)
    d.principle("Build your safety net first. Then invest a little, steadily, in low-fee funds "
                "that own many companies, and give it time to grow.")
    d.label("My first step this week", before=8)
    d.lines(2)

    # Homework: finding out ---------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Finding Out")
    d.h1("Finding Out")
    d.note("Session 5 · Homework. Find the answers to a few questions before you invest. Share "
           "what you learn with your buddy at your next monthly check-in.")
    d.label("At work (or a family member’s work)", before=4)
    for q in ["Is there a retirement plan? Can I join now?",
              "Does the company match what I put in? Up to how much?",
              "Is there a target-date fund or index fund? What is its yearly fee?",
              "How do I sign up? Can I start small, like 1% or 2% of my pay?"]:
        d.p(q, size=10, after=0)
        d.lines(1)
    d.label("If there’s no plan at work", before=6)
    for q in ["Where could I open an IRA (a bank, credit union, or investment company)?",
              "Is there a minimum to start? Can I set up a small automatic deposit each month?",
              "Does it offer low-fee index funds or target-date funds?"]:
        d.p(q, size=10, after=0)
        d.lines(1)
    d.p("**At tax time:** ☐ Ask free tax help (VITA) whether I qualify for the tax credit for "
        "retirement saving.", size=10, before=6, after=2)
    d.label("Before I sign anything, I’ll ask myself", before=6)
    d.checks([
        "Can I explain this in my own words?",
        "Is anyone pressuring me to decide now, or promising big, sure returns?",
        "Is the fee low?",
        "Have I talked with someone I trust?",
    ], size=10, after=1)
    d.question(1, "What I found out, and my next step:", 2, size=10)

    d.save(OUT)


if __name__ == "__main__":
    guide()
