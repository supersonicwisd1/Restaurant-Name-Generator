from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os

os.environ['OPENAI_API_KEY'] = 'your api key'

llm = OpenAI(temperature=0.7)

def generate_res_name_item(cuisine):
    # Chain 1: Resturant Name
    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a resturant for {cuisine} food. Suggest a professional name for this"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='resturant_name')

    # Chain 2: Menu Items
    prompt_template_menu = PromptTemplate(
        input_variables = ['resturant_name'],
        template = "Generate menu item for {resturant_name}. Return in a comma separated list"
    )
    food_chain = LLMChain(llm=llm, prompt=prompt_template_menu, output_key='menu_items')

    chain = SequentialChain(
        chains = [name_chain, food_chain],
        input_variables = ['cuisine'],
        output_variables = ['resturant_name', 'menu_items']
    )

    response = chain({'cuisine':cuisine})

    return response

if __name__ == '__main__':
    print(generate_res_name_item("Nigeria"))
