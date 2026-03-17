# Exam Template: Baan Mae Sai School (Official v2026)

This template defines the high-precision layout for creating exams for Don.

## Header Structure (Official Layout)
- **School Logo**: `assets/Screenshot_8.png` (Standard width: 0.8 inches).
- **School Name**: โรงเรียนบ้านแม่ทราย(คุรุราษฎร์เจริญวิทย์).
- **Education Area**: สำนักงานเขตพื้นที่การศึกษาประถมศึกษาแพร่ เขต 1.
- **Main Header Table**: 1x1 Table containing:
    - Logo (Centered)
    - "ข้อสอบวัดผลสัมฤทธิ์ปลายภาคเรียน  ภาคเรียนที่ [เทอม]"
    - "วิชา[ชื่อวิชา] ชั้น[ระดับชั้น]  คะแนนเต็ม [คะแนน] คะแนน  เวลา [เวลา] นาที"
    - "[School Name]  [Area]"
    - "*************************************************************"
- **Student Info Table**: 1x2 Table (Bordered)
    - Col 0: "ชื่อ–สกุล  ........................................................."
    - Col 1: "ชั้น  ........  เลขที่  ........"
- **Instructions**: "คำชี้แจง  [เนื้อหาคำชี้แจง]" (Bold, 6pt Space Before).

## Technical Specifications
- **Font**: TH SarabunPSK, 16pt (Style: Normal).
- **Page Size**: A4 (11906 x 16838 Twips).
- **Margins**: **1418 Twips** (approx. 2.5cm) on all sides.
- **Line Spacing**: Single (1.0).
- **Layout**:
    - Header/Info: 1 Column.
    - Questions: **2 Columns** using a **Continuous Section Break**.
- **Answer Key**: 5-column Grid Table at the end of the document on a NEW PAGE.

## Spacing Rules
- **Questions**: Space Before 6pt (to separate from options).
- **Options**: Line Spacing 1.0, Space Before/After 0pt (Extremely tight to save paper).
- **Margins**: Ensure the 1418 Twips limit is never exceeded.

## Reference Examples
- `examples/ข้อสอบ_Official_Template_ป5.docx`: The master reference for visual consistency.
