"""imported BeautifulSoup class from the bs4 module"""
from bs4 import BeautifulSoup

"""getting the data from the index.html file"""
with open("index.html") as file:
    contents = file.read()

"""created soup object"""
soup = BeautifulSoup(contents, "html.parser")

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