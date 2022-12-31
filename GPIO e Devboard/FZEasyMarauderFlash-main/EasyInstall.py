#!/bin/python3
import os
import platform
from git import Repo
import glob
import time
import shutil
import serial.tools.list_ports
import requests
import json
import esptool
from colorama import Fore, Back, Style

OPENASCII=Fore.GREEN+'''
#########################################
#    Questo script vi aiuterà 		#
#    ad installare o aggiornare		#
#    il vostro esp32 !!   		#
#########################################
'''+Style.RESET_ALL

print(OPENASCII)
print("Assicurati che il tuo devboard ESP32 o WiFi sia collegato!")
BR=str("115200")

def checkforserialport():
	global serialport
	serialport=''
	vids=['303A','10C4','1A86']
	com_port=None
	ports=list(serial.tools.list_ports.comports())
	for vid in vids:
		for port in ports:
			if vid in port.hwid:
				serialport=port.device
				device=vid
	if serialport=='':
		print(Fore.RED+"Non è stato rilevato alcun dispositivo ESP32."+Style.RESET_ALL)
		print(Fore.RED+"Collegare un devboard WiFi Flipper o un chip ESP32 e riprovare"+Style.RESET_ALL)
		choose_fw()
	if device=='':
		return
	elif device=='303A':
		print(Fore.BLUE+"Molto probabilmente stai usando un Flipper Zero WiFi Devboard o un ESP32-S2"+Style.RESET_ALL)
	elif device=='10C4':
		print(Fore.BLUE+"Molto probabilmente stai usando un ESP32-WROOM, un ESP32-S2-WROVER o un ESP32-S3-WROOM"+Style.RESET_ALL)
	elif device=='1A86':
		print(Fore.MAGENTA+"Molto probabilmente stai usando un chip ESP32 non ufficiale! Il successo non è garantito!"+Style.RESET_ALL)

	return

def checkforextrabins():
	extraesp32binsrepo="https://github.com/UberGuidoZ/Marauder_BINs.git"
	global extraesp32bins
	extraesp32bins=("Extra_ESP32_Bins")
	global scorpbins
	scorpbins=(extraesp32bins+"/Marauder/WROOM")
	if os.path.exists(extraesp32bins):
		print("La cartella Extra_ESP32_bins esiste!")
	else:
		print("La cartella Extra_ESP32_bins non esiste!")
		print("Non importa, la scaricherò io per te....")
		Repo.clone_from(extraesp32binsrepo, extraesp32bins)
	return

def choose_fw():
	choices='''
//======================================================\\\ 
|| Opzioni:						||
|| 1) Installa Marauder su WiFi Devboard o ESP32-S2	||
|| 2) Salva Impostazioni WiFi di Flipper Blackmagic 	||
|| 3) Installa Flipper Blackmagic			||
|| 4) Installa Marauder su ESP32-WROOM			||
|| 5) Installa Marauder su ESP32-S3			||
|| 6) Aggiorna tutti i file				||
|| 7) Esci						||
\\\======================================================//
'''
	global chip
	print(choices)
	fwchoice=int(input("Inserisci il numero relativo alla tua scelta: "))
	if fwchoice==1:
		print("Hai scelto di installare Marauder su WiFi Devboard o ESP32-S2")
		chip="esp32s2"
		checkforserialport()
		flash_esp32marauder()
	elif fwchoice==2:
		print("Hai scelto di salvare Impostazioni WiFi di Flipper Blackmagic ")
		chip="esp32s2"
		checkforserialport()
		save_flipperbmsettings()
	elif fwchoice==3:
		print("Hai scelto di installare Flipper Blackmagic")
		chip="esp32s2"
		checkforserialport()
		flash_flipperbm()
	elif fwchoice==4:
		print("Hai scelto di installare Marauder su ESP32-WROOM")
		chip="esp32"
		checkforserialport()
		flash_esp32wroom()
	elif fwchoice==5:
		print("Hai scelto di installare Marauder su ESP32-S3")
		chip="esp32s3"
		checkforserialport()
		flash_esp32s3()
	elif fwchoice==6:
		print("Hai scelto di aggiornare tutti i file")
		update_option()
	elif fwchoice==7:
		print("Hai scelto di uscire")
		print("Uscita in corso!")
		exit()
	else:
		print(Fore.RED+"Scelta non valida!"+Style.RESET_ALL)
		exit()
	return

