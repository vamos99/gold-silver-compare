# Altin ve Gumus Karsilastirma Araci

Bu klasor, belirli bir yil icin altin ve gumus fiyat performansini karsilastiran
Python uygulamasini icerir. Uygulama fiyat verisini alir, temel performans
hesaplarini yapar ve grafik uretir. Gemini API anahtari tanimliysa ek yorum
metni de uretebilir.

## Ozellikler

- Yahoo Finance fiyat verisi cekme
- Altin/gumus yillik getiri karsilastirmasi
- Matplotlib ile grafik uretimi
- API anahtari varsa Gemini destekli yorum
- API anahtari yoksa hesaplama odakli fallback cikti
- Basit loglama ve hata mesaji yonetimi

## Kurulum

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ortam Degiskeni

Gemini yorum ozelligi opsiyoneldir:

```bash
export GEMINI_API_KEY="your_api_key"
```

Ornek dosya:

```bash
cp env_setup.sh.example env_setup.sh
```

`env_setup.sh` icine gercek anahtar yaziliyorsa bu dosya Git'e eklenmemelidir.

## Calistirma

```bash
python main.py
```

## Proje Yapisi

- `main.py`: uygulama giris noktasi
- `src/data_fetcher.py`: fiyat verisi alma
- `src/analyzer.py`: getiri ve karsilastirma hesaplari
- `src/plotter.py`: grafik uretimi
- `src/commentator.py`: opsiyonel Gemini yorum katmani

## Sinirlar

- Finansal karar destegi veya yatirim tavsiyesi amacli degildir.
- Dis veri kaynagi ve opsiyonel Gemini API durumuna bagli calisir.
- Test ve veri dogrulama kapsami sinirlidir; repo egitim calismasi olarak
  tutulmustur.
