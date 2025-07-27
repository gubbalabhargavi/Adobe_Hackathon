import json
import os
from datetime import datetime
import fitz  # PyMuPDF
import re

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    data = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        data.append({"page": page_num + 1, "text": text})
    return data

def rank_sections(text_pages, keywords):
    ranked = []
    for page in text_pages:
        score = sum([page["text"].lower().count(kw.lower()) for kw in keywords])
        if score > 0:
            ranked.append({
                "page": page["page"],
                "text": page["text"],
                "score": score
            })
    return sorted(ranked, key=lambda x: -x["score"])[:3]

def main():
    with open("challenge1b_input.json", "r") as f:
        input_data = json.load(f)

    persona = input_data["persona"]["role"]
    job = input_data["job_to_be_done"]["task"]
    keywords = re.findall(r'\b\w+\b', persona + ' ' + job)

    output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in input_data["documents"]],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [],
        "sub_section_analysis": []
    }

    for doc in input_data["documents"]:
        filepath = os.path.join("input", doc["filename"])
        text_pages = extract_text_from_pdf(filepath)
        top_sections = rank_sections(text_pages, keywords)

        for rank, section in enumerate(top_sections):
            output["extracted_sections"].append({
                "document": doc["filename"],
                "page_number": section["page"],
                "section_title": f"Page {section['page']}",
                "importance_rank": rank + 1
            })
            output["sub_section_analysis"].append({
                "document": doc["filename"],
                "page_number": section["page"],
                "refined_text": section["text"][:1000]  # trim text for readability
            })

    with open("challenge1b_output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
