"""This module contains helper functions for building a playlist."""

def describe_song(title, artist):
    """Returns a description of a song."""
    return f"{title} by {artist}"

def build_playlist():
    """Builds a playlist from user input."""
    playlist = []
    while True:
        title = input("Enter a song title (or 'q' to quit): ")
        if title.lower() == 'q':
            break
        artist = input("Enter the artist: ")
        song = describe_song(title, artist)
        playlist.append(song)
    return playlist

def display_playlist(playlist):
    """Displays the full playlist."""
    print("\nYour Playlist:")
    for i, song in enumerate(playlist, 1):
        print(f"{i}. {song}")
