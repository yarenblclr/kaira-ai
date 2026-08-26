# Kaira AI – B2B Kozmetik Satış Asistanı

Kaira AI, toptan kozmetik satışı yapan Kaira markası için geliştirilmiş yapay zekâ destekli bir B2B satış uygulamasıdır.

## Projenin Amacı

Kaira'nın toptan satış müşterilerinin ürünler ve sipariş süreci hakkında yapay zekâ destekli bilgi almasını ve potansiyel müşteri taleplerinin kayıt altına alınmasını sağlamaktır.

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- HTML, CSS ve JavaScript
- Groq API
- Gunicorn
- Render
- Wix
- Git ve GitHub

## Sistem Nasıl Çalışıyor?

Kullanıcı Wix üzerindeki Kaira sitesinden AI satış asistanına mesaj gönderir.

Mesaj akışı:

Wix → Flask Backend → AIService → Groq API → Flask → Wix

Groq API anahtarı frontend tarafında tutulmaz. `.env` dosyasında saklanır ve `.gitignore` sayesinde GitHub'a gönderilmez.

## Backend Endpointleri

- `GET /health` → Backend'in çalışıp çalışmadığını kontrol eder.
- `POST /api/sohbet` → Kullanıcı mesajını AI servisine gönderir.
- `POST /api/leads` → Potansiyel müşteri kaydı oluşturur.
- `GET /api/leads` → Müşteri kayıtlarını listeler.
- `GET /dashboard` → Yönetim panelini gösterir.
- `GET /assistant` → Wix'e gömülen AI asistanını gösterir.

## Veritabanı

Müşteri talepleri SQLite veritabanında saklanmaktadır.

## Güvenlik

API anahtarları kaynak kod içerisine yazılmamıştır.

`.env`, `venv/` ve `kaira.db` GitHub repository'sine gönderilmez.

## Çalıştırma

Gerekli paketleri yüklemek için:

```bash
pip install -r requirements.txt