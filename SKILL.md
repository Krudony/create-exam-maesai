---
name: si-som-docx
description: "Professional Word (.docx) document management. Specialized in A4 school exams with 2-column layout, TH SarabunPSK 16pt font, and Baan Mae Sai School headers. Also supports standard school project (สรุปโครงการ) templates."
---

# Si-Som DOCX Skill

## Overview
A specialized skill for creating professional Word documents, particularly tailored for educational exams and school reports.

## Core Rules
1. **Font**: Always use **TH SarabunPSK 16pt** for general content, exams, and projects (18pt for titles).
2. **Page**: Always use **A4** (11906 x 16838 Twips).
3. **Margins**: 
   - Exams: **1418 Twips** (approx 2.5cm)
   - Projects: **1440 Twips** (1 inch)
4. **Layout (Exams)**:
   - Use `add_official_header` with **Screenshot_8.png** as the default logo.
   - School Name: **โรงเรียนบ้านแม่ทราย(คุรุราษฎร์เจริญวิทย์)**.
   - Questions are **2 Columns** using a **Continuous Section Break**.
   - **Tight Spacing**: Line Spacing 1.0, Space Before 0pt, Space After 0pt for options. Questions have Space Before 6pt.
5. **Layout (Projects)**:
   - Single Column, Single line spacing (1.0).
   - Standard 7-section structure.

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
- **References**:
  - `formatting_rules.md`: DXA/Twips conversions.
  - `exam_template.md`: Exam layout.
  - `project_template.md`: School project structure.

## ?? Personal References
- eferences/TeachingSchedule.md: ���ҧ�͹����ش�ͧ�͹ (�ش� �����ͧ)

