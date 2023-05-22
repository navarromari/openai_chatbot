import asyncpraw
import nest_asyncio
import asyncio
import pandas as pd
import sys
import os

nest_asyncio.apply()

async def get_top_posts(subreddit_list):
    # Create an async Reddit instance
    async with asyncpraw.Reddit(
        client_id=os.environ["id"],
        client_secret=os.environ["secret"],
        redirect_uri='http://localhost:8080',
        user_agent=["username"]
    ) as reddit:

        subreddit = await reddit.subreddit(subreddit_list)
        posts = subreddit.top(time_filter="all", limit=3000)
        print(type(posts))

        # Initialize post dataframe
        posts_df = []

        # Retrieve all available data from the subreddit
        async for post in posts:
            posts_df.append({
                'post_id': post.id,
                'subreddit': post.subreddit,
                'selftext': post.selftext,
                'post_url': post.url,
                'post_title': post.title,
                'score': post.score,
                'upvote_ratio': post.upvote_ratio
            })

    return pd.DataFrame(posts_df)

async def get_and_save():
    posts_df = await get_top_posts('nosleep+letsnotmeet+shortscarystories')
    posts_df.to_csv('SUBREDDIT_posts.csv', header=True, index=False)
    return posts_df

if __name__ == '__main__':

  ##Set your environment variables
  os.environ['id'] = input('insert your Reddit Client ID:')
  os.environ['secret'] = input('insert your Reddit Client secret:')
  os.environ['username'] = input('insert your Reddit username:')

  # Create an event loop and run the get_and_save function
  loop = asyncio.get_event_loop()
  posts_df = loop.run_until_complete(get_and_save())

  #Saving text into txt file

  posts_df_tmp = posts_df[['post_title', 'selftext']].astype(str)
  posts_df_tmp['combined_text'] = posts_df_tmp.agg('. '.join, axis=1)
  posts_df_tmp
  all_text = ' '.join(posts_df_tmp['combined_text'])

  f = open("/content/all_text_reddit.txt", "w")
  f.write(all_text)
  f.close()

