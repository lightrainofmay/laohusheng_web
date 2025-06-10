import streamlit as st
import openai
import os

from openai import OpenAI

def _(zh, en, lang):
    return zh if lang == "中文" else en

def render(lang):
    st.header(_(
        "智能问答：关于老虎笙", 
        "Ask AI: About Tiger Sheng", 
        lang
    ))

    st.markdown(_(
        """
        我是一个基于大模型的问答助手，您可以问我任何关于老虎笙的问题，比如：
        - 老虎笙象征什么？
        - 老虎笙的起源？
        - 谁是“道人”？
        """,
        """
        You may ask questions like:
        - What does Tiger Sheng symbolize?
        - What is its origin?
        - Who is the Taoist leader?
        - What is the story behind the tiger roles?
        """,
        lang
    ))

    user_input = st.text_input(_(
        "请输入你的问题：", 
        "Type your question:", 
        lang
    ))

    if user_input:
        try:
            with open("assets/tiger_sheng_knowledge.txt", "r", encoding="utf-8") as f:
                knowledge_text = f.read()
        except FileNotFoundError:
            st.error("未找到知识文件：assets/tiger_sheng_knowledge.txt")
            return

        system_prompt = _(  
            "你是一个熟悉老虎笙的AI助手，请严格根据提供的资料回答问题，不要编造信息。如果找不到答案，就回答“暂时不知道，建议您对该问题进行进一步的调研或实地访谈。”",
            "You are an AI assistant knowledgeable about Tiger Sheng. Answer strictly based on the provided text. If you cannot find an answer, say: 'I don't know yet. Consider investigating this question further through fieldwork or interviews.'",
            lang
        )

        # 扩展关键词匹配列表
        related_keywords = [
            "老虎笙", "跳虎", "tiger sheng", "tiger", "老虎", "铜铃", "舞蹈", "起源", "象征", 
            "道人", "山神", "猫", "鼓手", "送虎", "倮倮", "节日", "虎首", "跳虎节"
        ]

        if any(kw in user_input.lower() for kw in related_keywords):
            try:
                client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"以下是老虎笙相关资料：\n\n{knowledge_text}\n\n基于上述内容回答问题：{user_input}"}
                    ],
                    temperature=0.4
                )
                answer = response.choices[0].message.content
                st.write(answer.strip())
            except Exception as e:
                st.error(f"调用 GPT 出错: {e}")
        else:
            st.warning(_(
                "我只能回答老虎笙相关问题。",
                "Sorry, I can only answer questions related to Tiger Sheng.",
                lang
            ))