import numpy as np
import pandas as pd

# function 1
### START FUNCTION
def dictionary_of_metrics(items):
    """
    This function calculates the mean, median, standard deviation, variance,
    minimum value, and the maximum value.
    
    All the metrics calculated will be rounded to 2 decimal places

    Args:
    The function takes a list of numbers as input
    e.g list = [56,78,45,23,59,86,4]
    dictionary_of_metrics(list) = {'mean': 50.14,'median': 56.0,'var': 844.48,'std': 29.06,'min': 4,'max': 86}

    Returns:
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
    """
    This function calculates the five number summary. In statistics, the
    five number summary consists of the minimum value, first quartile'
    median, third quartile, and the maximum value.
    
    Args:
    The function takes a list of numbers as input
    e.g lists = [56,78,45,23,59,86,4]
    five_num_summary(list) = {'max': 86, 'median': 56.0, 'min': 4, 'q1': 34.0, 'q3': 68.5}
    
    Returns:
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
    """
    This function takes in a list of datetime strings as input 
     and returns only the date in 'yyyy-mm-dd' format.
       
    Args: 
         df (<list>): input of a datetime list strings ('yyyy-mm-dd hh:mm:ss')

    Returns: 
         list: a list of strings with elements in the 'yyyy-mm-dd' format
    """
    
    date = []  # declare an empty date list
    for i in dates: # iterate through the input list of datetime strings one after the other
        date1 = str(pd.to_datetime(i).date()) # datetime conversion to 'yyyy-mm-dd' and converted to strings
        date = date + [date1] # add each converted date into the initial empty variable list (date) declared above
    return date  # return the final list after all the dates have been added to the empty variable list (date)
### END FUNCTION

# function 4
### START FUNCTION
def extract_municipality_hashtags(df):
    """
    Modifies a dataframe to include two new columns: municipality and hashtag 
    
    Args: 
         df (dataframe): input of a dataframe 
         
    Returns: 
        dataframe: dataframe with two additional coloumns, 
        municipality column and list of hashtags from a tweet column
    """
    
    mun_dict = {
        '@CityofCTAlerts' : 'Cape Town',
        '@CityPowerJhb' : 'Johannesburg',
        '@eThekwiniM' : 'eThekwini',
        '@EMMInfo' : 'Ekurhuleni',
        '@centlecutility' : 'Mangaung',
        '@NMBmunicipality' : 'Nelson Mandela Bay',
        '@CityTshwane' : 'Tshwane'
    }
    
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
    
    df['Date'] = pd.to_datetime(df['Date']).apply(lambda i: i.date()) # convert datetime to date ('yyyy-mm-dd') and apply it to each element in 'Date' column of the dataframe
    return df.groupby(df['Date']).count() # group each tweet by the 'Date' column (now index) and return count for each day (column named 'Tweets')
### END FUNCTION

# function 6
### START FUNCTION
def word_splitter(df):
    """
    This function splits the sentences in a dataframe's column into a list of separate words
     Args: 
         df (dataframe): input of a dataframe 
         
    Returns: 
         dataframe: dataframe with an additional column Split Tweets from a Tweets column         
    """
    
    new_list = [] # declare an empty list
    tweets = df['Tweets'].str.lower()
    for i in range(len(tweets)):
        new_list.append(tweets[i].split())
    series_with_split_tweets = pd.Series(new_list,name='Split Tweets')
    data_frame_with_split_tweets = pd.concat((df,series_with_split_tweets),axis=1)
    return data_frame_with_split_tweets # returns the modified dataframe with split tweets
### END FUNCTION

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
    stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}
   
    stop_words = stop_words_dict['stopwords'] # defining the stop words 
    df["Without Stop Words"] = df["Tweets"].str.lower().str.split() # makes all the english stop words lowercase and split the words into a list
    df["Without Stop Words"] = df["Without Stop Words"].apply(lambda x: [word for word in x if word not in stop_words]) # gives all the words that are not in the stop words column
    return df # returns the modified dataframe without the english stop word
### END FUNCTION
