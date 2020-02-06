ENVIRONMENT = 'dev'

def fetch_data_prod():
    print("Retrieving real data....")

def fetch_data_test():
    print("Fake data...")
    return {
        "licence_id": "40810f08-4924-11ea-b77f-2e728ce88125",
        "public": False,
        "owner": "4e023ad0-4924-11ea-b77f-2e728ce88125"
    }

fetch_data = fetch_data_prod if ENVIRONMENT == 'prod' else fetch_data_test

data = fetch_data()
print(data)