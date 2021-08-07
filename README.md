# Hacker News Scraper

The Hacker News Scraper is a Python terminal application that allows users to view posts from Y Combinator's Hacker News. Hacker News is a news site focusing on computer science and entrepreneurship. Users can see their desired amount of posts and post information from either the "trending" or "newest" pages of the website. 

This application runs in Code Institute's mock terminal on Heroku. 

## User Experience (UX)

### User Stories:

-   The user wants to access Hacker News stories via the terminal.
-   The user wants to be able to see trending stories.
-   The user wants to be able to see the newest stories.
-   The user wants to choose how many stories they want to see.
-   The user wants to see information on the stories, e.g. title, link and post age.
-   The user wants to be able to keep feeding through posts after the initial ones are displayed. 
-   The user's input should be validated at all stages.

[Logic Flowchart](<readme/HN Scraper Flowchart.png>)

## Data Model

The model for this application consists of a Posts class. The class is instantiated with either the parsed HTML for the front page of Hacker News or the first page of newest posts.  

The get_info() method within this class is responsible for retrieving the post data from the parsed HTML. This method creates a dictionary for each post. Each dictionary stores the post title, link, and date posted. These dictionaries are then all stored in a single list that can be looped through to retrieve a requested amount of post data.