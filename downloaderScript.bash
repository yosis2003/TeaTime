#!/bin/bash

KEYWORD_FILE="keywords.txt"
OUTPUT_DIR="~/Videos/project"
VIDEOS_PER_KEYWORD=10
FORMAT="mp4"

mkdir -p "$OUTPUT_DIR"

# Make sure GNU parallel is installed
if ! command -v parallel &>/dev/null; then
    echo "❌ GNU Parallel not found. Please install it with: sudo apt install parallel -y"
    exit 1
fi

export OUTPUT_DIR VIDEOS_PER_KEYWORD FORMAT

download_keyword() {
    keyword="$1"
    [[ -z "$keyword" ]] && exit 0
    safe=$(echo "$keyword" | tr ' ' '_' | tr -cd '[:alnum:]_')
    mkdir -p "$OUTPUT_DIR/$safe"
    echo "🎯 Downloading for: $keyword"
    yt-dlp \
        "ytsearch${VIDEOS_PER_KEYWORD}:${keyword}" \
        -f "$FORMAT" \
        -o "${OUTPUT_DIR}/${safe}/%(title)s.%(ext)s" \
        --ignore-errors \
        --no-warnings \
        --add-header "User-Agent: Mozilla/5.0"
}

export -f download_keyword

# Run 4 parallel jobs (tweak -j to your liking)
parallel -j 4 --line-buffer download_keyword :::: "$KEYWORD_FILE"

echo "✅ All downloads complete!"
