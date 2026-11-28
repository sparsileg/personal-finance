# Personal Finance Survival Course

## Course guidelines

- The course format: 4 weekly sessions plus an optional 5th, each with teaching, then hands-on worksheets, then homework.
- Session length: about 90 minutes in total for Sessions 1–3, and about 105 for Sessions 4 and 5, including the opening inspiration, buddy check-in, and closing. Plan activities to fit this time.
- Each session opens with an inspirational thought tied to that week's topic: a short, well-known quote from a writer, leader, or traditional proverb, cited by author and source. The sponsor doesn't want religious messages, so don't use religious sources (scripture, sermons, religious texts) or religious wording. Choose simple guidance for a prosperous life, meaning a happy and meaningful one, not necessarily a wealthy one. Quote word for word, and only quotes whose source can be confirmed.
- Session 4 is the last session and closes the course (looking back, a buddy for the months after, a monthly check-in). Session 5 is optional: the facilitator and host decide whether a group will benefit from learning about investing. Only the overview and the Session 5 materials mention it; the materials for Sessions 1–4 don't.
- The buddy system: members pair up in class, stay in touch during the week for support and accountability, and can switch buddies each week. Each session should include a short buddy check-in and a buddy commitment for the coming week.
- The tone: positive and free of shame, grateful for what they already have, and encouraging them to give back to their community, church and friends.
- Audience: people receiving support through a community-based organization, food pantry, or church. Most have little financial literacy. Their situations vary: some have little or no employment, while others have steady jobs but haven't been able to save or plan for their financial future. Keep language plain, include examples that work across a range of incomes (including tight or irregular ones), and don't assume spare money, a bank account, or good credit. By the end, each participant should have a clear picture of their current finances, a simple working budget, a plan for handling debt, a first step toward an emergency fund (even a very small one), awareness of community resources available to them, and a buddy relationship that keeps them going after the course ends.

## Repository layout

Course materials are Word documents, numbered by session:

- `0 - Overview.docx`: the course at a glance: audience, goals, how sessions work, the materials, and a summary of each session
- `N - <Topic>.docx`: the session guide for session N, read by the facilitator and participants together. It works for the group in class or for someone reading alone, and includes 2–4 "Read Aloud" boxes, discussion questions, and minutes for each part (about 75 planned minutes for Sessions 1–3 and 90 for Sessions 4 and 5, leaving about 15 minutes of slack). A notes page follows the guide text on a new page. Then come the in-class worksheet (front and back: the worksheet, then an exercise ending with "The principle" and "My first step this week") and the homework sheet.
- `N - Facilitator Notes.docx`: at most two pages for the person leading session N: goals, their role (a council facilitator, not a teacher), how to prepare, timing and what to cut, and handling emotions and issues
- `N - Take-Home Worksheets.docx`: optional extra worksheets for home

The facilitator brings pencils (not pens) and blank paper to every session, and sets tables in a square or rectangle.

Everything is printed double-sided, so every worksheet (in-class, homework, take-home) starts on an odd page, beginning its own sheet; Word inserts a blank page where needed (`new_page_section` in `pflib.py`).

All five sessions use this format.

Sessions: 1 Understanding Your Money Story, 2 Creating a Budget, 3 Breaking the Debt Cycle, 4 Financial Safety Net, 5 Building Wealth (the optional session).

## Building the documents

The overview and the session documents are generated from Python scripts in `build/`, using python-docx:

- `o0.py` makes the overview. `sN.py` makes the session guide, `fN.py` the facilitator notes, and `tN.py` the take-home worksheets. `pflib.py` holds the shared layout helpers, and `template.docx` supplies the styles.
- `build/build.sh` builds all 16 documents into `build/out/`, and `build/build.sh --install` copies them over the files in the repo root.
- `build/render.sh NAME SCRIPT` builds one document and makes a PDF with page previews, to check where pages break.

Make content changes in the scripts, then rebuild and install. Edits made directly in Word are overwritten by the next install.
