import profiling
import profiling2
import streamlit as st
PAGES = {
    "Manulife": profiling,
    "Danamon": profiling2
}
st.sidebar.title('Pages')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()