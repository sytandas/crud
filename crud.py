#!/usr/bin/env python3

import sys
import psycopg2 

try:
    conn = psycopg2.connect("dbname='temp' use='dbuser' host='localhost' password='dbpass'")
except:
    print('I am unable to connect to the database')

def create():
    print('create function executed')

def read():
    print('read funciton executed')

def update():
    print('update function executed')

def delete():
    print('delete function executed')

def default():
    return 'choose right one'

selectChoice = {
        1: create,
        2: read,
        3: update,
        4: delete
        }

def selectFunction(number):
    return selectChoice.get(number, default)()

print(selectFunction(1))
#print(selectFunction(10))
