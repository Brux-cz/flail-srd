#!/usr/bin/env python3
"""
Extract card data from FLAIL images and create CSV for translation.
Uses image filenames and basic image analysis to identify cards.
"""

import os
import csv
from pathlib import Path

# Directory with extracted images (relative to project root)
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
IMAGE_DIR = PROJECT_ROOT / "source/images"  # TODO: update path when images are added
OUTPUT_CSV = PROJECT_ROOT / "cards/cards_to_translate.csv"

def get_card_images():
    """Get list of images that are likely cards (from card-heavy pages)."""
    card_pages = list(range(104, 109)) + list(range(20, 44))  # Card-heavy pages

    images = []
    for img_path in IMAGE_DIR.glob("*.jpeg"):
        # Extract page number from filename
        name = img_path.name
        try:
            page_num = int(name.split("_page_")[1].split("_")[0])
            if page_num in card_pages:
                images.append(img_path)
        except (IndexError, ValueError):
            continue

    return sorted(images, key=lambda x: x.name)

def main():
    # Ensure output directory exists
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    # Get card images
    card_images = get_card_images()
    print(f"Found {len(card_images)} potential card images")

    # Create CSV with image paths for manual/AI translation
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['image_path', 'page', 'name_en', 'type', 'stats', 'effect_en', 'name_cz', 'effect_cz'])

        for img_path in card_images:
            name = img_path.name
            page_num = int(name.split("_page_")[1].split("_")[0])
            writer.writerow([str(img_path), page_num, '', '', '', '', '', ''])

    print(f"Created {OUTPUT_CSV} with {len(card_images)} entries")
    print("Next step: Use AI vision to extract card text from images")

if __name__ == "__main__":
    main()
