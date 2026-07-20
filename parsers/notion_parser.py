from models.document import Document
from parsers.block_parser import parse_block


def parse_document(page_id: str, title: str, notion_blocks: list) -> Document:
    """
    將 Notion 回傳的 Block JSON
    轉成 Internal Document
    """

    blocks = []

    for block in notion_blocks:
        blocks.append(parse_block(block))

    return Document(
        page_id=page_id,
        title=title,
        blocks=blocks,
    )