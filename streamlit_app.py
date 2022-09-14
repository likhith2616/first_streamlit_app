import streamlit
streamlit.title('MY PARENTS NEW HEALTHY DINER')
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
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)),['Avacado,Strawberries')]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
