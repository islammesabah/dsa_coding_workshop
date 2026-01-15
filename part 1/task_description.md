# Coding & GenAI Workshop: Automation Tasks

This repository contains the projects and technical requirements for the "Workshop part 1" focused on using Generative AI to simplify university tasks.

## 📂 Task 1: Lecture Slides Renaming

The goal of this task is to resolve the problem of unclear and inconsistent naming conventions for lecture slides.

### Solution

Build a Python script to batch-rename PDF files into a standardized format:

* **Target Format:** `Lecture_{lecture_number}_EngGenAI_{lecture_title}`

### Setup & Requirements

* **Python:** Ensure you have Python installed (Download: [python.org](https://www.python.org/downloads/)).
* **Assistance:** You can use LLMs like ChatGPT to help build the script step-by-step.
* **Input Files:** The script should reference a `naming_list.txt` or similar file to map numbers to titles.

---

## 🤖 Task 2: AI Summarizer Tool Development

Develop a command-line tool that interfaces with the RPTU LLM infrastructure to generate concise, student-friendly notes.

### The Prompt Strategy

Instruct your AI (ChatGPT or Gemini) to act as an **Expert Python Developer** to create a script that:

* Reads content from a local file named `transcript.txt`.
* Transmits data securely to the RPTU infrastructure.
* Summarizes the input into 5–7 concise bullet points.
* Maintains strict accuracy: the script must explicitly state if data is missing to ensure zero hallucinations.

### Technical Specifications

* **API Endpoint:** `https://ai-api.rz.rptu.de/api/generate`
* **Architecture:** Use HTTP POST requests with a JSON body containing `model`, `prompt`, and `stream` fields.
* **Dependencies:** Standard Python libraries and the `requests` module.




