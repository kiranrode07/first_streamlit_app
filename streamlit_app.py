import streamlit

streamlit.title ('My parents new healthy dinner')

streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Omega 3 & Blueberry oat meal')
streamlit.text ('🥗 Kale, spinnach and rocket smoothie')
streamlit.text ('🐔 Hard boiled free-range eggs')
streamlit.text ('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
