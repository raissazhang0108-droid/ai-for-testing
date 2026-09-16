# parser.py

class MultiSourceParser:
    """
    负责把人类看的各种 PRD 或原型转换成大模型看得懂的纯文本（RAG 的输入层）
    """
    def parse_prd_word(self, file_path: str) -> str:
        # TODO: 编写读取 .docx 或 .pdf 文档的逻辑
        return "从Word中提取的纯文本"

    def parse_figma_nodes(self, file_id: str, token: str) -> str:
        # TODO: 调用 Figma API 获取节点图层，提取里面的 Text 文本
        return "从Figma原型图层中提取的交互文案"
