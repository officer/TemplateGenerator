from bs4 import BeautifulSoup
from logging import config, getLogger

def main():
  with open("./tests/contents/test_list.html") as fp:
    text = "".join( fp.readlines() )
    parser = BeautifulSoup(text, "html.parser")
    tbody = parser.find("tbody")
    trs = tbody.findAll("tr")
    for tr in trs:
      print(tr.find("td").find("a")["href"])

def test():
  with open ("./tests/contents/test_a.html") as fp:
    text = "".join( fp.readlines() )
    parser = BeautifulSoup(text, "html.parser")
    divs = parser.findAll("div", class_="part")
    for index in range(len(divs)):
      element = divs[index].find("pre")
      if element != None and element.string != None:
        print(index)
        print(element.string)
  
def main1():
  table = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
  }
  
  print(ans)

if __name__ == "__main__":
    config.fileConfig("config/logging.yaml")
    logger = getLogger(__name__)
    logger.info("test")
    main1()