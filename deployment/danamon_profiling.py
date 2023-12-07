import streamlit as st
import pandas as pd
from pandas.api.types import (is_categorical_dtype)

def app():
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
    
    dataset1 = pd.read_csv('../dataset/hasil_clustering.csv')
    dataset2 = pd.read_csv('../dataset/daily_stock_price_idx_30_dataset.csv')
    
    dataset = pd.concat([dataset1, dataset2['stock_price']], axis=1)
    
    def calculate_category(total_score):
        if total_score >= 0 and total_score <= 7:
            return "Conservative"
        elif total_score >= 8 and total_score <= 22:
            return "Moderate"
        elif total_score >= 23 and total_score <= 37:
            return "Balanced"
        elif total_score >= 38 and total_score <= 48:
            return "Growth"
        elif total_score >= 49 and total_score <= 56:
            return "Aggressive"
        
    def calculate_score(question, options):
        selected_option = st.radio(question, options)
        score = options[selected_option]
        return score
    
    st.markdown(
        """
        <h4>Pertanyaan 1 :</h4>
        """,
        unsafe_allow_html=True
    )
    q1 = calculate_score("Apakah tujuan investasi Anda?", {
        "Pertumbuhan kekayaan untuk jangka panjang": 5,
        "Pendapatan dan pertumbuhan dalam jangka panjang": 4,
        "Pendapatan berkala": 3,
        "Pendapatan dan keamanan dana investasi": 2,
        "Keamanan dana investasi": 1,
    })

    st.markdown(
        """
        <h4>Pertanyaan 2 :</h4>
        """,
        unsafe_allow_html=True
    )
    q2 = calculate_score("Berdasarkan tujuan investasi Anda, dana Anda akan diinvestasikan untuk jangka waktu?", {
        "≥ 10 tahun": 5,
        "7 - 10 tahun": 4,
        "4 - ≥ 6 tahun": 3,
        "1 - ≥ 3 tahun": 2,
        "< 1 tahun": 1
    })

    st.markdown(
        """
        <h4>Pertanyaan 3 :</h4>
        """,
        unsafe_allow_html=True
    )
    q3 = calculate_score("Berapa lama pengalaman Anda berinvestasi dalam produk yang nilainya berfluktuasi seperti saham, Reksa Dana, mata uang asing, komoditi, produk investasi terstruktur, waran, opsi, futures serta asuransi yang mengandung investasi?", {
        "> 10 tahun": 5,
        "8 - 10 tahun": 4,
        "4 - 7 tahun": 3,
        "< 4 tahun": 2,
        "0 tahun (Tidak Berpengalaman)": 1
    })
    
    st.markdown(
        """
        <h4>Pertanyaan 4 :</h4>
        """,
        unsafe_allow_html=True
    )
    q4 = calculate_score("Jenis investasi apa yang pernah dan/atau masih Anda miliki?", {
        "Opsi": 5,
        "Saham, Reksadana": 4,
        "Mata uang asing": 3,
        "Obligasi": 2,
        "Uang tunai": 1
    })

    st.markdown(
        """
        <h4>Pertanyaan 5 :</h4>
        """,
        unsafe_allow_html=True
    )
    q5 = calculate_score("Berapa persen dari aset milik Anda saat ini yang disimpan dalam bentuk produk investasi yang berfluktuasi, seperti contoh yang produk yang telah disebutkan pada pertanyaan nomor 3 di atas?", {
        "> 50%": 5,
        "> 25% - ≥ 50%": 4,
        "> 10% - ≥ 25%": 3,
        "> 0% - ≥ 10%": 2,
        "0%": 1
    })

    st.markdown(
        """
        <h4>Pertanyaan 6 :</h4>
        """,
        unsafe_allow_html=True
    )
    q6 = calculate_score("Berapa persen tingkat kenaikan dan penurunan nilai produk investasi (fluktuasi) yang dapat Anda terima?", {
        "<-20% - > +20%": 5,
        "-20% - +20%": 4,
        "-15% - +15%": 3,
        "-10% - +10%": 2,
        "-5% - +5%": 1
    })

    st.markdown(
        """
        <h4>Pertanyaan 7 :</h4>
        """,
        unsafe_allow_html=True
    )
    q7 = calculate_score("Bagaimana tingkat ketergantungan Anda pada hasil investasi untuk membiayai kebutuhan hidup sehari-hari?", {
        "Tidak bergantung pada hasil investasi sama sekali": 5,
        "Tidak bergantung pada hasil investasi, minimum sampai 5 tahun ke depan": 4,
        "Sedikit bergantung pada hasil investasi": 3,
        "Bergantung pada hasil investasi": 2,
        "Sangat bergantung pada hasil investasi": 1,
    })

    st.markdown(
        """
        <h4>Pertanyaan 8 :</h4>
        """,
        unsafe_allow_html=True
    )
    q8 = calculate_score("Pada umumnya berapa persen dari pendapatan bulanan rumah tangga Anda yang dapat disisihkan dan digunakan untuk investasi dan/atau tabungan?", {
        "> 50%": 5,
        "> 25% - 50%": 4,
        "> 10% - 25%": 3,
        "> 0% - 10%": 2,
        "0%": 1
    })

    total_score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8
    
    category = calculate_category(total_score)
    st.success(f"Total Skor Profiling Anda : {total_score} dengan Kategori {category}")

    # Menampilkan informasi dari dataset berdasarkan kategori
    if category == "Conservative":
        st.markdown(
        """
        <h4 class="skyblue-text" style="text-align:center">Profil Kategori: Conservative</h4>
        """,
        unsafe_allow_html=True
        )
        companies_in_cluster_1 = dataset.loc[dataset['cluster'] == 1, 'company_id']
        st.markdown("""
            <div style="font-size: 16px; text-align: justify; line-height: 1.5;">
                <p>Profiling dengan kategori <b>Conservative</b> dalam investasi menggambarkan gaya investasi yang lebih hati-hati dan <b>Conservative</b>. Investor dengan profil ini cenderung mengutamakan perlindungan modal dan kestabilan nilai investasi mereka. Oleh karena itu, untuk investor kategori <b>Conservative</b> yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain: </p>
            </div>
        """, unsafe_allow_html=True)
        st.write(', '.join(map(str, companies_in_cluster_1)))
        
    elif category == "Moderate":
        st.subheader("Profil Kategori: Moderate")
        companies_in_cluster_4 = dataset.loc[dataset['cluster'] == 4, 'company_id'].tolist()
        st.markdown("""
            <div style="margin-top: 10px; margin-bottom: 20px; font-size: 16px; text-align: justify; line-height: 1.5;">
                <p>Investor dengan profiling 'Moderate' cenderung memilih portofolio yang memiliki potensi pertumbuhan sedang, seperti saham perusahaan yang telah terbukti stabil dan memiliki potensi pertumbuhan. Oleh karena itu, untuk investor kategori 'Moderate' yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain: </p>
            </div>
        """, unsafe_allow_html=True)
        st.write(', '.join(map(str, companies_in_cluster_4)))

    elif category == "Balanced":
        st.subheader("Profil Kategori: Balanced")
        companies_in_cluster_0 = dataset.loc[dataset['cluster'] == 0, 'company_id'].tolist()
        st.markdown("""
            <div style="margin-top: 10px; margin-bottom: 20px; font-size: 16px; text-align: justify; line-height: 1.5;">
                <p>Profiling dengan kategori 'Balanced' dalam investasi menggambarkan gaya investasi yang seimbang antara pertumbuhan dan keamanan. Investor dengan profil ini cenderung mengutamakan perlindungan modal dan kestabilan nilai investasi mereka, sambil tetap mempertimbangkan peluang pertumbuhan. Oleh karena itu, untuk investor kategori 'Balanced' yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain: </p>
            </div>
        """, unsafe_allow_html=True)
        st.write(', '.join(map(str, companies_in_cluster_0)))
        
    elif category == "Growth":
        st.subheader("Profil Kategori: Growth")
        companies_in_cluster_3 = dataset.loc[dataset['cluster'] == 3, 'company_id'].tolist()
        st.markdown("""
            <div style="margin-top: 10px; margin-bottom: 20px; font-size: 16px; text-align: justify; line-height: 1.5;">
                <p>Investor dengan profil 'Growth' memiliki fokus pada pertumbuhan investasi dengan tingkat pengembalian yang tinggi. Kategori ini cenderung memilih portofolio yang memiliki potensi pertumbuhan yang signifikan. Oleh karena itu, untuk investor kategori 'Growth' yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain: </p>
            </div>
        """, unsafe_allow_html=True)
        st.write(', '.join(map(str, companies_in_cluster_3)))
        
    elif category == "Aggressive":
        st.subheader("Profil Kategori: Aggressive")
        companies_in_cluster_2 = dataset.loc[dataset['cluster'] == 2, 'company_id'].tolist()
        st.markdown("""
            <div style="margin-top: 10px; margin-bottom: 20px; font-size: 16px; text-align: justify; line-height: 1.5;">
                <p>Investor dengan profil 'Aggressive' memiliki orientasi pada risiko dan fokus pada pertumbuhan investasi dengan tingkat pengembalian yang tinggi. Kategori ini cenderung memilih portofolio yang berisiko tinggi, termasuk saham perusahaan inovatif atau sektor-sektor industri yang tengah berkembang secara agresif. Oleh karena itu, untuk investor kategori 'Aggressive' yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain:</p>
            </div>
        """, unsafe_allow_html=True)
        st.write(', '.join(map(str, companies_in_cluster_2)))
    
    company_mapping = {
    'BBCA': 'PT Bank Central Asia Tbk',
    'BBRI': 'PT Bank Rakyat Indonesia Tbk',
    'TLKM': 'PT Telekomunikasi Indonesia Tbk',
    'BMRI': 'PT Bank Mandiri Tbk',
    'ASII': 'PT Astra International Tbk',
    'ADRO': 'PT Adaro Energy Tbk',
    'UNVR': 'PT Unilever Indonesia Tbk',
    'INDF': 'PT Indofood Sukses Makmur Tbk',
    'ANTM': 'PT Aneka Tambang Tbk',
    'PGAS': 'PT Perusahaan Gas Negara Tbk',
    'PTBA': 'PT Bukit Asam Tbk',
    'KLBF': 'PT Kalbe Farma Tbk',
    'BBNI': 'PT Bank Negara Indonesia Tbk',
    'ITMG': 'PT Indo Tambangraya Megah Tbk',
    'UNTR': 'PT United Tractors Tbk',
    'SMGR': 'PT Semen Indonesia Tbk',
    'GOTO': 'PT GoTo Indonesia Tbk',
    'CPIN': 'PT Charoen Pokphand Indonesia Tbk',
    'HRUM': 'PT Harum Energy Tbk',
    'INCO': 'PT Vale Indonesia Tbk',
    'MEDC': 'PT Medco Energi Internasional Tbk',
    'BRPT': 'PT Bumi Resources Tbk',
    'ARTO': 'PT Aneka Roda Tbk',
    'MDKA': 'PT Merdeka Copper Gold Tbk',
    'BUKA': 'PT Bukalapak.com Tbk',
    'AKRA': 'PT AKR Corporindo Tbk',
    'TOWR': 'PT Tower Bersama Infrastructure Tbk',
    'EMTK': 'PT Elang Mahkota Teknologi Tbk',
    'AMRT': 'PT Sumber Alfaria Trijaya Tbk',
    'ESSA': 'PT Sri Rejeki Isman Tbk'
    }
    
    dataset['company_name'] = dataset['company_id'].map(company_mapping)
    
    def filter_dataframe(df: pd.DataFrame, category: str) -> pd.DataFrame:
        global column
        global left
        global right
        
        if category == "Balanced":
            list_recomendation = companies_in_cluster_0
        elif category == "Conservative":
            list_recomendation = companies_in_cluster_1
        elif category == "Aggressive":
            list_recomendation = companies_in_cluster_2
        elif category == "Growth":
            list_recomendation = companies_in_cluster_3
        elif category == "Moderate":
            list_recomendation = companies_in_cluster_4
            
        modification_container = st.container()
        with modification_container:
            show = ['company_id', 'company_name', 'stock_price', 'share_outstanding_q3_2023', 'eps_q3_2023', 'pe_ratio_q3_2023', 'price_to_sales_q3_2023', 'ebitda_q3_2023', 'return_on_assets_q3_2023', 'return_on_equity_q3_2023', 'return_on_capital_employed_q3_2023', 'interest_coverage_q3_2023']
            to_filter = st.multiselect("Filter column", options=list(df.columns), default=show)
            df = df[to_filter]
            to_filter_columns = ['company_id']

        for column in to_filter_columns:
            left, right = st.columns((1, 40))
            left.write("↳")
            
            if is_categorical_dtype(df[column]) or df[column].nunique():
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    list_recomendation,
                    default=list_recomendation,
                )
                df = df[df[column].isin(user_cat_input)]
                
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]
        return df            
    
    def filter_dataframe_show(df: pd.DataFrame, category: str) -> pd.DataFrame:
        global column
        global left
        global right
        
        if category == "Balanced":
            list_recomendation = companies_in_cluster_0
        elif category == "Conservative":
            list_recomendation = companies_in_cluster_1
        elif category == "Aggressive":
            list_recomendation = companies_in_cluster_2
        elif category == "Growth":
            list_recomendation = companies_in_cluster_3
        elif category == "Moderate":
            list_recomendation = companies_in_cluster_4
            
        modification_container = st.container()
        with modification_container:
            show = ['company_id', 'company_name', 'stock_price', 'share_outstanding_q3_2023', 'eps_q3_2023', 'pe_ratio_q3_2023', 'price_to_sales_q3_2023', 'ebitda_q3_2023', 'return_on_assets_q3_2023', 'return_on_equity_q3_2023', 'return_on_capital_employed_q3_2023', 'interest_coverage_q3_2023']
            df = df[show]
            to_filter_columns = ['company_id']

        for column in to_filter_columns:
            if is_categorical_dtype(df[column]) or df[column].nunique():
                df = df[df[column].isin(list_recomendation)]
        return df            
    
    modify = st.checkbox("Add filters")
    df = dataset
    
    if modify:
        return st.dataframe(filter_dataframe(dataset, category))
    else:
        st.dataframe(filter_dataframe_show(dataset, category))