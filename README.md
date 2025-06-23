Amharic E-commerce Data Extractor

A web scraping project designed to extract product and service data from popular Ethiopian e-commerce websites. The primary goal is to build a large-scale, structured dataset for the Amharic language to support Natural Language Processing (NLP) research and development.
🎯 Project Motivation
The field of Natural Language Processing has seen incredible advancements, but progress for low-resource languages like Amharic is often hindered by a lack of quality, domain-specific data. This project aims to address this gap by creating a valuable corpus from real-world e-commerce listings, providing a foundational resource for tasks like:
Sentiment Analysis
Named Entity Recognition (NER)
Price Prediction Models
Machine Translation
Text Classification

This scraper currently targets the following websites:
qefira.com
jiji.com.et
✨ Key Features
Robust Scraping: Built with the powerful and asynchronous Scrapy framework for high performance.
Dynamic Content Handling: Uses Selenium WebDriver to render JavaScript-heavy pages, ensuring all data is captured correctly.
Structured Data Extraction: Collects key information for each listing:
Product Title
Price
Category
Description
Location
Posted Date
Polite and Resilient: Configured with download delays and user-agent rotation to respect server resources and handle basic anti-scraping measures.
Flexible Output: Easily save data to common formats like JSON, CSV, or XML.
🛠️ Technology Stack
Programming Language: Python
Scraping Framework: Scrapy
Browser Automation: Selenium
🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.
Prerequisites
Python 3.8+
pip package manager
Git
Google Chrome browser
ChromeDriver
Installation
Clone the repository:
Generated bash
git clone https://github.com/Gebrehiwot-Tesfaye/Amharic-ecommerce-data-extractor.git
cd Amharic-ecommerce-data-extractor
Use code with caution.
Bash
Create and activate a virtual environment (recommended):
On macOS/Linux:
Generated bash
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Bash
On Windows:
Generated bash
python -m venv venv
.\venv\Scripts\activate
Use code with caution.
Bash
Install the required Python packages:
Generated bash
pip install -r requirements.txt
Use code with caution.
Bash
(Note: If a requirements.txt is not present, you can install packages manually: pip install scrapy selenium)
Set up ChromeDriver:
Download the ChromeDriver version that matches your Google Chrome browser version from the official site.
Unzip the downloaded file.
Place the chromedriver (or chromedriver.exe) executable in a directory that is included in your system's PATH, or place it directly in the project's root directory.
⚙️ How to Run the Spiders
You can run each spider individually and save the output to a file. The output file format is inferred from the extension (e.g., .json, .csv, .xml).
To scrape qefira.com and save to a JSON file:
Generated bash
scrapy crawl qefira -o qefira_data.json
Use code with caution.
Bash
To scrape jiji.com.et and save to a CSV file:
Generated bash
scrapy crawl jiji -o jiji_data.csv
Use code with caution.
Bash
The scraping process will start, and you will see logs in your terminal. A new file with the extracted data will be created in the root directory upon completion.
📂 Project Structure
Generated code
Amharic-ecommerce-data-extractor/
├── amharic_data_extractor/
│   ├── __init__.py
│   ├── spiders/
│   │   ├── __init__.py
│   │   ├── qefira_spider.py     # Spider for qefira.com
│   │   └── jiji_spider.py       # Spider for jiji.com.et
│   ├── items.py                 # Defines the data structure (Scrapy Items)
│   ├── middlewares.py           # Custom request/response processing
│   ├── pipelines.py             # Post-processing and data cleaning pipeline
│   └── settings.py              # Project settings (delays, user-agents, etc.)
├── scrapy.cfg                   # Scrapy project configuration file
└── README.md                    # This file
