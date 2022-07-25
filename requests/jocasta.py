#!/usr/bin/env python3
# https://gitlab.com/RojasRafael/jocasta-nu

import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--listPeople", "-lp", type=int, choices=range(1,7), help="List Start Wars Characters for each movie, even Jar jar. :(")
parser.add_argument("--listFilms", "-lf", action="store_true", default=False, help="List star wars films in release chronological order, even the prequels :(")
parser.add_argument("--shipsinMovie", "-sim", type=int, choices=range(1,7), default=False, help="list all ships in a given movie")
parser.add_argument("--hyperdriveGreater", "-hdr-gr", default=False, help="Search ships with an hyperdrive rating greating than given value")
parser.add_argument("--findShips", "-fs", nargs=2, metavar=('lower', 'upper'), help="find ships with a crew between two ranges")
args = parser.parse_args()

# Get the stuff from swapi
def swapiRequests(request_url):
    request = requests.get(request_url)
    request_json = (request.text)
    json_object = json.loads(request_json)
    return json_object


if args.listFilms:
    request_url = "https://swapi.dev/api/films/"
    ListFilms_object = swapiRequests(request_url)
    films = ListFilms_object['results']
    for film in films:
        filmName = film['title']
        filmNumber = film['episode_id']  
        print(filmNumber," - ",filmName) 


if args.listPeople:
    movieId = (args.listPeople)
    request_url = "https://swapi.dev/api/films/%s" % movieId
    listPeople_object = swapiRequests(request_url)

    for character in listPeople_object['characters']:
        request =  requests.get(character)
        request_json = (request.text)
        char_object = json.loads(request_json)
        print(char_object['name'])

if args.shipsinMovie:
    movieId = int(args.shipsinMovie)
    request_url = "https://swapi.dev/api/films/%s" % movieId
    shipsinMovie_object = swapiRequests(request_url)
    print("Startships in Movie: ", shipsinMovie_object['title'])    
    for starship in shipsinMovie_object['starships']:
         starship_object = swapiRequests(starship)
         print(starship_object['name'])


if args.hyperdriveGreater:
    hdr_gr = float(args.hyperdriveGreater)
    request_url = "https://swapi.dev/api/starships/"
    hdr_object =  swapiRequests(request_url)
    print("ships with HyperDrive rating equal or higher than: ", hdr_gr) 
    ships = hdr_object['results']
    for ship in ships:
        if float(ship['hyperdrive_rating']) >= hdr_gr:
            print(ship['name'], " - ", ship['hyperdrive_rating'])


if args.findShips:
    request_url = "https://swapi.dev/api/starships/"
    ships_object = swapiRequests(request_url)
    lower, upper = args.findShips
    print("ships with crew capacity between the range of: ", lower," and: ", upper)
    ships = ships_object['results']
    for ship in ships:
        crews = ship['crew']
        name = ship['name']
        if "-" in crews:	
            x = crews.split('-')    
            crews_lower = int(x[0])
            crews_upper = int(x[1])
            if int(lower) >= crews_lower and int(upper) <= crews_upper:
                print("Ship ",name," crew is within range ", crews)
        else:
            crewsint = int(crews.replace(',', ''))
            if int(lower) <= crewsint <= int(upper):
                print("Ship crew",name," within range: ", crewsint)
