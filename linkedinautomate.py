import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Configure Chrome options for headless mode (if needed)
options = Options()
options.add_argument("--headless")  # Run in headless mode (without opening a browser window)

# Path for chromedriver (not necessary with webdriver_manager)
driver_path = "path_to_your_chromedriver"  # Optional if you are using webdriver_manager

# Initialize the Chrome WebDriver
service = Service(ChromeDriverManager().install())  # Automatically handles driver updates

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Get LinkedIn credentials from the .env file
email = os.getenv("LINKEDIN_EMAIL")
password = os.getenv("LINKEDIN_PASSWORD")

def login_to_linkedin():
    """
    Logs in to LinkedIn using credentials from the .env file.
    """
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)  # Wait for the page to load
    
    try:
        email_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        email_input.send_keys(email)
        password_input.send_keys(password)

        password_input.send_keys(Keys.RETURN)  # Submit the login form
        time.sleep(3)  # Wait for login to complete
        print("Login successful")
    except Exception as e:
        print(f"Error during login: {e}")

def send_connection_request(profile_url):
    """
    Sends a connection request with a personalized message to the provided LinkedIn profile URL.
    """
    driver.get(profile_url)
    time.sleep(2)  # Wait for the profile page to load

    try:
        # Find and click the 'Connect' button
        connect_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Connect')]")
        connect_button.click()
        time.sleep(1)

        # Click 'Add a note' to send a personalized message
        add_note_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add a note')]")
        add_note_button.click()
        time.sleep(1)

        # Find the message area and send a personalized message
        message_area = driver.find_element(By.ID, "custom-message")
        message_area.send_keys(
            "I came across your profile and was impressed by your work in the AI/ML/Generative AI space. "
            "As someone who is deeply passionate about [mention your specific area of interest], "
            "I’m always eager to connect with like-minded professionals and share insights. "
            "I’d love to connect and potentially discuss opportunities for collaboration, learning, or simply exchanging ideas."
        )

        # Click the 'Send' button to send the connection request
        send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
        send_button.click()
        time.sleep(2)  # Wait for the action to complete
        
        print(f"Connection request sent to: {profile_url}")
    except Exception as e:
        print(f"Could not send connection request to {profile_url}: {e}")

def main():
    """
    Main function that orchestrates the login and sending of connection requests.
    """
    print("Running LinkedIn automation...")
    login_to_linkedin()  # Log in to LinkedIn

    # List of LinkedIn profile URLs to send connection requests to
    profiles_to_connect = [
        "https://www.linkedin.com/in/aleksandra-kiszkiel-ab76851b1/",  # Example URL
        # Add more LinkedIn profile URLs here
    ]

    # Iterate over the list of profiles and send connection requests
    for profile in profiles_to_connect:
        send_connection_request(profile)

    # Close the driver after completing the tasks
    driver.quit()
    print("Script execution completed.")

if __name__ == "__main__":
    main()
