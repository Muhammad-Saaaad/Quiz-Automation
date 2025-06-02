import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash" , api_key=os.getenv("GEMINI_APIKEY"))

class QuizGenerator(APIView):

    def get(self, request):
        if "topic" in request.data:

            prompt_template = ChatPromptTemplate.from_messages([
                ('system', """You are a helpful assistance that help me in making Question, answers, and options
                            for the following topic, make sure there are atleast 3 questions along with
                            it's correct answers and 3 options for each each question."""),
                ('human',"{topic}")
            ])

            chain = prompt_template | model | StrOutputParser()
            result = chain.invoke({"topic":request.data['topic']})

            print(result)

            return Response({"Message":result}, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"no query entered my user"}, status=status.HTTP_400_BAD_REQUEST)


