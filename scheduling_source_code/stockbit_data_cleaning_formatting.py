
# ==================================================================================================
# IMPORT LIBRARY
# ==================================================================================================
from bs4 import BeautifulSoup # ambil struktur html dari website
import pandas as pd # untuk menampung data scraped hasil dari BeautifulSoup

# ==================================================================================================
# FUNCTION LIST
# ==================================================================================================
def table_header_extract(ratio_specific_table) :
    '''fungsi untuk extract data pada header table dari file .html yang telah di scrape, di return dalam bentuk list'''
    
    # scrape table header dengan elemen html berikut
    table_head_container = ratio_specific_table.find_all('th',{"class" : "periods-list"})

    # tambah satu value column_name 
    temp_list_head_data = ['column_name']
    
    
    for info_head_container in table_head_container :    
        # mencoba cari nama produk dari tag div class : prd_link-product-name css-3um8ox. Jika error, input value "no_data"
        try :
            temp_list_head_data.append(info_head_container.text)
        except :
            temp_list_head_data.append('no_data')

    return temp_list_head_data

def table_content_extract(ratio_specific_table) :
    '''fungsi untuk extract data pada content table dari file .html yang telah di scrape, di return dalam bentuk dictionary'''
    
    # scrape table content dengan elemen html berikut
    table_content_container = ratio_specific_table.find_all('tr',{"class" : "dtr"})

    # inisiasi element masing-masing baris pada table content
    td_class_formula = [
                        'formula13202','formula1474','formula1482','formula1476','formula21462',
                        'formula860','formula863','formula866','formula1480'
    ]

    # inisiasi dictionary kosong untuk menampung hasil
    temp_table_content_data = {}
    
    # iniasiasi penamaan key dengan format row_i
    i = 0

    # looping untuk ambil data pada table content
    for info_content_container in table_content_container :
        
        # inisiasi list kosong
        list_content_data = []

        # ambil data pada kolom pertama yang berupa text 
        list_content_data.append(info_content_container.find('span',{'class' : 'acc-name'}).text)

        # ambil seluruh data pada kolom berupa angka dengan element dari td_class_formula
        number_content_container = info_content_container.find_all('td',{'class' : td_class_formula[i]})

        # lakukan looping untuk memasukan data pada kolom angka
        for nbr in number_content_container :
            try :
                list_content_data.append(nbr.text)
            except :
                list_content_data.append('no_data')
        
        # inisiasi nama key
        key_name = 'row_'+str(i)

        # masukan ke dalam dictionary untuk data satu baris
        temp_table_content_data[key_name] = list_content_data

        i = i + 1
    
    return temp_table_content_data

def data_cleaning(list_content_table_raw, row_number_table) :
    '''
    fungsi untuk melakukan konversi text gabungan angka dan huruf (B,M,K) ke dalam tipe data float dari hasil 
    fungsi table_content_extract, output berupa list
    '''
    
    # looping untuk konversi gabungan angka dan huruf menjadi float
    for i in range(1,len(list_content_table_raw[row_number_table]),1) :
        
        # jika terdapat missing data, maka isi dengan 0
        if list_content_table_raw[row_number_table][i] == 'n/a' :
            list_content_table_raw[row_number_table][i] = float(0)

        # jika terdapat data, maka lakukan split antara angka dan huruf, angka dilakukan cleaning dan huruf dilakukan konversi ke angka
        else :           
            temp_data = list_content_table_raw[row_number_table][i].split()

            temp_data[0] = temp_data[0].replace(',','')
            temp_data[0] = temp_data[0].replace('(','')
            temp_data[0] = temp_data[0].replace(')','')
            temp_data[0] = float(temp_data[0])

            if temp_data[1] == 'B' :
                zero_multi = 1000000000
            elif temp_data[1] == 'M' :
                zero_multi = 1000000
            elif temp_data[1] == 'K' :
                zero_multi = 1000
            else :
                zero_multi = 0
            
            list_content_table_raw[row_number_table][i] = temp_data[0] * zero_multi

    return list_content_table_raw

