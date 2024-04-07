from dotenv import load_dotenv
import os
from anthropic import Anthropic
import time
import sys
from elevenlabs.client import ElevenLabs
from elevenlabs import play, Voice

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
anthropic_client = Anthropic(api_key=anthropic_api_key)

elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
elevenlabs_client = ElevenLabs(api_key=elevenlabs_api_key)


def get_voice_by_id(voice_id):
    return Voice(voice_id=voice_id)


def play_audio(text, voice):
    audio = elevenlabs_client.generate(text=text, voice=voice)
    play(audio)


def analyze_website(website_url):
    prompt = f"""
             You are Sir David Attenborough. Describe this website {website_url} as if it is a nature documentary.
             Make it snarky and funny. Don't repeat yourself. Make it short.
             Do not include sounds or onomatopoeia in your response. 
             If anything remotely interesting, make a big deal about it!
             Limit your response to 500 characters.
             """

    message = anthropic_client.messages.create(
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="claude-3-opus-20240229",
    )
    return message.content[0].text


def main(url):
    # TODO: To update to allow user to select voice
    # David - Old Male with British accent
    david_voice = "Ua3ZHvF0sPwuaOZZHv76"

    # Mr. Jackson - Old Male with Australian accent
    jackson_voice = "nQp7c21spalXjDuOlq3z"

    # Victoria - Middle-aged Female with British accent
    victoria_voice = "HoM0mKfY5thIcHNJUfmb"

    print("👀 Analyzing website...")
    analysis = analyze_website(url)

    print("🎙️ Narrator says:")
    print(analysis)

    play_audio(analysis, victoria_voice)

    # wait for 5 seconds
    time.sleep(5)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing url to analyze.")
    else:
        param = str(sys.argv[1])
        main(param)
