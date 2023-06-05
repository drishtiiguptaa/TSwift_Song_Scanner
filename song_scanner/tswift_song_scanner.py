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
song_titles = [ "Tim McGraw", "Picture to Burn", "Teardrops on my Guitar", "APITW", "The Outside", 
               "TTWAS", "Stay Beautiful", "Should've Said No", "Mary's Song", "Our Song", 
               "IOMWIWY", "Invisible", "APGH", "Fearless", "Fifteen", "Love Story",
               "Hey Stephen", "White Horse", "YBWM", "Breathe", "Tell Me Why", "You're Not Sorry", 
               "The Way I Loved You", "Forever & Always", "The Best Day", "Change", "Jump Then Fall", "Untouchable",
               "Come In The Rain", "Superstar", "TOSOTD", "Today Was A Fairytale", "You All Over Me", 
               "Mr. Perfectly Fine", "We Were Happy", "That's When", "Don't You", "Bye Bye Baby", "ITWAM",
               "Mine", "Sparks Fly", "Back To December", "Dear John", "Mean", "The Story Of Us", "Never Grow Up", "Enchanted",
               "Better Than Revenge", "Innocent", "Haunted", "Last Kiss", "Long Live", "Ours", "Superman", "Electric Touch",
               "When Emma Falls In Love", "I Can See You", "Castles Crumbling", "Foolish One", "Timeless", "State Of Grace", 
               "Treacherous", "IKYWT", "All Too Well", "I Almost Do", "WANEGBT", "Stay Stay Stay", "The Last Time",
               "Holy Grund", "Sad Beautiful Tragic", "The Lucky One", "Everything Has Changed", "Starlight", "Begin Again",
               "The Moment I Knew", "Come Back...Be Here", "Girl At Home", "Ronan", "Better Man", "Nothing New", "Babe", "MIAB", 
               "IBYTAM", "Forever Winter", "Run", "TVFN", "Eyes Open", "Safe & Sound", "WTNY", "Blank Space", "Style", "OOTW", 
               "AYHTDWS", "Shake It Off", "IWYW", "Bad Blood", "Wildest Dreams", "HYGTG", "This Love", "I Know Places", "Clean", 
               "Wonderland", "YAIL", "New Romantics", "Ready For It", "End Game", "IDSB", "Don't Blame Me", "Delicate", "LWYMMD", 
               "So It Goes", "Gorgeous", "Getaway Car", "KOMH", "DWOHT", "Dress", "TIWWCHNT", "CIWYW", "New Year's Day", "IDWLF",
               "IFTYE", "Cruel Summer", "The Man", "The Archer", "ITHK", "MAATHP", "Paper Rings", "Cornelia Street", "DBATC", 
               "London Boy", "SYGB", "False God", "YNTCD", "Afterglow", "ME!", "INTHAF", "Daylight", "AOTGYLB", "cardigan", 
               "TLGAD", "exile", "MTR", "mirrorball", "seven", "august", "TIMT", "illicit affairs", "invisible string", "mad woman", 
               "epiphany", "betty", "peace", "hoax", "the lakes", "willow", "champagne problems", "gold rush", "TTDS", "tolerate it", 
               "NBNC", "happiness", "dorothea", "coney island", "ivy", "cowboy like me", "long story short", "marjorie", "closure", 
               "RWYLM", "it's time to go", "Lavender Haze", "Maroon", "Anti Hero", "SOTB", "YOYOK", "Midnight Rain", "Question...?", 
               "Vigilante Shit", "Bejeweled", "Labyrinth", "Karma", "Sweet Nothing", "Mastermind", "The Great War", "BTTWS", "Paris", 
               "High Infidelity", "Glitch", "WCS", "Dear Reader", "Hits Different", "You're Losing Me"
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
