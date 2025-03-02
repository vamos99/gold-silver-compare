import os
import time
import logging
import random
from google.generativeai import configure, GenerativeModel, list_models

class GeminiCommentator:
    def __init__(self):
        self.personalities = [
            "Komedyen", "Doktor", "Profesyonel Analist", "Psikolog", "Ekonomist",
            "Tarihçi", "Teknik Analist", "Yatırımcı", "Bankacı", "Filozof", 
            "Gazete Editörü", "Finans Uzmanı", "Borsa Yorumcusu"
        ]
        
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.api_working = False
        
        if not self.api_key:
            try:
                with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "env_setup.sh")) as f:
                    for line in f:
                        if "GEMINI_API_KEY" in line and "=" in line:
                            key_part = line.split("=")[1].strip().strip('"\'')
                            if key_part and key_part != "YOUR_API_KEY_HERE":
                                self.api_key = key_part
                                os.environ["GEMINI_API_KEY"] = key_part
                                logging.info("API anahtarı env_setup.sh dosyasından alındı.")
                                break
            except Exception as e:
                logging.error(f"env_setup.sh dosyasından API anahtarı alınamadı: {e}")
        
        if not self.api_key:
            logging.warning("GEMINI_API_KEY bulunamadı.")
            print("\033[91mUyarı: GEMINI_API_KEY bulunamadı! API kullanılamayacak.\033[0m")
            return
            
        try:
            configure(api_key=self.api_key)
            # Gemini Flash 2.0 için doğru model adını kullan
            model_name = "gemini-2.0-flash"  # veya "gemini-flash" veya "gemini-1.5-flash"
            try:
                self.model = GenerativeModel(model_name)
                self.api_working = True
                logging.info(f"Gemini API başarıyla yapılandırıldı. Model: {model_name}")
            except Exception as model_error:
                # İlk model başarısız olursa diğer modelleri dene
                alternative_models = ["gemini-1.0", "gemini-pro", "gemini-1.5-pro"]
                for alt_model in alternative_models:
                    try:
                        self.model = GenerativeModel(alt_model)
                        self.api_working = True
                        logging.info(f"Alternatif model başarıyla yapılandırıldı: {alt_model}")
                        break
                    except Exception:
                        continue
                
                if not self.api_working:
                    raise Exception("Hiçbir model yapılandırılamadı")
                    
        except Exception as e:
            logging.error(f"Gemini API yapılandırma hatası: {e}")
            print(f"\033[91mAPI yapılandırma hatası: {e}\033[0m")
            
            try:
                print("\033[93mKullanılabilir modeller listeleniyor...\033[0m")
                models = list_models()
                print("\nKullanılabilir Modeller:")
                for model in models:
                    print(f"- {model.name}")
            except Exception as list_error:
                print(f"\033[91mModeller listelenirken hata: {list_error}\033[0m")
    
    def test_api(self):
        if not self.api_working:
            print("\033[91mAPI yapılandırılmadı.\033[0m")
            return False
            
        try:
            response = self.model.generate_content("Merhaba, bu bir test mesajıdır.")
            print(f"\033[92mAPI çalışıyor! Cevap: {response.text}\033[0m")
            return True
        except Exception as e:
            print(f"\033[91mAPI test edilirken hata: {e}\033[0m")
            return False
    
    def ask_gemini(self, gold_change, silver_change, year):
        personality = random.choice(self.personalities)
        prompt = (
            f"{personality} gibi konuş. {year} yılında altın %{gold_change:.2f} değişti, "
            f"gümüş %{silver_change:.2f} değişti. Hangisi daha iyi kazandırdı? Çok kısa ve öz açıkla (1-2 cümle)."
        )
        
        if not self.api_working:
            logging.warning("Gemini API yapılandırılmadığı için basit hesaplama kullanılıyor.")
            return self._get_basic_response(gold_change, silver_change)
        
        for attempt in range(3):
            try:
                logging.info(f"Gemini API sorgu gönderiliyor (deneme {attempt+1}/3)")
                response = self.model.generate_content(prompt)
                
                if not response or not hasattr(response, 'text') or not response.text:
                    raise ValueError("API yanıt verdi ancak içerik boş")
                    
                return f"(Kişilik: {personality}) {response.text.strip()}"
                
            except Exception as e:
                logging.error(f"Gemini API hatası (deneme {attempt+1}/3): {e}")
                if attempt < 2:
                    time.sleep(3)
                    
        return self._get_basic_response(gold_change, silver_change)
    
    def _get_basic_response(self, gold_change, silver_change):
        if gold_change > silver_change:
            return f"Altın daha çok kazandırdı (%{gold_change:.2f})."
        return f"Gümüş daha çok kazandırdı (%{silver_change:.2f})."
