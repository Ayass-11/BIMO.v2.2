# BIMO.v2.1 Test Notes

## Hey BIMO Wake Word
- [ ] Normal mesafede tetikleniyor
- [ ] Yanlış tetiklenme kabul edilebilir seviyede
- [ ] Sessiz ortamda stabil
- [ ] Arka plan sesi varken stabil

## Bye BIMO Wake Word
- [ ] Session içinde tetikleniyor
- [ ] Yanlış tetiklenme yok (konuşma ortasında kapanmıyor)
- [ ] "See you later" sesi geliyor

## Session Akışı
- [ ] Hey BIMO → session açılıyor
- [ ] Arka arkaya konuşma çalışıyor
- [ ] VAD konuşma bitişini doğru algılıyor
- [ ] Bye BIMO → session kapanıyor
- [ ] Session sonrası tekrar Hey BIMO ile açılıyor

## Manuel Fallback
- [ ] SPACE basılı tut → konuş → bırak çalışıyor
- [ ] Kısa basışta "Too short" mesajı geliyor

## Gözlemler
- Bye false positive durumu: 
- Hey false positive durumu:
- VAD kesme süresi tercihi: SILENCE_LIMIT = 35
