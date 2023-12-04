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
        if total_score >= 0 and total_score <= 7:
            return "CONSERVATIVE"
        elif total_score >= 8 and total_score <= 22:
            return "MODERATE"
        elif total_score >= 23 and total_score <= 37:
            return "BALANCED"
        elif total_score >= 38 and total_score <= 48:
            return "GROWTH"
        elif total_score >= 49 and total_score <= 56:
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
    q1 = calculate_score("Berapa lama jangka waktu investasi Anda - kapan Anda akan membutuhkan uang ini?", {
        "Within 3 years": 0,
        "3-5 years": 3,
        "6-10 years": 5,
        "11-15 years": 8,
        "15+ years": 10,
    })

    st.header("Pertanyaan 2:")
    q2 = calculate_score("Apakah tujuan investasi penting Anda??", {
        "Untuk menjaga uang Anda": 0,
        "Untuk melihat pertumbuhan yang modera dalam akun Anda": 4,
        "Untuk melihat pertumbuhan yang lebih signifikan dalam akun Anda": 7,
        "Untuk mendapatkan pengembalian investasi yang tertinggi mungkin": 10
    })

    st.header("Pertanyaan 3:")
    q3 = calculate_score("Tolong tunjukkan pernyataan yang mencerminkan pandangan Anda secara keseluruhan terkait pengelolaan risiko!", {
        "Saya tidak suka risiko dan tidak bersedia menghadapkan investasi saya pada fluktuasi pasar apa pun demi mendapatkan pengembalian jangka panjang yang lebih tinggi.": 0,
        "Saya bersedia mengalami fluktuasi pasar yang moderat dalam jangka pendek untuk menghasilkan pertumbuhan modal.": 2,
        "Saya bersedia mengalami fluktuasi pasar yang rata-rata dalam jangka pendek untuk mencapai pengembalian jangka panjang yang lebih tinggi.": 4,
        "Saya ingin memaksimalkan pengembalian jangka panjang saya dan nyaman dengan fluktuasi pasar yang signifikan dalam jangka pendek.": 6,
    })
    
    st.header("Pertanyaan 4:")
    q4 = calculate_score("Jika Anda memiliki investasi yang mengalami penurunan sebesar 20 persen dalam waktu singkat, apa yang akan Anda lakukan?", {
        "Menjual semua sisa investasi": 0,
        "Menjual sebagian dari sisa investasi": 2,
        "Menahan investasi dan tidak menjual apa pun": 4,
        "Membeli lebih banyak dari investasi tersebut": 6
    })

    st.header("Pertanyaan 5:")
    q5 = calculate_score("Jika Anda dapat meningkatkan peluang meningkatkan pengembalian investasi dengan mengambil risiko lebih besar, apakah Anda akan?", {
        "Tidak mungkin mengambil risiko lebih besar": 0,
        "Bersedia mengambil sedikit risiko dengan sebagian dari portofolio Anda": 2,
        "Bersedia mengambil risiko lebih besar dengan sebagian besar portofolio Anda": 4,
        "Bersedia mengambil risiko lebih besar dengan seluruh portofolio Anda": 6
    })

    st.header("Pertanyaan 6:")
    q6 = calculate_score("Gambar berikut menunjukkan tiga portofolio model dan pengembalian tertinggi dan terendah yang mungkin diperoleh masing-masing dalam setiap tahunnya. Portofolio mana yang kemungkinan besar Anda pegang?", {
        "Portofolio A (Pengembalian: -1 hingga 8%)": 0,
        "Portofolio B (Pengembalian: -6 hingga 15%)": 3,
        "Portofolio C (Pengembalian: -12 hingga 22%)": 6
    })

    st.header("Pertanyaan 7:")
    q7 = calculate_score("Setelah beberapa tahun mengikuti rencana keuangan Anda, Anda meninjau kemajuan Anda dan menentukan bahwa Anda tertinggal jadwal dan perlu memodifikasi strategi Anda untuk mencapai tujuan. Apa yang akan Anda lakukan?", {
        "Tetap memegang investasi yang saat ini Anda miliki, tetapi tingkatkan kontribusi sebanyak mungkin": 0,
        "Sedikit meningkatkan paparan Anda terhadap investasi yang lebih berisiko dan sedikit meningkatkan kontribusi Anda": 3,
        "Pindahkan seluruh portofolio Anda ke investasi yang lebih berisiko, dengan harapan mencapai pengembalian jangka panjang tertinggi": 6
    })

    st.header("Pertanyaan 8:")
    q8 = calculate_score("Pernyataan mana yang paling cocok dengan pendekatan Anda dalam mencapai tujuan keuangan tepat waktu?", {
        "Saya harus mencapai tujuan keuangan saya pada tanggal target": 0,
        "Saya ingin mendekati pencapaian tujuan keuangan saya pada tanggal target": 2,
        "Jika saya belum mencapai tujuan keuangan saya pada tanggal target, saya memiliki fleksibilitas untuk menunda tanggal target": 4,
        "Saya secara teratur mengevaluasi tujuan keuangan dan tanggal target saya dan memiliki fleksibilitas untuk menyesuaikannya dengan kinerja investasi saya": 6
    })

    total_score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8
    
    st.success(f"Total Skor Profil Investasi Anda: {total_score} Kategori {calculate_category(total_score)}")