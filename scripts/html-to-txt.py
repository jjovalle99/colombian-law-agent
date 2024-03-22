import argparse
import os
from typing import List

from bs4 import BeautifulSoup


def get_file_names(path: str) -> List[str]:
    """Fetch sorted list of HTML file names from provided directory path.

    Args:
        path: A string representing the directory path containing HTML files.

    Returns:
        A sorted list of HTML file names in the directory.

    Raises:
        FileNotFoundError: If no HTML files are found in the specified directory.
    """
    file_names = [file for file in os.listdir(path) if file.endswith(".html")]
    if not file_names:
        raise FileNotFoundError("No .html files found in the directory.")
    file_names = sorted(file_names, key=lambda x: int(x.split("_")[1].split(".")[0]))
    return file_names


def load_htmls_as_txt(path: str, file_names: List[str]) -> List[str]:
    """Load the content of HTML files as text, using BeautifulSoup.

    Args:
        path: Directory path containing HTML files.
        file_names: A list of file names to be loaded and parsed.

    Returns:
        A list of textual contents extracted from each HTML file.
    """
    texts = []
    for file in file_names:
        with open(os.path.join(path, file), "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            texts.append(soup.get_text())
    return texts


def clean_data(texts: List[str]) -> List[str]:
    """Clean extracted texts from HTML files.

    Args:
        texts: A list of strings representing extracted HTML contents.

    Returns:
        A list of cleaned strings.
    """
    cleaned_texts = []
    for text in texts:
        if texts.index(text) == 0:
            split_patern = "\nSiguiente"
        elif texts.index(text) == len(texts) - 1:
            split_patern = "\nAnterior"
        else:
            split_patern = "\nAnterior | Siguiente"

        split_text = text.split(split_patern)
        if len(split_text) != 3:
            raise ValueError(f"Unexpected split for element: {split_text}")
        cleaned_texts.append(split_text[1].strip())
    return cleaned_texts


def save_texts(cleaned_texts: List[str], output_path: str) -> None:
    """Save cleaned texts to provided output directory.

    Args:
        cleaned_texts: The cleaned text to be saved.
        output_path: Directory path for saving output files.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for i, text in enumerate(cleaned_texts, start=1):
        file_name = f"cleaned_output_{i}.txt"
        file_path = os.path.join(output_path, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Clean text data extracted from HTML files"
    )
    parser.add_argument(
        "--input_path",
        type=str,
        required=True,
        help="The directory where the input HTML files are stored.",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        required=True,
        help="The directory where to save the output text files.",
    )
    args = parser.parse_args()

    try:
        file_names = get_file_names(args.input_path)
        texts = load_htmls_as_txt(args.input_path, file_names)
        cleaned_texts = clean_data(texts)
        save_texts(cleaned_texts, args.output_path)
        print("Processing completed successfully.")
    except Exception as e:
        print(f"Error: {e}")
