Here's the **complete and polished `README.md`** code block, ready to be copy-pasted into your GitHub repository:

```markdown
# 🧠 Adobe India Hackathon 2025 - Round 1B  
## Persona-Driven Document Intelligence

![Docker](https://img.shields.io/badge/containerized-Docker-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Model Size](https://img.shields.io/badge/model-%3C200MB-lightgrey)

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

The objective is to build a system that acts as an **intelligent document analyst**.  
Given:
- A **set of PDF documents**
- A **persona definition**
- A **job-to-be-done**

The system should extract the **most relevant sections and subsections** to help the persona efficiently accomplish their task.

---

## 🧠 Our Approach

### 1. **Text Extraction**
- Extract raw text from all PDF pages using `PyMuPDF (fitz)`.

### 2. **Semantic Chunking & Filtering**
- Segment text using layout cues like **font size**, **boldness**, and **indentation** to identify headings and sections.

### 3. **Embedding-Based Relevance Scoring**
- Embed both the **persona+task** and **each section** using `SentenceTransformers`.
- Compute **cosine similarity** to find semantically relevant content.

### 4. **Ranking**
- Rank all sections by similarity score.
- Select top sections for detailed review.

### 5. **Subsection Extraction**
- From selected sections, extract key paragraphs/sentences using a second semantic filtering stage.

### 6. **Output Generation**
- Save results in structured JSON including:
  - Input metadata
  - Ranked sections
  - Subsection snippets

---

## 🧰 Libraries & Models Used

| Library                | Purpose                                           |
|------------------------|---------------------------------------------------|
| `PyMuPDF (fitz)`       | PDF text & metadata extraction                    |
| `SentenceTransformers` | Semantic embeddings for persona and document      |
| `scikit-learn`         | Cosine similarity computation                     |
| `json`, `os`, `datetime` | File I/O and metadata formatting               |

> ✅ Lightweight model (<200MB), runs on CPU, no internet required.

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

---

### ▶️ Step 2: Run the Docker Container

```bash
docker run --rm ^
  -v %cd%\Challenge_1B\input:/app/input ^
  -v %cd%\Challenge_1B\output:/app/output ^
  --network none adobe1b:bhargavi
```

> ⚠️ Ensure:
>
> * PDFs are placed in `Challenge_1B/input`
> * `Challenge_1B/output` is empty before execution

---

## 📤 Output Format

The output is a file `challenge1b_output.json` in the `/output` folder, formatted as:

```json
{
  "metadata": {
    "input_files": ["document1.pdf", "document2.pdf"],
    "persona": "PhD Researcher in Computational Biology",
    "job_to_be_done": "Find recent breakthroughs in DNA sequencing",
    "timestamp": "2025-07-27T18:00:00"
  },
  "extracted_sections": [
    {
      "document": "document1.pdf",
      "title": "Advancements in DNA Sequencing",
      "page": 3,
      "score": 0.89
    }
  ],
  "subsection_analysis": [
    {
      "section_title": "Advancements in DNA Sequencing",
      "text_block": "Recent innovations include ...",
      "page": 3
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

> ❗ Do not distribute publicly until the competition ends.

After the hackathon, this repository will be available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙋‍♀️ Contact

Feel free to connect or reach out for queries:

📧 Email: [b22cs022@iitj.ac.in](mailto:b22cs022@iitj.ac.in)
🔗 GitHub: [gubbalabhargavi](https://github.com/gubbalabhargavi)

```

---

### ✅ What's Included:
- Clean structure
- Markdown best practices
- Shields.io badges
- Table of contents
- Easy Docker run instructions
- Full output example

Let me know if you’d like to add deployment instructions or GitHub Actions for CI/CD.
```
