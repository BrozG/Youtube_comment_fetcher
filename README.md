# Youtube_comment_fetcher
It fetches the comments from the youtube newest first 1000 comments


▶️ Step 1: Create a Google Cloud Project
Go to the Google Cloud Console.
Click on the top bar and select "New Project".
Enter a name like YouTube Sentiment App, then click Create.

▶️ Step 2: Enable YouTube Data API v3
After project creation, make sure your project is selected (top bar).
Go to APIs & Services → Library.
Search for YouTube Data API v3.
Click it → then click Enable.

▶️ Step 3: Create API Credentials
Go to APIs & Services → Credentials.
Click + Create Credentials → API key.
Copy the generated API key.
(Optional but recommended) Click the edit icon next to the key to:
Restrict key usage (HTTP referrers or IPs)
Limit quota

▶️ Step 4: Store API Key in .env File
Create a file named .env in your project root and paste your key like this:
API_KEY="Your API KEY" #Access the api key from Google cloud console
Replace "Your API KEY" with the actual key you copied.

format example is show in the env_example
