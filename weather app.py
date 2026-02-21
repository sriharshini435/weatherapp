import streamlit as st
import json
import requests


st.title("Weather app ⛅")
st.write("This application helps you display the weather information of different cities")
api_key = "39fcd22d8dfe4504bdd124819241109"
city=st.text_input("Enter a city name")

if st.button("display"):
    if city.strip()!= "" :
        base_url = (f"http://api.weatherapi.com/v1/current.json?key=39fcd22d8dfe4504bdd124819241109&q={city}&aqi=no")
        p = {
            'appid': api_key,
            'q': city
        }
        response=requests.get(base_url,params=p)
        if response.status_code ==200:
            data=response.json()
            #st.write(data)
            c=data["current"]["condition"]["icon"]
            c = "https:" + c
            st.image(c,width=100)
            st.subheader(f'☁️The weather info of {city}☁️ :')
            st.subheader(f'⏲️The date and time is, {data['location']['localtime']}⏲️')
            st.subheader(f"country: {data["location"]["country"]},city:{data["location"]["name"]}")
            st.write(f"🌡️Temp in celcius: {data['current']['temp_c']}C🌡️")
            st.write(f"🌡️Temp in farenheit: {data['current']['temp_f']}F🌡️")
            st.write(f"💧Humdity: {data['current']['humidity']}💧")
            st.write(f'The weather feels like {data["current"]["condition"]["text"]}')
            #hw: complete displaying eind speed and uv
            st.write(f"💨wind speed:{data["current"]["wind_kph"]}wind speed💨")
            st.write(f"uv:{data["current"]["uv"]}")

        else:
            st.error("pls enter a valid city or country")
