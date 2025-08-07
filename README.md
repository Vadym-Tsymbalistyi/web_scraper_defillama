# Defillama Scraper
├web_scraper_defillama/
│
├── config/                # Configuration module
│   └── config.py
│
├── data/                  # Stores input/output JSON files
│   ├── config.json
│   └── data.json
│
├── logs/                  # Logging output
│   └── scraper.log
│
├── scraper/               # Scraper logic
│   └── scraper.py
│
├── test/                  # Unit tests
│   └── _get_elements.test.py
│
├── utils/                 # Utility modules
│   ├── driver.py
│   ├── logger_setup.py
│   └── storage.py
│
├── main.py                # Entry point
├── .gitignore
└── README.md              # You are here
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
