# Product Price Tracker

This Python script tracks the price of a product from a specific website, compares it with the previous price, and sends an email notification in case of a change.

## Features

- Web scrapes the product price from a specified URL.
- Utilizes SQLite for storing historical price data.
- Sends email notifications in case of a price change.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (install them using `pip install -r requirements.txt`):
  - requests
  - beautifulsoup4
  - smtplib
  - email

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/product-price-tracker.git
   cd product-price-tracker
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
Modify the script to set your product URL, email settings, and other configurations.

Run the script:

bash
Copy code
python product_price_tracker.py
Configuration
product_url: URL of the product page to track.
to_email: Email address to receive price change notifications.
db_file: SQLite database file to store historical price data.
Email Configuration
The email settings are configured for a Mailtrap SMTP server. Replace the SMTP server details with your own if needed.
Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Requests
Beautiful Soup
SQLite
Email package
Mailtrap (for testing email notifications)
Contact
For any questions or feedback, feel free to contact [alirezafiv@gmail.com].

vbnet
Copy code

Make sure to replace placeholders such as `Matrix2030`, `alirezafiv@gmail.com`, and adapt the content based on your project's specific details. This README provides a quick overview, installation instructions, usage guidelines, and information for potential contributors.
