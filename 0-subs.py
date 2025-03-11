import requests

def number_of_subscribers(subreddit):
    # Set the User-Agent to avoid the "Too Many Requests" error
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    
    # Make a GET request to the subreddit about JSON endpoint
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    # Check if the response is valid
    if response.status_code == 200:
        # If the request was successful, get the number of subscribers from the JSON response
        data = response.json()
        return data['data']['subscribers']
    else:
        # If not a valid subreddit, return 0
        return 0
