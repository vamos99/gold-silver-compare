import logging

class PerformanceAnalyzer:
    @staticmethod
    def analyze(data):
        try:
            start_price = float(data['Close'].iloc[0].item())
            end_price = float(data['Close'].iloc[-1].item())
            change_percentage = ((end_price - start_price) / start_price) * 100
            return start_price, end_price, change_percentage
        except Exception as e:
            logging.error(f"Analiz hatası: {e}")
            return None, None, None
