import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 2 · Take-Home Worksheets (optional)"


def build():
    d = Doc("template.docx", margins=0.6, footer=FOOT + " · Which Paycheck Pays What")
    d.h1("Which Paycheck Pays What")
    d.note("Session 2 · Take-home, optional. These worksheets go deeper into what we talked about "
           "in class. Do them only if you have time after your tracker, which comes first.")
    d.p("Bills come due on certain days. For each paycheck, list the bills due before the next "
        "one, so nothing is late. Put housing, utilities, food, and getting to work first.",
        size=11)
    rows, merged, shade = [], {}, []
    for n in range(1, 5):
        merged[len(rows)] = (f"Paycheck {n}     Date: ____________     "
                             "Amount: $__________")
        shade.append(len(rows))
        rows.append([""] * 3)
        for _ in range(3):
            rows.append(["", "", "$"])
        merged[len(rows)] = "Left after these bills: $__________"
        rows.append([""] * 3)
    d.grid(["Bill", "Due date", "Amount"], rows, [4.3, 1.5, 1.5], height=0.27, size=10,
           merged_rows=merged, bold_rows=tuple(shade), shade_rows=tuple(shade))
    d.box([
        "**Tips.** Many companies will move a due date if you ask, so bills line up with your "
        "paychecks. Paid every two weeks? Two months a year have a third paycheck. Give it a job "
        "before it comes.",
    ])
    d.question(1, "Which paycheck is the tightest? What could I move to a different one?", 1,
               size=10)

    d.new_page_section(margins=0.6, footer=FOOT + " · Budget Success Plan")
    d.h1("My Budget Success Plan")
    d.note("Session 2 · Take-home, optional. A little planning now makes your budget easier to "
           "stick with.")
    d.label("1. How will I keep track of my budget? (Check all that apply.)", before=4)
    d.checks([
        "A notebook or paper",
        "Cash in envelopes for some areas, like groceries or gas",
        "A phone app (which one: ______________________)",
        "Text alerts from my bank, if I have an account",
        "Other: ________________________________",
    ], size=10, after=1)
    d.label("2. What day each week will I look at my budget? ______________________")
    d.label("3. What will probably be my biggest challenge?")
    d.checks([
        "Sticking to my grocery amount",
        "Buying things I didn’t plan to buy",
        "Income that changes from month to month",
        "Surprise expenses",
        "My partner or family isn’t on board",
        "Feeling too tight, with no room for fun",
        "Other: ________________________________",
    ], size=10, after=1)
    d.label("4. When I go over in one area, I will:")
    d.checks([
        "Move money from another area",
        "Accept it, and adjust next month",
        "Look for a little extra income or help",
        "Other: ________________________________",
    ], size=10, after=1)
    d.label("5. How will I celebrate sticking to my budget (without spending much)?")
    d.lines(2)
    d.label("My promise to myself this week", before=8)
    d.checks([
        "I will use the budget I made in class.",
        "I will write down what I spend each day.",
        "I will make one change: ________________________________",
        "I won’t be hard on myself if I slip. I’ll adjust and keep going.",
    ], size=10, after=1)
    d.p("Signed: ______________________________     Date: ______________", size=10, before=8)

    d.new_page_section(margins=0.6, footer=FOOT + " · Budget Problem-Solving")
    d.h1("Budget Problem-Solving")
    d.note("Session 2 · Take-home, optional. Work on these with your buddy or your family. For "
           "each one, think of two or three things the person could try.")
    for title, text in [
        ("The grocery budget that never holds",
         "“I plan to spend $300 on groceries but always spend $450. I shop when I’m "
         "hungry, I don’t make a list, and some food goes to waste.”"),
        ("Two good weeks, then nothing",
         "“I stick to my budget for about two weeks, then I feel deprived and give up until "
         "next month.”"),
        ("Something always comes up",
         "“Every month there’s a surprise, like a car repair, a medical bill, or a "
         "school trip, and it wrecks my budget. I end up borrowing.”"),
        ("Not on the same page",
         "“I want to budget, but my partner thinks it takes the fun out of life and keeps "
         "spending money we don’t have.”"),
    ]:
        d.label(title, before=8)
        d.p(text, italic=True, size=10, after=2)
        d.lines(3)
    d.save(OUT)


if __name__ == "__main__":
    build()
