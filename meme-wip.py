import praw

r = praw.Reddit(user_agent='.meme command from bonkersbot, the irc-bot. Searches for imgur links on r/dankmemes to add to separate file')
submissions = r.get_subreddit('dankmemes').get_hot(limit=5)

MIN_SCORE = 200

# Process all the submissions from the front page
for submission in submissions:
    # Check for all the cases where we will skip a submission:
    if "imgur.com/" not in submission.url:
        continue # skip non-imgur submissions
    if submission.score < MIN_SCORE:
        continue # skip submissions that haven't even reached 100 (thought this should be rare if we're collecting the "hot" submission)
    if "i.imgur.com/" in submission.url #checks for i.imgur link
        with open("memes.txt", "a") as myfile: # opens memes.txt
            myfile.write(submission.url) # writes link
