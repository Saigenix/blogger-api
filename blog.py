from main import getBloggerService
from ai import get_content
from random import randint
from image import generate_image
import os

# making blogger service
service = getBloggerService()

title = "Quantum Computing Explained"
customMetaData = f"this article related to {title}"
labels = ["Computer-Science", "Education"]
img = "https://i.pinimg.com/originals/cd/bc/f0/cdbcf077b62246123f74fcc919587b0b.jpg"


def buildHtml():
    html = get_content(title)
    return html


payload = {
    "content": buildHtml(),
    "title": title,
    "labels": labels,
    "customMetaData": customMetaData,
    #         "images": [ # Display image for the Post.
    #     {
    #       "url": img,
    #     },
    #   ],
    # "status":"pending",
}


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


postToBlogger(payload)
