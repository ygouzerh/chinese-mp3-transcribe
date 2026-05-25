# Transcribe MP3 files to formatted HSK exercise text
# Usage: just transcribe <folder_path> [parallelism]
# Example: just transcribe ~/Desktop/hsk3 8

transcribe folder parallelism="4":
    ./scripts/transcribe.sh "{{folder}}" "{{parallelism}}"

pdf folder:
    @cd "{{folder}}" && for prefix in $(printf '%s\n' *.txt | sed 's/-.*//' | sort -u); do \
        echo "Generating ${prefix}.pdf..."; \
        { for f in "${prefix}"-*.txt; do cat "$f"; printf '\f'; done; } \
            | paps --paper=a4 --font="Noto Sans CJK SC 11" | ps2pdf - "${prefix}.pdf"; \
    done; \
    echo "Generating: Done."
