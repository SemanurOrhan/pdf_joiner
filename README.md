# PDF Birleştirici (PyPDF2)

Küçük bir komut satırı aracı: listedeki PDF dosyalarını sırasıyla tek bir PDF dosyasında birleştirir. PyPDF2 kullanır.

## Gereksinimler

- Python 3.9+ (Windows/Powershell ile test edildi)
- pip
- Bağımlılıklar: `PyPDF2` (bkz. `requirements.txt`)

## Kurulum

PowerShell'de sanal ortam oluşturup bağımlılıkları yükleyin:

```powershell
# Proje klasörüne geçin
cd c:\Users\LENOVO\Desktop\pdf_joiner

# Sanal ortam (opsiyonel ama tavsiye edilir)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Bağımlılıklar
pip install -r requirements.txt
```

## Kullanım

PDF dosyalarını `pdf_joiner.py` ile aynı klasöre koyun ve birleştirme sırasını `pdf_joiner.py` içindeki `pdf_list` dizisinde belirleyin. Ardından çalıştırın:

```powershell
python pdf_joiner.py
```

- Çıktı dosyası adı: `merged.pdf`
- Birleştirme sırası: `pdf_list` dizisindeki sıra

### Sıralamayı/Dosyaları Değiştirme
`pdf_joiner.py` içindeki şu bölümü düzenleyin:

```python
pdf_list = [
    "1.pdf",
    "2.pdf",
    "3.pdf",
    "4.pdf",
    "5.pdf",
    "6.pdf",
    "7.pdf",
]
```

## Yaygın Hatalar ve Çözümler
### Yaygın Hatalar ve Çözümleri

- Dosya bulunamadı  
    - Betik çalıştırdığınız dizinde dosyanın gerçekten olduğundan emin olun. Farklı dizindeki dosyaları kullanacaksanız mutlak yol verin. Örnekler:
        ```python
        # raw string (Windows \ kaçışlarını önler)
        pdf = r"C:\Users\PCName\Desktop\pdf_joiner\1.pdf"

        # veya pathlib ile (daha güvenli)
        from pathlib import Path
        pdf = str(Path(__file__).parent / "1.pdf")
        ```
    - Betikle aynı dizinde çalıştırmak için:
        ```python
        from pathlib import Path
        import os
        os.chdir(Path(__file__).parent)
        ```

- Dosya kilitli / erişim hatası  
    - PDF başka bir program tarafından açık/ kilitliyse kapatıp tekrar deneyin.  
    - Yetki hatası alıyorsanız dosya/permisyonlarını kontrol edin (Windows: sağ tık → Özellikler → Güvenlik).

- Bozuk veya açılamayan PDF  
    - PDF tek başına açılabiliyor mu kontrol edin. Eğer açılmıyorsa dosya bozuk olabilir; sağlam bir yedekten değiştirin veya PDF onarım araçlarıyla düzeltin.  
    - PyPDF2 hata mesajı (ör. PdfReadError) alıyorsanız hangi dosyada sorun olduğunu tespit edip o dosyayı izole ederek test edin.

- Türkçe karakterler ve boşluklu yollar  
    - Python 3'te Unicode yollar desteklenir; genelde çalışır. Ancak komut satırı veya üçüncü taraf kütüphaneler bazen sorun çıkarabilir. Sorun yaşarsanız:
        - Yolu pathlib ile oluşturun ve str() ile verin.
        - Alternatif olarak boşluksuz / ASCII karakterli geçici bir isimle deneyin.
        - Windows PowerShell/Terminal'in kodlamasının UTF‑8 olduğundan emin olun.

- Hızlı kontrol listesi  
    - Dosya adlarını ve yolları yazım hatalarına karşı doğrulayın.  
    - Mutlak yol vererek test edin.  
    - PDF'leri tek tek açarak bozuk olup olmadığını kontrol edin.  
    - Gerekirse betiği yönetici/uygun kullanıcı haklarıyla çalıştırın.

## Proje Yapısı
```
pdf_joiner.py        # PDF birleştirme betiği
requirements.txt     # Python bağımlılıkları
README.md            # Bu dosya
```