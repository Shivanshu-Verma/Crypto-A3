import requests

BASE_URL = "http://localhost:5000"

def handle_response(response):
    try:
        data = response.json()
        if "error" in data:
            print("\nError:", data["error"])
        return data
    except Exception as e:
        print("Error:", e)
        return None

def fetch_challenge():
    response = requests.get(f"{BASE_URL}/challenge")
    data = handle_response(response)
    if data and "challenge" in data:
        print("\n[+] Challenge (hex):", data.get("challenge"))

def decrypt():
    ct = input("Enter ciphertext (hex): ").strip()
    payload = {"ct": ct}
    response = requests.post(f"{BASE_URL}/decrypt", json=payload)
    data = handle_response(response)
    if data and "decrypted" in data:
        print("\n[+] Decrypted output (hex):", data.get("decrypted"))

def reveal():
    pt = input("Enter plaintext (hex): ").strip()
    payload = {"pt": pt}
    response = requests.post(f"{BASE_URL}/reveal", json=payload)
    data = handle_response(response)
    if data and "flag" in data:
        print("\n[+] Revealed secret:", data.get("flag"))

def main():
    while True:
        print("\nChoose an API option:")
        print("1. Fetch challenge")
        print("2. Decrypt")
        print("3. Reveal Random String")
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            fetch_challenge()
        elif choice == "2":
            decrypt()
        elif choice == "3":
            reveal()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
