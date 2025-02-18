from flask import Flask, render_template , request
import requests
app = Flask(__name__)





@app.route("/")
def home():
    
    return  render_template("index.html")


@app.route("/weather", methods = ['POST'])
def get_place():
    try:
        if request.method == "POST":
            place = request.form['place']


            weather_data    = requests.get(f'https://api.tomorrow.io/v4/weather/realtime?location={place}&apikey=M3QZIUtGHaEDIFelvwatHwFP9UhHHmw7').json()

            temprature = weather_data['data']["values"]["temperature"]
            rainIntensity = weather_data['data']["values"]["rainIntensity"]
            humidity = weather_data['data']["values"]["humidity"]

            location = weather_data["location"]["name"]
            location_type = weather_data["location"]["type"]

            
            return render_template("weather.html" , location = location , location_type = location_type , humidity = humidity , rainIntensity = rainIntensity ,temprature = temprature)
        

    except requests.exceptions.RequestException as e:

        return f"Error with the weather API request: {e}"
    except KeyError as e:

        return f"Error: Missing expected data in the response: {e}"
    except Exception as e:

        return f"An unexpected error occurred: {e}"




if __name__ == '__main__':
    app.run(debug=True)
