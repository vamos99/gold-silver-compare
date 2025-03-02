import os
import logging
import matplotlib.pyplot as plt

class PerformancePlotter:
    @staticmethod
    def plot(gold_data, silver_data, year):
        try:
            # ... plotting code from original file ...
            if not os.path.exists("reports"):
                os.makedirs("reports", exist_ok=True)
                
            # Veri hazırlama ve grafik çizimi
            gold_data = gold_data.sort_index()
            silver_data = silver_data.sort_index()
            
            # İlk değerleri baz alarak yüzde değişimleri hesapla
            gold_base = gold_data['Close'].iloc[0]
            silver_base = silver_data['Close'].iloc[0]
            
            gold_pct_change = (gold_data['Close'] - gold_base) / gold_base * 100
            silver_pct_change = (silver_data['Close'] - silver_base) / silver_base * 100
            
            # Grafik çizimi
            fig, ax = plt.subplots(figsize=(10, 5))
            plt.plot(gold_data.index, gold_pct_change, color='gold', label='Altın')
            plt.plot(silver_data.index, silver_pct_change, color='gray', label='Gümüş')
            
            plt.axhline(y=0, color='r', linestyle='-', alpha=0.3)
            plt.xlabel('Tarih')
            plt.ylabel('% Değişim')
            plt.title(f"{year} Yılı Altın ve Gümüş Performans Karşılaştırması")
            plt.legend()
            plt.grid(True, alpha=0.3)
            
            # Etiketler
            gold_final = float(gold_pct_change.iloc[-1].item())
            silver_final = float(silver_pct_change.iloc[-1].item())
            
            plt.annotate(f"Altın: %{gold_final:.2f}", 
                        xy=(gold_data.index[-1], gold_final),
                        xytext=(10, 0), textcoords='offset points')
            plt.annotate(f"Gümüş: %{silver_final:.2f}", 
                        xy=(silver_data.index[-1], silver_final),
                        xytext=(10, 0), textcoords='offset points')
            
            plt.tight_layout()
            plt.savefig(f"reports/performance_{year}.png")
            return True
            
        except Exception as e:
            logging.error(f"Grafik oluşturma hatası: {e}")
            return False
