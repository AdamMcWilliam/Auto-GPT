import os

import praw

from dotenv import load_dotenv

load_dotenv()

def reddit_post(post_title, post_text, subreddit):
    reddit = praw.Reddit(
        client_id= os.environ.get("REDDIT_CLIENT_ID"),
        client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
        password=os.environ.get("REDDIT_PASSWORD"),
        user_agent = ("Karma-GPT by /u/reddit-karma-GPT"),
        username=os.environ.get("REDDIT_USERNAME"),
    )

    try:
        reddit.subreddit(subreddit).submit(post_title, selftext=post_text)
        print("Post sent successfully!")
    except Exception as e:
        print("Error sending post: {}".format(e))