import os
import re

def extract_head_and_body(html_content):
    """Extracts head and body content using regex (No dependencies)."""
    head_match = re.search(r"<head>(.*?)</head>", html_content, re.DOTALL | re.IGNORECASE)
    body_match = re.search(r"<body>(.*?)</body>", html_content, re.DOTALL | re.IGNORECASE)

    head_content = head_match.group(1) if head_match else ""
    body_content = body_match.group(1) if body_match else html_content  # Use full HTML if <body> is missing

    return head_content.strip(), body_content.strip()

def split_html_file(html_path, output_folder, num_splits=10):
    """Splits an HTML file into multiple smaller files without requiring external libraries."""
    print("Reading the HTML file...")
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    print("Extracting <head> and <body> content...")
    head_content, body_content = extract_head_and_body(html_content)

    # Split body content into smaller chunks
    body_elements = re.split(r"(?=<)", body_content)  # Splitting at each opening tag `<`
    total_elements = len(body_elements)

    if total_elements == 0:
        print("No valid content found in the HTML file.")
        return

    print(f"Total elements found: {total_elements}")
    chunk_size = total_elements // num_splits
    remainder = total_elements % num_splits

    os.makedirs(output_folder, exist_ok=True)

    start_index = 0
    for i in range(num_splits):
        print(f"Processing part {i+1}/{num_splits}...")
        end_index = start_index + chunk_size + (1 if i < remainder else 0)
        chunk = "".join(body_elements[start_index:end_index])
        start_index = end_index

        # Rebuild HTML with the extracted head and chunked body
        new_html_content = f"<html>\n<head>{head_content}</head>\n<body>{chunk}</body>\n</html>"

        chunk_html_path = os.path.join(output_folder, f'part_{i+1}.html')
        with open(chunk_html_path, 'w', encoding='utf-8') as chunk_file:
            chunk_file.write(new_html_content)

        print(f"Saved: {chunk_html_path}")

    print(f"Successfully split {html_path} into {num_splits} parts.")

if __name__ == "__main__":
    input_html = input("Enter the path to your HTML file: ")
    output_folder = input("Enter the output directory for HTML files: ")
    os.makedirs(output_folder, exist_ok=True)

    split_html_file(input_html, output_folder)
