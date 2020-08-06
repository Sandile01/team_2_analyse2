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
### START FUNCTION
def date_parser(dates):
    # your code here
    """
    This function takes in a list of datetime strings as input 
     and returns only the date in 'yyyy-mm-dd' format.
       
    Args: 
         df (<list>): input of a datetime list strings ('yyyy-mm-dd hh:mm:ss')

    Returns: 
         list: a list of strings with elements in the 'yyyy-mm-dd' format
    """
    date = [] #declare an empty date list
    for i in dates: # We iterate through the input list of datetime strings one after the other
        date1 = str(pd.to_datetime(i).date()) # Datetime conversion to 'yyyy-mm-dd' and converted to strings
        date = date + [date1] # Add each converted date into the initial empty variable list (date) declared above
    return date #return the final list after all the dates have been added to the empty variable list (date)
### END FUNCTION

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
### START FUNCTION
def number_of_tweets_per_day(df):
    """
    Calculation of the number of tweets posted per day 
    
    Args: 
         df(<dataframe>): input of a Tweets Pandas dataframe 
         
    Returns: 
         dataframe: dataframe grouped by day (Date should be the index in the format 'yyyy-mm-dd'), 
                    with the number of tweets for each day (column should be 'Tweets')
              
    """
    
    df['Date'] = pd.to_datetime(df['Date']).apply(lambda i: i.date())# convert datetime to date ('yyyy-mm-dd') and apply it to each element in 'Date' column of the dataframe

    return df.groupby(df['Date']).count() #Group each tweet by the 'Date' column (now index) and return count for each day (column named 'Tweets')

### END FUNCTION

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
    This function removes all the english stop words from given tweet
     Args: 
         df (dataframe): input of a dataframe 
         
    Returns: 
         dataframe: dataframe without the english stop words from a tweet
              
    """
    
    # your code here
    stop_words = stop_words_dict['stopwords'] # defining the stop words 
    df["Without Stop Words"] = df["Tweets"].str.lower().str.split() # makes all the english stop words lowercase and split the words into a list
    df["Without Stop Words"] = df["Without Stop Words"].apply(lambda x: [word for word in x if word not in stop_words]) # gives all the words that are not in the stop words column
    
    return df # returns the modified dataframe without the english stop word



### END FUNCTION
