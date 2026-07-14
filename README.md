# AI Documentation Summarizer

A small Python tool that scrapes documentation from a URL and uses Google Gemini to produce a structured summary — including overall purpose, endpoints, methods, and other useful details.

## Features

- Fetches page content from any URL with `requests` and BeautifulSoup
- Sends the extracted text to Gemini for analysis
- Returns a structured summary focused on APIs and documentation usage

## Tech Stack

- Python 3
- `requests` + BeautifulSoup for scraping
- OpenAI-compatible client pointed at the Gemini API
- `python-dotenv` for API key management

## Setup

1. Clone the repo and create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
