# function 1
# function 2
# function 3
def date_parser(dates):
    # your code here
    """This function takes as input a list of 
       datetime strings and returns only the
       date in 'yyyy-mm-dd' format"""
    """This function takes as input a list of 
       datetime strings and returns only the
       date in 'yyyy-mm-dd' format"""
    date = [] #declare an empty date list
    """We iterate through the input list of datetime 
       strings, do a date conversion to 'yyyy-mm-dd'. 
       Then we it to string by using str() and store 
       in a variable date1.
       The next step then add each converted date into 
       the initial empty variable list (date) and this 
       is converted to a list and after final iteration 
       is done, the list is then returned
    """
    for i in dates:
        date1 = str(pd.to_datetime(i).date())
        date = date + [date1]
    return date

# function 4
# function 5
def number_of_tweets_per_day(df):
    """
    This funtion takes a tweets pandas
    dataframe as input and calculates 
    the number of tweets posted per day    
    """
    df['Date'] = pd.to_datetime(df['Date']).apply(lambda i: i.date())
    return df.groupby(df['Date']).count()
# function 6
# function 7
