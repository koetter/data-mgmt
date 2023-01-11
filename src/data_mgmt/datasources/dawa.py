import os
import requests
import json

dataformater = ["json", "jsonp", "ndjson", "csv", "geojson", "geojsonz"]
datastrukturer = ["nestet", "flad", "mini"]

class AdresseAPI:

    services = ["adgangsadresser", "adresser"]

    def __init__(
        self
        ,datastruktur="nestet"
        ,dataformat="json"
        ,download=False
        ,valider=True
        ,srid="25832"):

        self.url = "https://api.dataforsyningen.dk"
        self.datastruktur = datastruktur
        self.dataformat = dataformat
        self.download = download
        self.valider = valider
        self.srid = srid

    def search(self
        ,service
        ,q=""
        ,vejnavn=""
        ,vejkode = ""
        ,husnr=""
        ,postnr=""
        ,kommunekode=""
        ,ejerlavkode = ""
        ,matrikelnr = ""
        ,esrejendomsnr = ""
        ,fuzzy=False
        ,):
        
        params = locals()

        if service in self.services:
            url = os.path.join(self.url, service)
        else:
            raise ValueError
        
        print(params)
        for param in params.keys():
            print(param, ":", params[param])
            if param in ["self", "service"]:
                continue
            elif (params[param] != "") & (type(params[param]).__name__ != "bool"):
                url = url + f"&{param}=" + params[param]
            elif params[param]:
                url = url + f"&{param}"
            
        print(url)
        
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            return response.json()
    
    def lookup(self, service, dawa_id):
        if service in self.services:
            url = os.path.join(self.url, service)
        else:
            raise ValueError
        
        url = os.path.join(url, dawa_id)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

    def autocomplete(self, service, q):
        url = os.path.join(self.url, "autocomplete")

    def datavask(self, service):
        pass

class Adgangsadresser(AdresseAPI):

    def __init__(
        self
        ,kvh=""):
        
        self.url = os.path.join(self.url, "adgangsadresser?")


class Adresser:
    
    def __init__(self):
        url = "https://api.dataforsyningen.dk/adresser"

class Autocomplete:

    def __init__(self):
        url = "https://api.dataforsyningen.dk/autocomplete"

class Navngivneveje:

    def __init__(self):
        url = "https://api.dataforsyningen.dk/navngivneveje"

class Vejstykker:

    def __init__(self):
        url = "https://api.dataforsyningen.dk/vejstykker"

class Vejnavne:

    def __init__(self):
        url = "https://api.dataforsyningen.dk/vejnavne"

class Postnumre:

    def __init__(self):
        url = "https://api.dataforsyningen.dk/postnumre"

class DAGI:
    pass

class Matrikel:
    pass

class BBR:
    pass

class Stednavn:
    pass

class Bygning:
    pass