def erase_esp32fw():
	global serialport
	print("Cancellazione del firmware...")
	esptool.main(['-p', serialport, '-b', BR, '-c', chip, '--before', 'default_reset', '-a', 'no_reset', 'erase_region', '0x9000', '0x6000'])
	print("Firmware cancellato!")
	print("Attesa di 3 secondi...")
	time.sleep(3)
	return

def checkforesp32marauder():
	print("Controllo delle versioni di Marauder")
	if os.path.exists("ESP32Marauder/releases"):
		print("Fantastico, hai la cartella delle ultime versioni di Marauder!")
	else:
		print("La cartella delle ultime versioni di Marauder non esiste, ma non importa, la scaricherò io per te...")
		os.makedirs('ESP32Marauder/releases')
		marauderapi="https://api.github.com/repos/justcallmekoko/ESP32Marauder/releases/latest"
		response=requests.get(marauderapi)
		jsondata=response.json()
		assetdls=range(0,7)
		for assetdl in assetdls:
			marauderasset=jsondata['assets'][assetdl]['browser_download_url']
			if marauderasset.find('/'):
				filename=(marauderasset.rsplit('/', 1)[1])
			downloadfile=requests.get(marauderasset, allow_redirects=True)
			open('ESP32Marauder/releases/'+filename, 'wb').write(downloadfile.content)
	esp32marauderfwc=('ESP32Marauder/releases/esp32_marauder_v*_flipper.bin')
	if not glob.glob(esp32marauderfwc):
		print("Il firmware ESP32 Marauder Flipper non esiste!")
	global esp32marauderfw
	for esp32marauderfw in glob.glob(esp32marauderfwc):
		if os.path.exists(esp32marauderfw):
			print("Il firmware del Marauder per es32 esiste in ", esp32marauderfw)
	return

def checkfors3bin():
	esp32s3fwc=('ESP32Marauder/releases/esp32_marauder_v*_mutliboardS3.bin')
	if not glob.glob(esp32s3fwc):
		print("Il file Mutliboards3.bin non esiste!")
	global esp32s3fw
	for esp32s3fw in glob.glob(esp32s3fwc):
		if os.path.exists(esp32s3fw):
			print("Il file bin del firmware per ESP32 esiste in ", esp32s3fw)
		else:
			print("Il file Mutliboards3.bin non esiste!")
	return

def checkforoldhardwarebin():
	espoldhardwarefwc=('ESP32Marauder/releases/esp32_marauder_v*_old_hardware.bin')
	if not glob.glob(espoldhardwarefwc):
		print("Old_hardware bin non esiste!")
	global espoldhardwarefw
	for espoldhardwarefw in glob.glob(espoldhardwarefwc):
		if os.path.exists(espoldhardwarefw):
			print("Old Hardware bin esiste in ", espoldhardwarefw)
		else:
			print("Old_hardware bin non esiste!")
	return

def prereqcheck():
	print("Controllo dei prerequisiti...")
	checkforextrabins()
	checkforesp32marauder()
	checkfors3bin()
	checkforoldhardwarebin()
	return

def flash_esp32marauder():
	global serialport
	erase_esp32fw()
	print("Installando il firmware di Marauder sulla Devboard WiFi o su ESP32-S2...")
	esptool.main(['-p', serialport, '-b', BR, '-c', chip, '--before', 'default_reset', '-a', 'no_reset', 'write_flash', '--flash_mode', 'dio', '--flash_freq', '80m', '--flash_size', '4MB', '0x1000', extraesp32bins+'/Marauder/bootloader.bin', '0x8000', extraesp32bins+'/Marauder/partitions.bin', '0x10000', esp32marauderfw])
	print(Fore.GREEN+"Installazione del firmware di Marauder su ESP32-S2 riuscita!"+Style.RESET_ALL)
	return

