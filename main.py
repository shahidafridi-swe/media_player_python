from abc import ABC, abstractmethod

class Description:
    def __init__(self,description) -> None:
        self.__description = description

    @property
    def get_description(self):
        return self.__description

class Media(ABC):
    def __init__(self, title, duration) -> None:
        self.title = title
        self.duration = duration

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def play(self):
        pass
    
class Music(Media,Description):
    def __init__(self, title, duration,description) -> None:
        Media.__init__(self,title,duration)
        Description.__init__(self,description)

    def play(self):
        print(f"Playing Music: {self.title}")
   
    def info(self):
        print(f"Title: {self.title}, Duration: {self.duration}, Description: {self.get_description}")

    
class Video(Media,Description):
    def __init__(self, title, duration,description) -> None:
        Media.__init__(self,title,duration)
        Description.__init__(self,description)

    def play(self):
        print(f"Playing Video: {self.title}")

    def info(self):
        print(f"Title: {self.title}, Duration: {self.duration}, Description: {self.get_description}")

    
class AudioBook(Media,Description):
    def __init__(self, title, duration,description) -> None:
        Media.__init__(self,title,duration)
        Description.__init__(self,description)

 
    def play(self):
        print(f"Playing Audiobook: {self.title}")

    def info(self):
        print(f"Title: {self.title}, Duration: {self.duration}, Description: {self.get_description}")


class Library:
    def __init__(self) -> None:
        self.__media_items = []
        self.__media_by_genre = {}
        self.__genre = ''
    

    def get_media_items(self):
        return self.__media_items

    def get_media_by_genre(self):
        return self.__media_by_genre
    
    def add_media(self, media):

        if isinstance(media, Music):
            self.__genre = 'Music'
        elif isinstance(media, Video):
            self.__genre = 'Video'
        elif isinstance(media, AudioBook):
            self.__genre = 'Audiobook'
        self.__media_items.append(media)
        if self.__genre in self.__media_by_genre.keys():
            self.__media_by_genre[self.__genre].append(media)
        else:
            self.__media_by_genre[self.__genre] = [media,]


class User(ABC):
    def __init__(self, name) -> None:
        self.__name = name

    @abstractmethod
    def play_media(self):
        pass

class FreeUser(User):
    def __init__(self, name) -> None:
        super().__init__(name)

    def play_media(self, library):
         for media in library.get_media_items():
            media.play() 


class PremiumUser(User):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__favourite_genre = ''


    def set_favourite_genre(self, genre):
        self.__favourite_genre = genre

    def get_favourite_genre(self):
        return self.__favourite_genre 
    
        
    def play_media(self, library):
        # for genre, mediaList in library.get_media_by_genre().items():
        #     if genre == self.get_favourite_genre():
        #         for media in mediaList:
        #             media.play()
        if self.get_favourite_genre() in library.get_media_by_genre():
            for media in library.get_media_by_genre()[self.get_favourite_genre()]:
                media.play()
        else:
            print("Invalid Genre")



video1 = Video("Gopal Bhar", "23.40 min", "Publisher: Sony" )
music1 = Music("Sura Yasin", "50.30 min", "Vocal: Hisham Al Arabi")

library = Library()

user1 = FreeUser("User 1")
user2 = PremiumUser("User 2")

library.add_media(video1)
library.add_media(music1)

user1.play_media(library)
user2.set_favourite_genre("Video")
user2.play_media(library)