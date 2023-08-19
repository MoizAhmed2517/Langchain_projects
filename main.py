from cuisine_list import cuisines
import streamlit as st
from langchain_wrapper import prompt_chain_response

st.title("Restaurant Name Generator")
cuisine_select = st.sidebar.selectbox("Pick a Cuisine", cuisines)

if cuisine_select:
    heading = prompt_chain_response(cuisine_select)
    st.markdown(f"Your restaurant name will be **{heading['restaurant_name']}**")
    st.write("**Menu item**")
    for items in heading['menu_item'].split(','):
        st.write("-", items)
        