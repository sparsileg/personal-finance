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
    d.label("Questions to ask at work (or a family member’s work)", before=8)
    d.checks([
        "Is there a retirement plan? Can I join now?",
        "Does the company match what I put in? Up to how much?",
        "What’s the simplest low-fee choice, like a target-date fund?",
        "Can I start with a small amount, like 1% or 2% of my pay?",
    ], size=10, after=1)
    d.label("Before I sign anything, I’ll ask myself", before=6)
    d.checks([
        "Can I explain this in my own words?",
        "Is anyone pressuring me to decide now, or promising big, sure returns?",
        "Have I talked with someone I trust?",
    ], size=10, after=1)

    d.new_page_section(margins=0.6, footer=FOOT + " · Looking Back, Looking Ahead")
    d.h1("Looking Back, Looking Ahead")
    d.note("Session 5 · Take-home, optional. Take a few quiet minutes to see how far you’ve come.")
    d.grid(["", "When I started", "Now"], [
        ["One word for how I feel about money", "", ""],
        ["How sure I feel about money (1–10)", "", ""],
        ["My biggest money worry", "", ""],
    ], [3.1, 2.1, 2.1], height=0.45, size=10)
    d.question(1, "The most important thing I learned:", 2)
    d.question(2, "The biggest change I’ve made:", 2)
    d.question(3, "What I’m most proud of:", 2)
    d.question(4, "One year from now, I hope to:", 2)
    d.question(5, "The habit I most want to keep:", 1)
    d.question(6, "One way I’ll help someone else with what I’ve learned:", 2)
    d.p("Signed: ______________________________     Date: ______________", size=10, before=8)
    d.save(OUT)


if __name__ == "__main__":
    build()