def flash_esp32wroom():
	global serialport
	print("Installando il firmware di Marauder su ESP32-WROOM...")
	erase_esp32fw()
	esptool.main(['-p', serialport, '-b', BR, '--before', 'default_reset', '--after', 'hard_reset', '-c', chip, 'write_flash', '--flash_mode', 'dio', '--flash_freq', '80m', '--flash_size', '2MB', '0x8000', scorpbins+'/partitions.bin', '0x1000', scorpbins+'/bootloader.bin', '0x10000', espoldhardwarefw])
	print(Fore.GREEN+"Installazione del firmware di Marauder su ESP32-WROOM riuscita!"+Style.RESET_ALL)
	return

def save_flipperbmsettings():
	global serialport
	print("Salvataggio delle impostazioni WiFi Flipper Blackmagic in Extra_ESP32_Bins/Blackmagic/nvs.bin")
	esptool.main(['-p', serialport, '-b', BR, '-c', chip, '-a', 'no_reset', 'read_flash', '0x9000', '0x6000', extraesp32bins+'/Blackmagic/nvs.bin'])
	print(Fore.GREEN+"Le impostazioni Wi-Fi Flipper Blackmagic sono state salvate in ", extraesp32bins+"/Blackmagic/nvs.bin!"+Style.RESET_ALL)
	return

def flash_flipperbm():
	if os.path.exists(extraesp32bins+"/Blackmagic/nvs.bin"):
		print("Installando le impostazioni di WiFi Flipper Blackmagic con reset...")
		erase_esp32fw()
		esptool.main(['-p', serialport, '-b', BR, '-c', chip, '--before', 'default_reset', '-a', 'no_reset', 'write_flash', '--flash_mode', 'dio', '--flash_freq', '80m', '--flash_size', '4MB', '0x1000', extraesp32bins+'/Blackmagic/bootloader.bin', '0x8000', extraesp32bins+'/Blackmagic/partition-table.bin', '0x9000', extraesp32bins+'/Blackmagic/nvs.bin', '0x10000', extraesp32bins+'/Blackmagic/blackmagic.bin'])
		print(Fore.GREEN+"Le impostazioni di WiFi Flipper Blackmagic sono state modificate applicando un reset!"+Style.RESET_ALL)
	else:
		print("Installando le impostazioni di WiFi Flipper Blackmagic senza reset...")
		erase_esp32fw()
		esptool.main(['-p', serialport, '-b', BR, '-c', chip, '--before', 'default_reset', '-a', 'no_reset', 'write_flash', '--flash_mode', 'dio', '--flash_freq', '80m', '--flash_size', '4MB', '0x1000', extraesp32bins+'/Blackmagic/bootloader.bin', '0x8000', extraesp32bins+'/Blackmagic/partition-table.bin', '0x10000', extraesp32bins+'/Blackmagic/blackmagic.bin'])
		print(Fore.GREEN+"Le impostazioni di WiFi Flipper Blackmagic sono state modificate senza applicare un reset!"+Style.RESET_ALL)
	return

def flash_esp32s3():
	global serialport
	erase_esp32fw()
	print("Installando il firmware di Marauder su ESP32-S3...")
	esptool.main(['-p', serialport, '-b', BR, '-c', chip, '--before', 'default_reset', '-a', 'no_reset', 'write_flash', '--flash_mode', 'dio', '--flash_freq', '80m', '--flash_size', '8MB', '0x0', extraesp32bins+'/S3/bootloader.bin', '0x8000', extraesp32bins+'/S3/partitions.bin', '0xE000', extraesp32bins+'/S3/boot_app0.bin', '0x10000', esp32s3fw])
	print(Fore.GREEN+"Installazione del firmware di Marauder su  ESP32-S3 riuscita!"+Style.RESET_ALL)
	return

def update_option():
	print("Controllare ed eliminare i file prima di sostituirli...")
	if os.path.exists("ESP32Marauder"):
		shutil.rmtree("ESP32Marauder")
	if os.path.exists("Extra_ESP32_Bins"):
		shutil.rmtree("Extra_ESP32_Bins")
	prereqcheck()
	return

prereqcheck()
choose_fw()
