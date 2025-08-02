#!/usr/bin/env bash
set -euo pipefail

folder_path="$1"
parallel_jobs="${2:-4}"

# Ensure the folder exists
if [ ! -d "$folder_path" ]; then
    echo "Error: Folder '$folder_path' does not exist" >&2
    exit 1
fi

# Create transcribe directory if it doesn't exist
mkdir -p transcribe

# Function to process individual files
process_file() {
    local basename="$1"
    local folder_path="$2"
    mp3_file="$folder_path/${basename}.mp3"
    output_file="transcribe/${basename}.txt"
    echo "Processing: $mp3_file -> $output_file" >&2
    uv run index.py "$mp3_file" > "$output_file"
    echo "Completed: ${basename}.txt" >&2
}

export -f process_file

# Process MP3 files with parallelization
find "$folder_path" -name "*.mp3" -print0 | \
xargs -0 -I {} basename {} .mp3 | \
awk '{if ($1 > 8) print $1}' | \
xargs -I {} -P "$parallel_jobs" bash -c 'process_file "$@"' _ {} "$folder_path"

echo "Transcription complete! Check the transcribe/ directory for results."