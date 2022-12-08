"""
Script for creating online files from book manuscript
"""

from pathlib import Path
import re

# Relative path where to find the online book files
SOURCE_FILE_PATH = "./manuscript"

# Relative path of manuscript directory
MANUSCRIPT_PATH = "./manuscript2/"

# Parts to be replaced in online book files to create manuscript files
replacements = {
    "I>": "info",
    "T>": "tip",
    "W>": "warning",
    "E>": "warning",
    "Q>": "question",
}


def main():
    """Main function"""

    # Create manuscript directory if it doesn't already exist
    Path(MANUSCRIPT_PATH).mkdir(exist_ok=True)

    # Iterate on online book files
    source_dir = Path(SOURCE_FILE_PATH)
    for child in source_dir.iterdir():
        # Select only Markdown files without considering home page
        if child.suffix == ".md" and child.name != "index.md":
            manuscript_file_path = Path(MANUSCRIPT_PATH + child.name)

            # Replace Leanpub-specific Markdown syntax with mkdocs-specific syntax
            with child.open() as source_file, manuscript_file_path.open(
                mode="w", encoding="utf-8"
            ) as manuscript_file:
                manuscript_content = source_file.read()
                for src, target in replacements.items():
                    # Create a regular expression for matching each Leanpub admonition block
                    admonition_re = rf"{src} "
                    target_expr = f"!!! {target}\n\n    "
                    # Replace all instances of this block with a mkdocs-compatible block
                    manuscript_content = re.sub(
                        admonition_re, target_expr, manuscript_content
                    )
                manuscript_file.write(manuscript_content)


if __name__ == "__main__":
    main()
