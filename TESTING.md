# Hacker News Scraper Testing Details

All code was validated using pep8online, with the only remaining error being a "line too long" error in run.py. I also used Autopep8 in VS Code to auto format my Python code on save. 

-   [Autopep8](https://pypi.org/project/autopep8/)
-   [Pep8 Online](http://pep8online.com/)

## Testing User Stories

-   The user wants to access Hacker News stories via the terminal.
    -   This application is run purely from the terminal, either on Code Institute's mock terminal or on a local machine. 
![Terminal view](readme/terminal-view.JPG)

-   The user wants to be able to see trending stories.
    -   This application gives the user the option to choose to view trending stories from Hacker News.
![Trending](readme/trending.JPG)

-   The user wants to be able to see newest stories.
    -   The user is also able to see the most recent stories from Hacker News.
![Newest](readme/newest.JPG)

-   The user wants to choose how many stories they want to see. 
    -   The user has the ability to instruct the program to view a certain amount of posts at a time. They will then be asked if they would like to view more.
![Post amount](readme/post-amount.JPG)

-   The user wants to see information on the stories, e.g. title, link and post age.
    -   Details about each post are displayed to the screen after the user has instructed the program how many posts they wish to view.
![Post details](readme/post-details.JPG)

-   The user wants to be able to keep feeding through posts after the initial ones are displayed.
    -   After the user initially instructs the program on how many posts they wish to view, if there are still posts to be displayed the user will be asked if they wish to view more. Each list of posts (trending/newest) can be drip fed to the user as long as there are some remaining.
![Post feed](readme/post-feed.JPG)

-   The user's input should be validated at all stages.
    -   All user input throughout the program is validated to ensure it can be correctly handled at runtime. 
    -   All number inputs are converted to integers, and all strings are converted to lowercase and checked to match the options a user is given.