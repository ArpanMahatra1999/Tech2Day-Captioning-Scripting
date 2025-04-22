# general libraries
import os
from dotenv import load_dotenv

# generative ai libraries
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# load environment variables
load_dotenv()


# generate script using product details
def generate_script(title, description):
    template = """
        Context: You are advertisement script writer for Instagram page "Tech2Day" for affiliate marketing of technology products.
        
        Write a short and catchy ad script for selling product below:
        Title: {title}
        Description: {description}
        
        Additional details:
        - Start script with announcement of title.
        - End the video script with attracting viewers to click link on Instagram page's bio.
        - Don't include emojis. Just include one person narration.
        - Tell audience to buy the product.
        - Use less than 1000 characters.
        - TELL STRICTLY LINK IS AVAILABLE IN BIO IN THE VERY END.
    """
    prompt = PromptTemplate(
        input_variables=["title", "description"],
        template=template
    )
    llm = ChatOpenAI(temperature=1.0, max_tokens=1024, model_name=os.getenv("OPENAI_MODEL_NAME"), openai_api_key=os.getenv('OPENAI_API_KEY'))
    chain = prompt | llm
    script = chain.invoke({
        "title": title,
        "description": description
    }).content
    script = script[1:] if script[0] == '"' else script
    script = script[:len(script) - 1] if script[-1] == '"' else script
    return script


# generate caption using product details
def generate_caption(title, description):
    template = """
        Context: You are Instagram page "Tech2Day" for affiliate marketing of technology products.
    
        Write an engaging Instagram post caption for selling product below:
        Title: {title}
        Description: {description}
        
        Additional details:
        - Generate title.
        - End the caption telling "Link is available in bio".
        - Also, tell users to follow @tech.2.day for more updates.
        - Separate paragraphs with 1 empty line.
        - Don't use a lot of emojis.
        - Use upto 10 hashtags.
        
        Respond in String format.
    """
    prompt = PromptTemplate(
        input_variables=["title", "authors", "description"],
        template=template
    )
    llm = ChatOpenAI(temperature=1.0, max_tokens=1024, model_name=os.getenv("OPENAI_MODEL_NAME"), openai_api_key=os.getenv('OPENAI_API_KEY'))
    chain = prompt | llm
    caption = chain.invoke({
            "title": title,
            "description": description
    }).content
    caption = caption[1:] if caption[0] == '"' else caption
    caption = caption[:len(caption)-1] if caption[-1] == '"' else caption
    return caption

