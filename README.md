\# AI Audiobook Generator



Bachelor thesis project: automatic conversion of an EPUB book into an audiobook

using NLP-based dialogue detection and speaker classification

(Narrator / Male / Female / Child) and local text-to-speech.



\## Setup (Windows)



```powershell

python -m venv .venv

.venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

python -m spacy download en\_core\_web\_sm

winget install Gyan.FFmpeg

python check\_env.py

```



\## Run



```powershell

streamlit run app.py

```



\## Structure



\- `src/` - pipeline modules

\- `data/books/` - source books (not committed)

\- `data/annotations/` - manually labeled dialogue for evaluation

\- `experiments/` - evaluation scripts and results

\- `thesis/` - thesis text

