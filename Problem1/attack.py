import requests
import time

# URL of the vulnerable server (adjust if needed)
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
        print("Decrypt error:", data.get("error"), data.get("exception"))
        return None
    return data["decrypted"]

def reveal(candidate_hex):
    url = f"{BASE_URL}/reveal"
    response = requests.post(url, json={"pt": candidate_hex})
    return response.json()

def complement_bytes(hexstr):
    # Convert hex string to bytes, then compute bytewise complement.
    b = bytes.fromhex(hexstr)
    comp = bytes((~x & 0xFF) for x in b)
    return comp.hex()

def main():
    # Get the challenge ciphertext from the server.
    challenge_ct = get_challenge()
    print("Fetched challenge ciphertext:", challenge_ct)
    
    # We have at most 128 decryptions before the counter runs out.
    for attempt in range(1, 1281):
        print(f"\nAttempt {attempt}:")
        
        dec_hex = decrypt(challenge_ct)
        if dec_hex is None:
            continue
        
        print("Decrypted output:", dec_hex)
        
        # First, try the decrypted output directly.
        res = reveal(dec_hex)
        if "flag" in res:
            print("\n[+] Flag recovered (direct match)!")
            print("Flag:", res["flag"])
            return
        else:
            print("Direct reveal response:", res.get("error"))
        
        # Next, try the complement of the decrypted output.
        dec_comp = complement_bytes(dec_hex)
        print("Trying complement:", dec_comp)
        res_comp = reveal(dec_comp)
        if "flag" in res_comp:
            print("\n[+] Flag recovered via complement!")
            print("Flag:", res_comp["flag"])
            return
        else:
            print("Complement reveal response:", res_comp.get("error"))
        
        # Wait a short time (optional) before next attempt.
        time.sleep(0.1)
    
    print("\n[-] Failed to recover flag after 1280 attempts.")

if __name__ == "__main__":
    main()
