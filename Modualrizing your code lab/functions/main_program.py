"""Main program to use the playlist functions."""

from my_functions import build_playlist, display_playlist

def main():
    # Build the playlist using user input
    playlist = build_playlist()
    # Display the final playlist
    display_playlist(playlist)

if __name__ == "__main__":
    main()
