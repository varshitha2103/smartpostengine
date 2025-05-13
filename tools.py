from langchain_core.tools import tool
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="mistral")

@tool
def generate_linkedin_carousel(text: str) -> str:
    """Generate a LinkedIn carousel script from input text"""
    prompt = f"""Write a 5-slide LinkedIn carousel script from this content:\n{text}"""
    response = llm.invoke(prompt)
    return response.content  # ✅ Only return the text

@tool
def generate_tweet_thread(text: str) -> str:
    """Generate a tweet thread (5–8 tweets) from input text"""
    prompt = f"""Create a 5-tweet thread for Twitter using this content:\n{text}"""
    response = llm.invoke(prompt)
    return response.content  # ✅ Only return the text

@tool
def generate_newsletter_intro(text: str) -> str:
    """Generate a newsletter intro from input text"""
    prompt = f"""Write a short, professional newsletter intro based on this:\n{text}"""
    response = llm.invoke(prompt)
    return response.content  # ✅ Only return the text



