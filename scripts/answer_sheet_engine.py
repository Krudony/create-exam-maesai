
import os
import sys
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

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

    # 2. Master Table 2x2
    master_table = doc.add_table(rows=2, cols=2)
    master_table.style = 'Table Grid'
    
    for row in master_table.rows:
        row.height = Cm(14.3)

    choices = ['ก', 'ข', 'ค', 'ง']

    for r in range(2):
        for c in range(2):
            cell = master_table.cell(r, c)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            
            # Clear default paragraph
            p_school = cell.paragraphs[0]
            p_school.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_school.paragraph_format.space_before = Pt(0)
            p_school.paragraph_format.space_after = Pt(0)
            run_school = p_school.add_run("โรงเรียนบ้านแม่ทราย(คุรุราษฎร์เจริญวิทย์)")
            set_font(run_school, size=14, bold=True)
            
            p_info = cell.add_paragraph()
            p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_info.paragraph_format.space_after = Pt(0)
            run_info = p_info.add_run("วิชา...................................... ชั้น........ เลขที่........")
            set_font(run_info, size=12)
            
            p_name = cell.add_paragraph()
            p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_name.paragraph_format.space_after = Pt(4)
            run_name = p_name.add_run("ชื่อ........................................................................")
            set_font(run_name, size=12)
            
            # --- Answer Grid ---
            rows_count = (num_questions + 1) // 2
            grid = cell.add_table(rows=rows_count, cols=10) # [No][ก][ข][ค][ง] x 2
            grid.style = 'Table Grid'
            grid.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            for g_row in grid.rows:
                g_row.height = Cm(0.48)
            
            for i in range(rows_count):
                # Set Left Column (Q 1-15)
                q_num = i + 1
                grid.cell(i, 0).text = str(q_num)
                for j, choice in enumerate(choices, 1):
                    grid.cell(i, j).text = choice
                
                # Set Right Column (Q 16-30)
                q_num_r = i + rows_count + 1
                if q_num_r <= num_questions:
                    grid.cell(i, 5).text = str(q_num_r)
                    for j, choice in enumerate(choices, 1):
                        grid.cell(i, 5 + j).text = choice
            
            # Formatting Grid Text
            for g_row in grid.rows:
                for g_cell in g_row.cells:
                    g_cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    for p in g_cell.paragraphs:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p.paragraph_format.space_before = Pt(0)
                        p.paragraph_format.space_after = Pt(0)
                        if p.runs:
                            set_font(p.runs[0], size=10)

    doc.save(output_path)
    print(f"Success: Created {output_path}")

if __name__ == "__main__":
    create_answer_sheet_4in1()
