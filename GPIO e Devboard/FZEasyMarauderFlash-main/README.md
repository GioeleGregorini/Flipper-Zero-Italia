# Easy Flipper Zero Marauder Flash
Questo tutorial è per installare facilmente Marauder su un ESP32 o WiFi Devboard per un Flipper Zero!
![ Schermata di EasyInstall](https://raw.githubusercontent.com/SkeletonMan03/FZEasyMarauderFlash/main/EasyInstall_Screenshot.png)

## Se hai Windows hai due prerequisiti:
È necessario installare [Git per Windows da qui](https://gitforwindows.org/).
Devi anche installare il [driver da qui](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?Tab=downloads) affinché il tuo esp32 venga riconosciuto.
## Se hai Macos o Linux puoi iniziare subito a seguire la guida:
# Come fare:
* Il passaggio 0 deve essere eseguito solo una volta
0) eseguire `pip3 install -r requirements.txt`.
1) Collegare la devboards o la scheda ESP32 tramite USB.
2) Tenere premuto il pulsante `BOOT` sul modulo. 
3) eseguire `python3 EasyInstall.py`.
4) Selezionare l'opzione di ciò che si desidera fare.

* Nota importante: potrebbe essere necessario eseguire questo script con `sudo` o come amministratore in Windows
