# AI Haber Yayın Sistemi

## Proje Amacı

Yapay zeka destekli haber toplama,
özetleme,
seslendirme,
video üretimi
ve yayınlama sistemi.

---

## Hedefler

- Günlük haberleri toplamak
- AI ile özetlemek
- Seslendirmek
- Video üretmek
- Web sitesinde yayınlamak
- YouTube kanalında yayınlamak

---

## Hedef Platformlar

### Web Sitesi

Korhanors.com

### YouTube

AI Haber Bülteni

### Podcast

Spotify
Apple Podcasts

---

## Kullanılacak Teknolojiler

### Backend

Python

### Yapay Zeka

OpenAI

### Seslendirme

ElevenLabs

### Video

MoviePy

### Veritabanı

SQLite

Gelecekte:
PostgreSQL

---

## Ana Modüller

- `news_fetcher.py` - RSS kaynaklarından haber çeker
- `news_cleaner.py` - HTML etiketlerini ve gereksiz boşlukları temizler
- `news_filter.py` - kısa/eksik haberleri, tekrar başlıkları ve önem puanını yönetir
- `news_categorizer.py` - haberleri kategoriye ayırır
- `statistics.py` - kategori bazlı istatistik üretir
- `script_generator.py` - günlük yayın metni üretir
- `html_generator.py` - istatistikli ve kategorili HTML haber paneli üretir
- `ai_summarizer.py` - OpenAI özeti için ayrıldı
- `text_to_speech.py` - seslendirme fazı için ayrıldı
- `video_creator.py` - video üretimi fazı için ayrıldı
- `publisher.py` - yayınlama otomasyonu için ayrıldı

---

## Güncel Çıktılar

- `data/raw/latest-news.json`
- `data/raw/YYYY-MM-DD-news.json`
- `data/stats/latest-statistics.json`
- `data/stats/YYYY-MM-DD-statistics.json`
- `outputs/scripts/daily-news-script.txt`
- `outputs/scripts/YYYY-MM-DD-script.txt`
- `outputs/html/daily-news.html`
- `outputs/html/YYYY-MM-DD-news.html`
