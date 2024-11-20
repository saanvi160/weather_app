import streamlit as st
import requests

st.title("Weather Information App")

city = st.text_input("Enter City Name:")
if city:
    api_key = "7593cfa80b2d03b26caf4fe7c583bd58"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      weather = data["weather"][0]["description"]
      temp = data["main"]["temp"]
      st.write(f"Weather: {weather}")
      st.write(f"Temperature: {temp}°C")
    else:
      st.error(f"Error: {response.json().get('message', 'Unable to fetch data')}")

