# Flask based weather APP

## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console
$ python3 -m venv venv
```

2. You also need to create a `.env` file and API_KEY from https://openweathermap.org/api

```console
API=<API_KEY>
```

3. Start the application:

```console
$ python weather.py
```

4. To view weather for your city, visit the URL: 

```console
http://127.0.0.1:5000/forecast?city={city}
```


![FastAPI](https://github.com/PremKarira/Weather_APP/blob/main/1.png?raw=true)



## License

This project is licensed under the terms of MIT license.