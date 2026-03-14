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
   - Header is **1 Column**.
   - Questions are **2 Columns** using a **Continuous Section Break**.
   - **Spacing**: Space Before 4pt for Questions, Space After 4pt for last option in a question.
5. **Layout (Projects)**:
   - Single Column, Single line spacing (1.0).
   - Standard 7-section structure (Principles, Objectives, Goals, Activities, Budget, Evaluation, Results).

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

