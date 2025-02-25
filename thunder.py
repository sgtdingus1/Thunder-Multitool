print('Installing libraries... ')
import requests
import random
import string
import time
import os
import platform
import socket
import subprocess
import psutil
import speedtest
from cryptography.fernet import Fernet

# Banner
banner = '''
                          ████████╗██╗  ██╗██╗   ██╗███╗   ██╗██████╗ ███████╗██████╗
                          ╚══██╔══╝██║  ██║██║   ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
                             ██║   ███████║██║   ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
                             ██║   ██╔══██║██║   ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
                             ██║   ██║  ██║╚██████╔╝██║ ╚████║██████╔╝███████╗██║  ██║
                             ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                                                  thunder.py        
'''

# Menu Options
options = '''
                       ╔════════════════════════════════════════════════════════════════╗
                       ║       -Discord Tools-         ║        -System Tools-          ║
                       ║ [1.1]  Webhook Spammer        ║  [2.1]  System Information     ║
                       ║ [1.2]  Webhook Killer         ║  [2.2]  IP Address             ║
                       ║ [1.3]  Self Spammer           ║  [2.3]  Ping A Website         ║
                       ║ [1.4]  Mass React             ║  [2.4]  Current Processes      ║
                       ║ [1.5]  Nitro Generator        ║  [2.5]  Network Speed Finder   ║
                       ╚══════════════════════════════╗ ╔═══════════════════════════════╝
                                          ╔═══════════╝ ╚═════════════╗
                                          ║       -Encryption-        ║
                                          ║ [3.1] Generate Key        ║
                                          ║ [3.2] Encrypt             ║
                                          ║ [3.3] Decrypt             ║
                                          ╚═══════════════════════════╝
                                                  [E/e] Exit'''

# Utility Functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def confirm_action(prompt):
    print(f"\n{prompt}")
    confirmation = input("      Are you sure? (Y/N): ").strip().lower()
    return confirmation == 'y'

def print_header(title):
    clear_screen()
    print(banner)
    print(f"\n      {'=' * 50}")
    print(f"{title.upper():^50}")
    print(f"      {'=' * 50}\n")

