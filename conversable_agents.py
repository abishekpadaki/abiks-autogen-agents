import os
import autogen
import pprint
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent

avi = ConversableAgent(
    "avi",
    system_message="Your name is Avi, and you love to argue. You add eggs into every meal 'cause you think that's the right way. Your conversation tone is a bit sarcastic and you have a Bangalore urban Kannada way of speaking.",
    llm_config={"config_list": [{"model": "gpt-4o-mini", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",
)

loh = ConversableAgent(
    "loh",
    system_message="Your name is Loh and you love arguing with your friend and judge them for doing weird things. You have a Bangalore urban Kannada way of speaking",
    llm_config={"config_list": [{"model": "gpt-4o-mini", "temperature": 0.7, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",
)

chat_result = loh.initiate_chat(avi, message="avi, why are you adding eggs to the lemon rice?", max_turns=3,summary_method="reflection_with_llm",
    summary_prompt="Summarize the conversation",)
pprint.pprint(chat_result.summary)
pprint.pprint(chat_result.cost)