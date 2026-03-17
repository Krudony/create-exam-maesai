---
name: si-som-docx
description: "Professional Word (.docx) document management. Specialized in A4 school exams with 2-column layout, TH SarabunPSK 16pt font, and Baan Mae Sai School headers. Also supports standard school project (สรุปโครงการ) templates."
---

# Si-Som DOCX Skill

## Overview
A specialized skill for creating professional Word documents, particularly tailored for educational exams and school reports.

## 🛠️ System Requirements (MANDATORY)
To use this skill successfully, the host machine MUST have:
1. **Python 3.x installed**: All document generation logic runs via Python engines.
2. **Required Libraries**: Run `pip install python-docx docxtpl` to install the necessary modules.
3. **TH SarabunPSK Font**: The documents use this font exclusively. If not installed on the system, the layout will break.
4. **School Logo**: Ensure the `assets/Screenshot_8.png` file exists (included in this skill).

## Core Rules
1. **Font**: Always use **TH SarabunPSK 16pt** for general content, exams, and projects (18pt for titles).
2. **Page**: Always use **A4** (11906 x 16838 Twips).
3. **Engine**: Use **SiSomDocxEngine** class from `scripts/docx_engine.py`.
4. **Margins**: 
   - Exams: **1418 Twips** (approx 2.5cm)
   - Projects: **1440 Twips** (1 inch)
4. **Layout (Exams)**:
   - **Section 1 (Header)**: Always **1 Column** (Full width). Use `add_official_header` with **Screenshot_8.png** as the default logo.
   - **Section 2 (Body)**: Use a **Continuous Section Break** to start **2 Columns** for the questions.
   - **Section 3 (Answer Key)**: Reset to **1 Column** on a new page. MUST include two parts:
     1. **Compact Table**: A 5-column grid summary (e.g., 1. ก, 2. ข, 3. ง...).
     2. **Academic Explanations**: Detailed rationale for each answer based on grammar rules, vocabulary, or logic.
   - School Name: **โรงเรียนบ้านแม่ทราย(คุรุราษฎร์เจริญวิทย์)**.
   - **Tight Spacing**: Line Spacing 1.0, Space Before 0pt, Space After 0pt for options. Questions have Space Before 6pt.
5. **Layout (Projects)**:
   - Single Column, Single line spacing (1.0).
   - Standard 7-section structure.

6. **Layout (Answer Sheets)**:
   - **4-in-1 Eco Mode**: 1 Page A4 MUST contain 4 sheets (2x2 grid).
   - **Strict Constraints**: 
     - Page Margins: 0.4cm all sides.
     - Master Table Row Height: Exactly 14.3cm.
     - Answer Grid Row Height: Exactly 0.48cm (Expanded for easy marking).
   - **Design**:
     - No "Topic" field (Only "Subject").
     - Optional Logo (Default: No Logo for max space).
     - Centered Alignment for all text and the grid table.
     - Visible Grid Borders for easy cutting.

## 🚫 Strict Interaction Rules
- **KILL THE PAGER**: Never call CLI tools (like `notebooklm`) directly if they support interactive output (rich/paging).
- **MANDATORY REDIRECTION**: Always redirect output to a file (e.g., `command > file.txt`) to force non-interactive mode and prevent hangs.
- **TERMINATE HANGS**: Any command showing signs of interactivity must be cancelled immediately.

## Workflow: NotebookLM Integration
When using NotebookLM to generate exams:
1. **List Sources**: Use `notebooklm source list --notebook [ID]` to identify content.
2. **Stable Extraction**: Use `notebooklm source fulltext [SOURCE_ID] --notebook [ID] > content.txt` to get raw data. DO NOT use `ask` for large results.
3. **AI Reasoning**: Read the extracted text and generate high-quality Thai questions.
4. **DOCX Build**: Use `docx_engine.py` to create the final document with the official header and tight layout.

## Workflow: Exam Generation
When the user asks for an "exam" or "ข้อสอบ":
1. Read `references/exam_template.md` for header details.
2. Use `scripts/docx_engine.py` to generate the document.

## Workflow: School Project Generation
When the user asks for a "school project" or "สรุปโครงการ":
1. Read `references/project_template.md` for layout and section details.
2. Use `scripts/project_engine.py` to generate the document with exact margins and spacing.

## Resources
- **Scripts**: 
  - `docx_engine.py`: Exam driver.
  - `project_engine.py`: School project driver (High precision spacing).
  - `answer_sheet_engine.py`: 4-in-1 Eco Mode answer sheet generator.
- **References**:
  - `formatting_rules.md`: DXA/Twips conversions.
  - `exam_template.md`: Exam layout.
  - `project_template.md`: School project structure.

## ?? Personal References
- eferences/TeachingSchedule.md: ���ҧ�͹����ش�ͧ�͹ (�ش� �����ͧ)

