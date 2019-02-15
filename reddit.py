import praw
import os

#Change client id and client secret!
reddit = praw.Reddit(client_id='d5F-aZ-nf6C08Q',
					 client_secret='yM5xi3gH92zrs8r35iKxmz6zsnI',
					 user_agent='my user agent')

choice = input("comment (c), titles (t), or account (a)? ")

#Path to where text files save, change on own device
save_path = "\\Users\\yoonp\\independentCS\\MLTEST\\textFiles\\"

if choice == "c" or choice == "t":
	sb = input("Which subreddit: ")
	
	
	subreddit = reddit.subreddit(sb)
	
	if choice == "c":
		cm = input("Num comments limit (or no limit say none): ")
		
		if cm == "none":
			with open(os.path.join(save_path,'commentFile.txt'), 'w+', encoding='utf-8') as file:
				for comment in subreddit.comments(limit=None):
					file.write(str(comment.body) + "\n")
		else:
			with open(os.path.join(save_path,'commentFile.txt'), 'w+', encoding='utf-8') as file:
				for comment in subreddit.comments(limit=int(cm)):
					file.write(str(comment.body) + "\n")
	
	else:
	
		cm = input("Num titles limit (or no limit say none): ")

		if cm == "none":
			with open(os.path.join(save_path,'titleFile.txt'), 'w+', encoding='utf-8') as file2:
				for sub in subreddit.hot(limit=None):
					file2.write(str(sub.title) + "\n")
		else:
			with open(os.path.join(save_path,'titleFile.txt'), 'w+', encoding='utf-8') as file2:
				for sub in subreddit.hot(limit=int(cm)):
					file2.write(str(sub.title) + "\n")

else:
	un = input("Which account: ")
	cm = input("Num comment limit (or no limit say none): ")
	
	if cm == "none":
		comments = reddit.redditor(un).comments.new(limit=None)
		
	else:
		comments = reddit.redditor(un).comments.new(limit=int(cm))
	
	with open(os.path.join(save_path,'accountFile.txt'), 'w+', encoding='utf-8') as file:
		for comment in comments:
			file.write(str(comment.body) + "\n")
		
#file.close()
#print(subreddit_comments)

   