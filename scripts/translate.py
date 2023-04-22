import os
import sys

import openai
import pysrt

openai.api_key = os.environ["OPENAI_API_KEY"]
input_data = sys.stdin.read()
subs = pysrt.from_string(input_data)

text_together = ""  # This will become all the text put together now
for sub in subs:
    sub.text = sub.text.replace("\n", " ")
    text_together += sub.text + " "


def generate_tweets(text_together):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # ... (Keep the system message)
            {"role": "assistant", "content": text_together},
            {
                "role": "user",
                "content": "Use the transcript to create a social media post to promote the podcast and its creators: Give me 3 tweets as an example",
            },
        ],
    )
    return response.choices[0].message.content


def identify_key_topics(text_together):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # ... (Keep the system message)
            {"role": "assistant", "content": text_together},
            {
                "role": "user",
                "content": "Identify key topics discussed in the podcast: Write this in bullet points.",
            },
        ],
    )
    return response.choices[0].message.content


def suggest_follow_up_topics(text_together):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # ... (Keep the system message)
            {"role": "assistant", "content": text_together},
            {
                "role": "user",
                "content": "Identify potential follow-up topics for the next episode: Write this in a list",
            },
        ],
    )
    return response.choices[0].message.content


def create_summary(text_together):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # ... (Keep the system message)
            {"role": "assistant", "content": text_together},
            {
                "role": "user",
                "content": "Create a concise summary of the transcript to highlight the podcast creators' expertise.",
            },
        ],
    )
    return response.choices[0].message.content


def generate_pitches(text_together):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # ... (Keep the system message)
            {"role": "assistant", "content": text_together},
            {
                "role": "user",
                "content": "Craft engaging social media posts to promote the podcast and its creators: Give me 3 pitches as an example",
            },
        ],
    )
    return response.choices[0].message.content


def combined_responses(text_together):
    tweets = generate_tweets(text_together)
    key_topics = identify_key_topics(text_together)
    follow_up_topics = suggest_follow_up_topics(text_together)
    summary = create_summary(text_together)
    pitches = generate_pitches(text_together)
    print(tweets, key_topics, follow_up_topics, summary, pitches, sep="\n\n")


combined_responses(text_together)
