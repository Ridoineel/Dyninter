import sys
import os
import argparse

# 
sys.path.append(os.path.dirname(__file__))
from Class import Color

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
		os.system("./main.py --help")

		exit()

	return arg_datas.file

def runFile(file_path):
	os.system("cls|clear")
	os.system(f"python3 {file_path}")