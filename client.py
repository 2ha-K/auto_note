from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()

notion_client = None

def client_connect() -> None:
    global notion_client

    notion_client = Client(auth=os.getenv("NOTION_TOKEN"))

def get_page_block(page_id: str):
    blocks = notion_client.blocks.children.list(
        block_id=page_id
    )
    print(blocks)

client_connect()
get_page_block("3a3b82c9b09480d489b9debb7b8b8555")
