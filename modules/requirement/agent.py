# agent.py
import json
from openai import OpenAI
from .prompt_templates import REQUIREMENT_REVIEW_PROMPT

class RequirementAgent:
    def __init__(self, client: OpenAI, model: str = "deepseek-chat"):
        self.client = client
        self.model = model

    def analyze_requirement(self, raw_text: str) -> dict:
        """
        调用大模型对需求进行智能化评审和结构化拆解
        """
        # 组装格式化提示词
        formatted_prompt = REQUIREMENT_REVIEW_PROMPT.format(raw_requirement_text=raw_text)
        
        # 调用大模型基座
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a professional QA Architect specializing in AI4SE."},
                {"role": "user", "content": formatted_prompt}
            ],
            temperature=0.1 # 测试场景通常要求低幻觉，保持稳定性
        )
        
        result_text = response.choices[0].message.content.strip()
        
        # 鲁棒性防御：解析大模型返回的 JSON
        try:
            return json.loads(result_text)
        except json.JSONDecodeError:
            # 实际工程中这里需要做重试或修复，展示你的异常兜底思维
            return {"error": "LLM output is not a valid JSON", "raw_output": result_text}
