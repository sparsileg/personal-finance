import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 5 · Building Wealth"


def guide():
    d = Doc("template.docx", margins=1.0, footer=FOOT)
    d.h1("Building Wealth")
    d.p("**Session 5 (optional):** Small, steady steps toward a secure and meaningful future",
        size=13, after=10)

    d.label("In this session, you will:", before=0)
    d.bullets([
        "Look back at how far you’ve come",
        "See how time helps even small amounts grow",
        "Learn simple, safe ways to save for later, and how to spot scams",
        "Make a plan for your next steps after this course",
        "Plan how you and your buddy will keep encouraging each other",
    ])
    d.p("“Wealth” here doesn’t mean being rich. It means having enough, with peace of "
        "mind, and room to help others.")
    d.how_to_use("Have your budget, debt plan, and safety net plan ready to use.")

    # 1 -------------------------------------------------------------------
    d.h2("1. Opening Inspiration", 5)
    d.read_aloud([
        "“If there is any one thing that will bring peace and contentment into the human heart, "
        "and into the family, it is to live within our means.” (Heber J. Grant, quoted by "
        "N. Eldon Tanner, “Constancy amid Change,” October 1979 general conference)",
    ])
    d.discuss(["What does a prosperous life mean to you, apart from money?"])

    # 2 -------------------------------------------------------------------
    d.h2("2. Check-In and Looking Back", 12)
    d.label("With last week’s buddy (4 minutes)")
    d.bullets([
        "Share how your safety net is going, even if it’s just a few dollars.",
        "Share one habit from this course you want to keep.",
    ])
    d.label("As a group (8 minutes)")
    d.bullets([
        "What’s the biggest change in how you think about money since our first session?",
        "Think back to your “money in one word” from Session 1. What word would you choose now?",
    ])

    # 3 -------------------------------------------------------------------
    d.h2("3. Time Is Your Best Friend", 15)
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
    d.h2("4. Growing Money for Later", 13)
    d.read_aloud([
        "**Saving** is for money you’ll need in the next few years, like your safety net. Keep it "
        "safe and easy to reach. **Investing** is for money you won’t need for five years or "
        "more, like retirement. It goes up and down, but over many years it usually grows more.",
        "Build your safety net and pay down costly debt first. Then, if your job offers a "
        "retirement plan with a **match**, put in at least enough to get the full match. It’s "
        "free money. Without a plan at work, you can open an account of your own, called an IRA, "
        "at a bank or credit union. A simple choice is a low-fee **target-date fund**, which "
        "spreads your money across many companies and adjusts as you get older. If your income "
        "is modest, you may also get a tax credit for saving. Free tax help (VITA) can tell you.",
    ], title="Saving and Investing Made Simple")
    d.read_aloud(
        ["Watch out for scams. Be careful if someone:"],
        title="Protect What You Build",
        bullets=[
            "Promises big, quick, or sure profits",
            "Pushes you to decide right now",
            "Wants you to pay with a gift card, a wire transfer, or crypto",
            "Sells something you can’t explain in your own words",
        ],
        after_bullets=["If it sounds too good to be true, it is. Talk to someone you trust "
                       "before you sign anything."])
    d.discuss([
        "Does your job, or a family member’s, offer a retirement plan? How could you find out?",
        "Who could you talk to before making a money decision?",
    ])

    # 5 -------------------------------------------------------------------
    d.h2("5. My Next Steps", 20)
    d.h3("On your own", 13, before=2)
    d.p("Turn to the **My Next Steps Plan** worksheet. Rate where you are today, then write one "
        "step for this week, this month, and this year. Small steps are best.")
    d.h3("With your buddy", 7)
    d.p("Choose a buddy to keep in touch with after the course, someone from any week. Trade "
        "phone numbers, then:")
    d.bullets([
        "Share your next steps.",
        "Agree on when you’ll check in each month, using the **Monthly Check-In** sheet.",
    ])

    # 6 -------------------------------------------------------------------
    d.h2("6. Celebration and Closing", 10)
    d.read_aloud([
        "Five weeks ago, many of us felt worried or stuck about money. Since then, we’ve looked "
        "honestly at our numbers, built a budget, made a plan for debt, and started a safety "
        "net, even a small one. Most of all, we’ve learned that we don’t have to do this alone.",
        "This isn’t the end. It’s a beginning. Keep tracking, keep saving first, keep giving, "
        "and keep encouraging each other. Small, steady steps change lives.",
    ], title="Look How Far You’ve Come")
    d.label("Gratitude and giving")
    d.p("Think of one way you can share what you’ve learned: with your family, a friend, or "
        "someone just starting out. Helping others is part of a prosperous life.")
    d.label("Closing circle")
    d.p("Finish this sentence: “I’m continuing my money journey by …” Then share one thing "
        "you’re grateful for from our time together.")

    # Notes ---------------------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Notes", odd=False)
    d.h1("Session 5 Notes")
    d.note("Space for your thoughts during our discussions.")
    for head in ["What a prosperous life means to me", "How small amounts grow",
                 "Saving, investing, and staying safe", "Things I want to remember"]:
        d.label(head, before=8)
        d.lines(4)

    # Worksheet: next steps ----------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · My Next Steps Plan")
    d.h1("My Next Steps Plan")
    d.note("Session 5 · In class. Small, specific steps work best. This page is yours to keep.")
    d.label("Where I am today (circle one for each: 1 = not started, 5 = going well)", before=4)
    d.grid(["Area", "Rating", "One thing I’m proud of here"], [
        ["Knowing where my money goes", "1   2   3   4   5", ""],
        ["Using a budget", "1   2   3   4   5", ""],
        ["Paying down debt (or staying out of it)", "1   2   3   4   5", ""],
        ["Building my safety net", "1   2   3   4   5", ""],
        ["Saving for later", "1   2   3   4   5", ""],
        ["Giving and helping others", "1   2   3   4   5", ""],
    ], [2.9, 1.5, 2.9], height=0.32)
    d.label("My next steps", before=6)
    d.grid(["When", "What I’ll do"], [
        ["This week", ""],
        ["This month", ""],
        ["In 3 months", ""],
        ["By this time next year", ""],
    ], [1.7, 5.6], height=0.45)
    d.label("My 3-month goals", before=6)
    d.grid(["", "Today", "In 3 months"], [
        ["My safety net", "$", "$"],
        ["What I owe", "$", "$"],
        ["Saving for later each month", "$", "$"],
    ], [2.9, 2.2, 2.2], height=0.3)
    d.label("Where to go with questions", before=6)
    d.p("☐ My buddy   ☐ 211   ☐ Free tax help (VITA)   ☐ A nonprofit credit counselor   "
        "☐ My job’s HR office   ☐ Other: ______________", size=10)
    d.page_break()
    d.h2("Keeping It Going")
    d.note("The back of your plan. If time runs short in class, finish this at home.")
    d.label("The habits I’ll keep (check all that apply)", before=4)
    d.checks([
        "Write down what I spend, at least for a few days each month",
        "Make a budget before each month begins, and save something first",
        "Put a little extra toward one debt at a time",
        "Use my safety net only for real emergencies, and refill it",
        "Check in with my buddy each month",
        "Give some time, talents, or money to others",
    ], size=10, after=1)
    d.label("Passing it on", before=6)
    d.p("Someone I’ll share one idea from this course with: ______________________________",
        size=10, after=4)
    d.p("The idea I’ll share: ______________________________________________________",
        size=10, after=4)
    d.p("One way I’ll give back this month (time, talents, or money): ____________________",
        size=10, after=6)
    d.label("A note to myself, to read in three months")
    d.lines(3)
    d.principle("Small, steady steps, kept up over time, add up. Start where you are, keep "
                "going, and lift others along the way.")

    # Monthly check-in -----------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Monthly Check-In")
    d.h1("Monthly Check-In")
    d.note("Session 5 · After the course. Talk with your buddy once a month for the next three "
           "months, and fill in one column each time.")
    d.p("My buddy: ______________________________   Phone: ____________________   We’ll talk "
        "on the ______ of each month.", size=10, after=8)
    d.grid(["", "Month 1", "Month 2", "Month 3"], [
        ["Date we talked", "", "", ""],
        ["Did I use my budget?", "☐ Yes ☐ Some ☐ No", "☐ Yes ☐ Some ☐ No", "☐ Yes ☐ Some ☐ No"],
        ["Safety net now", "$", "$", "$"],
        ["What I owe now", "$", "$", "$"],
        ["Saved for later this month", "$", "$", "$"],
        ["One thing that went well", "", "", ""],
        ["One thing that was hard", "", "", ""],
        ["How I gave or helped someone", "", "", ""],
        ["My goal for next month", "", "", ""],
    ], [2.2, 1.7, 1.7, 1.7], height=0.55)
    d.label("Questions to ask each other", before=8)
    d.bullets([
        "What are you proud of this month?",
        "What’s getting in the way, and what could help?",
        "How can I encourage you before we talk next?",
    ], size=10, after=1)

    d.save(OUT)


if __name__ == "__main__":
    guide()
