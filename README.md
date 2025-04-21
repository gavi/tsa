# TSA Passenger Volume Analysis

This project scrapes and analyzes TSA passenger volume data from 2019 to present.

## Features

- Scrapes TSA passenger volume data from [TSA.gov](https://www.tsa.gov/travel/passenger-volumes)
- Handles both historical and current year data
- Creates CSV files for each year
- Generates visualizations of the data

## Requirements

- Python 3.8+
- Required packages listed in `requirements.txt`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Scrape TSA data:
```bash
python tsa_scraper.py
```
This will create CSV files for each year (e.g., `tsa_passengers_2024.csv`)

2. Generate visualizations:
```bash
python tsa_visualizer.py
```
This will create three visualization files:
- `tsa_daily_trends.png`: Daily passenger volume trends
- `tsa_monthly_averages.png`: Monthly average passenger volumes
- `tsa_weekly_patterns.png`: Weekly patterns of passenger volume

## Data Format

Each CSV file contains:
- `Date`: The date of the passenger count
- `Passengers`: Number of passengers screened by TSA

## Notes

- The scraper automatically handles the current year's data differently
- Visualizations are saved as PNG files in the current directory
- The script updates existing CSV files with new data when run multiple times
