# EmailHarvest

A lightweight Python tool that automatically extracts email addresses from any website. Built with BeautifulSoup and regex, this scraper helps you collect email addresses for your contact lists or marketing purposes.

## Features

- Simple one-line command execution
- Automatic dependency installation
- Duplicate email removal
- User-friendly interface
- No configuration required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/EmailHarvest.git
cd EmailHarvest
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python email_scraping.py
```

When prompted, enter the website URL from which you want to extract email addresses. The script will then:
1. Fetch the webpage content
2. Parse it using BeautifulSoup
3. Extract all email addresses using regex
4. Display the unique email addresses found

## Example Output

```
Enter the website URL to scrape email addresses from: https://example.com
Email addresses found:
contact@example.com
support@example.com
```

## Requirements

- Python 3.6 or higher
- BeautifulSoup4
- requests

## Note

Please ensure you have permission to scrape the target website and comply with their robots.txt file and terms of service.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 