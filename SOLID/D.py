from abc import ABC, abstractmethod

# Abstract base class for a data source
class DataSource(ABC):
    def __init__(self,path):
        self.path = path

    # Define interface for reading and writing data
    @abstractmethod
    def read_data(self):
        pass
    @abstractmethod
    def write_data(self):
        pass

# DataSource implementation for text files
class TextDataSource(DataSource):
    def read_data(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data
    def write_data(self,data):
        with open(self.path,'w') as file:
            file.write(data)

# DataSource implementation for databases
class DbDataSource(DataSource):
    def read_data(self):
        return "data from database"
    def write_data(self,data):
        print(f"write {data} to database")

class Text(ABC):
  def __init__(self):
        self.data = ''
  
class TextOperationsMixin:
  # Returns True if the word is in the data
    def search_for_word(self, word):
        return word in self.data

    # Returns the number of occurrences of a word in the data
    def count_occurences(self, word):
        return self.data.count(word)
  
  
class TextOperations(TextOperationsMixin, Text):
  def __init__(self,text:str):
      super().__init__()
      self.data = text

# Perform text operations using a DataSource
class TextOperationsWithDataSource(TextOperationsMixin, Text):
    def __init__(self,data_source:DataSource):
        super().__init__()
        self.data_source = data_source
        self.data = self.data_source.read_data()

# Create DataSource instances
file = TextDataSource("D:\\data.txt")
db = DbDataSource("customers")

# # Use TextOperations with different data sources
# obj = TextOperationsWithDataSource(file)
# print(f"{obj.search_for_word('more')}")
# print(f"{obj.count_occurences('be')}")

obj = TextOperations('sdfdsfdsf sdf dsfsdf dsf sdf dsf sdfsdfewrew sdf ')
print(f"{obj.search_for_word('sdf')}")
print(f"{obj.count_occurences('sdf')}")

obj = TextOperationsWithDataSource(db)
print(f"{obj.search_for_word('data')}")
print(f"{obj.count_occurences('from')}")