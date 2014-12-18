#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dkingsolver'

######### IMPORTS ####
import json          #
import urllib2
import urllib        #
import codecs
import csv
import time
import re            #
######################

###### FILE ASSIGNMENTS ######
filename = 'home_isbn.txt'  ##
                            ##
output = 'book_data.csv'    ##
                            ##
lang_file = 'langs.csv'     ##
##############################

def books_output(books_string):

    for item in books_string:

        with open(output, 'wb') as csvfile:
            row_writer = csv.writer(csvfile, delimiter='*')
            row_writer.writerows(book_stats_list)



with open(lang_file, 'Ur') as langs:
    glangid = list(list(item) for item in csv.reader(langs, delimiter=','))

with open(filename, 'r') as ISBN_LIST:
    header = ['Title','Author','Cover URL','Publisher','Publish Date','Language','Description','ISBN']
    book_stats = []
    book_stats_list = []
    for line in ISBN_LIST.readlines():
        if "\n" in line:
            ISBN = str(line[:-1])
        else:
            ISBN = str(line)

        def ISBN_query(address):
            # Takes an ISBN Number and produces book details.

            authors = ''

            try:
                raw_book_data = urllib2.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:' + ISBN)  #+ '&key= ADD KEY HERE IF YOU HAVE ONE')
                book_data = json.load(raw_book_data)
            except:
                books_output(book_stats_list)
                print 'HTTP Error.  Find Last Output and start again from there.'

            try:
                try:
                    title_raw = book_data['items'][0]['volumeInfo']['title']
                    title = title_raw.encode('utf-8')
                except KeyError:
                    title = 'No Title Found for ISBN ' + ISBN
                try:
                    author = book_data['items'][0]['volumeInfo']['authors']
                    for name in author:
                        try:
                            #name.encode('utf-8')
                            authors_raw = unicode(authors) + unicode(name)
                            authors = authors_raw.encode('utf-8')
                        except UnicodeEncodeError:
                            print 'Author - Unicode error for ' + line
                        except UnicodeDecodeError:
                            print 'Author - Unicode Decode error for ' + line

                except KeyError:
                    authors = 'No Author Listed'
                try:
                    publisher_raw = book_data['items'][0]['volumeInfo']['publisher']
                    publisher = publisher_raw.encode('utf-8')
                except KeyError:
                    publisher = 'No Publisher Info'
                try:
                    date_raw = book_data['items'][0]['volumeInfo']['publishedDate']
                    date = date_raw.encode('utf-8')
                except KeyError:
                    date = 'No Publish Date Listed'
                try:
                    desc_raw = book_data['items'][0]['volumeInfo']['description']
                    desc = desc_raw.encode('utf-8')
                except KeyError:
                    desc = 'No Description Given'
                try:
                    lang = book_data['items'][0]['volumeInfo']['language']
                    for pair in glangid:
                        if lang == pair[0]:
                            full_lang = pair[1]

                except KeyError:
                    full_lang = 'No Language Listed'
                try:
                    cover = book_data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
                    #urllib.urlretrieve(cover,ISBN+'.jpg')
                except KeyError:
                    cover = "No Cover Image"

                book_stats.append(title)
                book_stats.append(authors)
                book_stats.append(cover)
                book_stats.append(publisher)
                book_stats.append(date)
                book_stats.append(full_lang)
                book_stats.append(desc)
                book_stats.append(ISBN)

                #return book_stats

            except KeyError:
                print 'ISBN ' + ISBN + ' Not Found.'
                #### Need to make it write to 2nd notepad doc of errors
                print '-----------------------------------------'

                #return book_stats
            return book_stats
        ISBN_query(ISBN)

        book_stats_list.append(book_stats)
        book_stats = []

book_stats_list.insert(0, header)

#print book_stats_list

books_output(book_stats_list)





