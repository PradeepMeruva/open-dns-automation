from cryptography.fernet import Fernet
from playwright.sync_api import sync_playwright
import sys
import json

def load_config():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    with open("config.json.encrypted", "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)
    return json.loads(decrypted)


def load_block_list():
    with open("block_list.json", "r") as file:
        data = json.load(file)
    return data["domains_to_block"]

def block_games():
    config = load_config()
    username = config["username"]
    password = config["password"]


    playwright = sync_playwright().start()  # Start Playwright
    browser = playwright.chromium.launch(headless=False)  # Launch browser in non-headless mode
    page = browser.new_page()
    page.goto("https://dashboard.opendns.com/")

     # Enter username
    page.fill("#username", username)
    
    # Enter password
    page.fill("#password", password)
    
    # Click the sign-in button
    page.click("#sign-in")

     # Wait for the page to load after login
    page.wait_for_load_state("networkidle")
    
    # Navigate to the content filtering page
    page.goto("https://dashboard.opendns.com/settings/644570811/content_filtering")

    page.wait_for_load_state("networkidle")

         # Load domains to block from the JSON file
    domains_to_block = load_block_list()

     # Iterate through the list and block each domain
    for domain in domains_to_block:
        print(f"Trying to block  {domain} .")
        page.fill("#block-domain", domain)  # Add domain to the block domain text box
        page.click("#add-domain")  # Click the add domain button  
        page.click("#confirm-add-already-blocked")
         
           
        print(f"Blocked  {domain} .")
    





        # Check the checkbox with id #dt_category[12]
    page.check("#dt_category\\[12\\]")  # Escape square brackets in the selector
    
    # Click the save button
    page.click("#save-categories")

  # Wait for the "apply" process to complete
    #page.wait_for_selector("#apply-status", state="hidden")  # Replace with the correct selector if needed
    page.wait_for_load_state("networkidle")




    



    

    print("Browser is open. Press Ctrl+C to exit.")
    try:
        # Keep the script running to keep the browser open
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        browser.close()
        playwright.stop()


def check_all_blocked_domains(page):
    # Select all checkboxes with the class "domains-list blocked-domain"
    checkboxes = page.locator("input.domains-list.blocked-domain")
    
    # Get the count of checkboxes
    count = checkboxes.count()
    
    # Iterate through each checkbox and check it
    for i in range(count):
        checkboxes.nth(i).check()
    print(f"Checked {count} blocked domains.")


def unblock_games():
    config = load_config()
    username = config["username"]
    password = config["password"]


    playwright = sync_playwright().start()  # Start Playwright
    browser = playwright.chromium.launch(headless=False)  # Launch browser in non-headless mode
    page = browser.new_page()
    page.goto("https://dashboard.opendns.com/")
    
    # Enter username
    page.fill("#username", username)
    
    # Enter password
    page.fill("#password", password)
    
    # Click the sign-in button
    page.click("#sign-in")
    
    # Wait for the page to load after login
    page.wait_for_load_state("networkidle")
    
    # Navigate to the content filtering page
    page.goto("https://dashboard.opendns.com/settings/644570811/content_filtering")
    
    # Uncheck the checkbox with id #dt_category[12]
    page.uncheck("#dt_category\\[12\\]")  # Escape square brackets in the selector
    
    # Click the save button
    page.click("#save-categories")
    
    # Wait for the "apply" process to complete
    #page.wait_for_selector("#apply-status", state="hidden")  # Replace with the correct selector if needed

    page.wait_for_load_state("networkidle")
    
 
    
 

    check_all_blocked_domains(page)
    
    # Click the delete button
    page.click("#delete-domains")
    
    print("Reversed actions completed. Browser is open. Press Ctrl+C to exit.")
    try:
        # Keep the script running to keep the browser open
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <block|unblock>")
        sys.exit(1)

    action = sys.argv[1].lower()
    if action == "block":
        block_games()
    elif action == "unblock":
        unblock_games()
    else:
        print("Invalid action. Use 'block' or 'unblock'.")
        sys.exit(1)