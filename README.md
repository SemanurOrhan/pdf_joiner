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

- Çıktı dosyası adı: `BMO_birlestirilmis.pdf`
- Birleştirme sırası: `pdf_list` dizisindeki sıra

### Sıralamayı/Dosyaları Değiştirme
`pdf_joiner.py` içindeki şu bölümü düzenleyin:

```python
pdf_list = [
    "1_2.pdf",
    "3.pdf",
    "4.pdf",
    "5.pdf",
    "6.pdf",
    "7.pdf",
]
```

## Yaygın Hatalar ve Çözümler
- Dosya bulunamadı: Listedeki dosya adları ile klasördeki adlar birebir aynı olmalı (uzantı dahil).
- Dosya kilitli/erişim: PDF başka bir programda açıkken birleştirme başarısız olabilir; kapatıp tekrar deneyin.
- Bozuk PDF: Sorunlu PDF tek başına açılabiliyor mu kontrol edin. Açılamıyorsa dosyayı düzeltin/değiştirin.
- Türkçe/Boşluklu yollar: Proje klasör yolunda boşluk veya Türkçe karakter sorun çıkarmaz; yine de aynı klasörde çalışmak en kolayıdır.

## Proje Yapısı
```
pdf_joiner.py        # PDF birleştirme betiği
requirements.txt     # Python bağımlılıkları (standart isim)
requirement.txt      # Mevcut eski dosya (opsiyonel; kaldırabilirsiniz)
README.md            # Bu dosya
.gitinore            # Git için gereksiz dosyaları dışla
.gitattributes       # Satır sonlarını normalize et
```

## GitHub'a Yükleme
Aşağıdaki adımlar yerelde bir Git deposu oluşturur ve ilk commit'i hazırlar. Uzaktan (GitHub) depoya itmek için bir repo URL'si gerekir.

```powershell
# Git yüklü mü?
git --version

# Depoyu başlat
git init

# Ana dalı main yap (yeni depolar için önerilir)
git branch -M main

# Dosyaları ekle ve commit et
git add .
git commit -m "Initial commit: PDF birleştirici"

# GitHub'da boş bir repo oluşturduktan sonra URL'nizi ekleyin
git remote add origin https://github.com/<kullanici_adi>/<repo_adi>.git

git push -u origin main
```

## Lisans
Bir lisans seçilmedi. Açık kaynak yapmak isterseniz bir `LICENSE` dosyası ekleyebilirsiniz (MIT yaygın bir tercih).
