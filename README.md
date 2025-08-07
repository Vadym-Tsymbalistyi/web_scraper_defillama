# Defillama Scraper

<!-- TODO: add info about the goal and technologies used -->

## Project Structure & Artifacts

```
├web_scraper_defillama/
│
├── config/                # Configuration module
│   └── app.yaml           # App configuration (input / output, pulling interval, etc.)
│   └── logging.json       # Logging configuration
│
├── src/                   
│   ├── scraper/...        # The main bussiness logic
│   ├── utils/...          # Utility modules
|
├── tests/...              # Unit tests
│
├── main.py                # Entry point
|
├── logs/...               # Logger output 
|
├── scraper_results/...    # Results of scrapping
│
|
└── README.md              # The main documentation
|
└── requirements.txt       # Required Python dependencies
|
├── .gitignore             # Git ignore config
```

## Getting Started / Demo Run

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

## Configuration

The App uses a [config/app.yamp](config/app.yaml) file for settings.

| Parameter                    | Type      | Description                                        | Default Value                |
|------------------------------|-----------|----------------------------------------------------|------------------------------|
| target_url                   | str       | Target URL of defillama website page to scrap      | https://defillama.com/chains |
| pulling_interval_in_sec      | int       | Data Pulling / scraping interval in seconds        | 300                          |
| proxies                      | list[str] | List of proxy servers as strings                   | Empty list (`[]`)            |
| result_output_base_dir       | str       | Path to results directory                          | scraper_results              |
| result_output_base_file_name | str       | File name prefix to use for storing data snapshots | data_snapshot                |

---

## Logging Setup

The logging configuration [config/logging.yaml](config/logging.yaml)
By default, logs are saved to the file `logs/app.log` and streamed to the console.

---

## Result Data

Each iteration of Scraper run produces a snapshot of page data in this time, for example:

```
├── scraper_results/                   
│   ├── data_snapshot_2025-08-07_20-10-05.json
│   ├── data_snapshot_2025-08-07_20-15-20.json
│ 
```

---

### Result Data Model & Format

<!-- TODO: add more info -->
The following info is extracted from the website:

* Name: String
* Protocols: String
* TVL: String

The data is stored in JSON format in the following structure:

```json
[
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
  }
]
```

See [scraper_results/](scraper_results/) for more examples.
--- 

## Unit testing

The command to run the tests:

```bash
pytest tests
```