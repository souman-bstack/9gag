import init as init
import lib.scraper as scraper
from lib.gag import Gag
import sys

def main():
    try:
        try:
            intent = sys.argv[1]
        except:
            print("Please provide correct no of arguments")
        init.init_all()
        if intent=='scrap':
            scraper.scrap_gags()
        else:
            try:
                object_count = int(sys.argv[2])
                Gag.get_gags(sys.argv[1], object_count)
            except:
                print("Count of object should be integer")
    except:
      print("An error has occured")

if __name__ == '__main__':
    main()
