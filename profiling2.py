import streamlit as st

def app():
    st.markdown(
    """
    <style>
        .skyblue-text {
            text-align: center;
            color: #87CEEB; /* kode hex untuk skyblue */
        }
    </style>
    """,
    unsafe_allow_html=True
    )

    def calculate_category(total_score):
        if total_score >= 0 and total_score <= 11:
            return "CONSERVATIVE"
        elif total_score >= 12 and total_score <= 19:
            return "MODERATE"
        elif total_score >= 20 and total_score <= 28:
            return "BALANCED"
        elif total_score >= 29 and total_score <= 35:
            return "GROWTH"
        elif total_score >= 36 and total_score <= 40:
            return "AGGRESSIVE"
        
    def calculate_score(question, options):
        selected_option = st.radio(question, options)
        score = options[selected_option]
        return score
    
    st.markdown(
        """
        <h1 class="skyblue-text">Investor Profile Questionnaire</h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown('---')
    
    st.header("Pertanyaan 1:")
    q1 = calculate_score("Apakah tujuan investasi Anda?", {
        "Pertumbuhan kekayaan untuk jangka panjang": 5,
        "Pendapatan dan pertumbuhan dalam jangka panjang": 4,
        "Pendapatan berkala": 3,
        "Pendapatan dan keamanan dana investasi": 2,
        "Keamanan dana investasi": 1,
    })

    st.header("Pertanyaan 2:")
    q2 = calculate_score("Berdasarkan tujuan investasi Anda, dana Anda akan diinvestasikan untuk jangka waktu?", {
        "≥ 10 tahun": 5,
        "7 - 10 tahun": 4,
        "4 - ≥ 6 tahun": 3,
        "1 - ≥ 3 tahun": 2,
        "< 1 tahun": 1
    })

    st.header("Pertanyaan 3:")
    q3 = calculate_score("Berapa lama pengalaman Anda berinvestasi dalam produk yang nilainya berfluktuasi seperti saham, Reksa Dana, mata uang asing, komoditi, produk investasi terstruktur, waran, opsi, futures serta asuransi yang mengandung investasi?", {
        "> 10 tahun": 5,
        "8 - 10 tahun": 4,
        "4 - 7 tahun": 3,
        "< 4 tahun": 2,
        "0 tahun (Tidak Berpengalaman)": 1
    })
    
    st.header("Pertanyaan 4:")
    q4 = calculate_score("Jenis investasi apa yang pernah dan/atau masih Anda miliki?", {
        "Opsi": 5,
        "Saham, Reksadana": 4,
        "Mata uang asing": 3,
        "Obligasi": 2,
        "Uang tunai": 1
    })

    st.header("Pertanyaan 5:")
    q5 = calculate_score("Berapa persen dari aset milik Anda saat ini yang disimpan dalam bentuk produk investasi yang berfluktuasi, seperti contoh yang produk yang telah disebutkan pada pertanyaan nomor 3 di atas?", {
        "> 50%": 5,
        "> 25% - ≥ 50%": 4,
        "> 10% - ≥ 25%": 3,
        "> 0% - ≥ 10%": 2,
        "0%": 1
    })

    st.header("Pertanyaan 6:")
    q6 = calculate_score("Berapa persen tingkat kenaikan dan penurunan nilai produk investasi (fluktuasi) yang dapat Anda terima?", {
        "<-20% - > +20%": 5,
        "-20% - +20%": 4,
        "-15% - +15%": 3,
        "-10% - +10%": 2,
        "-5% - +5%": 1
    })

    st.header("Pertanyaan 7:")
    q7 = calculate_score("Bagaimana tingkat ketergantungan Anda pada hasil investasi untuk membiayai kebutuhan hidup sehari-hari?", {
        "Tidak bergantung pada hasil investasi sama sekali": 5,
        "Tidak bergantung pada hasil investasi, minimum sampai 5 tahun ke depan": 4,
        "Sedikit bergantung pada hasil investasi": 3,
        "Bergantung pada hasil investasi": 2,
        "Sangat bergantung pada hasil investasi": 1,
    })

    st.header("Pertanyaan 8:")
    q8 = calculate_score("Pada umumnya berapa persen dari pendapatan bulanan rumah tangga Anda yang dapat disisihkan dan digunakan untuk investasi dan/atau tabungan?", {
        "> 50%": 5,
        "> 25% - 50%": 4,
        "> 10% - 25%": 3,
        "> 0% - 10%": 2,
        "0%": 1
    })

    total_score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8
    
    st.success(f"Total Skor Profil Investasi Anda: {total_score} Kategori {calculate_category(total_score)}")