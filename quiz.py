import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash" , api_key=os.getenv("GEMINI_APIKEY"))

def get(topic_):
    prompt_template = ChatPromptTemplate.from_messages([
        ('system', """You are a helpful assistance that help me in making Question, answers, and options
                    for the following topic, make sure there are atleast 3 questions along with
                    it's correct answers and 3 options for each each question."""),
        ('human',"{topic}")
    ])

    chain = prompt_template | model | StrOutputParser()
    result = chain.invoke({"topic":topic_})

    print(result)

    # return Response({"Message":result}, status=status.HTTP_200_OK)

topic= input("Enter a topic to generate a quiz based on that topic\n")

get(topic)