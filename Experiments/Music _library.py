class Song:
    """Represents an individual musical track."""

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = artist_count

    def __init__(self, name: str, artist: str, genre: str):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

    def __str__(self) -> str:
        return f"'{self.name}' by {self.artist} ({self.genre})"

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre: str):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist: str):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre: str):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist: str):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1


class MusicLibrary:
    """Manages a collection of Song objects."""
    
    def __init__(self, library_name: str):
        self.library_name = library_name
        self.songs = []

    def add_song(self, song: Song):
        """Adds a pre-built Song object to the library."""
        if isinstance(song, Song):
            self.songs.append(song)
            print(f"✅ Added: {song}")
        else:
            print("❌ Error: You can only add instances of the Song class.")

    def create_and_add_song(self, title: str, artist: str, genre: str):
        """Helper method to build and add a song in one step."""
        new_song = Song(title, artist, genre)
        self.add_song(new_song)

    def display_all_songs(self):
        """Prints formatted information about all songs in the library."""
        print(f"\n--- {self.library_name} ---")
        if not self.songs:
            print("The library is currently empty.")
            return
            
        for index, song in enumerate(self.songs, start=1):
            print(f"{index}. {song}")
        print(f"Total tracks: {len(self.songs)}\n")


if __name__ == "__main__":
# 1. Initialize a library container
    my_playlist = MusicLibrary("Chill Vibes Mix")

# 2. Build explicit Song objects and add them
    song1 = Song("Blinding Lights", "The Weeknd", "Pop")
    song2 = Song("Bohemian Rhapsody", "Queen", "Rock")
    song3 = Song("Blue Gangster", "Michael Jackson", "Pop")
    
    my_playlist.add_song(song1)
    my_playlist.add_song(song2)
    my_playlist.add_song(song3)

# 3. Use the dynamic factory method to add to the songs inline
    my_playlist.create_and_add_song("Stay", "The Kid LAROI & Justin Bieber", "Pop")

# 4. View information about all tracks in the collection
    my_playlist.display_all_songs()