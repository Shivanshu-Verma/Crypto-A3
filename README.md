# Crypto-A3 Project

## Overview

This project is a cryptographic challenge involving a server-client architecture. The server provides a challenge ciphertext that the client must decrypt and reveal a hidden flag. The project uses Triple DES (3DES) encryption and decryption mechanisms.

## Project Structure

The project is organized into the following directories and files:

```
Crypto-A3/
├── Problem1/
│   ├── attack.py
│   ├── client.py
│   ├── server/
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   ├── docker-compose.yml
│   │   ├── problem_1.py
│   │   ├── requirements.txt
│   │   └── string.txt
└── README.md
```

### Files Description

- **attack.py**: Script to automate the attack on the server by fetching the challenge, decrypting it, and attempting to reveal the flag.
- **client.py**: Interactive client script to manually interact with the server's API endpoints.
- **server/**: Directory containing the server-side code and configuration files.
  - **Dockerfile**: Docker configuration to build the server image.
  - **app.py**: Flask application providing the API endpoints for the challenge.
  - **docker-compose.yml**: Docker Compose configuration to run the server.
  - **problem_1.py**: Core logic for the cryptographic challenge, including encryption and decryption functions.
  - **requirements.txt**: Python dependencies required for the server.
  - **string.txt**: File containing the secret string to be revealed.

## Server Setup

### Prerequisites

- Docker
- Docker Compose

### Steps to Run the Server

1. **Navigate to the server directory:**

   ```sh
   cd Crypto-A3/Problem1/server
   ```

2. **Build and run the server using Docker Compose:**

   ```sh
   docker-compose up --build
   ```

3. The server will be accessible at `http://localhost:5000`.

## API Endpoints

### `/challenge` [GET]

Fetches the challenge ciphertext.

**Response:**

```json
{
  "challenge": "<hex-encoded-ciphertext>"
}
```

### `/decrypt` [POST]

Decrypts the provided ciphertext.

**Request:**

```json
{
  "ct": "<hex-encoded-ciphertext>"
}
```

**Response:**

```json
{
  "decrypted": "<hex-encoded-plaintext>"
}
```

### `/reveal` [POST]

Reveals the hidden flag if the provided plaintext matches the challenge.

**Request:**

```json
{
  "pt": "<hex-encoded-plaintext>"
}
```

**Response:**

```json
{
  "flag": "<hidden-flag>"
}
```

## Client Usage

### Running the Client

1. **Navigate to the project directory:**

   ```sh
   cd Crypto-A3/Problem1
   ```

2. **Run the client script:**

   ```sh
   python client.py
   ```

3. **Follow the on-screen prompts to interact with the server.**

### Client Options

- **Fetch challenge**: Retrieves the challenge ciphertext from the server.
- **Decrypt**: Decrypts a provided ciphertext using the server's decryption endpoint.
- **Reveal Random String**: Attempts to reveal the hidden flag by providing a plaintext.

## Attack Script

### Running the Attack Script

1. **Navigate to the project directory:**

   ```sh
   cd Crypto-A3/Problem1
   ```

2. **Run the attack script:**

   ```sh
   python attack.py
   ```

3. The script will automate the process of fetching the challenge, decrypting it, and attempting to reveal the flag.

## Dependencies

- **Flask**: Web framework for the server.
- **Werkzeug**: WSGI utility library for the server.
- **pycryptodome**: Cryptographic library for encryption and decryption.

## Conclusion

This project demonstrates a cryptographic challenge using Triple DES encryption. The server provides a challenge ciphertext, and the client must decrypt it to reveal a hidden flag. The project includes both manual and automated approaches to solve the challenge.

For any questions or issues, please refer to the source code and comments within the scripts.
