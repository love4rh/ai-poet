# from dotenv import load_dotenv
# .evn 파일 읽어서 환경 변수로 세팅하기
# load_dotenv()

import getpass
import os

from langchain.chat_models import init_chat_model

import streamlit as st


if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

model = init_chat_model("gpt-4o-mini", model_provider="openai")

st.title("인공지능 시인")
content = st.text_input("시의 주제를 제시해 주세요.")
st.write("시의 주제는 " + content)

if st.button("시 작성하기"):
  if content:
    with st.spinner("시를 작성하는 중입니다..."):
      # 모델에 요청 보내기
      # content + "에 대한 시를 작성해 주세요."
      result = model.invoke(content + "에 대한 시를 작성해 주세요.")
      st.write(result.content)
  else:
    st.write("시의 주제를 입력해 주세요.")

# result = model.invoke(content + "에 대한 시를 작성해 주세요.")
# print(result.content)

