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
You can visit the finished website [here](https://s3.us-east-2.amazonaws.com/redditgamedata.click/index.html?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLWVhc3QtMiJIMEYCIQCiIICeYzNMXCIjwr%2B8%2FoUcSRLN0AVRAAiM92j%2Bc2b2ggIhALUPiLX2ecyOQmTeYA%2BVn%2F4mFX%2B9l7WTdavJfsMWX6npKu0CCPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNDE2NjUyNzQ3NzU4IgzVftRJrKWF8mWnse0qwQLzuT85J2mkH499DRkkMFQCAXrEFbYi8JGUww2mROEUwBwY2xbFUYs5JPqigtvo1MUWpB5gTZt2ZQzVbBry2%2BV4QTRn3HLTZ8RFixTSQ4s6dmQ7UaEqV1Bf6TQeYFZEIWLD7jEi2JIwuz9RF%2BQScxSXt8AYLaJO9gCUA3AF7Ty7pAn%2FQDC6%2B5NgGbjexe%2BTOYZv4fEP%2FO2hQJL3K%2B6FOw40BvTNlOxQT6q5Jt4APbplKCPlVnBnCKieWZI4iArgkukIdp93rRSlSq3oK5lDniP7VmQgR9pZ3IhkT1WXNCRUrmc%2FuPWU%2FGxGZ4F67WIPoiyl1JbHFSnYztQW2YbxR49BlIcUmtbrwgbTbhFTtsiu%2BtiL7aoUxg8Ay%2FxhSFYjMkN1yZJZI3eKyQG1w%2FF659U%2BGa9qcL7%2FpFUMn19vVuAjgLgw3sr3rAY6sgIgA9jlkMo6lLDjWOnaVLiwVwaHyNSWZ5aU1Hbm7r%2BpVf7sdRxyaud6zkhXpRnZqvUloFJm9EVslROI2oKVr2pSv33RaLrMLVER6OzaY95P1egBmYAxp6RDHiM15vLvw%2BklL%2FqvMtHKWQx8LtLpoLZRwBBpeNoNuraE%2BSj%2BEOEdVe1rzFZvFeaeA%2Bmtmm4lxl7dFEPfnA3N%2BRkesI%2FO5h4LUdfLhDxUFTMwI2O4Fv7UHRWmhsRLKFCzruQiT3fdeOAmLjBEZGjpOJVVXQGkNj6m%2B7LDoeTg8tgt1gWCc%2FchK%2F4W%2F1s0YP%2B3CFwbOl8TUzqh93JmCmZd%2BKmDnBaVOmL0ai4HyvZUXZIpfuF5L5iICbnVbkGQL7x%2FXZ3wvAaTyHSoETBslFbn2cWmp4B8VRNmE%2F0%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T021855Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAWCATQMPXKHT5JO2G%2F20240110%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=2e920fbf47b37d84b1b767ff453f4aeb3bb29da762a8812bba113607da61800f) or by typing in redditgamedata.click
