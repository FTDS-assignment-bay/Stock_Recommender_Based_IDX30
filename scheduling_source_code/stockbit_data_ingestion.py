# ==================================================================================================
# IMPORT LIBRARY
# ==================================================================================================
import pandas as pd # untuk menampung data scraped hasil dari BeautifulSoup
import psycopg2 as db

# ==================================================================================================
# FUNCTION LIST
# ==================================================================================================
def run_ingestion() :
    # load data dari file .csv ke dataframe
    formatted_data = pd.read_csv('<insert your csv file that has been cleaned>.csv')

    # ubah bentuk data ke dalam tuple
    temp_data_postgre = formatted_data.drop(['company_id'],axis=1) # drop kolom company_id
    data_postgre_ready = temp_data_postgre.T # lakukan transpose
    data_postgre_ready = data_postgre_ready.reset_index() # reset index
    data_postgre_ready.rename(columns={'index': 'column_name'},inplace=True) # ubah nama kolom 'index' menjadi 'column_name' 
    ready = data_postgre_ready.values.tolist() # ubah dataframe menjadi list

    # ubah isi list menjadi tuple
    for i in range(0,len(ready)) :
        ready[i] = tuple(ready[i])    

    ready = tuple(ready)

    # inisiasi koneksi ke postgresql
    postgre_db = '<insert your db name here>'
    postgre_user = '<insert your user name here>'
    postgre_password = '<insert your password here>'
    postgre_host = '<insert where you host the database here>'
    postgre_port = '<insert which port that your db used here>'

    # lakukan koneksi ke postgresql
    conn_string = f"dbname={postgre_db} host={postgre_host} user={postgre_user} password={postgre_password} port={postgre_port}"
    conn = db.connect(conn_string)

    # insert data ke table stockbit_idx_30_financials_table_ratio_per_quarter
    cur = conn.cursor()
    query_insert = cur.executemany(
        "INSERT INTO stockbit_idx_30_financials_table_ratio_per_quarter VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        , ready
    )

    # commit hasil insert query
    conn.commit()

    # tutup koneksi ke postgresql
    conn.close()

# ==================================================================================================
# MAIN CODE
# ==================================================================================================
if __name__ == '__main__' :
    run_ingestion()