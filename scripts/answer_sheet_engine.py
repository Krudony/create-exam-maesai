
import os
import sys
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_cell_margins(cell, top=0, start=0, bottom=0, end=0):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m in [('top', top), ('start', start), ('bottom', bottom), ('end', end)]:
        node = OxmlElement(f'w:{m[0]}')
        node.set(qn('w:w'), str(m[1]))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_font(run, size=14, bold=False):
    run.font.name = 'TH SarabunPSK'
    r = run._element
    rPr = r.get_or_add_rPr()
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), 'TH SarabunPSK')
    rFonts.set(qn('w:hAnsi'), 'TH SarabunPSK')
    rFonts.set(qn('w:eastAsia'), 'TH SarabunPSK')
    rFonts.set(qn('w:cs'), 'TH SarabunPSK')
    rPr.append(rFonts)
    run.font.size = Pt(size)
    run.bold = bold

def create_answer_sheet_4in1(output_path="กระดาษคำตอบ_4in1_EcoMode.docx", num_questions=30):
    doc = Document()
    
    # 1. Page Setup (A4, 0.4cm margins)
    section = doc.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(0.4)
    section.bottom_margin = Cm(0.4)
    section.left_margin = Cm(0.4)
    section.right_margin = Cm(0.4)

    # 2. Master Table 2x2 (Spanning full page)
    master_table = doc.add_table(rows=2, cols=2)
    master_table.style = 'Table Grid' # Visible borders for easy cutting
    
    # Set Master Row Height (Exactly 14.3cm as per SKILL.md)
    for row in master_table.rows:
        row.height = Cm(14.3)

    # Fill each cell with an Answer Sheet
    for r in range(2):
        for c in range(2):
            cell = master_table.cell(r, c)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            set_cell_margins(cell, top=100, start=100, bottom=100, end=100)
            
            # --- Sheet Content ---
            p_school = cell.paragraphs[0]
            p_school.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run_school = p_school.add_run("โรงเรียนบ้านแม่ทราย(คุรุราษฎร์เจริญวิทย์)")
            set_font(run_school, size=14, bold=True)
            
            p_info = cell.add_paragraph()
            p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
            info_text = "วิชา...................................... ชั้น........ เลขที่........"
            run_info = p_info.add_run(info_text)
            set_font(run_info, size=12)
            
            p_name = cell.add_paragraph()
            p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run_name = p_name.add_run("ชื่อ........................................................................")
            set_font(run_name, size=12)
            
            # --- Answer Grid Table ---
            # Create sub-table for answers (e.g. 3 columns of 10 questions)
            # Layout: [No][A][B][C][D] | [No][A][B][C][D] | [No][A][B][C][D]
            # To fit 30 questions, let's use 2 columns of 15 questions to save space
            rows_count = (num_questions + 1) // 2
            grid = cell.add_table(rows=rows_count, cols=10) # 2 sets of (No, ก, ข, ค, ง)
            grid.style = 'Table Grid'
            grid.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            # Set Grid Row Height (Exactly 0.48cm as per SKILL.md)
            for g_row in grid.rows:
                g_row.height = Cm(0.48)
            
            for i in range(rows_count):
                # Set content for Col 1-5 (Questions 1-15)
                grid.cell(i, 0).text = str(i+1)
                for j in range(1, 5):
                    grid.cell(i, j).text = " "
                
                # Set content for Col 6-10 (Questions 16-30)
                if i + rows_count < num_questions:
                    grid.cell(i, 5).text = str(i + rows_count + 1)
                    for j in range(6, 10):
                        grid.cell(i, j).text = " "
            
            # Format Grid Font
            for g_row in grid.rows:
                for g_cell in g_row.cells:
                    g_cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    for p in g_cell.paragraphs:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        if p.runs:
                            set_font(p.runs[0], size=10)

    doc.save(output_path)
    print(f"Success: Created {output_path}")

if __name__ == "__main__":
    create_answer_sheet_4in1()
