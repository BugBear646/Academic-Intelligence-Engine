import fitz
import tempfile
import requests

def extract_pdf_text(pdf_url):

    try:

        response = requests.get(pdf_url, timeout=20)

        if response.status_code != 200:
            return ""

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:

            tmp.write(response.content)

            path = tmp.name

        doc = fitz.open(path)

        text = ""

        for page in doc:
            text += page.get_text()

        doc.close()

        return text

    except Exception as e:

        print(f"PDF extraction error: {e}")

        return ""