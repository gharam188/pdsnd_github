import pandas as pd
import time as time
import numpy as nb
def check_input(input_str,input_type):
    
    while True:
        input_read=input(input_str)
        try:
            if input_read in['chicago','Chicago','new_york_city','New_york_city','washington','Washington'] and input_type==1:
                break
            elif input_read in['january','february','march','april','may','june','all'] and input_type==2:
                break
            elif input_read in['sunday','monday','wednesday','tuesday','friday','saturday','all']and input_type==3:
                break
            else:
                if input_type==1:
                    print('wrong city')
                if input_type==2:
                   print('wrong month')
                if  input_type==3:
                    print('worng day')
             
        except ValueError:
            print('Sorry Error input')
            
    return input_read


def get_filters():
    print('\nHello! Let\'s explore some US bikeshare data!')
    city=check_input('\n Choose city :\n   . new_york_city\n   . chicago\n   . washington \n',1)
    month=check_input('\n select  month : \n . all\n .january \n .february \n .march \n .april\n .may\n .june \n',2)
    day=check_input('\n  Enter select  day : \n. all \n. sunday\n. monday\n. Tuesday \n. wednesday \n.tuesday \n.friday \n.saturday \n',3)
    print('_'*40)
    return city,month,day
"""      Asks user to specify a city, month, and day to analyze.

    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  """


   


   
"""       Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day """



def load_dat(city, month, day):
    CITY_DATA = {'chicago': 'chicago.csv','Chicago':'chicago.csv','new_york_city':'new_york_city.csv','New_york_city':'new_york_city.csv',
             'washington': 'washington.csv','Washington':'washington.csv'}
    
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

    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.day)

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # use the index of the days list to get the corresponding int
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = days.index(day) + 1

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df



     # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour
    
   
    
def time_of_trival(df):
    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].apply(lambda x: x.hour)
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\n This took %s seconds." % (time.time() - start_time))
    start_time=time.time()
    print(df['month'].mode()[0])
    print(df['day_of_week'].mode()[0])
    print(df['hour'].mode()[0])
    print('Elepsed time is seconds', time.time()-start_time)
 # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip
def station_and_trip(df)  :
    start_time=time.time()
    Start_station=df['Start Station'].mode()[0]
    End_station=df['End Station'].mode()[0]
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\n Most Commonly used combination of start station and end station trip:', Start_station, " & ", End_station)
    print("count",Combination_Station)
    print('Elapsed time is second',(time.time()-start_time))
    
def user_station(df,city):
    if city!='washington':
       print(df['Gender'].value_counts())
       print('most  Birth year frequence',df['Birth Year'].mode()[0])
       print(' Most Common Year:',df['Birth Year'].max())
       print('Earliest Year',df['Birth Year'].min())
"""Displays statistics on the total and average trip duration."""
    # TO DO: display total travel time


    # TO DO: display mean travel time

def  trip_duration(new_df):
    total_travel_time=new_df['Trip Duration'].sum()
    print('total travel time',total_travel_time)
    averg_tr=total_travel_time/new_df['Trip Duration'].count()
    print('average_travel time',averg_tr)
    Mean_Travel_Time = new_df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time / 60, " Minutes")

def main():
    while True:
      city,month,day=get_filters()
      df=load_dat(city,month,day)
      print(df.head())
      time_of_trival(df)
      station_and_trip(df)
      user_station(df, city)
      trip_duration(df)
      more_data = input('\n Would you like to view 5 lines of the selected raw data? Enter Yes or No.\n').title()
      answers = ['Yes', 'No']
      while more_data not in answers:
            print("Sorry, I didn't catch that. Try Again. \n")
            more_data = input('\n Would you like to view 5 lines of the selected raw data? Enter Yes if you want or type anything to exit.\n').title()
            break

      for i in df.index:
            if more_data == 'Yes':
                print(df.iloc[i * 5:(i + 1) * 5])
                more_data = input('\n Would you like to view 5 more lines of the selected raw data? Enter Yes if you want or type anything to exit.\n').title()
            else:
                print('End of data.\n')
                break

      restart = input('\n Would you like to restart? Enter Yes or No.\n').title()
      if restart.title() != 'Yes':
            print('Good Bye!')
            break
     
if __name__ == '__main__':
      main()
 
        
        
    