import logging
import yfinance as yf

class MetalDataFetcher:
    def __init__(self, symbol, year):
        self.symbol = symbol
        self.year = year
    
    def fetch_data(self):
        start_date = f"{self.year}-01-01"
        end_date = f"{self.year}-12-31"
        try:
            logging.info(f"{self.symbol} için {start_date} - {end_date} arası veriler indiriliyor.")
            data = yf.download(self.symbol, start=start_date, end=end_date, progress=False)
            if data.empty:
                logging.warning(f"{self.year} yılı için {self.symbol} verisi bulunamadı.")
                return None
            logging.info(f"{len(data)} kayıt bulundu.")
            return data
        except Exception as e:
            logging.error(f"Veri çekme hatası: {e}")
            return None
