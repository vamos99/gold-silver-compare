import os
import sys
import logging
from src.data_fetcher import MetalDataFetcher
from src.analyzer import PerformanceAnalyzer
from src.plotter import PerformancePlotter
from src.commentator import GeminiCommentator

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/agent_log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def main():
    setup_logging()
    os.makedirs("reports", exist_ok=True)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test-api":
        commentator = GeminiCommentator()
        commentator.test_api()
        return
    
    try:
        year = int(input("Hangi yılı analiz etmek istersiniz? "))
    except ValueError:
        print("Lütfen geçerli bir yıl girin.")
        return
    
    logging.info(f"{year} yılı için analiz başlatıldı.")
    
    # Veri çekme
    gold_fetcher = MetalDataFetcher("GC=F", year)
    silver_fetcher = MetalDataFetcher("SI=F", year)
    
    gold_data = gold_fetcher.fetch_data()
    silver_data = silver_fetcher.fetch_data()
    
    if not all([gold_data is not None, silver_data is not None]):
        print("Veri çekme hatası. Logları kontrol edin.")
        return
    
    # Analiz
    g_start, g_end, g_change = PerformanceAnalyzer.analyze(gold_data)
    s_start, s_end, s_change = PerformanceAnalyzer.analyze(silver_data)
    
    # Sonuçları göster
    print(f"\n{year} Yılı Sonuçları:")
    print(f"Altın: Başlangıç: ${g_start:.2f}, Bitiş: ${g_end:.2f}, Getiri: %{g_change:.2f}")
    print(f"Gümüş: Başlangıç: ${s_start:.2f}, Bitiş: ${s_end:.2f}, Getiri: %{s_change:.2f}")
    
    # AI yorumu
    commentator = GeminiCommentator()
    comment = commentator.ask_gemini(g_change, s_change, year)
    print("\nGemini Yorumu:", comment)
    
    # Grafik
    if PerformancePlotter.plot(gold_data, silver_data, year):
        print(f"\nGrafik kaydedildi: reports/performance_{year}.png")
    else:
        print("\nGrafik kaydedilemedi. Logları kontrol edin.")

if __name__ == "__main__":
    main()
