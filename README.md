# ScrapeSexStories-Reddit
This is a **Python** Script written in Python 3. It scrapes the **Reddit Api** for the subreddit **r/sexstories** and saves the stories inside folders using the respective tags for the stories.

###Saving format
**TODAY'S_DATE/TAG/STORY.TXT**
e.g;
2020_11_03/Milf/My_Milf_Neighbour

### Installation Process:
    git clone https://github.com/PrashantDhungana/ScrapeSexStories-Reddit.git
    cd ScrapeSexStories-Reddit
    pip install -r requirements.txt
    python Scrape.py

### Modules used:

1. **requests**(To perform HTTP request to the Reddit API)
1. **json**(To manipulate the API in json format)
1. **datetime**(To name the parent folder according to the current DAY)
1. **os**(To create folders and files where the Stories are saved)

### Example:
    cd 2022_3_19