import time
import random
import requests
import argparse
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Define colors
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW

# Define the URL for the API request - https://login.microsoftonline.com/common/GetCredentialType?mkt=en-US
# It is recommended to use FireProx (https://github.com/ustayready/fireprox) to get the best results
url = 'https://login.microsoftonline.com/common/GetCredentialType?mkt=en-US'
#url = 'https://<fireprox URL>/common/GetCredentialType?mkt=en-US'

# Set the payload to look normal using an arbitrary flowToken value
payload_template = {
    "isOtherIdpSupported": True,
    "checkPhones": False,
    "isRemoteNGCSupported": True,
    "isCookieBannerShown": False,
    "isFidoSupported": True,
    "country": "US",
    "forceotclogin": False,
    "isExternalFederationDisallowed": False,
    "isRemoteConnectSupported": False,
    "federationFlags": 0,
    "isSignup": False,
    "flowToken": "",
    "isAccessPassSupported": True,
}

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close"
}

# Function to make the API request and process the email
def process_email(email, valid_email_file):
    payload = payload_template.copy()
    payload["username"] = email

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            if "IfExistsResult" in response_json:
                if_exists_result = response_json["IfExistsResult"]
                if if_exists_result in (5, 0):
                    print(green + f"=> VALID {email} ({if_exists_result})")
                    with open(valid_email_file, 'a') as valid_file:
                        valid_file.write(email + '\n')
                else:
                    print(red + f"=> INVALID {email} ({if_exists_result})")
            else:
                print(red + f"INVALID INPUT {email}")
        else:
            print(red + f"API request failed for {email} with status code {response.status_code}")
    except Exception as e:
        print(red + f"Error processing {email}: {e}")

# Main function
def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Validate email addresses against Microsoft's API.")
    parser.add_argument("email_file", help="Path to the file containing email addresses.")
    parser.add_argument("output_file", help="Path to save valid email addresses.")
    parser.add_argument("throttle", type=float, help="Base throttling time in seconds (e.g., 0.5 for half a second).")
    parser.add_argument("jiggle", type=float, help="Maximum jiggle time to vary the throttle (e.g., 0.2).")

    args = parser.parse_args()

    email_file_path = args.email_file
    valid_email_file_path = args.output_file
    throttle = args.throttle
    jiggle = args.jiggle

    try:
        print(blue + "Starting email validation...")

        with open(email_file_path, 'r') as email_file:
            for line in email_file:
                email = line.strip()
                if email:
                    process_email(email, valid_email_file_path)
                    # Add jiggle time to the throttle
                    delay = throttle + random.uniform(-jiggle, jiggle)
                    delay = max(0, delay)  # Ensure delay is not negative
                    time.sleep(delay)

        print(yellow + f"Processing completed. Valid emails saved to {valid_email_file_path}.")
    except Exception as e:
        print(red + f"Error: {e}")

# Entry point
if __name__ == "__main__":
    main()

