import praw

r = praw.Reddit(user_agent='.meme command from bonkersbot, the irc-bot.')
submissions = r.get_subreddit(dankmemes).get_hot(limit=5)

