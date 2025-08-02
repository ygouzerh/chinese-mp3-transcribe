# Chinese Transcription Tool

A Python tool that transcribes Chinese audio files and formats them into HSK exercise materials with pinyin and English translations.

## Requirements

- Python 3.7+
- OpenAI API key
- `uv` package manager
- `openai` Python package

## Installation

1. Install the required package:
```bash
uv add openai
```

2. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

Basic usage:
```bash
uv run index.py path/to/your/audio.mp3
```

With custom model:
```bash
uv run index.py path/to/your/audio.mp3 --model gpt-4o-mini
```

### Command Line Arguments

- `mp3_file_path` (required): Path to the MP3 file to transcribe
- `--model` (optional): OpenAI model to use for processing (default: gpt-4o)

## Output Format

The tool generates structured output in the following format:

```
== Part number: ... ==

# Exercise number: ..
## Question number: 
- Pinyin: ... (with proper tones and capitalization)
- Simplified chinese: ...
- Translation in english
```

## Example

```bash
uv run index.py lesson1.mp3
```

Output:
```
== Part 1: Listening Comprehension ==

# Exercise 1: Daily Conversations
## Question 1: 
- Pinyin: Nǐ hǎo, nǐ jiào shén me míng zi?
- Simplified chinese: 你好，你叫什么名字？
- Translation in english: Hello, what is your name?
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.