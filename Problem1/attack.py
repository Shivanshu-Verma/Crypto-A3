import requests
import time

# Change this to your server's URL if needed.
BASE_URL = "http://localhost:5000"

def get_challenge():
    url = f"{BASE_URL}/challenge"
    response = requests.get(url)
    data = response.json()
    if "challenge" not in data:
        raise Exception("Failed to fetch challenge: " + data.get("error", "Unknown error"))
    return data["challenge"]

def decrypt(ciphertext_hex):
    url = f"{BASE_URL}/decrypt"
    response = requests.post(url, json={"ct": ciphertext_hex})
    data = response.json()
    if "decrypted" not in data:
        # Print error details if available.
        print("Decrypt error:", data.get("error"), data.get("exception"))
        return None
    return data["decrypted"]

def reveal(plaintext_hex):
    url = f"{BASE_URL}/reveal"
    response = requests.post(url, json={"pt": plaintext_hex})
    return response.json()

def main():
    # Get the challenge ciphertext (encrypted using the original key).
    challenge_ciphertext = get_challenge()
    print("Fetched challenge ciphertext:", challenge_ciphertext)
    
    # We'll try up to 128 attempts (due to the counter limit)
    for attempt in range(1, 129):
        print(f"\nAttempt {attempt}:")
        
        # Get a decrypted result using the altered key.
        dec_hex = decrypt(challenge_ciphertext)
        if dec_hex is None:
            # If error in decryption, skip this round.
            continue
        print("Decrypted output:", dec_hex)
        
        # Send the decrypted output to the reveal endpoint.
        reveal_response = reveal(dec_hex)
        if "flag" in reveal_response:
            print("\n[+] Flag recovered!")
            print("Flag:", reveal_response["flag"])
            return
        else:
            # The reveal endpoint returns an error message if the plaintext is not the challenge.
            print("Reveal response:", reveal_response.get("error"))
        
        # Optionally wait a short time before next attempt.
        time.sleep(0.1)
    
    print("\n[-] Failed to recover flag after 128 attempts.")

if __name__ == "__main__":
    main()
