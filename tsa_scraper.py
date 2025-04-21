import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os

def get_tsa_data(year):
    if year == datetime.now().year:
        url = "https://www.tsa.gov/travel/passenger-volumes"
    else:
        url = f"https://www.tsa.gov/travel/passenger-volumes/{year}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table')
    if not table:
        print(f"No data found for year {year}")
        return None
    
    data = []
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) == 2:
            date_str = cols[0].text.strip()
            passengers = cols[1].text.strip().replace(',', '')
            try:
                date = datetime.strptime(date_str, '%m/%d/%Y')
                data.append({
                    'Date': date,
                    'Passengers': int(passengers)
                })
            except ValueError:
                continue
    
    return pd.DataFrame(data)

def get_existing_data(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename, parse_dates=['Date'])
    return None

def main():
    current_year = datetime.now().year
    years = range(2019, current_year + 1)
    
    for year in years:
        filename = f"tsa_passengers_{year}.csv"
        existing_df = get_existing_data(filename)
        
        print(f"Processing year {year}...")
        new_df = get_tsa_data(year)
        
        if new_df is not None:
            if existing_df is not None:
                # Merge and keep only new/updated rows
                merged = pd.concat([existing_df, new_df])
                merged = merged.drop_duplicates(subset=['Date'], keep='last')
                merged = merged.sort_values('Date')
                merged.to_csv(filename, index=False)
                print(f"Updated {filename} with new data")
            else:
                new_df.to_csv(filename, index=False)
                print(f"Created {filename}")

if __name__ == "__main__":
    main() 