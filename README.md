# GamingTrendsWebsite

## The Lambda Function
The first part of my project was writing a function in Python that uses the Reddit API to search for mentions of games in a subreddit.
To identify mentions of games in a subreddit my program had to be able to distinguish between words that are game titles and those that are not.
To do this, I used the IGDB API and used their database to create a list of games.
Due to there being way more games than I realized and limitations with the IGDB API, I decided to make my project a tool for new and upcoming releases.
In the Python file attached, it is the exact code I wrote for my lambda function, except I took out my API keys and IDs.
The lambda function puts all of our found data into a JSON file and sends it to an s3 bucket.
I then uploaded my Python file with all of the dependencies in a zip file to my lambda function.
I added a trigger to execute our function at 8 pm every day so we can get new results.

## The HTML and JavaScript
The JavaScript fetches the data from the three local JSON files (in the s3 bucket).
It sorts the game in order by mentions on Reddit. The JSON file game_frequency.json has this value stored for all the games.
I created a table of the games displaying the "Game"."Release Date" "Mentions" and "Reddit Posts". The Reddit posts part also links to the posts.
I was hoping to add the cover images for the games but I couldn't figure out how to interpret the Cover ID we have in the JSON file. It has a number, but I don't know how to get an image from that number.
I also added a countdown timer so the user knows when the next update is (the next time the lambda function is triggered).

## Other AWS Services used
Once we have our JSON, HTML, and JS files in the s3 bucket, you can change the s3 bucket to host a static website.
When you do that you also have to create a bucket policy for the s3 bucket that grants public read access to the files. 
Make sure you only have data you want to be accessible in this bucket. In our case, the JSON files were for the public so this was fine.
I then used Route 53 to redirect our static website to a domain that I created. 

## Additional Files Provided
In this repository, I also included the JSON files.
The JSON files are from the first run of the lambda function working properly and are what I used as a reference when writing my JavaScript.
Also, here is the link to the finished website: [redditgamedata.click](redditgamedata.click)
