# 🕸️ Defillama Scraper

Python-based web scraper for collecting and storing data from Defillama.

---

## 📁 Project Structure

```plaintext
web_scraper_defillama/
│
├── config/
│   └── config.py
│
├── data/
│   ├── config.json
│   └── data.json
│
├── logs/
│   └── scraper.log
│
├── scraper/
│   └── scraper.py
│
├── test/
│   └── _get_elements.test.py
│
├── utils/
│   ├── driver.py
│   ├── logger_setup.py
│   └── storage.py
│
├── main.py
├── .gitignore
└── README.md 
 ```
## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Vadym-Tsymbalistyi/web_scraper_defillama.git
    ```

2. Go to the project directory:

    ```bash
    cd web_scraper_defillama
    ```
    
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:
    ```bash
    python main.py
    ```
   

## 1. Configuration

The script uses a `config.json` file for settings. If the file does not exist, it will be created automatically with default values:

| Parameter | Type       | Description                               | Default Value             |
|-----------|------------|-------------------------------------------|---------------------------|
| interval  | int        | Restart cycle interval in seconds         | 300                       |
| proxies   | list[str]  | List of proxy servers as strings           | Empty list (`[]`)          |

---

## 2. Logging Setup

- Logs are automatically saved to `scraper.log`.
- Logging is done both to the file and the console.

---

## 3. Data Storage

### Location

All scraped data is automatically saved in `data.json` at the project root.

### Data Format

The data is stored in JSON format with the following structure:

```json
  {
    "Name": "Ethereum",
    "Protocols": "1568",
    "TVL": "$82,896b"
  },
  {
    "Name": "Solana",
    "Protocols": "329",
    "TVL": "$9,85b"
  },
  {
    "Name": "BSC",
    "Protocols": "987",
    "TVL": "$6,794b"
  },
