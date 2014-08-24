from BookWatcher import *

# Check for apikey file
if not os.path.isfile(keyFile):
    create_keyfile()
    add_api_key('google books')

# Get google books api key
apiKey_googlebooks = get_api_key('google books')


# Add books
#9780375984648    # The Rule of Thoughts, ISBN13 from BN.com
#9780316235556    # The Broken Eye, ISBN13 from BN.com
#9780449818404    # Firefight, ISBN13 from BN.com
#9781429949620    # Words of Radience, ISBN13 from BN.com

# add_book(9780375984648)
# #add_book(9780316235556)
# add_book(9780449818404)
# add_book(9781429949620)
# add_book(9780698184947)
# add_book(9780375984631)

# add_book(9780316235556)
add_book(9781429992800)

# Idea List
# 3) Search twitter /check author feeds for deals on their books?
