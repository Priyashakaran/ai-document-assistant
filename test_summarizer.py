from flask import Flask, render_template, request
from pypdf import PdfReader

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# --------------------------------------------------
# Create Flask test_summarizerlication
# --------------------------------------------------

test_summarizer = Flask(__name__)


# --------------------------------------------------
# Load the summarization model
# --------------------------------------------------

model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


# --------------------------------------------------
# Home page
# --------------------------------------------------

@test_summarizer.route("/")
def home():

    return render_template("index.html")


# --------------------------------------------------
# PDF summarization
# --------------------------------------------------

@test_summarizer.route("/summarize", methods=["POST"])
def summarize():

    # Check whether a file was uploaded
    if "pdf" not in request.files:
        return "No PDF file was uploaded."


    # Get the uploaded PDF
    pdf_file = request.files["pdf"]


    # Check whether the user actually selected a file
    if pdf_file.filename == "":
        return "Please select a PDF file."


    # Check that the uploaded file is a PDF
    if not pdf_file.filename.lower().endswith(".pdf"):
        return "Please upload a PDF file."


    # --------------------------------------------------
    # Extract text from the PDF
    # --------------------------------------------------

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"


    # Check whether text was successfully extracted
    if not text.strip():
        return "Could not extract text from this PDF."


    print("Extracted text length:", len(text))


    # --------------------------------------------------
    # Prepare text for BART
    # --------------------------------------------------

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True
    )


    # --------------------------------------------------
    # Generate summary
    # --------------------------------------------------

    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        min_new_tokens=20,
        do_sample=False,
        num_beams=4,
        no_repeat_ngram_size=3
    )


    # --------------------------------------------------
    # Convert model output into readable text
    # --------------------------------------------------

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )


    # --------------------------------------------------
    # Send summary to webpage
    # --------------------------------------------------

    return render_template(
        "results.html",
        summary=summary
    )


# --------------------------------------------------
# Start Flask test_summarizerlication
# --------------------------------------------------

if __name__ == "__main__":

    test_summarizer.run(debug=True)