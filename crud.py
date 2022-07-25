#!/usr/bin/env python3

import sys
import psycopg2 

"""
try:
    conn = psycopg2.connect("dbname='temp' use='dbuser' host='localhost' password='dbpass'")
except:
    print('I am unable to connect to the database')
"""

#number = input("1.create, 2.read, 3.update, 4.delete/modify: ")
print("1.create, 2.read, 3.update, 4.delete/modify ")

def create():
    return "create"

def read():
    return "read"

def update():
    return "update"

def delete():
    return "delete"

def default():
    return "choose right one"

switcher = {
        1: create,
        2: read,
        3: update,
        4: delete
        }

def selectFunction(num):
    return switcher.get(num, default)()

number = int(input("choose:: "))
print(selectFunction(number))


