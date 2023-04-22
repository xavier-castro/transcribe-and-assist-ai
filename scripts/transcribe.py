import os
import sys

import openai

# https://www.youtube.com/watch?v=oStlkoJU-v8
openai.api_key = os.environ["OPENAI_API_KEY"]

video_id = sys.argv[1]
audio_file_path = os.path.join(os.getcwd(), "tmp", video_id + ".m4a")

audio_file = open(audio_file_path, "rb")
transcript = openai.Audio.transcribe(
    file=audio_file,
    model="whisper-1",
    response_format="srt",
    prompt="You are my social media manager taking notes of this video for me!",
)

print(transcript)
