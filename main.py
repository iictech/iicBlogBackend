from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

import datetime

# import uvicorn

# !TEMPURARY MODULE
import json

app = FastAPI()

class Article(BaseModel):
    id: str
    title: str
    body: str
    img_url: str
    likes: int
    tags: list = []
    posted_data: datetime.date
    author: str


@app.get("/getArticles/{fromId:, toId:}")
def get_articles(fromId: str, toId: str = None):
    # !TEMPORARY CODE
    jsonFile = open('article.json',)
    articleContent = json.load(jsonFile)
    # temp = Article(**articleContent)
    artList = []
    for i in range(0, 10):
        artList.append(Article(**articleContent))
        artList[i].body = artList[i].body.split(".")[0] + "."
        artList[i].body = artList[i].body[:100]
    return artList

@app.get("/getArticle/{id:}")
def get_article(id: str):
    # !TEMPORARY CODE
    jsonFile = open('article.json',)
    articleContent = json.load(jsonFile)

    tempId = "abc123"
    if id == tempId:
        return articleContent
    raise HTTPException(404, "I.D. Not Found")

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
