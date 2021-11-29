#! /usr/bin/env python3

import sys
import os
from time import sleep
from utils.Class import *
from utils.functions import *

def main():

	file_path = getFilePath()
	filename = os.path.basename(file_path)

	# DISPLAY
	Display.header(file_path, filename)

	runFile(file_path)

	edit_time = os.path.getmtime(file_path)

	while True:
		tmp_edit_time = os.path.getmtime(file_path)

		if edit_time != tmp_edit_time:
			Display.onChange()

			runFile(file_path)

			edit_time = tmp_edit_time

if __name__ == "__main__":
	main()