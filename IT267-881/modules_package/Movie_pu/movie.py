class Movie:
    def __init__(self) -> None:
        self._title = None
        self._year = None
        self._genre = None
        self_rating = 6


    def _add_movie(self,title:str,year:int,genre:str):
        self._title = title
        self.year = year
        self._genre = genre
    
    def _getmovie_detail(self):
        print(f'Title: {self._title}')
        print(f'Year: {self._year}')
        print(f'Genre: {self._genre}')

class Documentary(Movie):
    def __init__(self):
        Movie.__init__(self)

    def add_channel(self,ch:str):
        self.channel = ch

    def _getmovie_detail(self):
        Movie._getmovie_detail(self)
        print(f'Channel: {self.channel}')

if __name__ == '__main__':
    m1 = Documentary()
    m1._add_movie('my Octopus Teacher',2020,'Documentary')
    m1.add_channel('Netflix')
    m1._getmovie_detail()
