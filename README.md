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
You can visit the finished website [Here](https://s3.us-east-2.amazonaws.com/redditgamedata.click/index.html?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLWVhc3QtMiJGMEQCIEWjiQlT5FuykgXWIdNsMUjX0Nm290Rh7Mg7lC5uaxdWAiB%2BYzLAcB3JlOpvOc3AIGtnQEc13Oa77o1TO50CmRxnuSrtAgjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDQxNjY1Mjc0Nzc1OCIMb7G0Aat0Ttj7SmO9KsECOfGtZm7gJG22b0FfLrp9sJP00fMfXYrITVcV6SJ%2FTdwF5BUZGRbCqzG4uLeWaUJuNAToMuOncqSClcWYk6310J5YqfH9xy%2F%2FWxLuCWJACHhdFVvO10vvdGR7SWij1wL2rvZyzed5YNp1BnV2YaclVL8Q71mWaSiYPIztHn49%2F3UEax7vVzlgji55QUx9gcHidd%2Fque%2BDJ8OIdWz%2BVISpF8%2F%2BOOEOPCiGyUln5MjDbqLSXARwelDXgR%2BcBgIJb03J0abMejeM2Qk2KK2gnqz8cDkRlOBEfCksVOGiWw%2Fu6bXZIOj0ESRbf89f0rHoX7MESyc2Jo1%2BubsIAXCYAOJHe8wiBvy9eP0cNfyWv0ztdHPp%2BphStHsxqaf44UkyfBw%2BxQsggCk7pPJgep%2BX8cBe874eIbsN26uVasIlyWXZeSC8MJSRg6wGOrQC36itORXUZVAPxrldfAAMAl3Birb4MZZvmd4TGGfWGIqlF9ALwhpSuZzGvaS8H91OGyMVAb5%2BekmaQWOUTolhE%2FAnR1uf4T%2BaO%2BE28h95t4NHe%2B9XTpVa0tObW40qrha0vGnN8X8VgqKu4niKXubBlAXcPyxaUC%2FPq0sCOEA9GO0SLvYTVgxyNEC%2BR%2FxGJHSWBmFIj6ghe0FobEbp0uiu0qOh90RldbbkhsBmcPUc3jpAArqftjUOMsIdq9mNWLspR8eIpQ4hEW4VOwD9wam22WRSysBIfPR3x60aK%2F32PcBCVRj6RSvvbKyr%2BAK9FCcza81s6hgzLMFlRodMILbMLD%2ByNQ537LmnfKwtmp4Lj0StKkWO2WlUhepXOKUiKo59UmSYm2%2B5fH7VfhGTHnKy0bX2ILU%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231218T232229Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAWCATQMPXM4OUKV5W%2F20231218%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=788654cc1908d8313e1a096e92ed0e2a45a5db2dae8b6dae8cf28392331ed9cc) or by typing in redditgamedata.click
