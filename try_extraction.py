from src.extraction import extract_chapters

chapters = extract_chapters("data/books/alice.epub")

print(f"Chapters: {len(chapters)}")
for chapter in chapters:
    print(f"{len(chapter.paragraphs):4d} paragraphs | {chapter.title!r}")

print()
print(chapters[0].paragraphs[1])