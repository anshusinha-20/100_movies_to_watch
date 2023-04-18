# -------------------- MODULES --------------------
"""imported BeautifulSoup class from the bs4 module"""
from bs4 import BeautifulSoup

"""imported requests module"""
import requests


# # -------------------- WORKING WITH HACKERNEWS --------------------
# """variable to store the address for hackernews"""
# hnEndpoint = "https://news.ycombinator.com"
#
# """variable to store the response"""
# hnResponse = requests.get(url=hnEndpoint)
# hnResponse.raise_for_status()
#
# """variable to store the text from the hackernews website"""
# hnWebpage = hnResponse.text
#
# """created soup object"""
# soup = BeautifulSoup(hnWebpage, "html.parser")
#
# """list to store news texts"""
# hnNewsTexts = []
#
# """list to store news links"""
# hnNewsLinks = []
#
# """getting the details of the news"""
# hnNews = soup.findAll(name="span", class_="titleline")
#
# """loop to iterate over hnNews"""
# for news in hnNews:
#     hnNewsTexts.append(news.contents[0].text)
#     hnNewsLinks.append(news.contents[0].get("href"))
#
# """list to store all the votes"""
# hnNewsVotes = [int(score.getText().split(' ')[0]) for score in soup.findAll(name="span", class_="score")]
#
# print(hnNewsTexts)
# print(hnNewsLinks)
# print(hnNewsVotes)
#
# """printing the news and link with highest number of votes"""
# highestVoteIndex = hnNewsVotes.index((max(hnNewsVotes)))
# print(highestVoteIndex)
# print(hnNewsTexts[highestVoteIndex], hnNewsLinks[highestVoteIndex])


# -------------------- WORKING WITH HTML PARSING --------------------

# """getting the data from the index.html file"""
# with open("index.html") as file:
#     contents = file.read()
#
# """created soup object"""
# soup = BeautifulSoup(contents, "html.parser")

# """getting all anchor tags"""
# allAnchorTags = soup.find_all(name="a")

# """getting all anchor tags"""
# print(allAnchorTags)

# for i in allAnchorTags:
#     # """getting the texts of anchor tags"""
#     # print(i.getText())
#
#     """getting all the href of anchor tags"""
#     print(i.get("href"))

# """getting particulars"""
# collegeUrl = soup.select_one("p a").get("href")
# print(collegeUrl)