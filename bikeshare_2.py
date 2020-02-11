# Just updated the entire code as I saw that the solution was on the palatform

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for chicago, new york or washington?\n')
    
    while (city.lower() != 'chicago' and city.lower() != 'new york' and city.lower() != 'washington'):
        city = input('wrong input, please enter either chicago, new york or washington\n')
    
       
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month: all, january, febuary, march, april,may, june\n')
    
    while (month != 'all' and month != 'january' and month != 'febuary' and month != 'march' and month != 'april' and month != 'may' and month != 'june') :
        month = input('wrong month, please enter a correct one:\n')
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('please choose the day: all, monday, tuesday, wednsday, thursday, friday, saturday, sunday\n')

    while (day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednsday' and day != 'thursday' and day != 'friday' and day !='saturday' and day != 'sunday\n') :
        day = input('wrong month, please enter a correct one:\n')
        
        
    print('-'*40)
    return city, month, day


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
    
    if (city == 'chicago'):
        df = pd.read_csv('chicago.csv')
    elif (city == 'new york'):
        df = pd.read_csv('new_york_city.csv')
    elif (city == 'washington'):
        df = pd.read_csv('washington.csv')

    #Another commet to explain we are adding date columns from the df    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour            
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name       
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month:')
    print(df['month'].mode()[0])


    # TO DO: display the most common day of week
    print('The most common day of the week:') 
    print(df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    print('The most common start hour:')
    print(df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start nation')      
    print(df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('most commonly used end station')
    print(df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station')
    df['start_end'] = df['Start Station'] + df['End Station'] 
    print('most common combination of start and end stations')
    print(df['start_end'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total sum of total travel time')
    print(df['Trip Duration'].sum())     

    # TO DO: display mean travel time
    print('the mean travel time')
    print(df['Trip Duration'].mean())     

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('the count of user types')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if ('Gender' in df.columns):
        print('the count of gender')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('B
    print('Earliser birth year')
    print(df['Birth Year'].min())
    print('Most recent birth year')
    print(df['Birth Year'].max())
    print('Most common birth year')
    print(df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
        
        counter = 0
        while (raw_data == 'yes'):
               print(df.iloc [counter: counter + 5, ])
               counter = counter + 6
               raw_data = input('\nWould you like to see another 5 rows Enter yes or no.\n')
      
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
