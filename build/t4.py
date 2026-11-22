import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 4 · Take-Home Worksheets (optional)"


def build():
    d = Doc("template.docx", margins=0.6, footer=FOOT + " · My Surprise Expenses")
    d.h1("My Surprise Expenses")
    d.note("Session 4 · Take-home, optional. These worksheets go deeper into what we talked about "
           "in class. Do them only if you have time after your tracker, which comes first.")
    d.p("Think back over the past year. What surprise expenses came up, and how did you handle "
        "them?", size=11, after=4)
    d.grid(["What happened", "About when", "Cost", "How I paid", "Could I have planned for it?"],
           [[""] * 4 + ["☐ Yes  ☐ Maybe  ☐ No"] for _ in range(6)],
           [2.3, 1.0, 0.9, 1.5, 1.6], height=0.5, size=10)
    d.p("How I paid: savings, credit card, loan, borrowed from family or friends, payment plan, "
        "paid late, or went without.", size=9, after=6)
    d.label("What kinds of surprises come up most for me? (Check all that apply.)", before=4)
    d.grid(None, [
        ["☐ Car repairs", "☐ Medical or dental", "☐ Home or appliance repairs"],
        ["☐ Less work or lost job", "☐ Family needs or travel", "☐ School costs"],
        ["☐ Holidays and birthdays", "☐ Pets", "☐ Other: ______________"],
    ], [2.43, 2.43, 2.44], height=0.28, size=10)
    d.p("My surprises usually cost:   ☐ Under $100   ☐ $100–$300   ☐ $300–$500   "
        "☐ $500–$1,000   ☐ More", size=10, before=4, after=4)
    d.question(1, "If I’d had a safety net, how would these surprises have gone differently?",
               2, size=10)
    d.question(2, "Which of these could I start setting aside a little for each month? How much?",
               2, size=10)

    d.new_page_section(margins=0.6, footer=FOOT + " · Finding Money to Save")
    d.h1("Finding Money to Save")
    d.note("Session 4 · Take-home, optional. Check the ideas you’re willing to try. Small amounts "
           "add up.")
    d.label("Everyday ways", before=4)
    d.checks([
        "Save every $1 bill or all my loose change in a jar",
        "Put my safety net money aside first, on payday",
        "Save what’s left in a budget area at the end of the month",
        "Shop store brands, and save the difference: about $______ a month",
        "Cook at home one more night a week, and save the difference",
        "Pause one subscription: ________________________",
    ], size=10, after=1)
    d.label("One-time money")
    d.checks([
        "Sell things I don’t use (estimate: $______)",
        "Return something I bought but don’t need ($______)",
        "Put part of a tax refund or gift into my safety net ($______)",
        "Ask about free tax help (VITA) so more of my refund stays with me",
    ], size=10, after=1)
    d.label("A little extra income")
    d.checks([
        "Extra hours or shifts at work",
        "A side job using a skill I have: ________________________",
        "Seasonal work (holidays, harvest, summer)",
    ], size=10, after=1)
    d.label("A savings challenge (pick one to try this month)")
    d.checks([
        "**No-spend day:** one day a week, spend nothing beyond what I must",
        "**Pantry week:** eat from what’s already in the cupboard, and save the grocery money",
        "**$5 bills:** every $5 bill I get goes in the envelope",
        "**Growing dollar:** save $1 the first week, $2 the second, $3 the third, $4 the fourth",
    ], size=10, after=1)
    d.label("My plan", before=6)
    d.p("The two ideas I’ll start with: _____________________________________________________",
        size=10, after=4)
    d.p("About how much they could add each month: $________     I’ll start on: ______________",
        size=10)

    d.new_page_section(margins=0.6, footer=FOOT + " · Insurance and Other Safety Nets")
    d.h1("Insurance and Other Safety Nets")
    d.note("Session 4 · Take-home, optional. Check what you have now, then pick one gap to look "
           "into. If you’re not sure, that’s fine. Finding out is the first step.")
    d.grid(["Safety net", "I have it", "I don’t", "Not sure", "Where to find out"], [
        ["Health coverage (job, Medicaid, CHIP, marketplace)", "☐", "☐", "☐",
         "HealthCare.gov, 211, or my job"],
        ["Car insurance (if I drive)", "☐", "☐", "☐", "My agent or company"],
        ["Renter’s or home insurance", "☐", "☐", "☐", "An insurance agent"],
        ["Life insurance (if others depend on me)", "☐", "☐", "☐", "My job, or an agent"],
        ["Disability insurance", "☐", "☐", "☐", "My job"],
        ["Benefits I may qualify for (SNAP, WIC, EITC)", "☐", "☐", "☐", "211, or free tax help"],
        ["Local help (food pantry, utility or rent help)", "☐", "☐", "☐", "211, church, or community center"],
    ], [2.75, 0.7, 0.7, 0.75, 2.4], height=0.4, size=10)
    d.label("My people safety net", before=6)
    d.p("People I could turn to in a hard time: ___________________________________________",
        size=10, after=4)
    d.p("People who could turn to me: _____________________________________________________",
        size=10, after=6)
    d.label("My next step", before=4)
    d.p("The safety net I’ll look into first: _______________________________________________",
        size=10, after=4)
    d.p("What I’ll do (call, visit, ask at work): _____________________   By when: __________",
        size=10)
    d.save(OUT)


if __name__ == "__main__":
    build()