def data_change_type(list_content_table_raw, row_number_table) :
    '''
    fungsi untuk mengubah angka yang masih berupa text menjadi float dari hasil fungsi table_content_extract, 
    output berupa list
    '''

    # looping untuk konversi angka text menjadi float
    for i in range(1,len(list_content_table_raw[row_number_table]),1) :
        
        if list_content_table_raw[row_number_table][i] == 'n/a' :
            list_content_table_raw[row_number_table][i] = float(0)
        else :
            list_content_table_raw[row_number_table][i] = float(list_content_table_raw[row_number_table][i])    

    return list_content_table_raw

def data_formatting(list_content_table_raw, row_number_table) :
    '''
    fungsi untuk mengubah angka persentase yang masih berupa text menjadi float dari hasil fungsi table_content_extract, 
    output berupa list
    '''
    
    # looping untuk konversi angka dengan persentase text menjadi float
    for i in range(1,len(list_content_table_raw[row_number_table]),1) :

        if list_content_table_raw[row_number_table][i] == 'n/a' :
            list_content_table_raw[row_number_table][i] = float(0)
        else :
            temp_data = list_content_table_raw[row_number_table][i]
            temp_data = temp_data.replace('%','')
            list_content_table_raw[row_number_table][i] = float(temp_data) * 0.01

    return list_content_table_raw

def to_dataframe(header_data, content_data,cmp_id) :
    '''
    fungsi untuk mengubah hasil data yang sudah dilakukan cleaning & formatting menggunakan ketiga fungsi data_cleaning, 
    data_change_type, dan data_formatting menjadi bentuk dataframe dengan format yang sesuai pada tampilan stockbit
    
    '''
    
    # inisiasi dataframe baru
    final_data = pd.DataFrame(columns=header_data)

    # lakukan looping untuk mengisi data pada final_data
    for filling in content_data :
        final_data.loc[final_data.size] = filling

    # reset index
    final_data.reset_index(inplace=True)
    final_data.drop(['index'],axis=1,inplace=True)

    # tambah 1 kolom baru sebagai identifier data dari company mana
    final_data['company_id'] = cmp_id

    return final_data


