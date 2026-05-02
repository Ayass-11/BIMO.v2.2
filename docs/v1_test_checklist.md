# BIMO.v1 Test Checklist

## Ses Zinciri
- [x] Normal konuşma — STT doğru algılıyor
- [x] Kısa basış — sistem çökmüyor, sessizce geçiyor
- [x] Boş ses — LLM'e gitmiyor
- [x] Uzun sohbet (~1 saat) — zincir dağılmıyor

## Karakter
- [x] Normal sohbette BIMO hissi var
- [x] Teknik soruda karakter kasılmadan cevap veriyor
- [x] Duygusal durumda ton değişiyor

## Sistem
- [x] Config'den ayarlar okunuyor
- [x] Hata olunca sistem donmuyor, idle'a dönüyor
- [x] STT / LLM / TTS hataları ayrı loglanıyor

## Kapsam Dışı (v1'de test edilmedi)
- [ ] Wake word
- [ ] Kalıcı hafıza
- [ ] Türkçe destek
