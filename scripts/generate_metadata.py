import argparse
import json
import os
import re
from typing import Dict


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Generate metadata JSON for .txt files in a folder.")
    parser.add_argument("folder", type=str, help="Path to the folder containing .txt files")
    parser.add_argument("initial_source", type=str, help="The HTML source path for the first .txt file")
    return parser.parse_args()


def generate_metadata(folder: str, initial_source: str) -> Dict[str, str]:
    """
    Generate metadata for .txt files in the specified folder.

    Args:
        folder (str): Path to the folder containing .txt files.
        initial_source (str): The HTML source path for the first .txt file.

    Returns:
        Dict[str, str]: A dictionary mapping .txt file names to their corresponding source URLs.
    """
    metadata = {}
    # Get a sorted list of .txt files based on the numeric part of the file name
    txt_files = sorted(
        [f for f in os.listdir(folder) if f.endswith(".txt")], key=lambda x: int(re.search(r"\d+", x).group())
    )

    for i, file in enumerate(txt_files, start=1):
        # Assuming the source URL structure changes by appending "_prXXX" before the file extension
        if i == 1:
            source_url = initial_source
        else:
            base_url, ext = os.path.splitext(initial_source)
            source_url = f"{base_url}_pr{str(i-1).zfill(3)}{ext}"

        metadata[file] = source_url

    return metadata


def save_metadata(metadata: Dict[str, str], output_file: str = "metadata.json") -> None:
    """
    Save the generated metadata to a JSON file.

    Args:
        metadata (Dict[str, str]): A dictionary mapping .txt file names to their corresponding source URLs.
        output_file (str, optional): The path to the output JSON file. Defaults to "metadata.json".
    """
    with open(output_file, "w") as f:
        json.dump(metadata, f, indent=4)
    print(f"Metadata saved to {output_file}")


def main() -> None:
    """
    Main function to parse arguments, generate metadata, and save it to a JSON file.
    """
    args = parse_arguments()
    metadata = generate_metadata(args.folder, args.initial_source)
    save_metadata(metadata, output_file=os.path.join(args.folder, "metadata.json"))


if __name__ == "__main__":
    main()
