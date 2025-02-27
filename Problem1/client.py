import requests

BASE_URL = "http://localhost:5000"

def fetch_challenge():
    try:
        response = requests.get(f"{BASE_URL}/challenge")
        response.raise_for_status()
        data = response.json()
        print("\n[+] Challenge (hex):", data.get("challenge"))
    except Exception as e:
        print("Error fetching challenge:", e)

def decrypt():
    ct = input("Enter ciphertext (hex): ").strip()
    try:
        payload = {"ct": ct}
        response = requests.post(f"{BASE_URL}/decrypt", json=payload)
        response.raise_for_status()
        data = response.json()
        print("\n[+] Decrypted output (hex):", data.get("decrypted"))
    except Exception as e:
        print("Error during decryption:", e)

def reveal():
    pt = input("Enter plaintext (hex): ").strip()
    try:
        payload = {"pt": pt}
        response = requests.post(f"{BASE_URL}/reveal", json=payload)
        response.raise_for_status()
        data = response.json()
        print("\n[+] Revealed secret:", data.get("flag"))
    except Exception as e:
        print("Error revealing the secret string:", e)

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
