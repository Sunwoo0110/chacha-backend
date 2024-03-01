import os
import re
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, TransformChain, SequentialChain, SimpleSequentialChain, OpenAIModerationChain
from langchain.memory import ConversationBufferMemory, ChatMessageHistory
from langchain.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import OpenAI
import json
from dotenv import load_dotenv
# 성격 없는 프롬프트

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def get_memory(): # 대화 기록을 저장하는 메모리
    memory = ConversationBufferMemory(memory_key="chat_history", ai_prefix="bot", human_prefix="you")
    return memory

def get_search_chain(name, intro, set, line, situation): # 인격을 지정하기 위해 필요한 데이터를 가져오는 코드
    def get_data(input_variables):
        chat = input_variables["input"]
        return {"name": name, "intro": intro, "set": set, "line": line, "situation": situation}
    
    search_chain = TransformChain(input_variables=["input"], output_variables=["name", "intro", "set", "line", "situation"], transform=get_data)
    return search_chain

def get_current_memory_chain(): # 현재 대화 기록을 가져오는 코드
    def transform_memory_func(input_variables):
        current_chat_history = input_variables["chat_history"].split("\n")[-10:]
        current_chat_history = "\n".join(current_chat_history)
        return{"current_chat_history": current_chat_history}
    
    current_memory_chain = TransformChain(input_variables=["chat_history"], output_variables=["current_chat_history"], transform=transform_memory_func)
    return current_memory_chain

def get_chatgpt_chain(): # GPT-4를 사용하여 대화를 생성하는 코드
    llm = ChatOpenAI(model_name="gpt-4", openai_api_key=os.environ["OPENAI_API_KEY"])
    
    template = """ 너는 'you'가 말을 했을 때 'bot'이 대답하는 것처럼 대화를 해 줘.
    
    'bot'의 이름은 {name}
    'bot'은 이런 캐릭터야. {intro}
    'bot'은 이런 설정을 갖고 있어. 각 설정은 키워드나 짧은 문장으로 되어 있고, /로 구분되어 있으니까 참고해서 설정에 오류가 없도록 대화를 해 줘.
    설정: {set}
    'bot'의 대사를 보여 줄 테니까, 이걸 보고 'bot'의 말투와 비슷하게 말해. 각 문장은 /로 구분되어 있어.
    대사: {line}
    
    위에서 설명한 'bot'의 설정, 대사, 상황을 참고해서 'bot'의 말투로 'you'와 상황에 맞춰서 대화해 줘.
    다음 대화에서 'bot'이 할 것 같은 답변을 해 봐.
    1. 'bot'의 설정을 잘 반영해서 대답해야 돼. 없는 설정을 지어내면 안 돼.
    2. 자연스럽게 'bot'의 말투와 비슷하게, 주어진 상황에 맞춰서 대답해야 돼.
    3. 번역한 것 같은 말투, 기계적인 말투로 말하지 마.
    4. 'you'의 말을 이어서 만들지 말고, 'bot'의 말만 결과로 줘.
    5. 다섯 문장 이내로 짧게 대답해되, 'you'와 대화가 이어질 수 있도록 자연스럽게 말해 줘.
    6. 했던 말을 반복하거나, 앞뒤 문맥에 맞지 않는 말을 하지 마.
    7. 장애, 성차별, 폭력, 혐오, 성적인 내용을 포함한 대화는 하지 마. 윤리적이고 도덕적인 대화를 하도록 해.
    8. 대사를 똑같이 말하지 마. 말투만 참고해서 한국어 문법과 문맥에 맞는 말을 해 줘.
    9. 이전 대화에서 했던 말을 번복하지 마. 헷갈리게 말하지 말고 일관적인 태도를 취해.
    10. 'bot:'과 같은 이상한 출력을 하지 마. 필요한 답변만 생성해.
    
    이전 대화:
    {current_chat_history}
    you: {input}
    bot: 
    """
    
    prompt_template = PromptTemplate(input_variables=["input", "current_chat_history", "name", "set", "line", "situation"], template=template)
    chatgpt_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="output")
    
    return chatgpt_chain

def check_violent(text): # 욕필 함수
    file_path = os.path.join("..", "app/ai/badwords.json")
    absolute_file_path = os.path.abspath(file_path)
    with open(absolute_file_path, "r", encoding="utf-8") as f:
        json_data = f.read()
    violent_words = json.loads(json_data)
    
    for word in violent_words:
        if re.search(r'\b{}\b'.format(re.escape(word)), text, re.IGNORECASE):
            return True
    return False
            

class Custom2:
    def __init__(self, name, set, line, situation) -> None:
        self.memory = get_memory()
        self.search_chain = get_search_chain(name, set, line, situation)
        self.current_memory_chain = get_current_memory_chain()
        self.chatgpt_chain = get_chatgpt_chain()
        
        # self.overall_chain = SequentialChain(
        #     memory=self.memory,
        #     chains=[self.search_chain, self.current_memory_chain, self.chatgpt_chain],
        #     input_variables=["chat"],
        #     output_variables=["received_chat"],
        #     verbose=True
        # )
        
        self.history_for_chain = ChatMessageHistory() # 대화 내역을 기록하는 함수
        
        self.chain_with_message_history = RunnableWithMessageHistory(
            SequentialChain(
                memory=self.memory,
                chains=[self.search_chain, self.current_memory_chain, self.chatgpt_chain],
                input_variables=["input"],
                output_variables=["output"],
                verbose=True
            ),
            lambda session_id : self.history_for_chain,
            input_message_key = "input",
            history_messages_key="chat_history",
            )
    
    def receive_chat(self, chat, session_id):
        while True:
            response = self.chain_with_message_history.invoke({"input": chat}, {'configurable': {"session_id": session_id}})
            # print(self.history_for_chain.messages[session_id]) #메모리 잘 되는지 확인용
            if not check_violent(response["output"]):
                return response["output"]
            else:
                print("욕설이 포함된 대화입니다. 다시 생성 중...")
    