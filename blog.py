from main import getBloggerService
from ai import get_content
from random import randint
from image import generate_image
from helper import get_titles
import os

# topic
TOPIC = "computer Science"


# making blogger service
service = getBloggerService()



# img = "https://i.pinimg.com/originals/cd/bc/f0/cdbcf077b62246123f74fcc919587b0b.jpg"


def buildHtml(title):
    html = get_content(title)
    return html

def postToBlogger(payload):
    print("is it ok? y and n")
    x = input()
    if x == "y":
        generate_image(title)
        post = service.posts()
        insert = post.insert(blogId=os.getenv("BLOG_ID"), body=payload).execute()
        print(insert)
        print("Done posted successfully!")
        return insert
    else:
        print("not posted")


#driver code
title_list = get_titles(TOPIC)
# title_list = ["Complete Guide About Generative AI"]
for title in title_list:
    print(f"do you want this y,n {title}?")
    ans = input()
    if ans == "y":
        print(f"generating blog for... {title}")
        payload = {
        "content": buildHtml(title),
        "title": title,
        "labels": [TOPIC, "Education"],
        "customMetaData": f"this article related to {title}",
        #         "images": [ # Display image for the Post.
        #     {
        #       "url": img,
        #     },
        #   ],
        # "status":"pending",
        }
        postToBlogger(payload)
    else:
        continue