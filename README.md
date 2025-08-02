# Chinese Transcription Tool

A Python tool that transcribes Chinese audio files and formats them into HSK exercise materials with pinyin and English translations.

## Requirements

- Python 3.7+
- OpenAI API key
- `uv` package manager
- `openai` Python package
- `just` command runner (for batch processing)

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

### Single File Transcription

Basic usage:
```bash
uv run index.py path/to/your/audio.mp3
```

With custom model:
```bash
uv run index.py path/to/your/audio.mp3 --model gpt-4o-mini
```

### Batch Transcription

For processing multiple MP3 files in a folder, use the batch transcription script:

```bash
just transcribe <folder_path> [parallelism]
```

Examples:
```bash
# Process all MP3 files in ~/Desktop/hsk3 with 4 parallel jobs (default)
just transcribe ~/Desktop/hsk3

# Process with 8 parallel jobs for faster processing
just transcribe ~/Desktop/hsk3 8
```

The batch script will:
- Process all MP3 files in the specified folder
- Only process files with names greater than 8 (filtering logic)
- Create a `transcribe/` directory with corresponding `.txt` output files
- Run multiple transcriptions in parallel for efficiency

### Command Line Arguments

#### Single File (`index.py`)
- `mp3_file_path` (required): Path to the MP3 file to transcribe
- `--model` (optional): OpenAI model to use for processing (default: gpt-4o)

#### Batch Processing (`just transcribe`)
- `folder_path` (required): Path to folder containing MP3 files
- `parallelism` (optional): Number of parallel jobs (default: 4)

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