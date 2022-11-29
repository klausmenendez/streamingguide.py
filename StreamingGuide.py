# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Movie:

 def __init__(self,title,genre,director,year):
    self._title=title
    self._genre=genre
    self._director=director
    self._year=year

 def get_genre(self):
    return self._genre

 def get_title(self):
     return self._title

 def get_director(self):
     return self._director

 def get_year(self):
     return self._year
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class StreamingService:

  def __init__(self,name):
      self._name=name
      self._catalog={}
  def get_name(self):
      return self._name
  def get_catalog(self):
      return self._catalog

  def add_movie(self,movie1):
      self._catalog["title"]=movie1.get_title()
      self._catalog["genre"]=movie1.get_genre()
      self._catalog["director"]=movie1.get_director()
      self._catalog["year"]=movie1.get_year()
  def delete_movie(self, title1):
     if str(title1) in self._catalog:
          self._catalog.remove(title1)


class StreamingGuide:
    def __init__(self):
        self.StreamingServices=[]

    def add_streaming_service(self, service1):
        self.StreamingServices.append(service1)
    def delete_Streaming_Service(self, service2):
        for i in self.StreamingService:
            if self.streamingServices[i]==service1:
                 del self.StreamingService[i]
    def where_to_watch_movie(self, MovieTitle):
        self._LocationList=[]
        for service3 in self.StreamingServices:
            for titles in service3.get_catalog():
              if service3.get_catalog()[titles]==MovieTitle:
                 self._LocationList.append(MovieTitle + " " + service3.get_catalog()["year"])
        for services in self.StreamingServices:
            for titles in services.get_catalog():
                if services.get_catalog()[titles]==MovieTitle:
                   self._LocationList.append(services.get_name())
        return self._LocationList

#Movie1=Movie("The Bourne Identity", "action-thriller", "Doug Liman","2002")
#print(Movie1.get_year())
#source1=StreamingService("Netflix")
#source1.add_movie(Movie1)
#print(source1.get_catalog())
#Guide1=StreamingGuide()
#Guide1.add_streaming_service(source1)
#print(Guide1.where_to_watch_movie("The Bourne Identity"))










