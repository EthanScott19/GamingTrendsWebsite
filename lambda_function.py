def lambda_handler():
    import praw
    import boto3
    import requests
    import json
    import time
    from igdb.wrapper import IGDBWrapper
    from datetime import datetime, timedelta
    currentDate = datetime.now()
    currentDate = currentDate.strftime("%b %d %Y")
    date_object = datetime.strptime(currentDate, "%b %d %Y")
    currentDay = int(date_object.timestamp()) 
    weekBefore = date_object - timedelta(weeks=1)
    oneweekBeforeTimestamp = int(weekBefore.timestamp()) 
    twoweekBefore = date_object - timedelta(weeks=2)
    twoweekBeforeTimestamp = int(weekBefore.timestamp())
    threeweekBefore = date_object - timedelta(weeks=3)
    threeweekBeforeTimestamp = int(weekBefore.timestamp())
    fourweekBefore = date_object - timedelta(weeks=4)
    fourweekBeforeTimestamp = int(weekBefore.timestamp())
    weekahead = date_object + timedelta(weeks=1)
    fourweekahead = date_object + timedelta(weeks=4)
    fourweekAheadTimestamp = int(weekBefore.timestamp()) #All of this timestamp stuff was for a different way I was going to approach it, but I didn't end up using most of it. Kept just in case

    user_agent = "" #Insert name there
    reddit = praw.Reddit(
        client_id="" #Insert Reddit API ID here,
        client_secret="" #Insert Reddit API Secret here,
        user_agent=user_agent # setting up reddit scrapper
    )



    client_id = "" #IGDB client ID
    client_secret = "" #IGDB client secret
    token_url = "" #This is your twitch oath URL

    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(token_url, params=params)


    if response.status_code == 200:
        data = response.json()
        access_token = data.get("access_token")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        
    gameList = []
    games_info = {}
    wrapper = IGDBWrapper(client_id, access_token)
    byte_array = wrapper.api_request(
        'release_dates',
        'fields game.name, human, game.cover; where date >= {} & date <= {}; sort date desc; offset 0; limit 500;'.format(oneweekBeforeTimestamp,currentDay) #This is the first and original byte_array to fetch games on the IGDB database
    )
    gameMentions = {}
    gameFrequency = {}
    games_data = json.loads(byte_array.decode('utf-8'))
    for game in games_data:
        game_id = game.get('id')
        game_name = game.get('game').get('name').lower()
        release_date = game.get('human')
        coverId = game.get('game').get('cover')
        games_info[game_name] = {
            'id': game_id,
            'name': game_name,
            'release_date': release_date,
            'cover': coverId
        }
        gameList.append(game_name) #1

    byte_array = wrapper.api_request(
        'release_dates',
        'fields game.name, human, game.cover; where date >= {} & date <= {}; sort date desc; offset 0; limit 500;'.format(twoweekBeforeTimestamp,oneweekBeforeTimestamp)
    )
    gameMentions = {}
    gameFrequency = {}
    games_data = json.loads(byte_array.decode('utf-8'))
    for game in games_data:
        game_id = game.get('id')
        game_name = game.get('game').get('name').lower()
        release_date = game.get('human')
        coverId = game.get('game').get('cover')
        games_info[game_name] = {
            'id': game_id,
            'name': game_name,
            'release_date': release_date,
            'cover': coverId
        }
        gameList.append(game_name) #2


    byte_array = wrapper.api_request(
        'release_dates',
        'fields game.name, human, game.cover; where date >= {} & date <= {}; sort date desc; offset 0; limit 500;'.format(threeweekBeforeTimestamp,twoweekBeforeTimestamp)
    )
    gameMentions = {}
    gameFrequency = {}
    games_data = json.loads(byte_array.decode('utf-8'))
    for game in games_data:
        game_id = game.get('id')
        game_name = game.get('game').get('name').lower()
        release_date = game.get('human')
        coverId = game.get('game').get('cover')
        games_info[game_name] = {
            'id': game_id,
            'name': game_name,
            'release_date': release_date,
            'cover': coverId
        }
        gameList.append(game_name) #3


    byte_array = wrapper.api_request(
        'release_dates',
        'fields game.name, human, game.cover; where date >= {} & date <= {}; sort date desc; offset 0; limit 500;'.format(fourweekBeforeTimestamp,threeweekBeforeTimestamp)
    )
    gameMentions = {}
    gameFrequency = {}
    games_data = json.loads(byte_array.decode('utf-8'))
    for game in games_data:
        game_id = game.get('id')
        game_name = game.get('game').get('name').lower()
        release_date = game.get('human')
        coverId = game.get('game').get('cover')
        games_info[game_name] = {
            'id': game_id,
            'name': game_name,
            'release_date': release_date,
            'cover': coverId
        }
        gameList.append(game_name) #4

    byte_array = wrapper.api_request(
        'release_dates',
        'fields game.name, human, game.cover; where date >= {} & date <= {}; sort date desc; offset 0; limit 500;'.format(currentDay,fourweekAheadTimestamp)
    )
    gameMentions = {}
    gameFrequency = {}
    games_data = json.loads(byte_array.decode('utf-8'))
    for game in games_data:
        game_id = game.get('id')
        game_name = game.get('game').get('name').lower()
        release_date = game.get('human')
        coverId = game.get('game').get('cover')
        games_info[game_name] = {
            'id': game_id,
            'name': game_name,
            'release_date': release_date,
            'cover': coverId
        }
        gameList.append(game_name) #5
        #Comments 1-5 are extra byte arrays that I set up to try to fetch more data since the API would only let me get so much in one call. Whether this worked or not, I'm not 100% sure, but I did get more results after doing this.


    gameList = set(gameList) #Get rid of any overlap
    gameUrls = {} #To hold reddit post urls of game mentions

    gaming = reddit.subreddit("gaming") #Searching reddit for mentions of games in our gamedatabase
    for game_name,game_info in games_info.items():
        gameUrls[game_name] = []
        for post in gaming.search(game_name,limit=20,time_filter="month"):
            if game_name in post.title.lower():
                gameMentions[game_name]=game_info
                gameUrls[game_name].append(post.id) 
                
                
    gameDatajson = json.dumps(gameMentions, indent=2) #This JSON contains all the game data for games that came up in our reddit search. This includes(Game Name, Release Date, Cover image ID, Game ID)
    for game in list(gameUrls.keys()):
        if not gameUrls[game]:
            del gameUrls[game]
    for game_name, urls in gameUrls.items():
        gameFrequency[game_name] = len(urls)

    sorted_frequency = dict(sorted(gameFrequency.items(), key=lambda item: item[1], reverse=True))
    game_urls_json = json.dumps(gameUrls, indent=2) #Converting URL Dictionary to JSON
    game_frequency_json = json.dumps(sorted_frequency, indent=2) #Converting Game Frequency Dictionary to JSON. This will just show gameName : (int) where (int) is the amount of posts containing the games title.

    aws_access_key_id = '' #AWS Access Key ID
    aws_secret_access_key = '' #AWS Access Key Secret
    bucket_name = '' #Your bucket name

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key) #Prepping for sending JSONs to s3 bucket
    s3.put_object(Body=game_urls_json, Bucket=bucket_name, Key='game_urls.json') #1
    s3.put_object(Body=game_frequency_json, Bucket=bucket_name, Key='game_frequency.json') #2
    s3.put_object(Body=gameDatajson, Bucket=bucket_name, Key='game_data.json') #3
    #1-3 Sending our 3 JSONs to s3 bucket
    print("Done!")



