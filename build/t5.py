import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 5 · Take-Home Worksheets (optional)"


def build():
    d = Doc("template.docx", margins=0.6, footer=FOOT + " · Starting Early")
    d.h1("The Power of Starting Now")
    d.note("Session 5 · Take-home, optional. These worksheets go deeper into what we talked about "
           "in class. Do them whenever you have time.")
    d.p("This table shows what a monthly amount could grow to at about 7% a year. Real growth "
        "goes up and down, and isn’t guaranteed, but the pattern holds: time does much of the "
        "work.", size=11, after=4)
    d.grid(["Each month", "After 10 years", "After 20 years", "After 30 years"], [
        ["$10", "$1,700  (put in $1,200)", "$5,200  (put in $2,400)", "$12,200  (put in $3,600)"],
        ["$25", "$4,300  (put in $3,000)", "$13,000  (put in $6,000)", "$30,500  (put in $9,000)"],
        ["$50", "$8,700  (put in $6,000)", "$26,000  (put in $12,000)",
         "$61,000  (put in $18,000)"],
        ["$100", "$17,300  (put in $12,000)", "$52,100  (put in $24,000)",
         "$122,000  (put in $36,000)"],
    ], [1.1, 2.0, 2.1, 2.1], height=0.34, size=10)
    d.label("My numbers", before=6)
    d.p("My age now: ______     The age I’d like to stop working: ______     Years between: ______",
        size=10, after=4)
    d.p("An amount I could save for later each month, starting now or soon: $________", size=10,
        after=4)
    d.p("From the table, this could grow to about $____________ in ______ years.", size=10,
        after=6)
    d.question(1, "What surprises me about these numbers?", 2, size=10)
    d.question(2, "What would make it possible for me to start, or to add a little more?", 2,
               size=10)
    d.question(3, "Who else in my family could I share this with?", 2, size=10)
    d.box([
        "**Remember the order:** a starter safety net first, then costly debt, then saving for "
        "later. The one exception: if your job matches what you put in for retirement, try to get "
        "the full match as soon as you can.",
    ])

    d.new_page_section(margins=0.6, footer=FOOT + " · Saving or Investing")
    d.h1("Saving or Investing?")
    d.note("Session 5 · Take-home, optional. Money you’ll need soon belongs in savings. Money you "
           "won’t need for five years or more can be invested.")
    d.grid(["Goal", "When I’d need it", "Save", "Invest", "Why?"], [
        ["Safety net", "Any time", "☐", "☐", ""],
        ["New tires next year", "", "☐", "☐", ""],
        ["Holiday gifts this year", "", "☐", "☐", ""],
        ["A car in 3 years", "", "☐", "☐", ""],
        ["A child’s schooling in 15 years", "", "☐", "☐", ""],
        ["Retirement in 25 years", "", "☐", "☐", ""],
    ], [2.4, 1.5, 0.65, 0.65, 2.1], height=0.34, size=10)
    d.p("Answers: Save for the safety net, tires, gifts, and the car. Invest for schooling in 15 "
        "years and retirement.", size=9, italic=True, after=8)
    d.label("My own goals")
    d.grid(["My goal", "When I’d need it", "Save", "Invest", "About how much"], [
        ["", "", "☐", "☐", "$"],
        ["", "", "☐", "☐", "$"],
        ["", "", "☐", "☐", "$"],
    ], [2.4, 1.5, 0.65, 0.65, 2.1], height=0.4, size=10)
    d.question(1, "Which of my goals are far enough away to invest for?", 2, size=10)

    d.new_page_section(margins=0.6, footer=FOOT + " · What Fees Cost")
    d.h1("What Fees Cost")
    d.note("Session 5 · Take-home, optional. Every fund charges a yearly fee, called the "
           "**expense ratio**. It’s listed in the fund’s information or in your plan’s list of "
           "funds. Small differences add up over many years.")
    d.label("1. What a yearly fee costs", before=4)
    d.grid(["Yearly fee", "On $1,000", "On $10,000"], [
        ["0.05% (many index funds)", "50¢ a year", "$5 a year"],
        ["0.5%", "$5 a year", "$50 a year"],
        ["1%", "$10 a year", "$100 a year"],
        ["2%", "$20 a year", "$200 a year"],
    ], [3.1, 2.1, 2.1], height=0.3, size=10)
    d.label("2. What fees do over 30 years", before=8)
    d.p("$50 a month for 30 years, growing about 7% a year before fees. You put in $18,000.",
        size=10, after=2)
    d.grid(["Yearly fee", "It could grow to about", "Lost to fees"], [
        ["0.05%", "$60,400", "about $600"],
        ["1%", "$50,200", "about $10,800"],
        ["2%", "$41,600", "about $19,400"],
    ], [3.1, 2.1, 2.1], height=0.3, size=10)
    d.p("Real growth goes up and down, and isn’t guaranteed. But the fee comes out every year, "
        "good or bad.", size=9, italic=True, after=8)
    d.label("3. My numbers")
    d.p("A fund I’m looking at: ______________________________   Its yearly fee: ______%",
        size=10, after=4)
    d.p("On $1,000, that’s $________ a year. (Fee × 10. For example, 0.5% × 10 = $5.)",
        size=10, after=4)
    d.p("A lower-fee choice in the same plan, if there is one: ______________________   Fee: "
        "______%", size=10, after=6)
    d.question(1, "What surprised me about fees?", 2, size=10)
    d.question(2, "Who could help me find the fees in my plan?", 1, size=10)
    d.save(OUT)


if __name__ == "__main__":
    build()
