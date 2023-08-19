from secret_key import open_ai_key
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain, LLMChain

os.environ['OPENAI_API_KEY'] = open_ai_key
llm = OpenAI(temperature=0.7)

def prompt_chain_response(cuisine):
    prompt_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for it."
    )
    name = LLMChain(llm=llm, prompt=prompt_name, output_key="restaurant_name")

    prompt_menu = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated list"""
    )
    menu = LLMChain(llm=llm, prompt=prompt_menu, output_key="menu_items")

    chain = SequentialChain(
        chains=[name, menu],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    res = chain({"cuisine": cuisine})
    clean_response = {k: v.replace("\n", "") for k,v in res.items()}

    return {
        'restaurant_name': clean_response['restaurant_name'],
        'menu_item': clean_response['menu_items']
    }
