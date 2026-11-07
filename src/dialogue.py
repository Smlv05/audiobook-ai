import re
from dataclasses import dataclass

OPEN_QUOTE = "“"
CLOSE_QUOTE = "”"

# an opening quote up to the closing quote, or up to the end of the paragraph
# if the quote is never closed
DIALOGUE_PATTERN = re.compile(r"“[^”]*(?:”|$)")


@dataclass
class Segment:
    text: str
    kind: str  # "narration" or "dialogue"


def add_segment(segments: list[Segment], text: str, kind: str) -> None:
    text = text.strip()
    if text:
        segments.append(Segment(text, kind))


def split_paragraph(paragraph: str, in_quote: bool = False) -> list[Segment]:
    segments: list[Segment] = []
    position = 0

    # the previous paragraph ended inside a quote and this one does not
    # start with a new opening quote: the beginning is still the same speech
    if in_quote and not paragraph.lstrip().startswith(OPEN_QUOTE):
        end = paragraph.find(CLOSE_QUOTE)
        if end == -1:
            add_segment(segments, paragraph, "dialogue")
            return segments
        add_segment(segments, paragraph[: end + 1], "dialogue")
        position = end + 1

    for match in DIALOGUE_PATTERN.finditer(paragraph, position):
        add_segment(segments, paragraph[position:match.start()], "narration")
        add_segment(segments, match.group(), "dialogue")
        position = match.end()

    add_segment(segments, paragraph[position:], "narration")
    return segments


def ends_in_open_quote(paragraph: str, in_quote: bool) -> bool:
    last_open = paragraph.rfind(OPEN_QUOTE)
    last_close = paragraph.rfind(CLOSE_QUOTE)
    if last_open == -1 and last_close == -1:
        return in_quote  # no quotes at all, the state does not change
    return last_open > last_close


def split_chapter(paragraphs: list[str]) -> list[list[Segment]]:
    result: list[list[Segment]] = []
    in_quote = False

    for paragraph in paragraphs:
        result.append(split_paragraph(paragraph, in_quote))
        in_quote = ends_in_open_quote(paragraph, in_quote)

    return result