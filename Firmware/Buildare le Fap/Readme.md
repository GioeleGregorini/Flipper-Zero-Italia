##Come buildare le FAP
#Per buildare una FAP (flipper application) aggiornata alle API 11 e compatibile con tutti i firmware attuali alla loro ultima versione, è necessario seguire i seguenti passi:

Scaricare il firmware condiviso qui:.
Estrarre il firmware e trovare la cartella che contiene molti file.
Inserire i file della FAP in una cartella chiamata "application_user" all'interno del firmware estratto.
Trovare l'ID della FAP nel file "application.fam", ad esempio "sample_apps". Copiare l'ID perché servirà in seguito.
Aprire il terminale (su MacOS) o il cmd (su Windows).
Con il comando "cd", posizionarsi nella directory dove sono presenti le cartelle "applications", "applications_user", "assets" e così via.
Su MacOS, dare il comando "sudo ./fbt fap_[ID della FAP]" (ad esempio "sudo ./fbt fap_sample_apps").
Se tutto è andato bene, il terminale darà una conferma e la FAP sarà disponibile nella cartella "build/f7-firmware-D/.extapps".
NOTA: Potrebbe essere necessario rendere visibili i file e le cartelle nascoste su MacOS premendo insieme "shift+command+.". La cartella ".extapps" sarà semitrasparente.
