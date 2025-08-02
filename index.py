from openai import OpenAI
import sys
import argparse

client = OpenAI()

prompt_whisper = "以下是普通话录音，使用简体中文转录。包含北京话中的儿化音（如：这儿、哪儿、有点儿"

prompt_gpt_system = """You are a helpful assistant that transcripts Chinese audio to pinyin and translates HSK exercise materials. 

Format the output in the following structure:

== Part number: ... ==

# Exercise number: ..
## Question number: 
- Pinyin: ... (notes: Start by uppercase the sentence and lowercase for the rest of the words. Add the tones)
- Simplified chinese: ...
- Translation in english (do it yourself the translation)

Notes: Skip the intro and examples. Include erhua if it exists"""

prompt_gpt_user = "Here is the Chinese transcription to process: {transcription}"

parser = argparse.ArgumentParser(description="Transcribe Chinese audio to HSK exercise format")
parser.add_argument("mp3_file_path", help="Path to the MP3 file to transcribe")
parser.add_argument("--model", default="gpt-4o", help="OpenAI model to use for processing (default: gpt-4o)")

args = parser.parse_args()

mp3_file_path = args.mp3_file_path

print(f"Processing audio file: {mp3_file_path}", file=sys.stderr)

audio_file = open(mp3_file_path, "rb")

print("Transcribing audio with Whisper...", file=sys.stderr)
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    language="zh",
    response_format="text",
    prompt=prompt_whisper,
)

print("Processing transcription with GPT-4o...", file=sys.stderr)
# Add GPT-4o call to process the transcription
gpt_response = client.chat.completions.create(
    model=args.model,
    messages=[
        {
            "role": "system",
            "content": prompt_gpt_system
        },
        {
            "role": "user", 
            "content": prompt_gpt_user.format(transcription=transcription)
        }
    ]
)

print("Formatting complete!", file=sys.stderr)
print(gpt_response.choices[0].message.content)