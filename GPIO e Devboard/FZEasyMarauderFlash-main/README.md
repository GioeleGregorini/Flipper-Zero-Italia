# Easy Flipper Zero Marauder Flash
Questo tutorial è per installare facilmente Marauder su un ESP32 o WiFi Devboard per un Flipper Zero!
![ Schermata di EasyInstall](https://raw.githubusercontent.com/SkeletonMan03/FZEasyMarauderFlash/main/EasyInstall_Screenshot.png)

## Se hai Windows hai due prerequisiti:
È necessario installare [Git per Windows da qui](https://gitforwindows.org/).
Devi anche installare il [driver da qui](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?Tab=downloads) affinché il tuo esp32 venga riconosciuto.
## Se hai Macos o Linux puoi iniziare subito a seguire la guida:
# Come fare:
* Il passaggio 0 deve essere eseguito solo una volta
0) dopo essersi posizionati con il terminale nella cartella dove sono stati installati i file, eseguire `pip3 install -r requirements.txt`.
1) Collegare la devboards o la scheda ESP32 tramite USB.
2) Tenere premuto il pulsante `BOOT` sul modulo. 
3) eseguire `python3 EasyInstall.py`.
4) Selezionare l'opzione di ciò che si desidera fare (il programma ti aiuta a capire che tipo di modulo hai, verra scritto in blu dopo che avvi una delle 6 possibilità di installazione).

* Nota importante: potrebbe essere necessario eseguire questo script con `sudo` o come amministratore in Windows


## Spiegazione più approfondita:

Per posizionarsi con il terminale in una cartella, è possibile utilizzare il comando "cd" (che significa "change directory", ovvero "cambia directory" in italiano). Ad esempio, se si vuole entrare nella cartella "documents" nella directory corrente, è possibile utilizzare il comando "cd documents". Se si vuole invece entrare in una sottocartella della cartella "documents", ad esempio "project", si può utilizzare il comando "cd documents/project".

È inoltre possibile utilizzare il comando "cd .." per tornare alla directory superiore o alla cartella padre della directory corrente. Ad esempio, se si è nella cartella "project" all'interno della cartella "documents", utilizzando il comando "cd .." si tornerà alla cartella "documents".
"pip3" è un comando del terminale che viene utilizzato per installare pacchetti Python. "Requirements.txt" è un file che elenca le dipendenze o i pacchetti Python che sono necessari per far funzionare qualche altro programma. Eseguendo il comando "pip3 install -r requirements.txt", si stanno installando tutti i pacchetti Python elencati nel file "requirements.txt" nel sistema.

Collegare la devboards o la scheda ESP32 tramite USB al computer. La devboards o la scheda ESP32 sono schede di sviluppo utilizzate per creare progetti basati su microcontrollori.

Tenere premuto il pulsante BOOT sul modulo. Il pulsante BOOT è un pulsante presente sulla scheda di sviluppo che viene utilizzato per avviare il sistema o per eseguire determinate operazioni durante il processo di avvio, in questo caso imposta l'esp32 in modalità download, modalità che permette l'installazione di un nuovo firmware.

Eseguire il comando "python3 EasyInstall.py". "Python3" è un interprette di codice sorgente Python che viene utilizzato per eseguire il programma "EasyInstall.py". "EasyInstall.py" è il nome di un programma scritto in Python che probabilmente viene utilizzato per configurare o installare qualcosa sulla scheda di sviluppo.

Selezionare un'opzione tra le sei disponibili utilizzando il programma "EasyInstall.py". Il programma "EasyInstall.py" probabilmente mostra un menu con diverse opzioni che l'utente può scegliere per configurare o installare qualcosa sulla scheda di sviluppo.

Potrebbe essere necessario eseguire il programma "EasyInstall.py" con il comando "sudo" o come amministratore in Windows. "Sudo" è un comando del terminale che viene utilizzato per eseguire un altro comando con i privilegi di amministratore. In Windows, per eseguire un programma come amministratore, è necessario fare clic con il pulsante destro del mouse sul programma e selezionare "Esegui come amministratore" dal menu contestuale. Ciò è necessario in alcuni casi poiché alcune operazioni possono richiedere privilegi di amministratore per essere eseguite correttamente.
