import sys

from pflib import Doc

OUT = sys.argv[1]
S = 11


def build():
    d = Doc("template.docx", margins=0.8, footer="Session 1 · Facilitator Notes")
    d.h1("Session 1 Facilitator Notes")
    d.p("**Understanding Your Money Story.** Use with the Session 1 guide, which you and the "
        "group read together.", size=S, after=4)

    d.h2("Session goals")
    d.p("By the end of the session, each person should:", size=S, after=2)
    d.bullets([
        "Feel safe in the group and hopeful about what the course can do for them",
        "Have thought about the money messages they grew up with",
        "Have started (not necessarily finished) their **Financial Snapshot**",
        "Have noticed at least one thing that leads them to spend",
        "Have a buddy, and know how to use the **7-Day Money & Emotion Tracker** this week",
    ], size=S, after=1)
    d.p("If people leave feeling safe and hopeful, the session worked, even if worksheets are "
        "unfinished.", size=S, after=4)

    d.h2("Your role")
    d.p("You are not the teacher. The group works like a council: you keep time, invite every "
        "voice, and keep the room safe. If you know personal finance well, use that to ask good "
        "questions rather than give answers. Share a little of your own story; it shows that "
        "openness is welcome. **Reading aloud is always voluntary.** Ask for volunteers, never "
        "call on someone, and be ready to read a box yourself. Some people may not read easily.",
        size=S, after=4)

    d.h2("How to prepare")
    d.bullets([
        "Read the whole guide and fill out the Snapshot, front and back, yourself, so you know "
        "where people get stuck. The back, **What My Snapshot Tells Me**, ends with the principle "
        "and a first step. People can finish it at home, but read the principle aloud before moving on.",
        "Make a **local resource list** to hand out: 211, food pantries, SNAP and WIC offices, "
        "utility and rent assistance, free tax help, and nonprofit credit counseling.",
        "Bring a guide for each person, pens, name tags, a flipchart or whiteboard, a few "
        "calculators, and spare copies of the tracker.",
        "Arrange chairs in a circle, and arrive 15 minutes early to greet people as they come in.",
    ], size=S, after=1)

    d.h2("Timing")
    d.p("The plan below uses 75 minutes. That leaves about 15 minutes for a late start, a break, "
        "and the good conversations that always come up.", size=S, after=4, keep_next=True)
    d.grid(["Part", "Minutes", "If you're running behind"], [
        ["1. Opening Inspiration", "5", "Take one or two answers."],
        ["2. Welcome and Getting Started", "15", "Keep “money in one word” quick."],
        ["3. Money Messages from Growing Up", "12", "Use the first two questions."],
        ["4. Your Money Snapshot and buddies", "25", "Let people finish the Snapshot at home. "
         "Never skip choosing buddies."],
        ["5. What Leads Us to Spend", "10", "Use one question."],
        ["6. Wrap-up and Commitment", "8", "Never skip the homework and the closing circle."],
        ["Total", "75", ""],
    ], [3.0, 0.75, 3.15], height=0.26, size=10, bold_rows=(6,), shade_rows=(6,),
           keep_together=True)

    d.h2("Handling emotions and issues")
    for head, text in [
        ("Shame or embarrassment.", "Money is a tender subject, and many people have never said "
         "their numbers out loud. Thank people for their honesty, point back to the ground "
         "rules, and remind the group that today is a starting point, not a grade."),
        ("Tears or strong feelings.", "Pause, acknowledge the feeling, and offer a short break. "
         "Check in privately afterward. You don’t need to fix anything."),
        ("Crisis needs.", "If someone has no food, faces eviction, or has a shut-off notice, "
         "don’t try to solve it in the group. Talk with them privately after the session and "
         "give them the resource list."),
        ("Comparing incomes.", "Snapshots are private. Sharing is always optional, and no "
         "one’s numbers are better or worse than anyone else’s."),
        ("Someone dominating or giving advice.", "Thank them, then say, “Let’s hear from "
         "someone who hasn’t shared yet.” Steer advice toward experience: “What "
         "worked for you?”"),
        ("Trouble reading or writing.", "Let a buddy help, or talk through the worksheet "
         "together. Numbers can be rough guesses. No one should feel singled out."),
        ("Couples or family members.", "They may share more freely if they sit with different "
         "people. Let them choose."),
        ("Questions you can’t answer.", "Say, “Good question. Let’s find out,” "
         "write it down, and bring an answer next week."),
    ]:
        d.p(f"**{head}** {text}", size=S, after=4)
    d.save(OUT)


if __name__ == "__main__":
    build()
