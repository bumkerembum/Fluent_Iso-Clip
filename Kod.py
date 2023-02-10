import pyautogui

print('Press Ctrl-C to quit.')

i = 0
total_lengt = "kesilecek planenin uzunluğunu gir buraya"
plane_sayisi = "kaç parçaya bölünmesini istiyorsun"
mesafe = total_lengt / plane_sayisi

iso_clip = pyautogui.locateOnScreen('isoclip sekmesinin görüntüsü.png', grayscale=True, confidence=.5)#iso clip sayfasının tamamını al
x = iso_clip[0]
y = iso_clip[1]
try:
    while i < plane_sayisi:
        i = i + 1

        yazı = "clip" + str(i)# ISO-CLIP isim

        pyautogui.moveTo(x, y)
        pyautogui.move("x yönü değişim", "y yönü değişim")
        pyautogui.click() # ISO_Clip isim girme yerine tıklandı
        pyautogui.typewrite(yazı)

        maxi = total_lengt- i * (mesafe)
        mini = maxi - mesafe

        pyautogui.move("minimumun x yerine uzaklık", "minimumum y yerine uzaklık")
        pyautogui.click()
        pyautogui.typewrite(str(mini)) # minimum değeri girildi

        pyautogui.move("maximuma olan x uzaklığı", 0)
        pyautogui.click()
        pyautogui.typewrite(str(maxi)) #maximum değerine yazıldı

        pyautogui.move("ok x mesafesi", "ok y mesafesi")
        pyautogui.click()


except KeyboardInterrupt:
    print("\n")
