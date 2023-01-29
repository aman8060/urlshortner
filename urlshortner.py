import  pyshorteners
url = input("Enter the longer url: ");


def urlshort(url):
    s= pyshorteners.Shortener()
    print(s.tinyurl.short(url))

urlshort(url)