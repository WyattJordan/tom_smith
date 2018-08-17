# A search for the most common programmer name
Ever wondered who in your office has the typical name for a coder? So have I, so I'm crawling all of github to find out.

## Some implementation notes for me

Use pygithub3 (https://github.com/PyGithub/PyGithub)
Attempt to parallelize 
1. See if one program can have multiple log-ins (probs not)
2. Create virtual machines of some sort to simulate multiple computers
3. Make it a group effort? open source so users can help crawl?
4. Buy 30 raspberry pi's (or a similar board) and have them make the api requests

Dynamically update readme as more is parsed with stats:
  *Current number of users parsed
  *Most common name overall
  *Most common name per language
  *Include average number of repos for each name
  *Average number of lines of code? or size of memory used?
  *Brainstorm more interesting stats (check JSON data from user API request)

Tips for making the program able to stop/start whenever:
  *Keep account creation date ranges for parsed and unparsed users
  *Have the program pull the most up-to-date stats and combine with the acquired data just before pushing
  *