import streamlit as st
import manulife_profiling
import danamon_profiling

st.markdown(
    """
    <style>
        body {
            background-color: #87CEEB;  /* Ganti dengan warna atau gambar latar belakang yang diinginkan */
        }
        .skyblue-text {
            color: #007bff; /* kode hex untuk skyblue */
        }
    </style>
    """,
    unsafe_allow_html=True
    )
# Fungsi untuk menampilkan halaman profiling
def display_profiling_page(page):
    if page == "Manulife Profiling":
        manulife_profiling.app()
    elif page == "Danamon Profiling":
        danamon_profiling.app()

# Tampilan awal dengan dua kartu
st.markdown(
    """
    <h2 class="skyblue-text" style="text-align:center;">Investor Profile Questionnaire</h2>
    """,
    unsafe_allow_html=True
)
st.title("")

# Kartu untuk Manulife Profiling
col1, col2 = st.columns(2)
with col1:
    st.subheader("Manulife Profiling")
    # st.image("manulife_logo.png", use_column_width=True)
    if st.button("Go to Manulife Profiling"):
        st.experimental_set_query_params(page="Manulife Profiling")

# Kartu untuk Danamon Profiling
with col2:
    st.subheader("Danamon Profiling")
    # st.image("danamon_logo.png", use_column_width=True)
    if st.button("Go to Danamon Profiling"):
        st.experimental_set_query_params(page="Danamon Profiling")

# Tangkap nilai dari parameter query "page"
selected_page = st.experimental_get_query_params().get("page", [""])[0]

# Tampilkan halaman profiling sesuai dengan pilihan pengguna
if selected_page:
    display_profiling_page(selected_page)
