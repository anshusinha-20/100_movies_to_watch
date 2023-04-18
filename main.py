"""imported BeautifulSoup class from the bs4 module"""
from bs4 import BeautifulSoup

"""getting the data from the index.html file"""
with open("index.html") as file:
    contents = file.read()

"""created soup object"""
soup = BeautifulSoup(contents, "html.parser")

