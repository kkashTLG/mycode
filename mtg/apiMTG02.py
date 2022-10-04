#!/usr/bin/env python3

# imports always go at the top of your code
import requests

# define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():

    # create resp, which is our request object
    resp = requests.get(f"{API}sets")

    # display the methods available to our new objects
    print( dir(resp))

if __name__ == "__main__":
    main()


