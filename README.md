# concurrent-computing

## The API

This API was designed to be hosted on a Heroku App and integrated with 8 others for a college project.

## The Project

The process is about using kitchen oil to generate biodiesel. Each student would develop their own API to simulate a single step of the whole process, then the APIs would call each other and give biodiesel as output at the end. The oil tank is the starting point and is implemented here.

## How to run

#### On Heroku

* Fork or clone this repository to your own GitHub repository
* Upload it to Heroku
* Set up and enviroment variable. The KEY should be `BASE_URL` and the VALUE your API URL on Heroku
* Deploy master to Heroku
* Open App

#### Local

* Install the requirements from requirements.txt using `pip3 install -r requirements`
* Set up an enviroment variable for `BASE_URL`. It should be `htpp://localhost:5000` by default.
* Run main.py file using `python3 main.py`


## How it works

The API constantly adds to the oil volume every 5 seconds a random value between 100 and 200 liters, the oil tank has unlimited storage capacitiy.

You or someone else can make a POST request at `/oleo` and ask for oil, if the tank has enough oil it'll return your the amount you asked for.

Request Example:
```
json = {
  "volume": 30
}
```
