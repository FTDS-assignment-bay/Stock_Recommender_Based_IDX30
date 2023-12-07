import pandas as pd
import streamlit as st
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
    q1 = calculate_score("Berapa lama jangka waktu investasi Anda - kapan Anda akan membutuhkan uang ini?", {
        "Within 3 years": 0,
        "3-5 years": 3,
        "6-10 years": 5,
        "11-15 years": 8,
        "15+ years": 10,
    })

    st.markdown(
        """
        <h4>Pertanyaan 2 :</h4>
        """,
        unsafe_allow_html=True
    )
    q2 = calculate_score("Apakah tujuan investasi penting Anda??", {
        "Untuk menjaga uang Anda": 0,
        "Untuk melihat pertumbuhan yang modera dalam akun Anda": 4,
        "Untuk melihat pertumbuhan yang lebih signifikan dalam akun Anda": 7,
        "Untuk mendapatkan pengembalian investasi yang tertinggi mungkin": 10
    })

    st.markdown(
        """
        <h4>Pertanyaan 3 :</h4>
        """, 
        unsafe_allow_html=True
    )
    q3 = calculate_score("Tolong tunjukkan pernyataan yang mencerminkan pandangan Anda secara keseluruhan terkait pengelolaan risiko!", {
        "Saya tidak suka risiko dan tidak bersedia menghadapkan investasi saya pada fluktuasi pasar apa pun demi mendapatkan pengembalian jangka panjang yang lebih tinggi.": 0,
        "Saya bersedia mengalami fluktuasi pasar yang moderat dalam jangka pendek untuk menghasilkan pertumbuhan modal.": 2,
        "Saya bersedia mengalami fluktuasi pasar yang rata-rata dalam jangka pendek untuk mencapai pengembalian jangka panjang yang lebih tinggi.": 4,
        "Saya ingin memaksimalkan pengembalian jangka panjang saya dan nyaman dengan fluktuasi pasar yang signifikan dalam jangka pendek.": 6,
    })
    
    st.markdown(
        """
        <h4>Pertanyaan 4 :</h4>
        """,
        unsafe_allow_html=True
    )
    q4 = calculate_score("Jika Anda memiliki investasi yang mengalami penurunan sebesar 20 persen dalam waktu singkat, apa yang akan Anda lakukan?", {
        "Menjual semua sisa investasi": 0,
        "Menjual sebagian dari sisa investasi": 2,
        "Menahan investasi dan tidak menjual apa pun": 4,
        "Membeli lebih banyak dari investasi tersebut": 6
    })

    st.markdown(
        """
        <h4>Pertanyaan 5:</h4>
        """,
        unsafe_allow_html=True
    )
    q5 = calculate_score("Jika Anda dapat meningkatkan peluang meningkatkan pengembalian investasi dengan mengambil risiko lebih besar, apakah Anda akan?", {
        "Tidak mungkin mengambil risiko lebih besar": 0,
        "Bersedia mengambil sedikit risiko dengan sebagian dari portofolio Anda": 2,
        "Bersedia mengambil risiko lebih besar dengan sebagian besar portofolio Anda": 4,
        "Bersedia mengambil risiko lebih besar dengan seluruh portofolio Anda": 6
    })

    st.markdown(
        """
        <h4>Pertanyaan 6:</h4>
        """,
        unsafe_allow_html=True
    )
    q6 = calculate_score("Gambar berikut menunjukkan tiga portofolio model dan pengembalian tertinggi dan terendah yang mungkin diperoleh masing-masing dalam setiap tahunnya. Portofolio mana yang kemungkinan besar Anda pegang?", {
        "Portofolio A (Pengembalian: -1 hingga 8%)": 0,
        "Portofolio B (Pengembalian: -6 hingga 15%)": 3,
        "Portofolio C (Pengembalian: -12 hingga 22%)": 6
    })

    st.markdown(
        """
        <h4>Pertanyaan 7:</h4>
        """,
        unsafe_allow_html=True
    )
    q7 = calculate_score("Setelah beberapa tahun mengikuti rencana keuangan Anda, Anda meninjau kemajuan Anda dan menentukan bahwa Anda tertinggal jadwal dan perlu memodifikasi strategi Anda untuk mencapai tujuan. Apa yang akan Anda lakukan?", {
        "Tetap memegang investasi yang saat ini Anda miliki, tetapi tingkatkan kontribusi sebanyak mungkin": 0,
        "Sedikit meningkatkan paparan Anda terhadap investasi yang lebih berisiko dan sedikit meningkatkan kontribusi Anda": 3,
        "Pindahkan seluruh portofolio Anda ke investasi yang lebih berisiko, dengan harapan mencapai pengembalian jangka panjang tertinggi": 6
    })

    st.markdown(
        """
        <h4>Pertanyaan 8:</h4>
        """,
        unsafe_allow_html=True
    )
    q8 = calculate_score("Pernyataan mana yang paling cocok dengan pendekatan Anda dalam mencapai tujuan keuangan tepat waktu?", {
        "Saya harus mencapai tujuan keuangan saya pada tanggal target": 0,
        "Saya ingin mendekati pencapaian tujuan keuangan saya pada tanggal target": 2,
        "Jika saya belum mencapai tujuan keuangan saya pada tanggal target, saya memiliki fleksibilitas untuk menunda tanggal target": 4,
        "Saya secara teratur mengevaluasi tujuan keuangan dan tanggal target saya dan memiliki fleksibilitas untuk menyesuaikannya dengan kinerja investasi saya": 6
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
                <p>Profil kategori Conservative dalam berinvestasi menunjukkan perilaku yang lebih berhati-hati dan lebih memprioritaskan perlindungan modal. Investor ini cenderung memiliki pengalaman dan pengetahuan yang terbatas tentang investasi, dan mungkin bahkan tidak memiliki pengalaman atau pengetahuan sama sekali di bidang ini. Oleh karena itu, untuk investor kategori <b>Conservative</b> yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain: </p>
            </div>
        """, unsafe_allow_html=True)
        st.write(', '.join(map(str, companies_in_cluster_1)))
        
    elif category == "Moderate":
        st.subheader("Profil Kategori: Moderate")
        companies_in_cluster_4 = dataset.loc[dataset['cluster'] == 4, 'company_id'].tolist()
        st.markdown("""
            <div style="margin-top: 10px; margin-bottom: 20px; font-size: 16px; text-align: justify; line-height: 1.5;">
                <p>Investor dengan profiling Moderate cenderung memilih portofolio yang memiliki potensi pertumbuhan sedang, seperti saham perusahaan yang telah terbukti stabil dan memiliki potensi pertumbuhan. Oleh karena itu, untuk investor kategori 'Moderate' yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain: </p>
            </div>
        """, unsafe_allow_html=True)
        st.write(', '.join(map(str, companies_in_cluster_4)))

    elif category == "Balanced":
        st.subheader("Profil Kategori: Balanced")
        companies_in_cluster_0 = dataset.loc[dataset['cluster'] == 0, 'company_id'].tolist()
        st.markdown("""
            <div style="margin-top: 10px; margin-bottom: 20px; font-size: 16px; text-align: justify; line-height: 1.5;">
                <p>Profil kategori Balanced dalam investasi mencerminkan pendekatan yang seimbang antara pertumbuhan dan keamanan. Investor dengan profil ini mampu menerima sejumlah risiko demi potensi keuntungan, sambil tetap memperhitungkan peluang pertumbuhan. Oleh karena itu, untuk investor kategori 'Balanced' yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain: </p>
            </div>
        """, unsafe_allow_html=True)
        st.write(', '.join(map(str, companies_in_cluster_0)))
        
    elif category == "Growth":
        st.subheader("Profil Kategori: Growth")
        companies_in_cluster_3 = dataset.loc[dataset['cluster'] == 3, 'company_id'].tolist()
        st.markdown("""
            <div style="margin-top: 10px; margin-bottom: 20px; font-size: 16px; text-align: justify; line-height: 1.5;">
                <p>Investor dengan profil Growth memiliki fokus pada pertumbuhan investasi dengan tingkat pengembalian yang tinggi. Mereka cenderung memilih portofolio yang menjanjikan potensi pertumbuhan yang signifikan dalam jangka panjang dan umumnya memiliki pengalaman yang cukup dalam dunia investasi. Oleh karena itu, untuk investor kategori 'Growth' yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain: </p>
            </div>
        """, unsafe_allow_html=True)
        st.write(', '.join(map(str, companies_in_cluster_3)))
        
    elif category == "Aggressive":
        st.subheader("Profil Kategori: Aggressive")
        companies_in_cluster_2 = dataset.loc[dataset['cluster'] == 2, 'company_id'].tolist()
        st.markdown("""
            <div style="margin-top: 10px; margin-bottom: 20px; font-size: 16px; text-align: justify; line-height: 1.5;">
                <p>Investor dengan profil Aggressive memiliki orientasi pada risiko dan menekankan pertumbuhan investasi dengan tingkat pengembalian yang tinggi. Mereka cenderung memilih portofolio yang memiliki risiko tinggi, termasuk saham perusahaan inovatif atau sektor-sektor industri yang tengah berkembang secara agresif. Oleh karena itu, untuk investor kategori 'Aggressive' yang tertarik dengan emiten dari indeks IDX30, terdapat sejumlah rekomendasi kode emiten yang dapat dipertimbangkan untuk melakukan investasi, antara lain:</p>
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
