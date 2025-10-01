# Developing with GPT and OSS Models
This is the repository for the LinkedIn Learning course "Developing with GPT and OSS Models". The full course is available from [LinkedIn Learning][lil-course-url].

![Developing with GPT and OSS Models][lil-thumbnail-url] 

This repository contains practical examples and implementations for building applications with GPT and open-source language models, including web applications, RAG (Retrieval Augmented Generation) systems, and local AI model integration.

## Project Contents
This repository includes several example applications:

- **`app.py`** - Flask web application with OpenAI-compatible API integration
- **`ai_web_app.py`** - Advanced AI web application
- **`rag_local.py`** - Local RAG (Retrieval Augmented Generation) implementation
- **`rag_logic.py`** - Core RAG processing logic
- **`openai_sdk.py`** - OpenAI SDK utilities and examples
- **`langchain_tools_import_patch.py`** - LangChain tools integration patches
- **Static files** - CSS and JavaScript for web interfaces
- **Templates** - HTML templates for Flask applications

## Prerequisites
To run these applications, you need:
- Python 3.10 or higher
- Ollama (for local model serving)
- A local AI model (e.g., GPT-OSS or similar)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd developing-with-gpt-oss-models-4168183
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv rag_venv
   # On Windows:
   rag_venv\Scripts\activate
   # On macOS/Linux:
   source rag_venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   # For RAG applications:
   pip install -r rag_requirements.txt
   ```

4. Install and start Ollama:
   - Download Ollama from [https://ollama.com](https://ollama.com)
   - Pull a compatible model (e.g., `ollama pull gpt-oss:20b`)
   - Start the Ollama server

## Usage
### Basic Web Application
```bash
python app.py
```
Navigate to `http://localhost:5000` to access the web interface.

### RAG Applications
```bash
python rag_local.py
```

### AI Web Application
```bash
python ai_web_app.py
```

## Configuration
The applications are configured to work with local Ollama endpoints by default. You can modify the base URL and API settings in the respective Python files to work with different AI service providers.


[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQG0eDHsyOSqTA/learning-public-crop_675_1200/B4EZVdqqdwHUAY-/0/1741033220778?e=2147483647&v=beta&t=FxUDo6FA8W8CiFROwqfZKL_mzQhYx9loYLfjN-LNjgA
