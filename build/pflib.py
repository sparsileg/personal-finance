"""Helpers for building the course .docx files on an existing document's styles."""
import copy
import re

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ACCENT = RGBColor(0x1F, 0x4E, 0x79)
BOX_FILL = "EAF1F8"
BOX_LINE = "1F4E79"


def _set_margins(section, inches):
    for side in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
        setattr(section, side, Inches(inches))


class Doc:
    def __init__(self, template, margins=1.0, footer=None):
        self.d = Document(template)
        body = self.d.element.body
        for el in list(body):
            if el.tag != qn("w:sectPr"):
                body.remove(el)
        sec = self.d.sections[0]
        _set_margins(sec, margins)
        sec.footer_distance = Inches(0.4)
        if footer:
            self._footer(sec, footer)

    # ----- page furniture -------------------------------------------------
    def _footer(self, section, text):
        ft = section.footer
        ft.is_linked_to_previous = False
        p = ft.paragraphs[0] if ft.paragraphs else ft.add_paragraph()
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
        width = section.page_width - section.left_margin - section.right_margin
        pPr = p._p.get_or_add_pPr()
        tabs = OxmlElement("w:tabs")
        tab = OxmlElement("w:tab")
        tab.set(qn("w:val"), "right")
        tab.set(qn("w:pos"), str(int(width / 635)))  # EMU -> twips
        tabs.append(tab)
        pPr.append(tabs)
        r = p.add_run(text + "\t")
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
        self._field(p, "PAGE", 9)

    def _field(self, p, instr, size):
        for kind, val in (("begin", None), ("instr", instr), ("separate", None), ("text", "1"), ("end", None)):
            r = p.add_run()
            r.font.size = Pt(size)
            r.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
            if kind == "instr":
                el = OxmlElement("w:instrText")
                el.set(qn("xml:space"), "preserve")
                el.text = f" {val} "
            elif kind == "text":
                el = OxmlElement("w:t")
                el.text = "1"
            else:
                el = OxmlElement("w:fldChar")
                el.set(qn("w:fldCharType"), kind)
            r._r.append(el)

    def new_page_section(self, margins=0.6, footer=None):
        """Start a new section on a new page (worksheets start at the top of a page)."""
        sec = self.d.add_section(WD_SECTION.NEW_PAGE)
        _set_margins(sec, margins)
        sec.footer_distance = Inches(0.35)
        if footer:
            self._footer(sec, footer)
        return sec

    def page_break(self):
        self.d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # ----- text -------------------------------------------------------------
    def _runs(self, p, text, size=None, italic=False, color=None, bold=False):
        # **bold** markup
        for i, part in enumerate(re.split(r"\*\*", text)):
            if not part:
                continue
            r = p.add_run(part)
            r.bold = bold or (i % 2 == 1)
            r.italic = italic
            if size:
                r.font.size = Pt(size)
            if color is not None:
                r.font.color.rgb = color
        return p

    def _space(self, p, before=None, after=None, keep_next=False):
        pf = p.paragraph_format
        if before is not None:
            pf.space_before = Pt(before)
        if after is not None:
            pf.space_after = Pt(after)
        if keep_next:
            pf.keep_with_next = True
        return p

    def h1(self, text):
        return self._space(self.d.add_paragraph(text, style="Heading 1"), before=0, after=4)

    def h2(self, text, minutes=None):
        p = self.d.add_paragraph(style="Heading 2")
        p.add_run(text)
        if minutes:
            r = p.add_run(f"  ({minutes} minutes)")
            r.font.size = Pt(12)
            r.bold = False
        return self._space(p, before=14, after=4, keep_next=True)

    def h3(self, text, minutes=None, before=8):
        p = self.d.add_paragraph(style="Heading 3")
        p.add_run(text)
        if minutes:
            r = p.add_run(f"  ({minutes} minutes)")
            r.font.size = Pt(11)
        return self._space(p, before=before, after=2, keep_next=True)

    def label(self, text, before=6, after=2, size=None):
        p = self.d.add_paragraph()
        self._runs(p, text, bold=True, size=size)
        return self._space(p, before=before, after=after, keep_next=True)

    def p(self, text, italic=False, size=None, after=6, before=None, keep_next=False, color=None):
        p = self.d.add_paragraph()
        self._runs(p, text, size=size, italic=italic, color=color)
        return self._space(p, before=before, after=after, keep_next=keep_next)

    def note(self, text, after=6):
        """Small italic line under a worksheet title."""
        return self.p(text, italic=True, size=10, after=after, color=RGBColor(0x40, 0x40, 0x40))

    def _list(self, items, marker, size=None, indent=0.3, after=2):
        out = []
        for i, it in enumerate(items, 1):
            p = self.d.add_paragraph()
            pf = p.paragraph_format
            pf.left_indent = Inches(indent)
            pf.first_line_indent = Inches(-0.22)
            pf.space_after = Pt(after)
            pf.tab_stops.add_tab_stop(Inches(indent))
            self._runs(p, (marker(i) if callable(marker) else marker) + "\t", size=size)
            self._runs(p, it, size=size)
            out.append(p)
        if out:
            out[-1].paragraph_format.space_after = Pt(8)
        return out

    def bullets(self, items, size=None, **kw):
        return self._list(items, "•", size=size, **kw)

    def numbered(self, items, size=None, **kw):
        return self._list(items, lambda i: f"{i}.", size=size, **kw)

    def checks(self, items, size=None, **kw):
        return self._list(items, "☐", size=size, **kw)

    def discuss(self, questions, heading="Discuss"):
        self.label(heading)
        return self.bullets(questions)

    # ----- boxes and tables ----------------------------------------------
    @staticmethod
    def _shade(cell, fill):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), fill)
        tcPr.append(shd)

    @staticmethod
    def _borders(table, color="808080", size=4, left_only=None):
        tblPr = table._tbl.tblPr
        b = OxmlElement("w:tblBorders")
        for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = OxmlElement(f"w:{side}")
            if left_only and side != "left":
                e.set(qn("w:val"), "nil")
            else:
                e.set(qn("w:val"), "single")
                e.set(qn("w:sz"), str(left_only or size))
                e.set(qn("w:color"), color)
            b.append(e)
        tblPr.append(b)

    @staticmethod
    def _cell_margins(table, top=60, bottom=60, left=100, right=100):
        tblPr = table._tbl.tblPr
        m = OxmlElement("w:tblCellMar")
        for side, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
            e = OxmlElement(f"w:{side}")
            e.set(qn("w:w"), str(v))
            e.set(qn("w:type"), "dxa")
            m.append(e)
        tblPr.append(m)

    def _width(self):
        s = self.d.sections[-1]
        return s.page_width - s.left_margin - s.right_margin

    @staticmethod
    def _cant_split(row):
        trPr = row._tr.get_or_add_trPr()
        e = OxmlElement("w:cantSplit")
        trPr.append(e)

    @staticmethod
    def _header_row(row):
        trPr = row._tr.get_or_add_trPr()
        e = OxmlElement("w:tblHeader")
        trPr.append(e)

    @staticmethod
    def _row_height(row, inches):
        trPr = row._tr.get_or_add_trPr()
        h = OxmlElement("w:trHeight")
        h.set(qn("w:val"), str(int(inches * 1440)))
        h.set(qn("w:hRule"), "atLeast")
        trPr.append(h)

    @staticmethod
    def _fix_widths(t, widths):
        tblPr = t._tbl.tblPr
        lay = tblPr.find(qn("w:tblLayout"))
        if lay is None:
            lay = OxmlElement("w:tblLayout")
            tblPr.append(lay)
        lay.set(qn("w:type"), "fixed")
        tw = tblPr.find(qn("w:tblW"))
        if tw is None:
            tw = OxmlElement("w:tblW")
            tblPr.append(tw)
        tw.set(qn("w:w"), str(int(sum(widths) * 1440)))
        tw.set(qn("w:type"), "dxa")
        for gc, w in zip(t._tbl.tblGrid.findall(qn("w:gridCol")), widths):
            gc.set(qn("w:w"), str(int(w * 1440)))
        for row in t.rows:
            for tc, w in zip(row._tr.findall(qn("w:tc")), widths):
                row_cell_w = tc.get_or_add_tcPr()
                e = row_cell_w.find(qn("w:tcW"))
                if e is None:
                    e = OxmlElement("w:tcW")
                    row_cell_w.insert(0, e)
                e.set(qn("w:w"), str(int(w * 1440)))
                e.set(qn("w:type"), "dxa")

    def read_aloud(self, paragraphs, title=None, bullets=None, after_bullets=None):
        """A shaded box the group reads aloud."""
        t = self.d.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        self._borders(t, BOX_LINE, left_only=24)
        self._cell_margins(t, top=100, bottom=60, left=180, right=160)
        self._fix_widths(t, [self._width() / 914400])
        c = t.cell(0, 0)
        self._shade(c, BOX_FILL)
        self._cant_split(t.rows[0])
        p = c.paragraphs[0]
        r = p.add_run("READ ALOUD" + (f":  {title}" if title else ""))
        r.bold = True
        r.font.size = Pt(10)
        r.font.color.rgb = ACCENT
        self._space(p, after=4)
        for text in paragraphs:
            q = c.add_paragraph()
            self._runs(q, text)
            self._space(q, after=6)
        if bullets:
            for b in bullets:
                q = c.add_paragraph()
                q.paragraph_format.left_indent = Inches(0.3)
                q.paragraph_format.first_line_indent = Inches(-0.2)
                self._runs(q, "•\t" + b)
                self._space(q, after=3)
        for text in after_bullets or []:
            q = c.add_paragraph()
            self._runs(q, text)
            self._space(q, after=6)
        last = c.paragraphs[-1]
        last.paragraph_format.space_after = Pt(2)
        self._space(self.d.add_paragraph(), after=0).paragraph_format.line_spacing = Pt(6)
        return t

    def box(self, paragraphs, fill="F2F2F2", size=10):
        t = self.d.add_table(rows=1, cols=1)
        self._borders(t, "A6A6A6", size=4)
        self._cell_margins(t, top=80, bottom=60, left=140, right=140)
        self._fix_widths(t, [self._width() / 914400])
        c = t.cell(0, 0)
        self._shade(c, fill)
        self._cant_split(t.rows[0])
        for i, text in enumerate(paragraphs):
            q = c.paragraphs[0] if i == 0 else c.add_paragraph()
            self._runs(q, text, size=size)
            self._space(q, after=3)
        self._space(self.d.add_paragraph(), after=0).paragraph_format.line_spacing = Pt(6)
        return t

    def grid(self, headers, rows, widths, height=0.3, size=10, header_fill="D9E2F3",
             bold_rows=(), shade_rows=(), merged_rows=None, keep_together=False):
        """A bordered table. rows: list of lists of cell text ('' for blank)."""
        n = len(widths)
        t = self.d.add_table(rows=(1 if headers else 0) + len(rows), cols=n)
        self._borders(t, "808080", 4)
        self._cell_margins(t, top=30, bottom=30, left=80, right=80)
        t.autofit = False
        start = 0
        if headers:
            hr = t.rows[0]
            self._header_row(hr)
            for i, h in enumerate(headers):
                c = hr.cells[i]
                self._shade(c, header_fill)
                self._runs(c.paragraphs[0], h, size=size, bold=True)
            start = 1
        merged_rows = merged_rows or {}
        for ri, row in enumerate(rows):
            tr = t.rows[start + ri]
            self._row_height(tr, height)
            self._cant_split(tr)
            if ri in merged_rows:
                c = tr.cells[0].merge(tr.cells[n - 1])
                self._runs(c.paragraphs[0], merged_rows[ri], size=size,
                           bold=ri in bold_rows)
                if ri in shade_rows:
                    self._shade(c, "F2F2F2")
                continue
            for ci, text in enumerate(row):
                c = tr.cells[ci]
                self._runs(c.paragraphs[0], text, size=size, bold=ri in bold_rows)
                if ri in shade_rows:
                    self._shade(c, "F2F2F2")
        self._fix_widths(t, widths)
        for ri, row in enumerate(t.rows):
            if keep_together and ri < len(t.rows) - 1:
                for c in row.cells:
                    for q in c.paragraphs:
                        q.paragraph_format.keep_with_next = True
            for c in row.cells:
                for q in c.paragraphs:
                    q.paragraph_format.space_after = Pt(0)
        self._space(self.d.add_paragraph(), after=0).paragraph_format.line_spacing = Pt(4)
        return t

    def money_table(self, title, items, total, widths=(4.6, 2.0), cols=1, size=10, height=0.28):
        """Label | $____ rows; cols=2 puts two label/amount pairs side by side."""
        rows = []
        if cols == 1:
            rows = [[it, "$"] for it in items]
            w = list(widths)
            hdr = [title, "Amount"]
        else:
            half = (len(items) + 1) // 2
            left, right = items[:half], items[half:]
            for i in range(half):
                r = right[i] if i < len(right) else ""
                rows.append([left[i], "$", r, "$" if r else ""])
            w = list(widths) * 2
            hdr = [title, "Amount", "", "Amount"]
        bold = ()
        merged = None
        if total:
            if cols == 1:
                rows.append([total, "$"])
            else:
                rows.append(["", "", total, "$"])
            bold = (len(rows) - 1,)
        return self.grid(hdr, rows, w, height=height, size=size, bold_rows=bold,
                         shade_rows=bold)

    def lines(self, n, gap=0.36):
        """Writing lines: a full-width tab with an underscore leader."""
        width = self._width()
        for _ in range(n):
            p = self.d.add_paragraph()
            pf = p.paragraph_format
            pf.space_after = Pt(0)
            pf.space_before = Pt(0)
            pf.line_spacing = Pt(gap * 72)
            pPr = p._p.get_or_add_pPr()
            tabs = OxmlElement("w:tabs")
            tab = OxmlElement("w:tab")
            tab.set(qn("w:val"), "right")
            tab.set(qn("w:leader"), "underscore")
            tab.set(qn("w:pos"), str(int(width / 635) - 10))
            tabs.append(tab)
            pPr.append(tabs)
            r = p.add_run("\t")
            r.font.color.rgb = RGBColor(0xA6, 0xA6, 0xA6)
        self._space(self.d.add_paragraph(), after=0).paragraph_format.line_spacing = Pt(4)

    def question(self, n, text, nlines=2, size=None):
        p = self.d.add_paragraph()
        self._runs(p, f"{n}. {text}" if n else text, size=size)
        self._space(p, before=4, after=0, keep_next=True)
        self.lines(nlines)

    ORDER = {
        "pPr": ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl",
                "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens",
                "kinsoku", "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE",
                "autoSpaceDN", "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
                "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc", "textDirection",
                "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr",
                "sectPr", "pPrChange"],
        "tblPr": ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize",
                  "tblStyleColBandSize", "tblW", "jc", "tblCellSpacing", "tblInd", "tblBorders",
                  "shd", "tblLayout", "tblCellMar", "tblLook", "tblCaption", "tblDescription"],
        "trPr": ["cnfStyle", "divId", "gridBefore", "gridAfter", "wBefore", "wAfter", "cantSplit",
                 "trHeight", "tblHeader", "tblCellSpacing", "jc", "hidden"],
        "tcPr": ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap",
                 "tcMar", "textDirection", "tcFitText", "vAlign", "hideMark"],
    }

    def _reorder(self, root):
        W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        for tag, order in self.ORDER.items():
            rank = {n: i for i, n in enumerate(order)}
            for el in root.iter(W + tag):
                kids = list(el)
                kids.sort(key=lambda k: rank.get(k.tag.replace(W, ""), len(order)))
                for k in kids:
                    el.remove(k)
                for k in kids:
                    el.append(k)

    def save(self, path):
        self._reorder(self.d.element.body)
        for s in self.d.sections:
            self._reorder(s.footer._element)
        self.d.save(path)
