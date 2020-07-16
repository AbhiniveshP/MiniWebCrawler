import requests, random
url = "https://icanhazdadjoke.com/search"

def getResults():
    
    term = input('Please Enter a Term of Your Choice: ')

    response = requests.get(url, 
                        headers= {"Accept": "application/json"},
                        params= {"term":term})

    data = response.json()

    return data['results']

def printResult(results):

    if (len(results) <= 0):
        print("Sorry Can't find a joke with your input term!!!")

    elif (len(results) == 1):
        print("The only joke obtained with your search term: \n" + results[0]['joke'])

    else:
        resultChosen = random.choice(results)
        print("One of the jokes from your search term would be: \n" + resultChosen['joke'])

results = getResults()
printResult(results)