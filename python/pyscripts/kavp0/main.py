import requests
import webbrowser

apiKeyFile = open("apikey.txt", 'r')
API_KEY = apiKeyFile.readline() 
apiKeyFile.close()


distanceMatrixURL  = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

def get_travel_time(start, end):
    r = requests.get(distanceMatrixURL + "origins=" + start + "&destinations=" + end + "&key=" + API_KEY)
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]  
    return("Trip Info:\n{} -> {}\nTime: {}".format(start, end, time))



print(get_travel_time("California", "New York"))