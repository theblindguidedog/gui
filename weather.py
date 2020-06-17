from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Air Quality App')
root.geometry("600x100")

# Create Zipcode Lookup Function
def zipLookup():
    #zip.get()
    #zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row=1, column=0, columnspan=2)
    
    # Vegas Zip 89129, Baton Rouge Area 70801
    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=761C9502-4E89-4148-ADCA-7ACE99C66391")
        api = json.loads(api_request.content)
        date = api[0]['DateObserved']
        state = api[0]['StateCode']
        city = api[0]['ReportingArea']
        quality = str(api[0]['AQI'])
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"  #42e924
        elif category == "Moderate":
            weather_color = "#FFFF00" #fcff34
        elif category == "Unhealthy for Sensitive Groups":
                weather_color = "#f57e22" #ff9900
        elif category == "Unhealthy":
            weather_color = "#f4001c" #FFFF00
        elif category == "Very Unhealthy":
            weather_color = "#8b3696" #990066
        elif category == "Hazardous":
            weather_color = "#780025" #660000

        root.configure(background=weather_color)

        myLabel = Label(root, text=city + " " + "(" + state + ")" + " Air Quality " + quality + " " + "(" + category + ")", font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)
zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)


root.mainloop()
