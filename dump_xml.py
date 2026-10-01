import zipfile
import re

def dump_xml_text(docx_filename, txt_filename):
    with zipfile.ZipFile(docx_filename) as zf:
        xml_content = zf.read('word/document.xml').decode('utf-8')
    
    # Simple regex to extract text within <w:t> tags
    text_list = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml_content)
    
    with open(txt_filename, 'w', encoding='utf-8') as f:
        for t in text_list:
            if t.strip():
                f.write(t + '\n')
    print(f"Dumped raw text from {docx_filename} to {txt_filename}")

if __name__ == '__main__':
    dump_xml_text("Basic_Kanji_320_Stroke_Order_Meanings_Examples.docx", "kanji_raw_xml_text.txt")