# Discord Tools
def webhook_spammer():
    print_header("Webhook Spammer")
    webhook_url = input("      Webhook URL: ").strip()
    message = input("      Message: ").strip()
    try:
        amount = int(input("      Message count: ").strip())
        delay = float(input("      Delay (seconds): ").strip())
    except ValueError:
        print("\n      Invalid input. Please enter numbers for amount and delay.")
        input("      Press Enter to return to the menu...")
        return

    print(f"\n      Webhook URL: {webhook_url}")
    print(f"      Message: {message}")
    print(f"      Amount: {amount}")
    print(f"      Delay: {delay}")

    if confirm_action("      You are about to start spamming the webhook."):
        for _ in range(amount):
            try:
                response = requests.post(webhook_url, json={'content': message})
                if response.status_code == 204:
                    print(f"      Sent message: {message}")
                else:
                    print(f"      Failed to send message. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"      Error: {e}")
            time.sleep(delay)
    else:
        print("\n      Action canceled.")
    input("\n      Press Enter to return to the menu...")

def webhook_deleter():
    print_header("Webhook Killer")
    webhook_url = input("      Webhook URL: ").strip()
    print(f"\n      Webhook URL: {webhook_url}")

    if confirm_action("      You are about to delete this webhook."):
        try:
            response = requests.delete(webhook_url)
            if response.status_code == 204:
                print("\n      Webhook deleted successfully.")
            else:
                print(f"\n      Failed to delete the webhook. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"\n      Error: {e}")
    else:
        print("\n      Action canceled.")
    input("\n      Press Enter to return to the menu...")

def message_spam():
    print_header("Self Spam")
    channel_id = input("      Channel ID: ").strip()
    token = input("      Token: ").strip()
    message = input("      Message: ").strip()

    try:
        amount = int(input("      Amount Of Messages: ").strip())
        delay = float(input("      Delay (in seconds): ").strip())
    except ValueError:
        print("\n      Invalid input. Please enter numbers for amount and delay.")
        input("      Press Enter to return to the menu...")
        return

    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,da;q=0.8",
        "Authorization": f"Bearer {token}",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://discord.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": f"https://discord.com/channels/@me/{channel_id}",
        "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-discord-timezone": "America/Chicago",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjM3MDUzMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

    payload = {
        "mobile_network_type": "unknown",
        "content": message,
        "nonce": str(int(time.time() * 1000)), 
        "tts": False,
        "flags": 0
    }

    for _ in range(amount):
        try:
            # Send the message
            response = requests.post(url, headers=headers, json=payload)

            # Handle response
            if response.status_code == 200 or response.status_code == 201:
                print(f"      Message sent successfully: {message}")
            elif response.status_code == 429:  # Rate limited
                retry_after = float(response.headers.get('Retry-After', 5))
                print(f"      Rate limited, trying again in {retry_after} seconds...")
                time.sleep(retry_after)  # Wait for retry time
                continue  # Retry the same message
            else:
                print(f"      Error: {response.status_code} - {response.text}")
                break  # Exit the loop on error
        except requests.exceptions.RequestException as e:
            print(f"      Request failed: {e}")
            break  # Exit the loop on exception

        time.sleep(delay)  # Apply delay between messages

    input("\n      Press Enter to return to the menu...")

def reaction_spam():
    print_header("Mass React")
    channel_id = input("      Channel ID: ").strip()
    token = input("      Token: ").strip()
    emoji = input("      Emoji (e.g., 🔥 or :fire:): ").strip()
    limit = int(input("      Number of messages to react to: ").strip())

    # Convert custom emoji to API format (e.g., ":fire:" -> "fire")
    if emoji.startswith(":") and emoji.endswith(":"):
        emoji = emoji.strip(":")
    else:
        # Unicode emoji (e.g., 🔥)
        pass

    # Fetch messages from the channel
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    params = {
        "limit": limit
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"      Error fetching messages: {response.status_code} - {response.text}")
            return

        messages = response.json()
        if not messages:
            print("      No messages found in the channel.")
            return

        # React to each message
        for message in messages:
            message_id = message['id']
            react_url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
            react_response = requests.put(react_url, headers=headers)

            if react_response.status_code == 204:
                print(f"      Reacted to message {message_id} with {emoji}")
            elif react_response.status_code == 429:  # Rate limited
                retry_after = float(react_response.headers.get('Retry-After', 5))
                print(f"      Rate limited, retrying in {retry_after} seconds...")
                time.sleep(retry_after)
                continue  # Retry the same reaction
            else:
                print(f"      Failed to react to message {message_id}: {react_response.status_code} - {react_response.text}")

            time.sleep(0.5)  # Small delay to avoid rate limits

    except Exception as e:
        print(f"      An error occurred: {e}")

    input("\n      Press Enter to return to the menu...")

def nitro_generator():
    print_header("Nitro Generator")
    amount = input('      How many codes: ').strip()

    try:
        amount = int(amount)
        if amount <= 0:
            print("      Please enter a positive number.")
            input("\n      Press Enter to return to the menu...")
            return
    except ValueError:
        print("      Invalid input. Please enter a number.")
        input("\n      Press Enter to return to the menu...")
        return

    count = 0
    codes = []

    while count < amount:
        code = "      https://discord.gift/" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        codes.append(code)
        count += 1

    print("\n      Generated Nitro Codes:")
    for code in codes:
        print(code)

    input("\n      Press Enter to return to the menu...")

# System Tools
def system_information():
    print_header("System Information")
    print(f"      OS: {platform.system()} {platform.release()}")
    print(f"      Processor: {platform.processor()}")
    print(f"      CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"      Total RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")
    input("\n      Press Enter to return to the menu...")

def ip_address():
    print_header("IP Address")
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"\n      Your IP Address: {ip}")
    input("\n      Press Enter to return to the menu...")

def ping_website():
    print_header("Ping A Website")
    website = input("      Enter a website to ping (e.g., google.com): ").strip()
    try:
        result = subprocess.run(['ping', '-c', '4', website], capture_output=True, text=True)
        print(f"\n      Ping Results for {website}:\n{result.stdout}")
    except Exception as e:
        print(f"\n      Error: {e}")
    input("\n      Press Enter to return to the menu...")

def current_processes():
    print_header("Current Processes")
    print("\n      Current Running Processes:")
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"      PID: {proc.info['pid']}, Name: {proc.info['name']}")
    input("\n      Press Enter to return to the menu...")

def network_speed_test():
    print_header("Network Speed Test")
    print("      Testing your network speed... This may take a few seconds.\n")

    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        print("      Testing download speed...")
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        print(f"      Download Speed: {download_speed:.2f} Mbps")

        print("      Testing upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        print(f"      Upload Speed: {upload_speed:.2f} Mbps")

    except Exception as e:
        print(f"      Error: {e}")

    input("\n      Press Enter to return to the menu...")

# Encryption Tools
def generate_key():
    print_header("Generate Encryption Key")
    key = Fernet.generate_key()
    print(f"\n      Generated Encryption Key: {key.decode()}")
    input("\n      Press Enter to return to the menu...")

def encrypt_data():
    print_header("Encrypt Data")
    key = input("      Enter encryption key: ").strip()
    data = input("      Enter data to encrypt: ").strip()
    try:
        fernet = Fernet(key.encode())
        encrypted_data = fernet.encrypt(data.encode())
        print(f"\n      Encrypted Data: {encrypted_data.decode()}")
    except Exception as e:
        print(f"\n      Error: {e}")
    input("\n      Press Enter to return to the menu...")

def decrypt_data():
    print_header("Decrypt Data")
    key = input("      Enter encryption key: ").strip()
    data = input("      Enter data to decrypt: ").strip()
    try:
        fernet = Fernet(key.encode())
        decrypted_data = fernet.decrypt(data.encode())
        print(f"\n      Decrypted Data: {decrypted_data.decode()}")
    except Exception as e:
        print(f"\n      Error: {e}")
    input("\n      Press Enter to return to the menu...")


# Main Function
def main():
    while True:
        clear_screen()
        print(banner)
        print(options)
        
        option = input('\n      Option: ').strip()

        if option.lower() == 'e':
            print("\n      Exiting...")
            break

        elif option == '1.1':
            webhook_spammer()

        elif option == '1.2':
            webhook_deleter()

        elif option == '1.3':
            message_spam()

        elif option == '1.4':
            reaction_spam()

        elif option == '1.5':
            nitro_generator()

        elif option == '2.1':
            system_information()

        elif option == '2.2':
            ip_address()

        elif option == '2.3':
            ping_website()

        elif option == '2.4':
            current_processes()

        elif option == '2.5':
            network_speed_test()

        elif option == '3.1':
            generate_key()

        elif option == '3.2':
            encrypt_data()

        elif option == '3.3':
            decrypt_data()

        else:
            print('\n      Invalid option. Press Enter to return to the menu.')
            input()

if __name__ == "__main__":
    main()