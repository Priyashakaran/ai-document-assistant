# AI Document Assistant

An AI-powered web application that allows users to upload PDF documents and automatically generate concise summaries using a pretrained BART summarization model.

The application combines **Flask**, **PyPDF**, and **Hugging Face Transformers** to create a simple document summarization workflow.

---

## Features

* Upload PDF documents through a web interface
* Extract text from PDF files using PyPDF
* Generate AI-powered summaries using BART
* Display the generated summary on a dedicated results page
* Simple and responsive web interface
* Separate upload and results pages
* Handles invalid file types and PDFs with no extractable text

---

## How It Works

The application follows this workflow:

```text
User uploads PDF
       ↓
Flask receives the file
       ↓
PyPDF extracts text
       ↓
BART processes the extracted text
       ↓
AI-generated summary
       ↓
Results page displays the summary
```

---

## Technologies Used

### Backend

* Python
* Flask
* PyPDF

### AI / NLP

* Hugging Face Transformers
* Facebook BART Large CNN
* PyTorch

### Frontend

* HTML
* CSS
* Jinja2 templates

---

## AI Model

This project uses:

**`facebook/bart-large-cnn`**

BART is a transformer-based sequence-to-sequence model that has been fine-tuned for summarization tasks.

The model is loaded locally using Hugging Face Transformers.

---

## Project Structure

```text
AI_DOCUMENT_ASSISTANT/
│
├── test_summarizer.py
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── .gitignore
├── requirements.txt
└── README.md
```

The `venv/` directory is intentionally excluded from Git using `.gitignore`.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-document-assistant.git
```

Move into the project directory:

```bash
cd ai-document-assistant
```

---

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application:

```powershell
python test_summarizer.py
```

You should see Flask start the development server.

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## Using the Application

1. Open the application in your browser.
2. Select a PDF document.
3. Click **Summarize PDF**.
4. The application extracts text from the PDF.
5. BART generates a summary.
6. The generated summary is displayed on the results page.
7. Click **Upload Another PDF** to process another document.

---

## Current Limitations

This is the first version of the application and intentionally uses a simple summarization pipeline.

### Long documents

The current implementation does not yet use document chunking.

Very long PDFs may therefore be truncated when the extracted text is passed to the model because transformer models have input-length limitations.

A future version could implement:

* Text chunking
* Sentence-aware chunking
* Chunk-level summarization
* Combining chunk summaries into a final document summary

### PDF extraction

The application works best with PDFs containing selectable text.

Scanned PDFs or image-based documents may require OCR before summarization.

---

## Future Improvements

Possible improvements for future versions include:

* PDF text chunking for long documents
* OCR support for scanned PDFs
* Support for additional document formats
* Adjustable summary length
* Download summary as a TXT or PDF file
* Document metadata display
* Improved error handling
* Summary history
* More advanced document analysis

---

## What I Learned

This project helped me understand the practical workflow involved in building an AI-powered document application:

* Building a Flask web application
* Handling file uploads
* Extracting text from PDFs
* Loading pretrained transformer models
* Tokenizing input text
* Generating text with a sequence-to-sequence model
* Passing AI-generated results to a frontend using Jinja2
* Understanding transformer input-length limitations
* Understanding why long-document summarization may require chunking

---

## Project Status

**Version 1.0 — Completed**

The current version focuses on the core PDF-to-summary workflow without adding unnecessary complexity.

---

## Author

**Priyasha Rathore**

MCA | Python | Backend Development | AI & NLP

---

## License

This project is intended for learning, portfolio development, and experimentation.
