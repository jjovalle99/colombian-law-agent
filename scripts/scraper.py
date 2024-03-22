import argparse
import asyncio
import os
from typing import List

from dotenv import load_dotenv
from playwright.async_api import Browser, async_playwright

load_dotenv()


async def fetch_page_content(browser: Browser, url: str) -> str:
    """Fetches the HTML content of a page by URL.

    Args:
        browser: The Playwright browser object.
        url: The URL of the page to fetch.

    Returns:
        The HTML content of the page as a string.
    """
    # Create a new browser context and page instance.
    context = await browser.new_context()
    page = await context.new_page()
    # Navigate to the given URL, waiting until page's content is fully loaded.
    await page.goto(url, wait_until="domcontentloaded")

    # Query all elements matching the specified selector.
    links = await page.query_selector_all(".caja_vja_encabezado")
    print(f"Found {len(links)} links in {url}")

    # Iterate over the found links, clicking on every 10th link.
    for link in links:
        await link.click()

    # Retrieve the full HTML content of the page.
    content = await page.content()
    await context.close()  # Close the browser context.
    return content


async def write_content_to_file(file_name: str, content: str) -> None:
    """Writes the content to an HTML file.

    Args:
        file_name: The name of the file where the content will be written.
        content: The content to write into the file.
    """
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)


async def process_url(browser: Browser, url: str, idx: int, output_path: str) -> None:
    """Processes each URL: fetches content and writes it to a file.

    Args:
        browser: The Playwright browser object.
        url: The URL to process.
        idx: The index of the URL, used for file naming.
        output_path: The path where the output files will be saved.
    """
    print(f"Processing URL {idx}: {url}")
    content = await fetch_page_content(browser, url)
    await write_content_to_file(
        os.path.join(output_path, f"output_{idx}.html"), content
    )


async def main(urls: List[str], output_path: str) -> None:
    """The main function to set up the browser and process the URLs.

    Args:
        urls: A list of URLs to process.
        output_path: The path where the output files will be saved.
    """
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(
            f"wss://chrome.browserless.io?token={os.getenv('BROWSERLESS_API_KEY')}"
        )
        # Create a list of tasks, one for each URL to process.
        tasks = [
            process_url(browser, url, idx, output_path)
            for idx, url in enumerate(urls, start=1)
        ]
        # Execute all tasks concurrently.
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch content from webpages and save as HTML files."
    )
    parser.add_argument(
        "--output_path",
        type=str,
        required=True,
        help="The directory where to save the output HTML files.",
    )
    parser.add_argument(
        "--webpage",
        action="append",
        required=True,
        help="The webpage URL(s) to fetch. Can be specified multiple times.",
    )

    args = parser.parse_args()
    asyncio.run(main(args.webpage, args.output_path))
