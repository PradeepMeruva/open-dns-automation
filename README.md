# OpenDNS Automation Script

This project automates the process of blocking and unblocking domains on OpenDNS using Playwright. It securely manages sensitive information and provides an easy-to-use interface for non-Python developers.

---

## Features
- **Block Domains**: Automatically block a list of domains.
- **Unblock Domains**: Automatically unblock domains and reverse actions.
- **Secure Configuration**: Uses encrypted configuration files for sensitive information.
- **Cross-Platform**: Works on macOS, Windows, and Linux.

---

## Prerequisites
1. **Python**: Install Python 3.12 or higher. You can download it from [python.org](https://www.python.org/downloads/).
2. **Node.js**: Install Node.js (required for Playwright). Download it from [nodejs.org](https://nodejs.org/).
3. **Playwright Dependencies**: Install browser dependencies for Playwright:
   ```bash
   npx playwright install
   ```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd open-dns-automation
```

### 2. Create a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Sensitive Information
#### a. Create a `config.json` file:
```json
{
    "username": "your-opendns-username",
    "password": "your-opendns-password"
}
```

#### b. Encrypt the Configuration File:
Run the following script to encrypt the `config.json` file:
```bash
python encrypt_config.py
```
This will generate:
- `config.json.encrypted`: Encrypted configuration file.
- `key.key`: Encryption key file.

#### c. Add Domains to Block:
Create a `block_list.json` file:
```json
{
    "domains_to_block": [
        "discord.com",
        "padlet.com",
        "roblox.com",
        "example.com"
    ]
}
```

---

## Usage Instructions

### Run the Script
The script accepts a parameter to specify the action (`block` or `unblock`).

#### Block Domains:
```bash
python3 app.py block
```

#### Unblock Domains:
```bash
python3 app.py unblock
```

---

## Notes for Non-Python Developers
1. **Install Python**:
   - Follow the instructions on [python.org](https://www.python.org/downloads/) to install Python.
   - Ensure Python is added to your system's PATH.

2. **Install Node.js**:
   - Download and install Node.js from [nodejs.org](https://nodejs.org/).

3. **Run Commands**:
   - Open a terminal or command prompt and navigate to the project folder.
   - Use the provided commands to block or unblock domains.

---

## Security Notes
- **Do not share `key.key`**: The encryption key file should be kept private and excluded from version control.
- **Add Sensitive Files to `.gitignore`**:
   Ensure the following files are excluded from Git:
   ```
   key.key
   config.json.encrypted
   ```

---

## Troubleshooting
- **Playwright Errors**:
  If you encounter browser-related errors, ensure Playwright dependencies are installed:
  ```bash
  npx playwright install
  ```
- **Python Errors**:
  Ensure you are using Python 3.12 or higher.

- **Environment Issues**:
  If virtual environment activation fails, ensure you are using the correct command:
  - macOS/Linux:
    ```bash
    source env/bin/activate
    ```
  - Windows:
    ```bash
    env\Scripts\activate
    ```

---

## License
This project is licensed under the MIT License.
