import requests
import json

def get_movies_from_tastedive(input):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {} 
    params_diction["q"] = input
    params_diction["type"] = "movies"
    params_diction["limit"] = "5" 
    resp = requests.get(baseurl, params=params_diction)
    results_ds = resp.json()
    return(results_ds)

#print(get_movies_from_tastedive("Bridesmaids"))
#print(get_movies_from_tastedive("Black Panther"))
    
def extract_movie_titles(d):
    movie_titles=[]
    for movie in d['Similar']['Results']:
        movie_titles.append(movie['Name'])
    return movie_titles 

def get_related_titles(lst):
    titles=[]
    for movie in lst:
        new_dict=get_movies_from_tastedive(movie)
        new_list=extract_movie_titles(new_dict)
        for item in new_list:
            if item in titles:
                continue
            else:
                titles.append(item)
    return titles

get_related_titles(["Black Panther", "Captain Marvel"])