import urllib.request

def check_connection(url):
    code = urllib.request.urlopen(url).getcode()

    # code for success is 200
    if code == 200:
        print("ok")
    else:
        print("down")
    
def main():
    url = input("Enter url here: ")
    check_connection(url)

if __name__ == "__main__":
    main()