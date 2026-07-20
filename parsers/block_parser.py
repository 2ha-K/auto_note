from models.document import Block
from parser.rich_text import rich_text_to_text


def parse_block(block: dict) -> Block:
    """
    將單一 Notion Block 轉成 Internal Block
    """

    block_type = block["type"]

    parser = BLOCK_PARSERS.get(block_type)

    if parser:
        result = parser(block)
    else:
        result = parse_unknown(block)

    # 遞迴解析 children
    if "children" in block:
        result.children = [
            parse_block(child)
            for child in block["children"]
        ]

    return result


# ------------------------
# Individual Parsers
# ------------------------

def parse_paragraph(block: dict) -> Block:
    data = block["paragraph"]

    return Block(
        id=block["id"],
        type="paragraph",
        text=rich_text_to_text(data["rich_text"]),
    )


def parse_heading(block: dict) -> Block:
    data = block[block["type"]]

    return Block(
        id=block["id"],
        type=block["type"],
        text=rich_text_to_text(data["rich_text"]),
    )


def parse_code(block: dict) -> Block:
    data = block["code"]

    return Block(
        id=block["id"],
        type="code",
        text=rich_text_to_text(data["rich_text"]),
        language=data["language"],
    )


def parse_bulleted(block: dict) -> Block:
    data = block["bulleted_list_item"]

    return Block(
        id=block["id"],
        type="bulleted_list_item",
        text=rich_text_to_text(data["rich_text"]),
    )


def parse_numbered(block: dict) -> Block:
    data = block["numbered_list_item"]

    return Block(
        id=block["id"],
        type="numbered_list_item",
        text=rich_text_to_text(data["rich_text"]),
    )


def parse_quote(block: dict) -> Block:
    data = block["quote"]

    return Block(
        id=block["id"],
        type="quote",
        text=rich_text_to_text(data["rich_text"]),
    )


def parse_callout(block: dict) -> Block:
    data = block["callout"]

    return Block(
        id=block["id"],
        type="callout",
        text=rich_text_to_text(data["rich_text"]),
    )


def parse_unknown(block: dict) -> Block:
    """
    尚未支援的 Block
    """

    return Block(
        id=block["id"],
        type=block["type"],
        text=""
    )


# ------------------------
# Registry
# ------------------------

BLOCK_PARSERS = {
    "paragraph": parse_paragraph,
    "heading_1": parse_heading,
    "heading_2": parse_heading,
    "heading_3": parse_heading,
    "code": parse_code,
    "bulleted_list_item": parse_bulleted,
    "numbered_list_item": parse_numbered,
    "quote": parse_quote,
    "callout": parse_callout,
}