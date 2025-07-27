

---

```markdown
# 🧠 Adobe India Hackathon 2025 - Round 1B  
## Persona-Driven Document Intelligence

![Docker](https://img.shields.io/badge/containerized-Docker-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Model Size](https://img.shields.io/badge/model-<200MB-lightgrey)

---

## 📚 Table of Contents
- [👤 Team Member](#-team-member)
- [📌 Challenge Summary](#-challenge-summary)
- [🧠 Our Approach](#-our-approach)
- [🧰 Libraries & Models Used](#-libraries--models-used)
- [🐳 How to Build and Run](#-how-to-build-and-run)
- [📤 Output Format](#-output-format)
- [⚠️ Constraints Followed](#️-constraints-followed)
- [🔐 License](#-license)
- [🙋‍♀️ Contact](#-contact)

---

## 👤 Team Member  
**Gubbala Bhargavi**  
📧 Email: [b22cs022@iitj.ac.in](mailto:b22cs022@iitj.ac.in)  
🔗 GitHub: [gubbalabhargavi](https://github.com/gubbalabhargavi)  

---

## 📌 Challenge Summary

The objective of this round is to build an **intelligent document analyst**.  
Given:
- A **set of PDF documents**
- A **persona definition**
- A **job-to-be-done**

The system must extract the **most relevant sections and subsections** from the documents to help the persona accomplish their task effectively.

---

## 🧠 Our Approach

### 1. **Text Extraction**
- All PDF files in `/app/input` are parsed using `PyMuPDF (fitz)`.
- Extracts **page-wise text** with layout information.

### 2. **Semantic Chunking & Filtering**
- Documents are segmented based on **headings** using visual layout cues (font size, boldness).
- Basic heuristics help detect potential section titles.

### 3. **Embedding-Based Relevance Scoring**
- The **persona + task** string is embedded using a **lightweight SentenceTransformer model**.
- Each section is also embedded.
- Compute **cosine similarity** between persona-task and each section.

### 4. **Ranking**
- Sections are **ranked** based on similarity scores.
- Top sections are selected for further processing.

### 5. **Subsection Extraction**
- From top sections, extract **key sentences/paragraphs** aligned with the persona's goal using further filtering.

### 6. **Output Generation**
- Outputs a structured JSON file to `/app/output`, containing:
  - Metadata
  - Ranked sections (title, page, rank)
  - Subsections with rich semantic context

---

## 🧰 Libraries & Models Used

| Library              | Purpose                                           |
|----------------------|---------------------------------------------------|
| `PyMuPDF (fitz)`     | PDF text & layout metadata extraction             |
| `SentenceTransformers` | Semantic embeddings for persona and sections     |
| `scikit-learn`       | Cosine similarity computation                     |
| `json`, `os`, `datetime` | File handling & formatting utilities          |

> ✅ Model is < 200MB, CPU-only, no internet access needed.

---

## 🐳 How to Build and Run

### 📁 Folder Structure
```

Adobe\_Hackathon/
├── Dockerfile
├── main.py
└── Challenge\_1B/
├── challenge1b\_input.json
├── input/           # Put PDFs here
└── output/          # Output JSON will be saved here

````

---

### 🔨 Step 1: Build Docker Image
```bash
docker build --platform linux/amd64 -t adobe1b:bhargavi .
````

### ▶️ Step 2: Run the Docker Container

```bash
docker run --rm ^
  -v %cd%\Challenge_1B\input:/app/input ^
  -v %cd%\Challenge_1B\output:/app/output ^
  --network none adobe1b:bhargavi
```

> Make sure:
>
> * PDFs are placed in `Challenge_1B/input`
> * `Challenge_1B/output` is empty before running

---

## 📤 Output Format

The output JSON file (e.g., `challenge1b_output.json`) contains:

```json
{
  "metadata": {
    "input_files": [...],
    "persona": "...",
    "job_to_be_done": "...",
    "timestamp": "..."
  },
  "extracted_sections": [
    {
      "document": "...",
      "title": "...",
      "page": ...,
      "score": ...
    }
  ],
  "subsection_analysis": [
    {
      "section_title": "...",
      "text_block": "...",
      "page": ...
    }
  ]
}
```

---

## ⚠️ Constraints Followed

| Constraint               | Met? |
| ------------------------ | ---- |
| Model size < 200MB       | ✅    |
| No internet access       | ✅    |
| CPU-only execution       | ✅    |
| Processing time < 60 sec | ✅    |

---

## 🔐 License

This project is submitted as part of the **Adobe India Hackathon 2025**.

> ❗ Do not distribute before the official deadline.

MIT License applies **after** the competition ends.

---

## 🙋‍♀️ Contact

Feel free to reach out for questions or discussions:

📧 Email: [b22cs022@iitj.ac.in](mailto:b22cs022@iitj.ac.in)
🔗 GitHub: [gubbalabhargavi](https://github.com/gubbalabhargavi)

```

---

✅ You can copy-paste this into your `README.md` file. If you'd like to auto-link sections or turn this into a GitHub Pages site later, I can help with that too.
```
