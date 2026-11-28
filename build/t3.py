import sys

from pflib import Doc

OUT = sys.argv[1]
FOOT = "Session 3 · Take-Home Worksheets (optional)"


def situation(d, n):
    d.label(f"Time {n}", before=6)
    d.p("What happened? ___________________________________________________________________",
        size=10, after=4)
    d.p("How was I feeling? ______________________   What did I borrow or charge? $___________",
        size=10, after=4)
    d.p("What could I do differently next time? ________________________________________________",
        size=10, after=2)


def build():
    d = Doc("template.docx", margins=0.6, footer=FOOT + " · Debt Triggers")
    d.h1("What Leads Me into Debt")
    d.note("Session 3 · Take-home, optional. These worksheets go deeper into what we talked about "
           "in class. Do them only if you have time after your tracker, which comes first.")
    d.p("Think about the last few times you used a credit card, a loan, or borrowed money.",
        size=11, after=2)
    for n in (1, 2, 3):
        situation(d, n)
    d.label("What leads me to borrow? (Check all that apply.)", before=8)
    d.grid(["Feelings", "People", "Surprises", "Sales and offers"], [
        ["☐ Stress or worry", "☐ Friends going out", "☐ Car repairs", "☐ “Limited time” sales"],
        ["☐ Feeling down", "☐ Gifts and holidays", "☐ Medical bills", "☐ “Buy now, pay later”"],
        ["☐ Boredom", "☐ Family needs", "☐ Less work or income", "☐ Store card offers"],
        ["☐ Feeling left out", "☐ Keeping up with others", "☐ School costs", "☐ Shopping for fun"],
    ], [1.8, 1.85, 1.8, 1.85], height=0.28, size=10)
    d.label("My plan", before=6)
    d.p("My biggest trigger: ____________________________________________________", size=10,
        after=4)
    d.p("**Before** it happens, I can: ____________________________________________", size=10,
        after=4)
    d.p("**In the moment,** I will (wait a day, call my buddy, leave the card at home): "
        "_______________________", size=10, after=4)
    d.p("**If I slip,** I will (adjust my budget, pay it off fast, not give up): "
        "__________________________", size=10, after=4)
    d.p("Instead of borrowing for a small emergency, I could: "
        "______________________________________", size=10, after=4)

    d.new_page_section(margins=0.6, footer=FOOT + " · Calling a Creditor")
    d.h1("Calling Someone I Owe")
    d.note("Session 3 · Take-home, optional. A short script makes the call easier. Practice it with "
           "your buddy first.")
    d.label("Before I call", before=4)
    d.checks([
        "Have my account number, my balance, and my budget in front of me",
        "Know what I can honestly afford to pay each month: $________",
        "Have paper and a pencil to write down what they say",
    ], size=10, after=1)
    d.label("What I’ll say")
    d.p("“Hi, my name is ____________, and I’m calling about my account ending in ______. "
        "I want to pay what I owe, but money is tight right now because ________________. "
        "Is there any way you can help me with a lower interest rate, a lower payment, a payment "
        "plan, or by removing a late fee?”", italic=True, size=11)
    d.p("If they say no, ask: “Is there a hardship program? May I speak with a supervisor?” "
        "Stay calm and polite. Don’t agree to a payment you can’t make.", size=10)
    d.label("Call log", before=6)
    d.grid(["Date", "Who I called", "Who I spoke with", "What they agreed to"],
           [[""] * 4 for _ in range(5)], [1.0, 1.8, 1.7, 2.8], height=0.55, size=10)
    d.label("Talking with a debt collector")
    d.bullets([
        "Ask for the collector’s name, company, and address. Write them down.",
        "Ask them to send proof of the debt in writing. Don’t pay a debt you don’t recognize.",
        "They can’t call before 8 a.m. or after 9 p.m., threaten you, or lie to you.",
        "You can tell them in writing to contact you only by mail, or to stop contacting you.",
        "Problems? You can file a complaint with the Consumer Financial Protection Bureau "
        "(consumerfinance.gov).",
    ], size=10, after=1)

    d.new_page_section(margins=0.6, footer=FOOT + " · The Day My Debt Is Paid")
    d.h1("The Day My Debt Is Paid")
    d.note("Session 3 · Take-home, optional. Imagine the day you make your last payment on your "
           "first debt, or on all of them.")
    d.question(1, "Which debt will I pay off first? About when?", 2)
    d.question(2, "How will I feel when it’s paid?", 2)
    d.question(3, "How will I celebrate, without spending much?", 2)
    d.question(4, "Where will that monthly payment go next? (The next debt? Savings? Giving?)", 2)
    d.question(5, "What will be different in my life, and my family’s, without this debt?", 3)
    d.question(6, "Who will I tell first?", 1)
    d.save(OUT)


if __name__ == "__main__":
    build()
