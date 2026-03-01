#%%

import os
os.environ['REQUESTS_CA_BUNDLE'] = "C:/Users/shibin.xie/AppData/Local/.certifi/cacert.pem"

import os
from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import display, Markdown
from pdf2image import convert_from_path
from pypdf import PdfReader, PdfWriter  # Import pypdf

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


# Directory containing PNG files
fpath = r"C:\Users\shibin.xie\Documents\MI Presentations\Samsung Forum\Edge AI"  # Replace with actual base directory

pdf_file_path = os.path.join(fpath, "edge AI talk slides v1.1.pdf")

temp_file_path = os.path.join(fpath, "temp_selected_pages.pdf")

# ==========================================
# STEP 1: Create a new PDF with selected pages
# ==========================================

# Define which pages you want (0-based index)
# Example: 0 is Page 1, 4 is Page 5
# pages_to_keep = [1, 1, 2, 5] 

# pages_to_keep = [1] + list(range(4, 10))

pages_to_keep = list(range(1, 4))

# pages_to_keep = list(range(12, 17))+ list(range(23, 27))

reader = PdfReader(pdf_file_path)
writer = PdfWriter()

for page_num in pages_to_keep:
    # Check if page exists to avoid errors
    if page_num < len(reader.pages):
        writer.add_page(reader.pages[page_num])

# Save the extracted pages to a temporary file
with open(temp_file_path, "wb") as f:
    writer.write(f)

print(f"Created temporary PDF with {len(pages_to_keep)} pages.")
#%%