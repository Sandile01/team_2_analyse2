# function 1
### START FUNCTION
def dictionary_of_metrics(items):
    # your code here
    """
    This function calculates the mean, median, standard deviation, variance,
    minimum value, and the maximum value.
    
    All the metrics calculated
    will be rounded to 2 decimal places

    Args:
    The function takes a list of numbers as input
    e.g list = [56,78,45,23,59,86,4]
    dictionary_of_metrics(list)

    returns:
    The function returns a dictionary containing the calculated netrics.
    All the metrics calculated will be rounded to 2 decimal places
    """
    my_list = ['mean',round(np.mean(items),2),
               'median',round(np.median(items),2),
               'var', round(np.var(items, ddof =1),2),
               'std',round(np.std(items, ddof = 1),2),
               'min', round(np.min(items),2),
               'max', round(np.max(items),2)
               ]
    dict_list = {my_list[i]:my_list[i+1] for i in range(0, len(my_list),2)}
    return dict_list

### END FUNCTION
# function 2
### START FUNCTION
def five_num_summary(items):
    # your code here
    """
    This function calculates the five number summary. In statistics, the
    five number summary consists of the minimum value, first quartile'
    median, third quartile, and the maximum value.
    
    Args:
    The function takes a list of numbers as input
    e.g list = [56,78,45,23,59,86,4]
    five_num_summary(list)
    returns
    The function will return a dictionary containing the calculated five number summary
     with all values in the dictionary rounded to two decimal places
    """
    my_list = ['max', round(np.max(items),2),
               'median',round(np.median(items),2),
               'min', round(np.min(items),2),
               'q1', round(np.quantile(items, .25),2),
               'q3',round(np.quantile(items, .75),2)
              ]
    dict_list = {my_list[i]:my_list[i+1] for i in range(0, len(my_list),2)}
    return dict_list
### END FUNCTION
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
### START FUNCTION
def extract_municipality_hashtags(df):
    # your code here
    mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}
     """
    Modifies a dataframe to include two new columns: municipality and hashtag 
    
    Args: 
         df (dataframe): input of a dataframe 
         
    Returns: 
         dataframe: dataframe with two additional coloumns,
              municipality column and list of hashtags from a tweet column
    """
    
    
    df["municipality"] = df["Tweets"].map(lambda x: x if x.startswith("@") else x) # iterate over the column to search for words that start wtih @
    df["municipality"] = df["municipality"].map(mun_dict) # map the output to the mun-dict dictionary 
    df["hashtags"] = df["Tweets"].str.lower().str.findall(r"(#\S+)") # set to lower string and find the pattern
    df["hashtags"] = df["hashtags"].apply(lambda x: np.nan if len(x)==0 else x) # for where it is empty it should return NaN 
    
    return df # return dataframe with additional columns

### END FUNCTION
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
def word_splitter():
    new_list = []
    tweets = df['Tweets'].str.lower()
    for i in range(len(tweets)):
        new_list.append(tweets[i].split())
    series_with_split_tweets = pd.Series(new_list.name='Split Tweets')
    data_frame_with_split_tweets = pd.concat((df,series_with_split_tweets),axis=1)
    return data_frame_with_split_tweets

# function 7

### START FUNCTION
def stop_words_remover(df):
    """
    This function removes all the english stop words from given tweet.
    
    """
    
    # your code here
    stop_words = stop_words_dict['stopwords']
    df["Without Stop Words"] = df["Tweets"].str.lower().str.split()
    df["Without Stop Words"] = df["Without Stop Words"].apply(lambda x: [word for word in x if word not in stop_words])
    
    return df


### END FUNCTION
