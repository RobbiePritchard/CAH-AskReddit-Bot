import praw
import time
from random import randint





#Create the Reddit object 
r = praw.Reddit(user_agent='cardsagainsthumanityAnswerer by /u/kangaroorob')

#Login
username = 'CardAgainstRedAskBot'
password = 'wontthefastcatfallapple'
r.login(username, password,disable_warning=True)
done = []


while True:
	#get top posts
	submissions = r.get_subreddit('askreddit').get_new(limit=50)

	#post
	try:

		for submission in submissions:

			#No Repeats
			if submission.id not in done:

				#Handle Serious Tag
				if '[serious]' in submission.title.lower():
					print '______________________'
					print 'Ignored [Serious] submission'
					print '______________________'
				else:

					#Get the random card
					f = open('cardsagainst.txt')
					allString = f.read()
					splitString = allString.split('<>')
					randomCard =  splitString[randint(0,len(splitString))]
					
					#Comment!
					submission.add_comment(randomCard)
					print '______________________'
					print submission.title
					print randomCard
					print '- - - - - - - - - - - '
					print 'Comment Added'
					print '______________________'
					done.append(submission.id)
		#wait for new submissions
		print '\nWaiting for new Submissions be back soon!\n'
		time.sleep(1800)
	except praw.errors.RateLimitExceeded as error:
            print '\nSleeping for %d seconds\n' % error.sleep_time
            time.sleep(error.sleep_time)
