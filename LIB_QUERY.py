#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dkingsolver'

######### IMPORTS ####
import csv


###### FILE ASSIGNMENTS ######
filename = 'book_data.csv'  ##


def extract_lines(FILE_NAME):
    #Opens input file as read only.
    # Made for use with comma seperated CSV files
    #Iterates over lines in file, and comma seprated elements in line, making a list within a list
    #Example: [['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close\n']
    infile = open(FILE_NAME, "r")
    line_list = []
    for line in infile:
        row_elements = line.split("*")
        line_list.append(row_elements)
    return line_list

book_data = extract_lines(filename)

def prompt():
    print "---- Search Library ----"
    print "Enter a number to search the corresponding field"
    print "Title = 0 Author = 1 Publisher = 3 "
    print "Date Published = 4 Language = 5 "
    print "Desc. Keyword = 6 ISBN = 7"
    field = raw_input('INPUT #: ')

    return field

def query():
    query = raw_input('Find: ')
    return query

search_field = int(prompt())
search_query = query()

print '--------------------------------------------------------------------------------------'



def book_find(number, da_query):

    found_count = 0

    for line in book_data:
        if da_query.lower() in line[number].lower():
            found_count = found_count + 1
            print '---------------------------------------------------------------------------------------'
            for item in line:
                print item
            print '-----------------------------------------------------------------------------------------'

    print 'Books Found: ' + str(found_count)
    found_count = 0

book_find(search_field, search_query)

