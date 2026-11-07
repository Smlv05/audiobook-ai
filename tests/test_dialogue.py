from src.dialogue import Segment, split_chapter, split_paragraph

def test_pure_narration():
    result = split_paragraph("Anna entered the room.")
    assert result == [Segment("Anna entered the room.", "narration")]


def test_pure_dialogue():
    result = split_paragraph("“Where are you going?”")
    assert result == [Segment("“Where are you going?”", "dialogue")]


def test_dialogue_then_attribution():
    result = split_paragraph("“Where are you going?” asked Anna.")
    assert result == [
        Segment("“Where are you going?”", "dialogue"),
        Segment("asked Anna.", "narration"),
    ]


def test_split_dialogue():
    result = split_paragraph("“Hello,” she said, “how are you?”")
    assert result == [
        Segment("“Hello,”", "dialogue"),
        Segment("she said,", "narration"),
        Segment("“how are you?”", "dialogue"),
    ]


def test_nested_single_quotes():
    result = split_paragraph("“She said ‘no’ to me,” he replied.")
    assert result == [
        Segment("“She said ‘no’ to me,”", "dialogue"),
        Segment("he replied.", "narration"),
    ]


def test_empty_paragraph():
    assert split_paragraph("") == []

def test_unclosed_quote_at_end():
    result = split_paragraph("She thought; “and how funny it’ll seem!")
    assert result == [
        Segment("She thought;", "narration"),
        Segment("“and how funny it’ll seem!", "dialogue"),
    ]


def test_continuation_without_opening_quote():
    result = split_paragraph("Oh dear, what nonsense I’m talking!”", in_quote=True)
    assert result == [Segment("Oh dear, what nonsense I’m talking!”", "dialogue")]


def test_continuation_with_opening_quote():
    result = split_paragraph("“And how odd it looks,” she said.", in_quote=True)
    assert result == [
        Segment("“And how odd it looks,”", "dialogue"),
        Segment("she said.", "narration"),
    ]


def test_split_chapter_carries_open_quote():
    result = split_chapter(["“First part,” he said, “and then", "the rest of it.” He left."])
    assert result[1] == [
        Segment("the rest of it.”", "dialogue"),
        Segment("He left.", "narration"),
    ]