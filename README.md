# AI Story Generator

This project consists of a Flask backend API that uses Google's Gemini AI model to generate stories, paired with a Streamlit frontend for user interaction.

## Project Structure

- `backend.py` - Flask backend API
- `app.py` - Streamlit frontend application
- `requirements.txt` - Required dependencies
- `.env` - Environment variables (you need to create this)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Shahood-Sajid/AI-Story-Generator.git
cd AI-Story-Generator
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a .env file

Create a `.env` file in the project root with your Google Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

You can get a Gemini API key from [Google AI Studio](https://ai.google.dev/).

## Running the Application

### 1. Start the Flask backend

In one terminal:

```bash
python backend.py
```

The Flask backend will run on http://localhost:5000

### 2. Start the Streamlit frontend

In another terminal:

```bash
streamlit run app.py
```

The Streamlit interface will typically open automatically in your browser at http://localhost:8501

## Usage

1. Enter your story requirements in the text area
2. Adjust advanced options if desired
3. Click "Generate Story" button
4. View your generated story and download it if you want

## Features

- ✨ Creative story generation based on user input
- 📏 Adjustable story length and genre selection
- 📥 Download generated stories as markdown files
- 🎨 Clean, user-friendly interface

## Troubleshooting

- Ensure both the Flask backend and Streamlit frontend are running simultaneously
- Check that your Gemini API key is valid and has access to the gemini-2.0-flash model
- Verify that the ports (5000 for Flask, 8501 for Streamlit) are not in use by other applications

## Extensions and Future Improvements

- Add user authentication
- Save story history
- Add image generation for story scenes