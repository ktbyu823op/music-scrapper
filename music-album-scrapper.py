from extractors.bandcamp import extract_bandcamp_album

print("This is Music Album Scrapper from Bandcamp.com")
keyword = input("Enter the keyword you want to search : ")

albums = extract_bandcamp_album(keyword)

file = open(f"{keyword}_album.csv", "w", encoding="utf-8-sig")
file.write("Title,Artist,Length,Release,Link\n")

for album in albums:
    file.write(f"{album["title"]},{album["artist"]},{album["length"]},{album["release"]},{album["link"]}\n")
