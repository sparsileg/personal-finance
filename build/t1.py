import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 1 · Take-Home Worksheets (optional)"


def purchase(d, n):
    d.label(f"Purchase {n}", before=8)
    d.p("What did I buy? ____________________________________   How much? $__________", size=10, after=4)
    d.p("Where was I? ____________________________________   Who was I with? ________________", size=10, after=4)
    d.p("How was I feeling right before?", size=10, after=1)
    d.p("     ☐ Stressed   ☐ Bored   ☐ Tired   ☐ Sad   ☐ Lonely   ☐ Happy   ☐ Excited   "
        "☐ Other: __________", size=10, after=4)
    d.p("What happened right before? (A hard day? Saw a sale? Out with friends?)", size=10, after=0)
    d.lines(1)
    d.p("How did I feel afterward?", size=10, after=1)
    d.p("     ☐ Great   ☐ Good   ☐ No different   ☐ Guilty   ☐ Worried   ☐ Other: __________",
        size=10, after=4)


def build():
    d = Doc("template.docx", margins=0.6, footer=FOOT + " · Money Messages")
    d.h1("Money Messages from My Past")
    d.note("Session 1 · Take-home, optional. These worksheets go deeper into what we talked about "
           "in class. Do them only if you have time after your tracker, which comes first.")
    d.p("Think back to when you were growing up. There are no right or wrong answers.", after=8)

    d.label("1. What was the “money mood” in your home growing up?", before=2)
    d.p("     ☐ Relaxed and open     ☐ Worried and stressed     ☐ Never talked about     "
        "☐ Caused arguments     ☐ Other: ____________", size=10)
    d.label("2. What did you hear about money growing up? (Check all that apply.)")
    d.checks([
        "“Money doesn’t grow on trees.”",
        "“We can’t afford that.”",
        "“You have to work hard for money.”",
        "“Rich people are greedy.”",
        "“Money isn’t important.”",
        "“Save your money.”",
        "“Spend it while you have it.”",
        "Other: ____________________________________",
    ], size=10, after=1)
    d.label("3. Finish this sentence: “In my family, money was …”")
    d.lines(2)
    d.label("4. What money habits did you learn by watching your family?")
    d.lines(3)
    d.label("5. Which of those habits help you today? Which ones don’t?")
    d.lines(2)
    d.label("6. What’s one new money message you’d like to live by, and maybe pass on?")
    d.lines(2)

    d.new_page_section(margins=0.6, footer=FOOT + " · Spending Triggers")
    d.h1("What Leads Me to Spend")
    d.note("Session 1 · Take-home, optional. Think about the last two times you bought something "
           "you hadn’t planned to buy.")
    purchase(d, 1)
    purchase(d, 2)
    d.label("Looking at both purchases", before=10)
    d.question(1, "Where do I tend to buy things I didn’t plan to buy?", 1, size=10)
    d.question(2, "How am I usually feeling before I do?", 1, size=10)
    d.question(3, "When does it tend to happen? (End of the day? Payday? Weekends?)", 1, size=10)
    d.question(4, "What’s ONE thing I could do differently the next time I feel this way?", 2, size=10)

    d.new_page_section(margins=0.6, footer=FOOT + " · The Future I Want")
    d.h1("The Future I Want")
    d.note("Session 1 · Take-home, optional. Dream a little. Imagine your money stress is gone.")
    d.question(1, "How would my daily life be different?", 3)
    d.question(2, "How would I feel?", 2)
    d.question(3, "How could I help my family, church, or community?", 3)
    d.question(4, "What would be possible for me that isn’t possible now?", 3)
    d.question(5, "What part of this picture excites me most?", 2)
    d.question(6, "What’s ONE small step I could take this month toward it?", 2)
    d.save(OUT)


if __name__ == "__main__":
    build()
