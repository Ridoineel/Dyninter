import sys
import os
import time  

#
sys.path.append(os.path.dirname(__file__))
from variables import *

class Color:
	success = lambda _str: '\033[92m' + _str + '\033[0m'
	danger = lambda _str: '\033[91m' + _str + '\033[0m'
	primary = lambda _str: '\033[96m' + _str + '\033[0m'
	warning = lambda _str: '\033[33m' + _str + '\033[0m'

class Style:
	bold = lambda _str: '\033[1m' + _str + '\033[0m'
	underline = lambda _str: '\033[4m' + _str + '\033[0m'
	blink = lambda _str: '\033[5m' + _str + '\033[0m'

class Display:

	@staticmethod
	def header(file_path, filename):
		# version of this
		print(Color.primary(f"[{prog_name}] {prog_version}"))
		time.sleep(1.5)

		# Starting
		print(Color.primary(f"[{prog_name}] Starting `python3 {file_path}"))
		time.sleep(1.5)

		# running
		print(Color.primary(f"[{prog_name}] Running"), end="")
		sys.stdout.flush()

		for i in range(4):
			print(end=Style.bold(Color.primary(".")))
			sys.stdout.flush()
			time.sleep(0.7)
		
		time.sleep(1)

	@staticmethod
	def onChange():
		os.system("cls|clear")

		print(Color.primary(f"[{prog_name}] Modification..."))

		time.sleep(1.5)

	@staticmethod
	def onError():
		print()
		print(Color.danger(f"[{prog_name}] program crashed - waiting for changes before restart"))

	@staticmethod
	def waitingChange():
		print()
		print(Color.primary(f"[{prog_name}] exit - waiting for changes before restart"))
