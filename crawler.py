import urllib.request
from bs4 import BeautifulSoup

# url = 'https://yahoo.com'
# connection = urllib.request.urlopen(url)
#
# data = connection.read()
#
# links = []
# connections = []
# while true:
#     newlink = soup.find(
# soup = BeautifulSoup(data,'html.parser')
# for link in soup.find_all('a'):
#     links.append(link.get('href'))

visitedLinks = []
firstPageLinks = []

def checkValid(testLink):
    try:
        urllib.request.urlopen(testLink)
    except urllib.error.HTTPError as err:
        #print("HTTPError code:")
        #if err.code == 403:
            #print("403")
        return False
    except ValueError:
        #print("value error")
        return False
    except urllib.error.URLError:
        return False
    return True

def checkVisited(testLink):
    for link in visitedLinks:
        if link == testLink:
            return False
    return True



def newLink(currentLink,i):
    if i < 100:
        visitedLinks.append(currentLink)
        connection = urllib.request.urlopen(currentLink)
        data = connection.read()

        currentLinks = []
        linkToBeCrawled = ''

        soup = BeautifulSoup(data,'html.parser')
        for link in soup.find_all('a'):
            if link.get('href') != currentLink:
                currentLinks.append(link.get('href'))
                if i == 0:
                    firstPageLinks.append(link.get('href'))

        try:
            linkToBeCrawled = currentLinks[0]
        except IndexError:
            currentLinks = firstPageLinks
            print("resetting back to home page")


        isValid = False
        while(isValid == False):
            if checkValid(linkToBeCrawled) == False or checkVisited(linkToBeCrawled) == False:
                try:
                    currentLinks.remove(currentLinks[0])
                    linkToBeCrawled = currentLinks[0]
                except IndexError:
                    currentLinks = firstPageLinks
                    print("resetting back to home page")
            else:
                isValid = True

        # try:
        #     urllib.request.urlopen(linkToBeCrawled)
        # except urllib.error.HTTPError as err:
        #     print("HTTPError code")
        #     if err.code == 403:
        #         print("403")
        #         links.remove(links[0])
        #         linkToBeCrawled = links[0]
        # for link in visitedLinks:
        #     if link == linkToBeCrawled:
        #         #links[0] is previous linkToBeCrawled
        #         links.remove(links[0])
        #         linkToBeCrawled = links[0]

        print(i+". "+linkToBeCrawled)

        i = i+1
        newLink(linkToBeCrawled,i)
    else:
        print("done")

link = "https://www.yahoo.com"
visitedLinks.append(link)
newLink(link,0)
