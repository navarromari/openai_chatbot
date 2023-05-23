# Meet Spooky!

<img align="left" alt="gif" height="150" style="border-radius:50px;" src="https://64.media.tumblr.com/ba023943349fbcbd4308ea24e13a74c6/08626ce375ab130b-c1/s540x810/a755100840a2d7c38556d429b648ff71a0ffb1b0.pnj">

 Spooky is a *chatbot* that I created to explore the **OpenAI API** and learn more about topics such as **artificial intelligence** and **data manipulation**.

<br>
<br>
<br>
<br>

## Project Overview

My idea was to create a chatbot that could narrate personalized horror stories, using the information provided by users. Spooky would tell the stories from a third-person perspective and be able to adapt the plot and details to make them relevant and relatable to the user's situation.

Users could request a specific story in a particular scenario or simply engage in an informal conversation with the chatbot, and Spooky would narrate a story with the elements he recognize in the conversation.

## Data Collection

To accomplish this, I wanted Spooky to learn from popular short horror stories shared on popular Reddit forums. I used [**PRAW (Python Reddit API Wrapper API)**](https://praw.readthedocs.io/en/stable/index.html) to retrieve the top posts from the chosen forums and saved them in a text file.

In order to incorporate this content into the prompt, I needed to embed the data. I used the [**Llama Index**](https://gpt-index.readthedocs.io/en/latest/index.html) open-source library to create an index, which is a more easily searchable file containing chunks of the subreddit posts. This allowed me to search for and find the most relevant chunks to reply to user input. These chunks are also sent as prompts to the [OpenAI API](https://openai.com/blog/openai-api).

## Project Limitations

Unfortunately, I realized that it would be costly to keep this project online, as I would have to pay per user input. Additionally, I didn't have enough opportunity to thoroughly test Spooky and ensure that it stays in character and functions perfectly. If I had the means to experiment extensively with the bot, I could adapt the context so that it works seamlessly. 

### Nevertheless, Spooky seems conscious of who he is and is capable of telling some stories, as you can see when I run my code in a Google Collab notebook :)

![image](https://github.com/navarromari/openai_chatbot/assets/95860545/5d0f8148-3a03-45d8-8ba3-822503f16f10)

![image](https://github.com/navarromari/openai_chatbot/assets/95860545/d0d7442a-c17f-4a37-a8eb-37d504edc97b)

