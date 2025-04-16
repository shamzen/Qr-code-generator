import qrcode
import re
import sys

def is_url(text):
    url_pattern = re.compile(r'^(http|https)://[^\s]+$')
    return url_pattern.match(text) is not None

def generate_qr(data, filename="qr_output.png"):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

def main():
    print("🔷 Smart QR Code Generator 🔷")
    main_input = input("Enter a URL or text: ").strip()

    if not main_input:
        print("🛑 No input provided. Exiting.")
        sys.exit(1)

    if is_url(main_input):
        generate_qr(main_input)
    else:
        print("📝 Detected plain text input. Extra details required.")
        title = input("Enter a title: ").strip()
        desc = input("Enter a description: ").strip()

        if not title or not desc:
            print("⚠️ Both title and description are required for text input.")
            sys.exit(1)

        combined = f"Title: {title}\nDescription: {desc}\n\n{main_input}"
        generate_qr(combined)

if __name__ == "__main__":
    main()
