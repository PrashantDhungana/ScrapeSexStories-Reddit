# ScrapeSexStories-Reddit
This is a **Python** Script written in Python 3. It scrapes the **Reddit Api** for the subreddit **r/sexstories** and saves the stories inside folders using the respective tags for the stories.

###Saving format
**<Today's_Date>/<tag>/<story>**
e.g;
2020_11_03/Milf/My_Milf_Neighbour

### Modules used:

1. **requests**(To perform HTTP request to the Reddit API)
1. **json**(To manipulate the API in json format)
1. **datetime**(To name the parent folder according to the current DAY)
1. **os**(To create folders and files where the Stories are saved)
