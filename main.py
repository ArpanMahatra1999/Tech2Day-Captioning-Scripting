# general libraries
import os
import time
import requests
from dotenv import load_dotenv

# functions
from llm_functions import generate_script, generate_caption
from email_functions import send_email_with_attachments

# load environment variables
load_dotenv()

if __name__ == "__main__":
    response = requests.get(os.getenv("WEEKLY_TECHS"))
    techs = response.json()
    files = list()
    for tech in techs:
        script = generate_script(tech["title"], tech["description"])
        caption = generate_caption(tech["title"], tech["description"])
        files.append({
            "title": tech["title"],
            "weekday": tech["weekday"],
            "script": f"""Generate video for script: {script}.
                        Don't forget to tell in the end that ORDER YOUR COPY NOW! THE LINK IS AVAILABLE IN BIO.""",
            "caption": caption
        })
        time.sleep(30)
        print(f"{tech['title']} captioned and scripted...")
    send_email_with_attachments(files)