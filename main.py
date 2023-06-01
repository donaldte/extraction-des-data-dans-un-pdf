import PyPDF2

def extract_pdf_data(file_path):
    pdf_data = {}
    
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        num_pages = len(reader.pages)
        
        for page_number in range(num_pages):
            #page = reader.getPage(page_number)
            page = reader.pages[page_number]
            content = page.extract_text()
            
            # Split content into lines
            lines = content.split('\n')
            
            # Extract heading and content
            heading = lines[0].strip()
            content = ' '.join(lines[1:]).strip()
            
            pdf_data[heading] = content
    
    return pdf_data

# Usage example
file_path = r"C:\Users\ENG.TEDOM\Desktop\code extrat text in file\p_django.pdf"
data = extract_pdf_data(file_path)

print(data)

# # Print the extracted data
# for heading, content in data.items():
#     print(f'{heading}: {content}')
