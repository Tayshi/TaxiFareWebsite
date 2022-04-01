import streamlit as st

# import controllers streamlit
import datetime

# import build/call/retrieve/display (End step)
import requests
import numpy as np

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

# - date and time - pickup_datetime : 2013-07-06 17:18:00
# date
date = st.date_input(
    "Date",
    datetime.date(2013, 7, 6))
st.write('Date is:', date)

# time
time = st.time_input('Time', datetime.time(17, 18, 00))
st.write('Time set for', time)


# - pickup longitude - pickup_longitude : -73.950655
nb_pick_lon = st.number_input('Insert a pickup longitude', value=-73.950655)
st.write('The pickup longitude is ', nb_pick_lon)

# - pickup latitude - pickup_latitude : 40.783282
nb_pick_lat = st.number_input('Insert a pickup latitude', value=40.783282)
st.write('The pickup latitude is ', nb_pick_lat)

# - dropoff longitude - dropoff_longitude : -73.984365
nb_dropoff_lon = st.number_input('Insert a dropoff longitude', value=-73.984365)
st.write('The dropoff longitude is ', nb_dropoff_lon)

# - dropoff latitude - dropoff_latitude : 40.769802
nb_dropoff_lat = st.number_input('Insert a dropoff latitude', value=40.769802)
st.write('The dropoff latitude is ', nb_dropoff_lat)


# - passenger count - passenger_count): 1
# with slider ?
passenger_count = st.slider('Select a passenger count', 1, 10, 1)
st.write('passenger count', passenger_count)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

'''

2. Let's build a dictionary containing the parameters for our API...
'''

# - date and time - pickup_datetime : 2013-07-06 17:18:00
# - pickup longitude - pickup_longitude : -73.950655
# - pickup latitude - pickup_latitude : 40.783282
# - dropoff longitude - dropoff_longitude : -73.984365
# - dropoff latitude - dropoff_latitude : 40.769802
# - passenger count - passenger_count): 1

pickup_datetime = f"{date} {time}"

dict_predict = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': nb_pick_lon,
    'pickup_latitude': nb_pick_lat,
    'dropoff_longitude': nb_dropoff_lon,
    'dropoff_latitude': nb_dropoff_lat,
		'passenger_count': passenger_count

}
dict_predict

'''
3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

@st.cache
def get_predict():

    # my_url = 'https://docker-tfm-ipbs6r3hdq-ew.a.run.app/predict'
    my_url = 'https://api-ipbs6r3hdq-ew.a.run.app/predict'
    url_wagon = 'https://taxifare.lewagon.ai/predict'
    response = requests.get(url_wagon, params=dict_predict) # my_url
    taxi_fare = response.json()
    return round(taxi_fare['fare'], 2)

st.write('', get_predict())


# lat_lon_np = np.array([[float(nb_pick_lat), float(nb_pick_lon)],
#              [float(nb_dropoff_lat), float(nb_dropoff_lon)]])

# @st.cache
# def get_map_data():

#     return pd.DataFrame(
#             lat_lon_np,
#             columns=['lat', 'lon']
#         )

# df = get_map_data()
# st.map(df)
