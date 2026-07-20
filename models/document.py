from dataclasses import dataclass, field, asdict

@dataclass
class Block:
    id: str
    type: str
    text: str = ""
    language: str | None = None
    children: list["Block"] = field(default_factory=list) #field() = 我要對這個欄位做額外設定。

    def to_dict(self):
        return asdict(self)


@dataclass
class Document:
    page_id: str
    title: str
    blocks: list[Block]

    def to_dict(self):
        return asdict(self)