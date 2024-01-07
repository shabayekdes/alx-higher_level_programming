#!/usr/bin/python3
from sys import argv
import requests


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    req = requests.post("http://741e42b6cc21.7177cab4.alx-cod.online:5000/search_user", {"q": letter})

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