def run_cleaning_data() :
    '''fungsi ini untuk menjalankan proses data cleaning secara menyeluruh'''

    # inisiasi list company dari IDX30
    list_idx_30 = [
                'BBCA','BBRI','TLKM','BMRI','ASII','ADRO','UNVR','INDF','ANTM','PGAS',
                'PTBA','KLBF','BBNI','ITMG','UNTR','SMGR','GOTO','CPIN','HRUM','INCO',
                'MEDC','BRPT','ARTO','MDKA','BUKA','AKRA','TOWR','EMTK','AMRT','ESSA'               
    ]

    # inisiasi nama kolom pada final_data
    list_final_data = ['column_name', 'Q3 2023', 'Q2 2023', 'Q1 2023', 'Q4 2022', 'Q3 2022', 'Q2 2022', 'Q1 2022', 
                        'Q4 2021', 'Q3 2021', 'Q2 2021', 'Q1 2021', 'Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020', 
                        'Q4 2019', 'Q3 2019', 'Q2 2019', 'Q1 2019', 'Q4 2018', 'Q3 2018', 'Q2 2018', 'Q1 2018', 
                        'Q4 2017', 'Q3 2017', 'Q2 2017', 'Q1 2017', 'Q4 2016', 'Q3 2016', 'Q2 2016', 'Q1 2016', 
                        'Q4 2015', 'Q3 2015', 'Q2 2015', 'Q1 2015', 'Q4 2014', 'Q3 2014', 'Q2 2014', 'Q1 2014', 
                        'Q4 2013', 'Q3 2013', 'Q2 2013', 'Q1 2013', 'Q4 2012', 'Q3 2012', 'Q2 2012', 'Q1 2012', 
                        'Q4 2011', 'Q3 2011', 'Q2 2011', 'Q1 2011', 'Q4 2010', 'Q3 2010', 'Q2 2010', 'Q1 2010', 
                        'Q4 2009', 'Q3 2009', 'Q2 2009', 'Q1 2009', 'Q4 2008', 'Q3 2008', 'Q2 2008', 'Q1 2008',
                        'Q4 2007', 'company_id'
    ]

    # iniasiasi dataframe untuk menampung hasil
    final_data = pd.DataFrame(columns=list_final_data)

    # looping masing-masing company dengan ID dan hasil scrape file .html nya 
    for cmp in list_idx_30 :    
        with open('<insert your html scrape file here>.html') as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        # lakukan pembatasan hanya di div class = 'tbl-ratio'
        table_ratio_container = soup.body.find('div',{"class" : "tbl-ratio"})

        # ambil header table
        list_head_data = table_header_extract(table_ratio_container)

        # ambil isi table
        table_content_data = table_content_extract(table_ratio_container)
        
        # proses cleaning & formatting data
        clean_data = list(table_content_data.values())
        
        clean_data = data_cleaning(clean_data,0)
        clean_data = data_change_type(clean_data,1)
        clean_data = data_change_type(clean_data,2)
        clean_data = data_change_type(clean_data,3)
        clean_data = data_cleaning(clean_data,4)
        clean_data = data_formatting(clean_data,5)
        clean_data = data_formatting(clean_data,6)
        clean_data = data_formatting(clean_data,7)
        clean_data = data_change_type(clean_data,8)

        result_data = to_dataframe(list_head_data, clean_data, cmp)

        final_data = pd.concat([final_data,result_data],ignore_index=True,axis=0)

        # isi missing value dengan angka 0
        final_data.fillna(value=float(0),inplace=True)

    # rename nama column
    rename_column = final_data.columns
    column_step_one = [y.lower() for y in rename_column]
    column_step_two = [z.replace(' ','_') for z in column_step_one]
    final_data.columns = column_step_two

    final_data['column_name'] = final_data['column_name'].str.replace(' (Quarter)','')
    final_data['column_name'] = final_data['column_name'].str.replace(' ','_')
    final_data['column_name'] = final_data['column_name'].str.lower()

    # reverse kolom company_id menjadi di depan
    reverse_column = list(final_data.columns)
    reverse_column.reverse()

    final_data = final_data[reverse_column]

    # ==================================================================================================
    # DATAFRAME NEW FORMAT FOR MODELING PROCESS
    # ==================================================================================================

    # inisiasi nama kolom untuk dataframe dengan format baru
    new_column_name = ['company_id']

    first_column_name = final_data['column_name'].unique()
    second_column_name = list(final_data.columns.drop(['column_name','company_id']))

    for first in first_column_name :
        for second in second_column_name :
            new_column_name.append(first+'_'+second)

    formatted_data = pd.DataFrame(columns=new_column_name)


    # looping process untuk masing-masing company dari IDX30
    for new_idx in list_idx_30 :
        
        # filter data untuk company new_idx
        company_data = final_data[final_data['company_id'] == new_idx]

        # lakukan reset index
        company_data.reset_index(inplace=True)
        company_data.drop(columns=['index'],inplace=True)

        # ambil data pada baris pertama sebagai acuan
        first_data = company_data.loc[[0]]

        # ambil nama kolom
        first_data_column = first_data.columns
        
        # inisiasi prefix header dari column_name pada baris pertama
        prefix_header = first_data['column_name'][0]

        # assign header baru dengan prefix_header dengan y
        first_new_header = [prefix_header+'_'+y for y in first_data_column]

        # rename kolom lama dengan kolom baru
        first_data.columns = first_new_header

        # rename khusus untuk company_id
        first_data.rename(columns={prefix_header+'_company_id' : 'company_id'},inplace=True)
        
        # drop kolom column_name
        first_data.drop([prefix_header+'_column_name'],axis=1,inplace=True)

        # lakukan looping untuk baris kedua hingga baris ke 9 dengan proses yang sama seperti diatas
        for i in range(1,9,1) :
            next_data = company_data.loc[[i]]
            next_data_column = next_data.columns
            next_prefix_header = next_data['column_name'][i]
            next_new_header = [next_prefix_header+'_'+y for y in next_data_column]
            next_data.columns = next_new_header
            next_data.rename(columns={next_prefix_header+'_company_id' : 'company_id'},inplace=True)
            next_data.drop([next_prefix_header+'_column_name'],axis=1,inplace=True)
        
            # lakukan merge baris pertama dengan baris selanjutnya
            first_data = first_data.merge(next_data, on='company_id',how='left')

        # masukan data hasil looping ke dalam dataframe dengan format terbaru
        formatted_data = pd.concat([formatted_data,first_data], ignore_index=True, axis=0)

    # simpan data hasil format terbaru ke dalam .csv
    formatted_data.to_csv('<insert your csv file name here>.csv',mode='w',index=False)


# ==================================================================================================
# MAIN CODE
# ==================================================================================================
if __name__ == '__main__' :
    run_cleaning_data()