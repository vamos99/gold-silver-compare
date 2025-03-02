# Altın vs Gümüş Yatırım Analizi (Gold vs Silver Investment Analysis)

Bu proje, belirli bir yılda **altın mı yoksa gümüş mü daha çok kazandırdı** sorusuna **Yahoo Finance API** ve **Gemini Flash 2.0 API** kullanarak cevap veren bir yapay zeka tabanlı analiz aracıdır.

## 📌 Özellikler

- 📊 **Yahoo Finance API** kullanarak geçmiş altın ve gümüş fiyat verilerini çeker.
- 🧠 **Gemini Flash 2.0 API** ile farklı kişiliklerde yatırım analizleri sunar.
- 🔢 **Matematiksel yedekleme sistemi**, Gemini API çalışmazsa temel hesaplamalar yapar.
- 📈 **Grafikler oluşturur**, yatırımcıların görsel olarak karşılaştırma yapmasını sağlar.
- 📝 **Log sistemi**, veri çekme ve API hatalarını kaydederek hata ayıklamayı kolaylaştırır.
- 🏗️ **SOLID ve Clean Code prensiplerine uygun şekilde geliştirilmiştir.
- 🛠️ **Virtual Environment** (Sanal Ortam) kullanarak bağımlılıkları izole eder.
- 📄 **Detaylı bir rapor ve README içeriğiyle birlikte ZIP olarak teslim edilmeye hazırdır.

---

## 🚀 Kurulum

### 1️⃣ Depoyu Kopyalayın
Öncelikle projeyi yerel makinenize klonlayın veya ZIP dosyası olarak indirin:

```bash
git clone https://github.com/vamos99/gold-silver-compare.git
cd gold-silver-compare
```

### 2️⃣ Virtual Environment Oluşturun ve Etkinleştirin

Python bağımlılıklarını izole etmek için bir sanal ortam oluşturun:

```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux için
venv\Scripts\activate      # Windows için
```

### 3️⃣ Gerekli Kütüphaneleri Yükleyin

Bağımlılıkları yüklemek için:

```bash
pip install -r requirements.txt
```

### 4️⃣ API Anahtarlarını Tanımlayın

`env_setup.sh` dosyasını oluşturun ve aşağıdaki gibi API anahtarlarınızı girin:

```bash
#!/bin/bash
export GEMINI_API_KEY="your_gemini_api_key"
```

### 5️⃣ Uygulamayı Çalıştırın

```bash
python compare.py
```

## 📊 Kullanım

1. Programı çalıştırdıktan sonra belirtilen yıl için altın ve gümüş fiyat analizini alabilirsiniz.
2. Eğer Gemini API çalışmazsa, sistem matematiksel yedekleme mekanizmasını devreye sokacaktır.
3. Çıktılar hem grafiksel hem de metinsel olarak sunulacaktır.

## 📜 Kullanılan Teknolojiler

- Python 3.x
- Yahoo Finance API
- Gemini Flash 2.0 API
- Matplotlib, Pandas, Requests
- SOLID & Clean Code Prensipleri
- Logging Mekanizması

## 📖 Proje Geliştirme Süreci

Bu proje geliştirilirken aşağıdaki yapay zeka modellerinden destek alınmıştır:
- Claude 3.7
- Claude 3.5 Sonnet
- GPT-4
- Gemini Flash 2.0

Tüm modeller, kod yapısı, optimizasyonlar ve analiz yöntemleri hakkında geri bildirim sağlamak için kullanılmıştır.
