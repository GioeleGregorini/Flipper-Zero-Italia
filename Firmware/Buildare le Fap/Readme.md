# Come buildare le FAP
## Per buildare una FAP (flipper application) aggiornata alle API 11 e compatibile con tutti i firmware attuali alla loro ultima versione, è necessario seguire i seguenti passi:

- Scaricare l'ultimo firmware [qui](https://github.com/flipperdevices/flipperzero-firmware).

- Estrarre il firmware e trovare la cartella che contiene molti file(vedi [questo file](https://github.com/GioeleGregorini/Flipper-Zero-Italia/blob/2e12485359e3760476508f839c8496a25dee6f83/Firmware/Buildare%20le%20Fap/Cartella.jpg)).

- Inserire i file della FAP in una cartella chiamata "application_user" all'interno del firmware estratto.

- Trovare l'ID della FAP nel file "[application.fam](https://github.com/GioeleGregorini/Flipper-Zero-Italia/blob/2e12485359e3760476508f839c8496a25dee6f83/Firmware/Buildare%20le%20Fap/Application.fam.jpg)", ad esempio "sample_apps". Copiare l'ID perché servirà in seguito.

- Aprire il terminale (su MacOS) o il cmd (su Windows).

- Con il comando "cd", posizionarsi nella directory dove sono presenti le cartelle "applications", "applications_user", "assets" e così via.

## Su MacOS:

Dare il comando "sudo ./fbt fap_[ID della FAP]" (ad esempio "sudo ./fbt fap_sample_apps").Potrebbe essere necessario inserire la password del mac.

## Su Windows:

Dare il comando "fbt fap_[ID della FAP]" (ad esempio "fbt fap_sample_apps"). Potrebbe essere necessario avviare il terminale come amministratore, e dovete avere python installato.

## Se tutto è andato bene:
il terminale darà una conferma e la FAP sarà disponibile nella cartella "build/f7-firmware-D/.extapps".

NOTA: Potrebbe essere necessario rendere visibili i file e le cartelle nascoste:

su MacOS premete insieme "shift+command+.". La cartella ".extapps" sarà semitrasparente.

su windows nelle impostazioni di esplora risorse spuntate l'opzione file nascosti.
