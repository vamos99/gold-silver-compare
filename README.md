# Gold Silver Compare

Bu repo, altin ve gumus fiyat hareketlerini belirli bir yil icin karsilastiran
egitim amacli Python calismasini icerir. Kaynak kod `projectGPT/` klasorundedir.

## Kapsam

- Yahoo Finance uzerinden fiyat verisi alma
- Yillik performans karsilastirmasi
- Grafik olusturma
- Gemini API anahtari varsa yorum uretme, yoksa hesaplama odakli cikti verme

## Calistirma

```bash
cd projectGPT
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Gemini yorumu icin:

```bash
export GEMINI_API_KEY="..."
```

API anahtari yoksa proje temel fiyat karsilastirmasi ve grafik uretimiyle
calisacak sekilde tasarlanmistir.

## Notlar

- Bu calisma yatirim tavsiyesi degildir.
- Repo egitim/odev teslimi olarak konumlandirilmistir.
- ZIP gibi teslim artefaktlari yerine kaynak kod ve rapor dosyalari takip
  edilmelidir.
