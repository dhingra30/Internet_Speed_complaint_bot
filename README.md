# Internet_Speed_complaint_bot
Internet Speed Complaint Bot

# README.md

## Internet Speed Twitter Bot

This Python script utilizes Selenium to automate the process of measuring internet speed and posting the results on Twitter if the speed does not meet predefined thresholds.

### Overview

The bot performs the following tasks:

1. Navigates to [Speedtest.net](https://www.speedtest.net/) to measure download and upload speeds.
2. Compares the measured speeds against predefined thresholds.
3. If the speeds are below the thresholds, it automatically posts a message on Twitter mentioning the speed issue.

### Requirements

- Python 3.x
- Selenium library
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/dhingra30/Internet_Speed_complaint_bot.git
   cd <repository-directory>
   ```

2. Install the required libraries:
   ```bash
   pip install selenium
   ```

3. Ensure you have ChromeDriver installed and available in your system PATH.

### Configuration

Before running the bot, make sure to update the following variables in the script:

- `TWITTER_EMAIL`: Your Twitter account email.
- `TWITTER_PASSWORD`: Your Twitter account password.
- `TWITTER_USERNAME`: Your Twitter handle (optional).
- `DOWN_SPEED`: Minimum expected download speed (in Mbps).
- `UP_SPEED`: Minimum expected upload speed (in Mbps).

### Usage

To run the bot, execute the following command:

```bash
python main.py
```

### Important Notes

- This script uses hardcoded values for email and password. Consider using environment variables or secure vaults to store sensitive information.
- Ensure compliance with Twitter's automation policies when using bots.
- The script opens a Chrome browser window and will not close automatically. Make sure to close it manually when done.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Disclaimer

Use this script responsibly and be mindful of your internet service provider's terms of service. Automating actions on Twitter may lead to account suspension if not done in compliance with their policies.