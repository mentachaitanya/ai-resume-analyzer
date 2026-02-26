from fpdf import FPDF
import io

class ResumePDF(FPDF):
    def header(self):
        # We don't want a header on every page for a resume usually
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def section_title(self, label):
        self.set_font('helvetica', 'B', 12)
        self.set_fill_color(240, 240, 240)
        self.set_text_color(16, 185, 129) # Primary green color
        self.cell(0, 10, f" {label.upper()}", 0, 1, 'L', fill=True)
        self.ln(2)

    def resume_body(self, text):
        self.set_font('helvetica', '', 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 7, text)
        self.ln(5)

def generate_resume_pdf(text: str) -> io.BytesIO:
    pdf = ResumePDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Process text - AI usually returns markdown-ish text
    # We'll split by common section markers
    sections = {
        "Contact Information": "",
        "Summary": "",
        "Experience": "",
        "Education": "",
        "Skills": "",
        "Projects": ""
    }
    
    # Simple heuristic to split text into sections if possible
    lines = text.split('\n')
    current_section = "Summary"
    
    for line in lines:
        clean_line = line.strip().replace('#', '').replace('*', '')
        if not clean_line: continue
        
        # Check if line is a section header
        found_header = False
        for sec in sections.keys():
            if sec.lower() in clean_line.lower() and len(clean_line) < 30:
                current_section = sec
                found_header = True
                break
        
        if not found_header:
            sections[current_section] += clean_line + "\n"

    # Build PDF
    for title, content in sections.items():
        if content.strip():
            pdf.section_title(title)
            # Ensure latin-1 encoding for default FPDF fonts
            clean_content = content.encode('latin-1', 'ignore').decode('latin-1')
            pdf.resume_body(clean_content)
    
    buf = io.BytesIO()
    pdf.output(buf)
    buf.seek(0)
    return buf
