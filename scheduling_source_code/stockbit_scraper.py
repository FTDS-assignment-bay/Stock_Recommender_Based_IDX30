# ==================================================================================================
# IMPORT LIBRARY
# ==================================================================================================
from selenium import webdriver # untuk proses otomasi scrape
from time import sleep # untuk menambah jeda setiap proses scraping

# ==================================================================================================
# CLASS & FUNCTION DEFINITION
# ==================================================================================================
# inisiasi class untuk scrape file .html dari stockbit 
# untuk path hasil download .html dapat disesuaikan dengan device masing-masing
# referensi https://github.com/basnugroho/indonesia-stocks-scraper/blob/master/Stockbit/Stockbit_Downloader

class Stockbit_Downloader:
    '''class untuk mendefinisikan instance scraping untuk Stockbit'''
    def __init__(self, download_path='<insert your scrape result path here>',
                 target_url='https://stockbit.com/'):
        '''fungsi init untuk mendefinisikan lokasi hasil scrape file .html, target url yang akan di scraped, dan inisiasi webdriver yang akan digunakan'''
        self.download_path = download_path # inisiasi download_path
        self.driver = webdriver.Chrome() # perlu dicek kompatibilitas webdriver dengan chrome version agar berjalan lancar, letakkan webdriver di satu folder yang sama dgn file ini
        self.target_url = target_url # inisiasi target_url yang akan dilakukan scraping
        self.empty_inlineXBRL_list = []
        self.submitted_inlineXBRL_list = []

    def login(self, username="<insert your username in stockbit>", password="<insert your password in stockbit>"):
        '''fungsi untuk melakukan otomasi login ke target_url'''
        self.driver.get(self.target_url+"#/login") # inisiasi driver untuk membuka halaman login dari stockbit
        inputUsername = self.driver.find_element_by_xpath('//input[@id="username"]') # otomasi input username dengan mencari element xpath
        inputUsername.send_keys(username)
        inputPass = self.driver.find_element_by_xpath('//input[@id="password"]') # otomasi input password dengan mencari element xpath
        inputPass.send_keys(password)
        loginBtn = self.driver.find_element_by_id(id_="email-login-button") # otomasi klik tombol login dengan mencari id dari button tersebut
        loginBtn.click()

    def load_stock_financials(self, stock):
        '''fungsi untuk membuka halaman financials dari suatu nama company dengan variable stock'''
        self.driver.get(self.target_url+"#/symbol/"+stock+"/financials")

    def close_browser(self):
        '''fungsi untuk menutup halaman dari stockbit'''
        self.driver.close()

    def save_income_statement_html(self, stock_code):
        '''fungsi untuk menyimpan data hasil scrape ke dalam bentuk .html'''
        try:
            file = open('<insert your scrape result path here>.html', 'w', encoding='utf-8')
            file.write(self.driver.page_source)
            file.close()
        except:
            print('save file error')


def run_scraper() :
    '''fungsi utama untuk jalankan proses scraping'''
    # list company yang akan di scraped datanya
    list_idx_30 = [
                'BBCA','BBRI','TLKM','BMRI','ASII','ADRO','UNVR','INDF','ANTM','PGAS',
                'PTBA','KLBF','BBNI','ITMG','UNTR','SMGR','GOTO','CPIN','HRUM','INCO',
                'MEDC','BRPT','ARTO','MDKA','BUKA','AKRA','TOWR','EMTK','AMRT','ESSA'               
    ]

    # jalankan proses scrape
    dl = Stockbit_Downloader()
    dl.login(); sleep(5)
    for idx_thirty in list_idx_30 :
        dl.load_stock_financials(idx_thirty); sleep(5) # kode ini dan dibawahnya perlu di looping dari list IDX30 di stockbit
        dl.save_income_statement_html(idx_thirty); sleep(5)
    dl.close_browser()

# ==================================================================================================
# MAIN CODE
# ==================================================================================================

if __name__ == '__main__' :
    run_scraper()