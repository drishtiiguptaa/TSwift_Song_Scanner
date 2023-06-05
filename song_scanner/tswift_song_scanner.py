from collections import Counter
import re

def can_form_song(title, available_letters):
    title_letters = re.sub(r'[^a-zA-Z]', '', title.lower())
    title_counter = Counter(title_letters)
    for letter, count in title_counter.items():
        if count > available_letters.get(letter, 0):
            return False
    return True

def get_possible_songs(song_titles, available_letters):
    possible_songs = []
    for title in song_titles:
        if can_form_song(title, available_letters):
            possible_songs.append(title)
    return possible_songs

# Example usage
song_titles = [ "Tim McGraw", "Picture to Burn", "Teardrops on my Guitar", "A Place in this World", "The Outside", 
               "Tied Together With a Smile", "Stay Beautiful", "Should've Said No", "Mary's Song", "Our Song", 
               "I'm Only Me When I'm With You", "Invisible", "A Perfectly Good Heart"
]

available_letters = {
    "a": 4,
    "l": 3,
    "o": 2,
    "h": 1,
    "m": 1,
    "r": 1,
    "y": 1,
    "s": 2,
    "n": 1,
    "g": 1,
    "u": 1
}

possible_songs = get_possible_songs(song_titles, available_letters)
if not possible_songs:
    print ("NO POSSIBLE SONGS")
print("Possible songs:")
for song in possible_songs:
    print(song)
