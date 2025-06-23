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
Use code with caution.
📊 Sample Data Output (JSON)
Each record extracted by the scraper will follow this structure:
Generated json
{
  "product_name": "Slightly Used iPhone 12 Pro",
  "price": "ETB 65,000",
  "description": "Clean phone, no scratches, 128GB storage, battery health 90%. Comes with original box and charger.",
  "category": "Electronics > Mobile Phones",
  "location": "Addis Ababa, Bole",
  "posted_date": "Posted on 25 Oct"
}
Use code with caution.
Json
🗺️ Future Roadmap
This project is under active development. Future plans include:
Implement a Data Cleaning Pipeline: Standardize data formats (e.g., convert prices to integers, parse dates into ISO format).
Integrate Proxy Rotation: Use proxies to enable large-scale, uninterrupted scraping.
Add Database Integration: Implement a pipeline to save data directly to a database like PostgreSQL or MongoDB.
Expand to More Websites: Add spiders for other relevant Ethiopian e-commerce platforms.
Improve Error Handling: Enhance logging and implement automatic retries for failed requests.
🤝 Contributing
Contributions are welcome! If you have ideas for improvement or want to add a new feature, please feel free to:
Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit your changes (git commit -m 'Add some amazing feature').
Push to the branch (git push origin feature/your-feature-name).
Open a Pull Request.
Please also feel free to open an issue to report bugs or suggest enhancements.
📜 License
This project is licensed under the MIT License - see the LICENSE.md file for details.
⚖️ Disclaimer
This tool is intended for educational and research purposes only. Please be responsible and respectful when scraping websites. Ensure you are not violating the terms of service of the targeted sites and do not overload their servers with requests. The developers of this project are not responsible for any misuse of this tool.
