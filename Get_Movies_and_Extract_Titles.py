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
    #print(results_ds)


def extract_movie_titles(d):
    movie_titles=[]
    for movie in d['Similar']['Results']:
        movie_titles.append(movie['Name'])
    return movie_titles  



#print(extract_movie_titles(get_movies_from_tastedive("Black Panther")))
