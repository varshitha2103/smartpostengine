from tools import (
    generate_linkedin_carousel,
    generate_tweet_thread,
    generate_newsletter_intro
)

def run_tools(content: str):
    linkedin = generate_linkedin_carousel.run(content)
    twitter = generate_tweet_thread.run(content)
    newsletter = generate_newsletter_intro.run(content)

    return f"""### LinkedIn Carousel:
{linkedin}

### Tweet Thread:
{twitter}

### Newsletter Intro:
{newsletter}
"""
