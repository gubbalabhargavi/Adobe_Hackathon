# Adobe India Hackathon 2025 - Round 1B  
## Persona-Driven Document Intelligence  
**Team Member:** Gubbala Bhargavi  
**GitHub Repo:** [Adobe_Hackathon](https://github.com/gubbalabhargavi/Adobe_Hackathon)

---

## 📌 Challenge Summary

The objective of this round is to build a system that acts as an intelligent document analyst. Given:
- A set of PDFs,
- A persona (role),
- A job-to-be-done (task),

The system should extract the most relevant **sections** and **subsections** from the documents to help that persona accomplish their task.

---

## 🧠 Our Approach

We approached the problem using the following high-level steps:

1. **Text Extraction:**  
   All PDF files in the `/app/input` folder are parsed using `PyMuPDF` to extract page-wise raw text.

2. **Semantic Chunking and Filtering:**  
   We segment the text by headings using layout features like font size and boldness. Basic heuristics are used to identify potential section titles.

3. **Embedding-Based Relevance Scoring:**  
   - The persona and job-to-be-done text is embedded using a lightweight SentenceTransformer model.
   - Each document section is also embedded.
   - Cosine similarity is computed between the persona-task vector and section vectors.

4. **Ranking:**  
   Sections are ranked based on relevance scores and the top few are picked for final output.

5. **Subsection Extraction:**  
   From top-ranked sections, fine-grained sentences/paragraphs are extracted that match the persona-task intent using semantic filtering again.

6. **Output Format Generation:**  
   A JSON output is written to `/app/output` that includes metadata, extracted sections (with title, rank, and page), and relevant refined subsection texts.

---

## 🧰 Libraries & Models Used

| Library | Purpose |
|--------|---------|
| `PyMuPDF (fitz)` | Page-wise text and metadata extraction from PDFs |
| `SentenceTransformers` | Embedding documents and queries for semantic comparison |
| `scikit-learn` | Cosine similarity computation |
| `json`, `os`, `datetime` | File handling and formatting |

> **Note:** The model used is under 200MB and is run entirely on CPU. No internet access is needed during execution.

---

## 🐳 How to Build and Run Your Solution

Your solution should be run in a Docker container with this structure:

### 📁 Folder Structure
Adobe_Hackathon/
│
├── Dockerfile
├── main.py
├── Challenge_1B/
│ ├── challenge1b_input.json
│ ├── input/ # Contains PDFs
│ └── output/ # Output JSON will be saved here

### 🔨 Step 1: Build the Docker Image

```bash
docker build --platform linux/amd64 -t adobe1b:bhargavi .
Step 2: Run the Container
Make sure your input PDFs are in a local input/ folder and output is an empty folder.

bash
docker run --rm ^
  -v %cd%\Challenge_1B\input:/app/input ^
  -v %cd%\Challenge_1B\output:/app/output ^
  --network none adobe1b:bhargavi
📤 Output Format
The output will be a file like challenge1b_output.json inside /output, with the following fields:

metadata: input file list, persona, job-to-be-done, timestamp

extracted_sections: ranked sections with document, title, page number

subsection_analysis: text blocks from relevant sections with context

⚠️ Constraints Followed
Constraint	Met?
Model size < 200MB	✅
No internet access	✅
CPU-only execution	✅
Processing time < 60s	✅

🔐 License
This project is submitted as part of the Adobe India Hackathon 2025. Do not distribute before the deadline.
MIT License applies after the competition.

🙋‍♀️ Contact
📧 Email: b22cs022@iitj.ac.in
🔗 GitHub: gubbalabhargavi
