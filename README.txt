Python with docx2pdf (Windows/Mac)

Requires Word to be installed but wraps it neatly:

pip install docx2pdf
docx2pdf /path/to/folder/

Or in a script:

from docx2pdf import convert
convert("input_folder/", "output_folder/")