from src.dialogue import split_chapter
from src.extraction import extract_chapters

chapters = extract_chapters("data/books/alice.epub")
paragraphs = chapters[1].paragraphs[:15]

for segments in split_chapter(paragraphs):
    for segment in segments:
        print(f"[{segment.kind:9}] {segment.text}")
    print()