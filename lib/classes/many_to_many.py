class Article:
    
    all= []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
        
    #property for title 
        
    @property
    def title(self):
        return self._title
    @title.setter
    def title (self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
       
       
    # property for author
            
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author 
            
    # property for magazine  
          
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
            
            
            
            
            
            
            
            
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name (self, new_name):
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self._name = new_name
                else:
                    ValueError("Name must be longer than 0 characters")
            else:
                TypeError("Name must be a string")

    def articles(self):
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None
        
    def __repr__(self):
        return f'<Author: name = {self.name}>'





class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2<= len(name) <= 16:
            self._name = name
            
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) >0:
            self._category = category
        

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        them = [article.author for article in self.articles() if isinstance(article.author, Author)]
        return list(set(them))
    

    def article_titles(self):
        titles = []
        for article in self.articles():
            titles.append(article.title)
        if titles:
            return titles
        else:
            return None

    def contributing_authors(self):
        counts = {}
        
        for article in self.articles():
            if article.author in counts:
                counts[article.author] += 1
                
            else:
                counts[article.author] = 1
                
        better_authors = []
        for author, count in counts.items():
            if count >2:
                better_authors.append(author)
                
            if len(better_authors) == 0:
                return None
            
            return better_authors