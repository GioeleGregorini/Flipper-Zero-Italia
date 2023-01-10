## Ecco a voi un utile script python per generare la chiave necessaria per leggere i personaggi nfc Disney Infinity

Il codice era gia stato pubblicato in [questa pagina](https://nfc.toys/interop-inf.html) dove sono spiegati anche altri protocolli nfc di giocattoli, come amibo e skylander.
Dato che era non funzionante ho provveduto a sistemare alcune righe del codice che però non è di mia proprietà.

Lascio tutti i crediti a [nfc.toys](https://nfc.toys/index.html).

## Come fare:

- Scaricate il file Disney_Infinity_Key_Generator.py.

- Leggete l'uid del personaggio facendo skip quando il flipper  cerca di decifrare la key.

- segnatevi l'uid, lo useremo con lo script utilizzando il comando ./Disney_Infinity_Key_Generator.py [uid letto],
- oppure python3 Disney_Infinity_Key_Generator.py [uid letto], a seconda del vostro sistema operativo.

- L'output dello script sarà la vostra chiave.


## Esempio del comando:
  
  ./Disney_Infinity_Key_Generator.py 045d60ba4f4880
  
## Esempio output del comando:
  
  88f8a009843d
  

## Se volete mettere la chiave nel vostro flipper zero:

Aggiungetela al file mf_classic_dict_user che si trova in /ext/nfc/assets/.
