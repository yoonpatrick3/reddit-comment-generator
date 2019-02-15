#from textgenrnn import textgenrnn
import praw
import os


sb = input("Which subreddit: ")
cm = int(input("Num comments: "))

reddit = praw.Reddit(client_id='d5F-aZ-nf6C08Q',
                     client_secret='yM5xi3gH92zrs8r35iKxmz6zsnI',
                     user_agent='my user agent')

					 
subreddit = reddit.subreddit(sb)

save_path = "\\Users\yoonp\independentCS\MLTEST\textFiles\\"
		
with open(os.path.join(save_path,'commentFile.txt'), 'w+', encoding='utf-8') as file:
	for comment in subreddit.comments(limit=cm):
		file.write(str(comment.body) + "\n")
		
with open(os.path.join(save_path,'titleFile.txt'), 'w+', encoding='utf-8') as file2:
	for sub in subreddit.hot(limit=cm):
		file2.write(str(sub.title) + "\n")

#file.close()
#print(subreddit_comments)

   