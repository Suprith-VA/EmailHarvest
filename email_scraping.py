import re

import sys
import subprocess


try:
    from bs4 import BeautifulSoup
except ImportError:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'BeautifulSoup4'])
    

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])



def scrape_emails(url):
    # Make a request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all email addresses in the HTML using a regular expression
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = set(re.findall(email_pattern, str(soup)))

    return emails

# Example usage:
url = input("Enter the website URL to scrape email addresses from: ")
emails = scrape_emails(url)
print("Email addresses found:")
for email in emails:
    print(email)
