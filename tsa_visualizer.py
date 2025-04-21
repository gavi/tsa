import pandas as pd
import matplotlib.pyplot as plt
import glob
from datetime import datetime
import numpy as np

def load_all_data():
    files = glob.glob('tsa_passengers_*.csv')
    all_data = []
    
    for file in files:
        year = int(file.split('_')[2].split('.')[0])
        df = pd.read_csv(file, parse_dates=['Date'])
        df['Year'] = year
        all_data.append(df)
    
    return pd.concat(all_data, ignore_index=True)

def plot_daily_trends(df):
    plt.figure(figsize=(15, 8))
    for year in df['Year'].unique():
        year_data = df[df['Year'] == year]
        plt.plot(year_data['Date'], year_data['Passengers'], label=str(year), alpha=0.7)
    
    plt.title('TSA Passenger Volume by Year')
    plt.xlabel('Date')
    plt.ylabel('Number of Passengers')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('tsa_daily_trends.png')
    plt.close()

def plot_monthly_averages(df):
    df['Month'] = df['Date'].dt.month
    monthly_avg = df.groupby(['Year', 'Month'])['Passengers'].mean().reset_index()
    
    plt.figure(figsize=(15, 8))
    for year in monthly_avg['Year'].unique():
        year_data = monthly_avg[monthly_avg['Year'] == year]
        plt.plot(year_data['Month'], year_data['Passengers'], 
                label=str(year), marker='o', alpha=0.7)
    
    plt.title('Monthly Average TSA Passenger Volume')
    plt.xlabel('Month')
    plt.ylabel('Average Number of Passengers')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.tight_layout()
    plt.savefig('tsa_monthly_averages.png')
    plt.close()

def plot_weekly_patterns(df):
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    weekly_avg = df.groupby(['Year', 'DayOfWeek'])['Passengers'].mean().reset_index()
    
    plt.figure(figsize=(15, 8))
    for year in weekly_avg['Year'].unique():
        year_data = weekly_avg[weekly_avg['Year'] == year]
        plt.plot(year_data['DayOfWeek'], year_data['Passengers'], 
                label=str(year), marker='o', alpha=0.7)
    
    plt.title('Weekly Pattern of TSA Passenger Volume')
    plt.xlabel('Day of Week')
    plt.ylabel('Average Number of Passengers')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.tight_layout()
    plt.savefig('tsa_weekly_patterns.png')
    plt.close()

def main():
    df = load_all_data()
    
    # Create visualizations
    plot_daily_trends(df)
    plot_monthly_averages(df)
    plot_weekly_patterns(df)
    
    print("Visualizations saved as PNG files in the current directory")

if __name__ == "__main__":
    main() 