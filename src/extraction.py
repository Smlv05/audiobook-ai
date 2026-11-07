import warnings
from dataclasses import dataclass

import ebooklib
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from ebooklib import epub

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)


@dataclass
class Chapter:
    title: str
    paragraphs: list[str]


def clean_text(text: str) -> str:
    return " ".join(text.split())


def is_chapter(title: str, paragraphs: list[str]) -> bool:
    if not paragraphs:
        return False
    if "project gutenberg" in title.lower():
        return False
    return True


def extract_chapters(epub_path: str) -> list[Chapter]:
    book = epub.read_epub(epub_path)
    chapters: list[Chapter] = []

    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_content(), "lxml")

        title_tag = soup.find(["h1", "h2", "h3"])
        title = clean_text(title_tag.get_text(" ", strip=True)) if title_tag else ""

        paragraphs = [clean_text(p.get_text()) for p in soup.find_all("p")]
        paragraphs = [p for p in paragraphs if p]

        if is_chapter(title, paragraphs):
            chapters.append(Chapter(title=title, paragraphs=paragraphs))

    return chapters