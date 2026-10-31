import importlib
import shutil
import sys

PACKAGES = [
    "ebooklib",
    "bs4",
    "lxml",
    "spacy",
    "pydub",
    "streamlit",
    "pandas",
    "sklearn",
    "matplotlib",
]


def main() -> None:
    print(f"Python: {sys.version.split()[0]}")
    failed = False

    for name in PACKAGES:
        try:
            importlib.import_module(name)
            print(f"[ok]   {name}")
        except ImportError:
            print(f"[FAIL] {name}")
            failed = True

    try:
        import spacy

        spacy.load("en_core_web_sm")
        print("[ok]   spaCy model en_core_web_sm")
    except Exception:
        print("[FAIL] spaCy model en_core_web_sm")
        failed = True

    if shutil.which("ffmpeg"):
        print("[ok]   ffmpeg")
    else:
        print("[FAIL] ffmpeg not found in PATH")
        failed = True

    print("\nEnvironment OK" if not failed else "\nSome checks failed")


if __name__ == "__main__":
    main()