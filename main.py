import settings
# from plexapi.server import MyPlexAccount
from plexapi.server import PlexServer
from plexapi.myplex import MyPlexAccount
import plexapi
from pprint import pprint

def connect():
    try:
        plex = PlexServer()   # Defaults to localhost:32400
    except plexapi.exceptions.NotFound as e:
      plex = PlexServer(settings.baseurl, settings.token)
    return plex

def list_client(plex):
    for client in plex.clients():
        print(client.isPlayingMedia())


def main():
    global plex
    plex = connect()
    list_client(plex)

if __name__ == "__main__":
    main()
