import pandas as pd
import numpy as np
import calendar
import datetime
import time
#Created a dictionary containing the data sources for the three cities
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
  
       
#Created a list for months and days            
months = ['all', 'january', 'feburary', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#Function to figure out the filtering requirements of the user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
                  
  
 #Created a loop to get user input for the cities, handeling invalid input from the user   
    while True:
       city = input('Would you like to see data for chicago, new york city , or washington? \n ').lower()
       if city in CITY_DATA.keys():
           filname = CITY_DATA[city]
           break
       else:
           print('error occurred! Please enter a valid city')
        
#Created a loop to get user input for the month, handeling invalid input from the user    
    while True:
        month = input('what month would you like to see data for? \n ').lower()
        if month in months:
            break
        else:
            print("error occurred! Please enter a valid month")
     
#Created a loop to get user input for a day of the week, handeling invalid input from the user    
    while True:
        day = input('what day of the week would you like data for? \n ').lower()
        if day in days:
            break
        else:
            print('error occurred! Please enter a valid day of the week')
        
    print('-'*40)
    return city, month, day
#Function to load data from CITY_DATA .csv files
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #df to read the csv file
    df = pd.read_csv(CITY_DATA[city])    
    
    
    return df
#Function to allow the user to view raw data
def raw_data(df):
    i = 0
    pd.set_option('display.max_columns', 100)
    while True:
        view_data=input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_data=='yes':
            five_rows=df.iloc[i:i+5]
            print(five_rows)
            i += 5
        else:
            print('Great! I hope the data helped with your exploring')
            break
      
#Function to display time stats of bike rentals            
def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    
    
    if month != 'all':
        #Filter by month to create the new dataframe
        df = df[df['month'] == months.index(month)]
     
    if day != 'all':
        #Filter by day to create new dataframe
        day = df[df['day'] == days.index(day)]
    
    #Display of most common month for bike rental
    common_month = df['month'].mode()[0]
    common_month = calendar.month_name[common_month]
    print("The most common month is:  {}".format(common_month))
    
    
        
    
    #Display of the most common day of the week for bike rental
    common_weekday = df['day'].mode()[0]
    common_weekday = calendar.day_name[common_weekday]
    print("The most common day of the week is:  {}".format(common_weekday))
    
    #Display of the most common hour of bike rental
    common_hour = df['hour'].mode()[0]
    print("The most common hour is:  {}".format(common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#Function to display the most common location that bikes are rented and returned
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
   #Display most commonly used start station
    common_start_station = df['Start Time'].mode()[0]
    print("The most commonly used start station is:  {}".format(common_start_station))
    
    #Display most commonly used end station
    common_end_station = df['End Time'].mode()[0]
    print("The most commonly used end station is:  {}".format(common_end_station))
    
    #Display most frequent combination of start station and end station trip
    station_combination = df['Start Station'] + df['End Station']
    print('The most frequent combination of start and end station is:  {}'.format(station_combination.mode()[0] ))                                  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#Function for trip duration time
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #Total travel time
    total_travel = df['Trip Duration'].sum()
    print(str(datetime.timedelta(seconds=int(total_travel))))
    
    #Mean travel time
    total_travel_time = df['Trip Duration'].mean()
    print(str(datetime.timedelta(seconds=int(total_travel_time))))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#Function to for user statistics     
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #Total of user type(subscriber, customer, dependent)
    user_total = df['User Type'].value_counts()
    print('The total amount of user types is: \n{}'.format(user_total))
    
    #Total count of gender(male and female) only for the columns that gender is in
    if "Gender" in df.columns:
       gender_total = df['Gender'].value_counts()
       print('The total amount of gender is:  \n{}'.format(gender_total))
    
    #Displays the most recent, earliest, and most common birth year only for the columns that birth year is in
    if "Birth Year" in df.columns:   
       recent_birthyear = df['Birth Year'].max()
       print('The most recent birth year is:  {}'.format(int(recent_birthyear)))
    
       earliest_birthyear = df['Birth Year'].min()
       print('The earliest birth year is:  {}'.format(int(earliest_birthyear)))
    
       common_birthyear = df['Birth Year'].mode()[0]
       print('The most common birth year is:  {}'.format(int(common_birthyear)))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#Main function: calls all the previous functions    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)         
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
     main()