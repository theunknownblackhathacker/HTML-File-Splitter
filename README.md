HTML File Splitter 📝
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This simple Python script helps you split a large HTML file into smaller parts while keeping the `<head>` section intact. It's perfect if you have a big webpage and want to break it into smaller, more manageable pieces.

📌 What This Script Does
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
✅ Reads an HTML file from your computer  
✅ Extracts the `<head>` section (keeps it the same in all parts)  
✅ Splits the `<body>` content into smaller parts  
✅ Saves the smaller parts as new HTML files in a folder  
No extra software or libraries needed—just plain Python! 🐍💡

🛠️ How to Use It:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1️⃣ Install Python (if you don’t have it).

Make sure you have Python 3 installed. You can check by opening a terminal or command prompt and typing:

python --version

or

python3 --version

If Python isn’t installed, download it from python.org and install it.

2️⃣ Open a Command Prompt (Windows) or Terminal (Mac/Linux) and navigate to the folder where you saved the script. Then, run:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sh python split_html.py

or (on some systems):

sh python3 split_html.py

3️⃣ Follow the Prompts
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Enter the path to your HTML file

Example: Enter the path to your HTML file: my_large_file.html

Enter the folder where you want to save the smaller files

Example: Enter the output directory for HTML files: output

The script will split the file and save smaller pieces in the output folder.

📂 Example Output Files
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
If you split my_large_file.html, the script will create files like this inside the output folder:

output/

├── part_1.html

├── part_2.html

├── part_3.html

...

Each file will have the same <head> content and a portion of the <body>.

⚙️ Customization
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
By default, the script splits into 10 parts. To change this, edit the line:

### def split_html_file(html_path, output_folder, num_splits=10):

Change 10 to your preferred number of parts.

❓ Troubleshooting
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
If you get "File not found", double-check the file path you entered.
If the script doesn’t run, try using python3 instead of python.
Make sure your HTML file has a <body> section for best results.

🎉 Congratulations!
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
You have successfully split your HTML file into smaller parts. 🚀

If you found this helpful, you can star it!😁💻✨

