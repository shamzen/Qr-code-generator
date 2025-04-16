# 🔷 Smart QR Generator

A smart Python-based QR code generator that handles both URLs and plain text inputs — but with a twist of logic: if you're entering plain text, it'll *demand* a title and description for context. No lazy QR codes here.

## 💡 Features

- ✅ Detects if input is a URL or plain text
- 🧠 Requires title and description for text (to prevent vague QR codes)
- 🖼️ Generates a clean PNG image (`qr_output.png`)
- 🧪 Simple, readable Python code (no web dependencies)
- 🐍 Works great in terminal environments, automation scripts, and backends

---

## 🚀 Usage

### 1. Install Dependencies

```bash
pip install qrcode[pil]


### 2. Run the Script
python qr_generator.py

    It will prompt you like:
    🔷 Smart QR Code Generator 🔷
            Enter a URL or text:


3. Output

The script will generate a file named qr_output.png in the same directory.

⚙️ Example:- 
URL input:

Enter a URL or text: https://example.com
✅ QR Code saved as qr_output.png

Plain Text input:

Enter a URL or text: Hello world
📝 Detected plain text input. Extra details required.
Enter a title: Greeting
Enter a description: A cheerful message
✅ QR Code saved as qr_output.png

🧠 Future Features (Optional Ideas):
 Add CLI flags (--url, --text, --title, --desc)

 Bulk QR generation from .csv or .json

 REST API version with Flask or FastAPI

 Save history/log of generated codes

 📁 File Info:-
 qr_generator.py – Main script

qr_output.png – Generated output file (overwrites each time)


👨‍💻 Author:-
Shivam raj  — Ethical Hacker, Bug Hunter, Creator of clever scripts and smarter tools.
📡 “In code we trust. In logic we demand.”

