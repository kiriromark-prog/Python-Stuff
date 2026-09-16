from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
# AI model for generating responses
# Remember to use a free model.
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
)
# Ask and you shall receive.
response = llm.invoke("is using AI to code bad?")

# I just found out it not only returns a whole fucking block of metadata which is unnessary.
# After further research, i wrote this block of code to filter out the metadata and only return the text content of the response.

if isinstance(response.content, list):
    print("".join(
        block["text"] for block in response.content
        if isinstance(block, dict) and block.get("type") == "text"
    ))
else:
    print(response.content)
    