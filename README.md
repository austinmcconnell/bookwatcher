BookWatcher
===========

BookWatcher is a program that notifies you whenever your favorite books drop below a certain price.

(Current Capability)
When you add a book, BookWatcher searches Google Books API, gathers all the pertinent information, and stores it in a json file. As you add more books, your booklist will grow to accomodate them.

(Future Capability)
Each day/week, script will check booksellers (e.g. Amazon, BN, Google) and store the price for each book on your booklist.

Once the price reaches a designated value (e.g. .99c for Kindle books, $5 for paperback), BookWatcher will notify you via email/text/other.

(Hopeful Thinking)
I'm considering adding a feature where you can store authorization information for a bookseller and let the script purchas for you. Is this even possible with Captcha-type checks?

Installation
============

Dependencies
============
This script is written in Python3 and needs a compatible Google API wrapper. There is no official Python3 Google API code, but there is an unofficial port at https://github.com/enorvelle/GoogleApiPython3x. This is what I'm using.

