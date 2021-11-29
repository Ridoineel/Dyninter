import sys
import os
import argparse

# 
sys.path.append(os.path.dirname(__file__))
from Class import Color, Display
from variables import *

parentDir = os.path.dirname(os.path.dirname(__file__))

def parse_object():
    """ Return command line arguments object """
    
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-f', '--file', help="python program file")

    return argparser.parse_args()

def getFilePath():
	arg_datas = parse_object()

	if not arg_datas.file:
		print(Color.warning("Warning: Missing file path (ex: -f example.py)"))
		print()

		prog_path = os.path.join(parentDir, prog_name + ".py")
		os.system(f"{prog_path} --help")

		exit()

	return arg_datas.file

def runFile(file_path):
	os.system("cls|clear")
	
	if os.system(f"python3 {file_path}") != 0: # Error
		Display.onError()
	else:
		Display.waitingChange()