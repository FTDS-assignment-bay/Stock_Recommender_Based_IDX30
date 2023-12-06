# ==================================================================================================
# IMPORT LIBRARY
# ==================================================================================================
import schedule
import time
import stockbit_scraper as ss
import stockbit_data_cleaning_formatting as sdcf
import stockbit_data_ingestion as sdi

# ==================================================================================================
# FUNCTION LIST
# ==================================================================================================
def first_process():
    ss.run_scraper()

def second_process():
    sdcf.run_cleaning_data()

def third_process():
    sdi.run_ingestion()

# ==================================================================================================
# TASK SCHEDULING
# ==================================================================================================

# lakukan penjadwalan setiap 93 hari sekali

# lakukan task pertama pada jam 8 pagi
schedule.every(93).day.at("08:00").do(first_process)

# lakukan task kedua pada jam 8 pagi
schedule.every(93).day.at("08:30").do(second_process)

# lakukan task ketiga pada jam 8 pagi
schedule.every(93).day.at("09:00").do(third_process)

# ==================================================================================================
# MAIN CODE
# ==================================================================================================
while True:
 
    # cek jika ada task yang masih di pending untuk dijalankan atau tidak
    schedule.run_pending()
    time.sleep(1)