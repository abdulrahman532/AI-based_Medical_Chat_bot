import streamlit as st
from PIL import Image
import pytesseract
import re

st.set_page_config(page_title="Prescription Reader")
st.title("💊 Prescription Medication Extractor")

uploaded_file = st.file_uploader("Upload a prescription image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Prescription", use_column_width=True)

    # OCR - extract raw text
    text = pytesseract.image_to_string(image, config="--psm 6")
    text_clean = text.replace("‘", "").replace("_", " ").replace("—", "-").strip()

    # Patterns
    drug_pattern = r"(?i)([A-Z][a-zA-Z0-9]+\s+\d+\s?(mg|ml|units)?)"
    tabs_pattern = r"(?i)(Tabs?\s*(No\.)?\s*\d+)"
    sig_pattern = r"(?i)(Sig[:\-]?\s?.+)"
    refill_pattern = r"(?i)(Refill\s?[xX]?\s?\d+|Refill\s?.*times?)"

    # Combine matches into a structured block
    st.markdown("### 💊 Detected Medication Info")

    lines = text_clean.split("\n")
    results = []

    for line in lines:
        line = line.strip()
        if re.search(drug_pattern, line) or re.search(sig_pattern, line) or re.search(tabs_pattern, line) or re.search(refill_pattern, line):
            results.append(line)

    if results:
        for i, line in enumerate(results, 1):
            st.markdown(f"**{i}.** {line}")
    else:
        st.warning("⚠ No medication data detected.")
