import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Enter your desired city by choosing from 'chicago','new york city','washington': ").lower()
        if city in ('chicago','new york city','washington'):
            break
        else:
            print("It seems you entered city name incorrectly")
            continue
    
    while True:
        month = input("Enter your desired month by choosing from: 'all','january','february','march','april','may','june': ").lower()
        if month in ('all','january','february','march','april','may','june'):
            break
        else:
            print("It seems you entered the month incorrectly")
            continue
    
    while True:
        day = input("Enter your desired day by choosing from: 'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday': ").lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print("It seems you entered the day of week incorrectly")
            continue

    
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

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
    most_common_month = df['Start Time'].dt.month_name().mode()[0]
    print("The most common month: {}".format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['Start Time'].dt.day_name().mode()[0]
    print("The most common day: {}".format(most_common_day))
    # TO DO: display the most common start hour
    most_common_satrthour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour: {}".format(most_common_satrthour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station : {}".format(most_commonly_used_start_station))
    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station : {}".format(most_commonly_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_combination = (df['Start Station'] + " , " + df['End Station']).mode()[0]
    print("Most frequent combination of Start Station and End Station respectively: ({})".format(most_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {}".format(total_travel_time))
    
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("Average of total travel time: {}".format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    

    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
        
    except:
        print("Oops! There is no 'Gender' table for this city, I can't calculate number of 'Genders' for you")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("Oldest user's year of birth : " + str(df['Birth Year'].min()))
        
        print("Youngest user's year of birth : " + str(df['Birth Year'].max()))
        
        print("Most Popular users' birth year : " + str(df['Birth Year'].mode()))

    except:
        print("Oops! There is no 'Birth Year' table for this city, I can't specify oldest, youngest and most popular birth year")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == "yes"):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no: ").lower()
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = pd.DataFrame(load_data(city, month, day))

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
            
if __name__ == "__main__":
	main()