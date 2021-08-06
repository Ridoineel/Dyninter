#! /usr/bin/env python3
# coding: utf-8;

"""
    Dyninter <-> The dynamic python interpreter
    Author: RidoineEl <ridoineelofficiel@gmail.com/>
"""

import argparse

def parse_object():
    """ Return command line arguments object """
    
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-f', '--file', help="python file")

    return argparser.parse_args()

arg_datas = parse_object()

if not arg_datas.file: 
    exit()

filepath = arg_datas.file
last_content = ""

while True:
    _file = open(filepath, "r")
    
    # file code (content)
    content =  ''.join(_file.readlines())

    if (content != last_content) :
        print("<================= Start Execution ===================>\n")
        exec(content)
        print("\n<================= End Execution ===================>\n")
        
        last_content = content
    
    #end, close the file
    _file.close()
