from selenium import webdriver
from bs4 import BeautifulSoup


def get_page_num(keyword):
    browser = webdriver.Chrome()
    url = f"https://bandcamp.com/search?q={keyword}&item_type=a"
    browser.get(url)

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagelist = soup.find("ul", class_="pagelist")
    if pagelist == None:
        return 1
    pages = pagelist.find_all("li")
    page_num = len(pages)
    return page_num


def extract_bandcamp_album(keyword):
    pages = get_page_num(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        browser = webdriver.Chrome()
        url = f"https://bandcamp.com/search?item_type=a&page={page+1}&q={keyword}"
        browser.get(url)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        album_list = soup.find("ul", class_="result-items")
        albums = album_list.find_all("li", class_="searchresult data-search")
        for album in albums:
            info = album.find("div", class_="result-info")
            title = info.find("div", class_="heading").find("a")
            artist = info.find("div", class_="subhead")
            length = info.find("div", class_="length")
            release = info.find("div", class_="released")
            link = info.find("div", class_="itemurl").find("a")
            album_data = {
                "title": title.string.replace("\n", "").replace("  ", ""),
                "artist": artist.string.replace("by ", "")
                .replace("\n", "")
                .replace("  ", ""),
                "length": length.string.replace("\n", "")
                .replace("  ", "")
                .replace(",", "-"),
                "release": release.string.replace("\n", "")
                .replace("  ", "")
                .replace("released", "")
                .replace(",", " -"),
                "link": link.string.replace("\n", "").replace("  ", ""),
            }
            results.append(album_data)
    return results
