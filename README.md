# AI Audiobook Generator

Bachelor thesis project: automatic conversion of an EPUB book into an audiobook
using NLP-based dialogue detection and speaker classification
(Narrator / Male / Female / Child) and local text-to-speech.

## Setup (Windows)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m spacy download en_core_web_sm
winget install Gyan.FFmpeg
python check_env.py
```

## Books

Books are not stored in the repository. Download an English EPUB from
[Project Gutenberg](https://www.gutenberg.org) (choose "EPUB (no images)")
and put it into `data/books/`.

The demo scripts expect _Alice's Adventures in Wonderland_ saved as
`data/books/alice.epub`.

## Run

```powershell
streamlit run app.py
python try_extraction.py
python try_dialogue.py
```

## Tests

```powershell
python -m pytest -v
```

## Structure

- `src/` - pipeline modules (`extraction.py`, `dialogue.py`)
- `tests/` - unit tests
- `data/books/` - source books (not committed)
- `data/annotations/` - manually labeled dialogue for evaluation
- `experiments/` - evaluation scripts and results
- `thesis/` - thesis text
