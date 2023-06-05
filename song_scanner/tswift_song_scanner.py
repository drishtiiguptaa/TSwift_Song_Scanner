from collections import Counter

def can_form_song(title, available_letters):
    title_counter = Counter(title.lower().replace(" ", ""))
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
song_titles = [
    "Hello",
    "Shape of You",
    "Bohemian Rhapsody",
    "Yesterday",
    "Don't Stop Believin'",
    "Wonderwall"
]

available_letters = {
    "a": 4,
    "l": 3,
    "o": 2,
    "h": 1
}

possible_songs = get_possible_songs(song_titles, available_letters)
print("Possible songs:")
for song in possible_songs:
    print(song)
