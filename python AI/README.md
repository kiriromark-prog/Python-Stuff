# Gemini AI Response Generator

A Python application leveraging Google's Gemini models via LangChain to generate AI responses while automatically filtering out unnecessary metadata for clean text output.

## Features

* **LangChain Integration:** Easily interacts with Google's Gemini generative models using `langchain-google-genai`.
* **Clean Output Formatting:** Automatically strips metadata structures from response objects and returns plain text.
* **Environment Security:** Uses `.env` configuration to protect your API keys from being exposed.

---

## Prerequisites

Ensure you have the following installed on your system:
* **Python 3.10+**
* **pip** (Python package installer)
* A **Google Gemini API Key** (obtainable via [Google AI Studio](https://aistudio.google.com/))

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone <your-repository-url>
