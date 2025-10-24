#!/bin/bash

# ================================
# Usage:
#   ./extract_audio_recursive.sh /path/to/source /path/to/output
#
# Example:
#   ./extract_audio_recursive.sh ~/videos ~/audio_mp3
#
# Requires: ffmpeg
# ================================

# Exit immediately if a command fails
set -e

# Input arguments
SRC_DIR="$1"
OUT_DIR="$2"

# Validate inputs
if [[ -z "$SRC_DIR" || -z "$OUT_DIR" ]]; then
  echo "Usage: $0 <source_dir> <output_dir>"
  exit 1
fi

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "Error: ffmpeg not found. Please install it first."
  exit 1
fi

echo "🎬 Source: $SRC_DIR"
echo "🎧 Output: $OUT_DIR"
echo

# Loop through all MP4 files recursively
find "$SRC_DIR" -type f -iname "*.mp4" | while IFS= read -r src_file; do
  # Get the relative path from source
  SRC_DIR_CLEAN="${SRC_DIR%/}"
  rel_path="${src_file#$SRC_DIR_CLEAN/}"

  # Replace .mp4 with .mp3
  rel_audio="${rel_path%.mp4}.mp3"


  # Construct output path
  out_file="$OUT_DIR/$rel_audio"

  # Create output directory if it doesn't exist
  mkdir -p "$(dirname "$out_file")"

  echo "🎵 Extracting: $rel_path"
  echo "allah $src_file"
  echo "syria $rel_audio"

  # Extract audio (high-quality MP3) - FIXED: removed bash -c and use direct ffmpeg call
  ffmpeg -i "$src_file" "$out_file"

  echo "✅ Saved: $rel_audio"
  echo
done

echo "✨ Done! All audio tracks exported to $OUT_DIR"