import json
import os
from apiclient.discovery import build

bookFile = 'booklist.json'
keyFile = 'apikeys.json'
searchFile = 'searchresults.json'


def create_keyfile():
    keys = {}
    with open(keyFile, mode='w') as f:
        json.dump(keys, f, indent=4)


def add_api_key(apiID):
    with open(keyFile, mode='r') as f:
        keys = json.load(f)

    keys[apiID] = input('What is API key for %s: ' % (apiID))

    with open(keyFile, mode='w') as f:
        json.dump(keys, f, indent=4)


def get_api_key(apiID):
    with open(keyFile, mode='r') as f:
        keys = json.load(f)
    for key in keys:
        if key == apiID:
            apikey = keys[apiID]
            return apikey


def build_api_call(isbn):
    api_key = get_api_key('google books')
    service = build('books', 'v1', developerKey=api_key)
    request = service.volumes().list(source='public',
                                     q=isbn,
                                     maxResults=1)
    return request


def call_api(request):
    # Execute request
    response = request.execute()

    # Write request results to json file for debugging/visual inspection
    with open(searchFile, mode='w', encoding='utf-8') as f:
        json.dump(response, f, indent=4)

    return response


def process_api_response(response):
    for book in response.get('items', []):
        if os.path.isfile(bookFile):
            with open(bookFile, mode='r', encoding='utf-8') as f:
                booklist = json.load(f)
        else:
            booklist = {}

        # Extract ISBN 13 number
        ISBN_items = book['volumeInfo']['industryIdentifiers']
        for item in ISBN_items:
            if item['type'] == 'ISBN_13':
                ISBN_13 = item['identifier']
            if item['type'] == 'ISBN_10':
                ISBN_10 = item['identifier']

        # Add pertinent information to booklist
        booklist[ISBN_13] = {}
        booklist[ISBN_13]['Title'] = book['volumeInfo']['title']
        booklist[ISBN_13]['Author'] = book['volumeInfo']['authors'][0]
        booklist[ISBN_13]['Published'] = book['volumeInfo']['publishedDate']
        booklist[ISBN_13]['Publisher'] = book['volumeInfo']['publisher']
        booklist[ISBN_13]['Genre'] = book['volumeInfo']['categories'][0]
        booklist[ISBN_13]['Cover'] = book['volumeInfo']['imageLinks']['thumbnail']
        booklist[ISBN_13]['ISBN_10'] = ISBN_10
        booklist[ISBN_13]['ISBN_13'] = ISBN_13
        booklist[ISBN_13]['ID'] = book['id']
        booklist[ISBN_13]['PublicDomain'] = book['accessInfo']['publicDomain']
        booklist[ISBN_13]['epub'] = book['accessInfo']['epub']['isAvailable']

        #booklist[ISBN_13]['ASIN']= 'FutureAddition'

        # Write data to file
        with open(bookFile, mode='w', encoding='utf-8') as f:
            json.dump(booklist, f, indent=4)
    return booklist[ISBN_13]['Title']


def add_book(isbn):

    if type(isbn) == int:
        isbn = str(isbn)

    if os.path.isfile(bookFile):
        with open(bookFile, mode='r', encoding='utf-8') as f:
            booklist = json.load(f)
        for item in booklist:
            if item == isbn:
                print()
                print(booklist[item]['Title'] +
                      ' is already on the booklist.')
                return

    request = build_api_call(isbn)
    response = call_api(request)
    bookTitle = process_api_response(response)
    print(bookTitle + ' has been added to booklist.')


def remove_book(isbn):
    # Add code at later point to remove book after purchased
    print('Add code here')


def get_amazon_link():
    print('add code here')
