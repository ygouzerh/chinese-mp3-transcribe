# Transcribe MP3 files to formatted HSK exercise text
# Usage: just transcribe <folder_path> [parallelism]
# Example: just transcribe ~/Desktop/hsk3 8

transcribe folder parallelism="4":
    ./scripts/transcribe.sh "{{folder}}" "{{parallelism}}"