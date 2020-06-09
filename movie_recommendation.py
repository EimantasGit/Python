#Using cached data as it's a practice problem (use requests.get() for actual data)
import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    url = 'https://tastedive.com/api/similar'
    param = {}
    param['q']= movie
    param['type']= 'movies'
    param['limit']= 5
    
    #Gets json data
    results = requests_with_caching.get(url, params=param)
    #Converts json data to python dictionary
    results = json.loads(results.text)
    return results
    
def extract_movie_titles(results):
    
    suggested_movies = []
    return [x['Name'] for x in results['Similar']['Results']]


def get_related_titles(movie_list):
    list_n = []
    movie_set = set()
    for movie in movie_list:
        #Append creates a list in a list, so we use extend
        list_n.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    movie_set = set(list_n)
    #We remove any non-unique values by converting to set
    #Then convert back to list
    return list(movie_set)

def get_movie_data(movie):
    
    url = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = movie
    param['r'] = 'json'
    
    results = requests_with_caching.get(url, params = param)
    results = json.loads(results.text)
    return results

#Finding movies' rating on Rotten Tomatoes
def get_movie_rating(movie_dictionary):
    ratings = movie_dictionary['Ratings']
    rating_integer = 0
    
    for item in ratings:
        if item['Source'] == 'Rotten Tomatoes':
            rating_integer = int(item['Value'][:-1]) #Remove % so we can convert to int
    return rating_integer

def get_sorted_recommendations(movie_list):
    dict_n = {}
    list_n = get_related_titles(movie_list)
    
    for item in list_n:
        rating = get_movie_rating(get_movie_data(item))
        dict_n[item] = rating
    return [item[0] for item in sorted(dict_n.items(), key=lambda item: (item[1], item[0]), reverse = True)]
###############################################################################
