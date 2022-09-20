[11:33 AM] Aplut .
import streamlit
import pandas
import requests
import snowflake.connector

from urllib.error import URLError



streamlit.title('My name is Aplut')
streamlit.title('chennai is okay')

streamlit.header('Breakfast Menu 🥣 🥗 🐔 🥑🍞')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


def get_fruityvice_data(this_fruit_choice):  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())  return fruityvice_normalized


streamlit.header("Fruityvice Fruit Advice!")
try:  fruit_choice = streamlit.text_input('What fruit would you like information about?')  if not fruit_choice:    streamlit.error('Please select the fruit to get information.')  else:    back_from_function= get_fruityvice_data(fruit_choice)    streamlit.dataframe(back_from_function)
except URLError as e:  streamlit.error()

    

  
#streamlit.write('The user entered ', fruit_choice)

#streamlit.text(fruityvice_response.json())

#streamlit.stop()




streamlit.header("View Our Fruit List - Add Your Favorites!")

def get_fruit_load_list():  with my_cnx.cursor() as my_cur:    my_cur.execute("select * from fruit_load_list")    return my_cur.fetchall()
if streamlit.button('Get Fruit Load List'):  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])  my_data_rows=get_fruit_load_list()  my_cnx.close()  streamlit.dataframe(my_data_rows)  

def insert_row_snowflake(new_fruit):  with my_cnx.cursor() as my_cur:    my_cur.execute("insert into fruit_load_list values('"+new_fruit+"')")    return "Thanks for adding "+new_fruit    

fruit_choice = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])    back_from_function = insert_row_snowflake(fruit_choice)    streamlit.text(back_from_function)

