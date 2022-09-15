import pandas
import streamlit
streamlit.title('MY MOMS NEW HEALTHY DINER')
streamlit.header('Breakfast Menu')
streamlit.text('1. Oats & Corns')
streamlit.text('2. Spinach')
streamlit.text('3. cakes')
streamlit.text('-------------------------------------------------------------')

streamlit.header('Breakfast Favorites')
streamlit.text('1. Omega 3 & Blueberry Oatmeal')
streamlit.text('2. Kale, Spinach & Rocket Smoothie')
streamlit.text('3. Hard-Boiled Free-Range Egg')
streamlit.text('4. Avacado')
streamlit.text('-------------------------------------------------------------')

streamlit.header('Build Your Own Fruit Smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)),[('Avacado,Strawberries')]
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section to display API fruity vice response
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/apple")
streamlit.text(fruityvice_response.json())
                
