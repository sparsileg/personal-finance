import sys

from pflib import Doc

OUT = sys.argv[1]
T = "template.docx"
FOOT = "Session 1 · Understanding Your Money Story"

INCOME = [
    "Pay from work (after taxes)",
    "Benefits (SNAP, SSI, Social Security, unemployment, etc.)",
    "Child support",
    "Side jobs or gig work",
    "Help from family or others",
    "Other: ____________________",
]


def guide():
    d = Doc(T, margins=1.0, footer=FOOT)
    d.h1("Understanding Your Money Story")
    d.p("**Session 1:** Where you are today, and how you got here", size=13, after=10)

    d.label("In this session, you will:", before=0)
    d.bullets([
        "Think about what you learned about money growing up",
        "Take an honest, judgment-free look at your money right now",
        "Notice what leads you to spend",
        "Choose a buddy to support you this week",
    ])
    d.how_to_use("All you need is a pencil.")

    # 1 -------------------------------------------------------------------
    d.h2("1. Opening Inspiration", 5)
    d.read_aloud([
        "“Not everything that is faced can be changed; but nothing can be changed until it is "
        "faced.” (James Baldwin, “As Much Truth As One Can Bear,” *The New York Times Book "
        "Review*, 1962)",
    ])
    d.discuss([
        "Why can it be hard to look honestly at our money? What could looking make possible?",
    ])
    d.p("This course helps each of us face our money without shame, and take small steps "
        "from there.")
    d.p("**The road ahead:** first a budget that fits your life (Session 2), then a plan for "
        "debt (Session 3), and then a small safety net and a plan for keeping going after the "
        "course (Session 4). Each step makes the next one possible.")

    # 2 -------------------------------------------------------------------
    d.h2("2. Welcome and Getting Started", 15)
    d.read_aloud(
        ["This group works like a council. There is no teacher or expert. We read together, "
         "talk together, and learn from each other. Each person makes their own plan. To help "
         "each other, we will:"],
        title="What to Expect in This Class",
        bullets=[
            "Take part, and give everyone a turn. No one, not even the facilitator, should do "
            "most of the talking.",
            "Trust and support each other. Listen, ask questions, and get to know each other.",
            "Keep our comments kind and on topic.",
            "Make promises to ourselves, and keep them.",
        ])
    d.label("Money in one word")
    d.p("Go around the group. Share your first name and one word that describes how you feel "
        "about money right now. There are no wrong answers.")
    d.label("Our ground rules")
    d.bullets([
        "What’s shared here stays here.",
        "No shaming or judging, of others or of ourselves.",
        "Everyone’s situation is valid.",
        "You can always pass.",
        "We’re here to learn and grow, not to be perfect.",
    ])
    d.p("Is there anything the group would like to add?")

    # 3 -------------------------------------------------------------------
    d.h2("3. Money Messages from Growing Up", 12)
    d.p("All of us learned something about money growing up, sometimes from what was said, but "
        "more often from what we saw. Take a moment to think, then share only what you’re "
        "comfortable sharing.")
    d.discuss([
        "What was the “money mood” in your home growing up? Was it relaxed, worried, "
        "never talked about, or a cause of arguments?",
        "Finish this sentence: “In my family, money was …”",
        "What’s one money habit you picked up from your family? Is it one you want to keep?",
        "What’s one message from your past that may not be helping you now?",
    ])
    d.p("**Remember:** Those early messages still shape us today, but we can choose new ones.")

    # 4 -------------------------------------------------------------------
    d.h2("4. Your Money Snapshot", 25)
    d.read_aloud([
        "Many of us avoid looking at our money because it feels stressful. But looking honestly "
        "at your numbers is not about judging yourself. It’s like reading a map: you can’t "
        "plan a route until you know where you’re starting from.",
        "Today you’ll write down the money that comes in and goes out in a typical month. Best "
        "guesses are fine, and some lines may be zero. Whatever your numbers show, they describe "
        "where you are today, not who you are. Many people in this room are in the same place, "
        "and every one of us can take the next small step from here. Your snapshot is private. "
        "You share only what you choose to share.",
    ])
    d.h3("On your own: My Financial Snapshot worksheet", 13)
    d.p("Turn to the **My Financial Snapshot** worksheet. If you get stuck on a number, write "
        "your best guess and keep going. You can finish it at home.")
    d.h3("Choose your buddy", 10)
    d.p("Pair up with someone you don’t know well. (A group of three is fine.) This is your "
        "buddy for the coming week. Trade phone numbers or another way to stay in touch, and "
        "write them on your tracker. Then share:")
    d.bullets([
        "One thing that surprised you about your numbers (only what you’re comfortable sharing)",
        "One expense you’d like to keep a closer eye on this week",
    ])

    # 5 -------------------------------------------------------------------
    d.h2("5. What Leads Us to Spend", 10)
    d.read_aloud([
        "Most of us don’t overspend because we’re careless. We spend because of how we "
        "feel or what’s happening around us. Common triggers are stress, boredom, being tired, "
        "celebrating, being with friends, or seeing a sale. Sadness or loneliness can send us to "
        "the store, too. Spending makes us feel better for a little while, so it’s easy to "
        "repeat.",
        "Noticing a trigger is the first step to changing it. When you know what sets you off, "
        "you can plan ahead: wait a day before buying, leave the card at home, or call your "
        "buddy instead.",
    ])
    d.discuss([
        "Think of something you bought recently that you hadn’t planned to buy. How were you "
        "feeling right before?",
        "Which triggers do you recognize in yourself?",
        "What’s one thing you could do the next time you feel that way?",
    ])

    # 6 -------------------------------------------------------------------
    d.h2("6. Wrap-up and This Week’s Commitment", 8)
    d.label("This week, I will:", before=2)
    d.numbered([
        "Write down every purchase for 7 days on the **7-Day Money & Emotion Tracker**. Small "
        "purchases count. Use the tracker, your phone, or a notebook, whatever works for you.",
        "Next to each purchase, write how I felt right before I bought it.",
        "Each evening, ask myself: “What did I learn about my money habits today?”",
        "Call or text my buddy at least once to share how it’s going and to encourage each other.",
        "Gather what I have for next week: pay stubs or benefit letters, and recent bills. We’ll "
        "use them, with my tracker, to build a budget.",
    ])
    d.p("**Want to go further?** The Session 1 take-home worksheets are optional. Do them only "
        "if you have time after your tracker.")
    d.label("Gratitude and giving")
    d.p("Whatever our money looks like today, each of us has things to be grateful for. As we get "
        "our money in order, we’ll be better able to give back to our families, friends, "
        "church, and community.")
    d.label("Closing circle")
    d.p("Share one word for how you feel right now (compare it to your word from the start), and "
        "one thing you’re grateful for that money didn’t buy.")
    d.p("**Next week:** We’ll use what you learn from tracking to build a budget that fits "
        "your real life.", italic=False)

    # Notes ---------------------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · Notes", odd=False)
    d.h1("Session 1 Notes")
    d.note("Space for your thoughts during our discussions.")
    for head in ["Money messages from growing up", "My money snapshot", "What leads me to spend",
                 "Things I want to remember"]:
        d.label(head, before=8)
        d.lines(4)

    # Worksheet: snapshot ------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · My Financial Snapshot")
    d.h1("My Financial Snapshot")
    d.note("Session 1 · In class. Use a typical month. Best guesses are fine. Leave blank "
           "anything that doesn’t apply. Small purchases are easy to forget; your tracker this "
           "week will fill them in. This page is private.")
    d.money_table("Money coming in (each month)", INCOME, "Total coming in",
                  widths=(2.75, 0.9), cols=2)
    d.p("**Not paid monthly?** Paid every week: one paycheck × 4. Paid every two weeks or twice a month: one paycheck × 2. If you’re paid every week or every two weeks, a few months a year bring an extra paycheck. Leave it out here, and give it a job before it comes.", size=9, before=2, after=2)
    d.money_table("Money going out (each month)", [
        "Rent or mortgage",
        "Utilities (electric, gas, water)",
        "Phone and internet",
        "Groceries",
        "Eating out and takeout",
        "Car payment and insurance",
        "Gas, bus fare, rides",
        "Debt payments (credit cards, loans)",
        "Childcare",
        "Medical and prescriptions",
        "Personal care and household items",
        "Subscriptions (streaming, apps)",
        "Everything else",
    ], "Total going out", widths=(2.75, 0.9), cols=2)
    d.label("Money math", before=8)
    d.grid(["Total coming in", "Minus total going out", "What’s left"],
           [["$", "− $", "= $"]], [2.43, 2.43, 2.44], height=0.34)
    d.p("If what’s left is less than zero, you’re not alone, and it isn’t a failure. "
        "It’s a starting point, and that is exactly what this course is for.", size=10)
    d.page_break()
    d.h2("What My Snapshot Tells Me")
    d.note("The back of your snapshot. If time runs short in class, finish this at home.")
    d.label("Quick check (mark one for each)", before=6)
    d.p("1. Do I know where my money goes each month?", size=10, after=1)
    d.p("     ☐ Yes     ☐ Mostly     ☐ Some idea     ☐ Not really", size=10, after=5)
    d.p("2. At the end of the month, I usually:", size=10, after=1)
    d.p("     ☐ Have some money left     ☐ Just break even     ☐ Run short", size=10, after=5)
    d.p("3. When something unexpected comes up (a car repair, a medical bill), I usually:", size=10, after=1)
    d.p("     ☐ Use savings    ☐ Borrow from family or friends    ☐ Use a credit card "
        "or loan    ☐ Fall behind", size=10, after=6)
    d.question(4, "Where does the biggest share of my money go?", 2, size=10)
    d.question(5, "What surprised me, or what was I relieved to see?", 2, size=10)
    d.question(6, "One expense I’ll watch closely on my tracker this week:", 1, size=10)
    d.question(7, "One thing I’m grateful for that money didn’t buy:", 1, size=10)
    d.principle("You can’t change what you don’t look at. Knowing your numbers, without "
                "judging them, is the first step to changing them.")
    d.label("My first step this week", before=8)
    d.lines(2)

    # Homework: tracker --------------------------------------------------
    d.new_page_section(margins=0.6, footer=FOOT + " · 7-Day Money & Emotion Tracker")
    d.h1("7-Day Money & Emotion Tracker")
    d.note("Session 1 · Homework. Write down everything you buy, and how you felt right before. "
           "Need more room? Use the back of the page. Bring this to Session 2.")
    d.p("My buddy this week: ______________________________   Phone: ____________________", size=10, after=2)
    d.p("Check in with your buddy at least once this week. Date we talked: ____________", size=10, after=8)
    rows, merged, shade = [], {}, []
    for day in range(1, 8):
        merged[len(rows)] = f"Day {day}     Date: ____________"
        shade.append(len(rows))
        rows.append([""] * 4)
        for _ in range(3):
            rows.append([""] * 4)
        merged[len(rows)] = "What I learned about my money habits today:"
        rows.append([""] * 4)
    d.grid(["What I bought", "Amount", "Where", "How I felt before"], rows,
           [2.9, 1.0, 1.7, 1.7], height=0.3, size=10, merged_rows=merged,
           bold_rows=tuple(shade), shade_rows=tuple(shade))
    d.label("After 7 days: my week in review", before=10)
    d.question(1, "What surprised me most about my spending?", 2, size=10)
    d.question(2, "What did I notice about my feelings and my spending?", 2, size=10)
    d.question(3, "What’s one spending habit I’d like to change?", 2, size=10)
    d.question(4, "What’s one thing I’m proud of from this week?", 2, size=10)

    d.save(OUT)


if __name__ == "__main__":
    guide()
