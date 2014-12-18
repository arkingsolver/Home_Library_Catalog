Home Library Card Catalog
=========================
Quick Summary:
  Uses Google Books API to generate a personal library catalog system.
  
I have a problem with books.  The kind of problem where I have a whole room in my house for books, which is kind of like a library except they are anything but organized.

To remedy the situation I wrote a couple Python scripts to first pull Google Books data about a list of isbn numbers and then make a searchable catalog system from that data.

In the example files "home_isbn.txt" is a list of ISBN numbers belonging to the books on one of my book cases.

I made this for my own use and it is not polished.  OUTPUT scripts breaks without internet connection, and there is no error handling anywhere.

YOU MADE TO EDIT LIB_CAT_OUTPUT.py AND ADD IN GOOGLE BOOKS API KEY WHERE NOTED IF YOUR ISBN LIST IS LONG

<h3>File List</h3>

<i>INPUTS</i>
<br>
<b>home_isbn.txt</b> - The only true input file.  A list of ISBN numbers (one on each line).
<br>
<b>langs.csv</b> - Used as a look-up database for the Google Books Language abbrevations.

<i>SCRIPTS</i>
<br>
<b>LIB_CAT_OUTPUT.py</b> - Script takes 'home_isbn.txt' as an input and returns 'book_data.csv' as an output.
<br>
<b>LIB_QUERY.py</b> - Loads book_data.csv and lets you perform searches on it according to various fields.

<i>OUTPUT</i>
<br>
<b>book_data.csv</b> - Saved form of the Google Books API data.

<h3>USE INSTRUCTIONS</h3>
To use these scripts on your own ISBN list, perform the following:

-Download everything.

-Edit home_isbn.txt, remove my ISBN #s and add your own.  One per line.

-Run LIB_CAT_OUTPUT.py and wait.

-With luck it should output/overwrite book_data.csv.

-Run LIB_QUERY.py and do a search on your library to view detailed book info!



