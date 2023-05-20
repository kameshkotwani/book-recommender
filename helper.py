from pickle import load
import numpy as np
# contains the class to preprocess the data and send to the main app
class Helper:
    def __init__(self):
        with open('./models/popular.pkl','rb') as f:
            self._popular_df_books = load(f)
        with open('./models/books.pkl','rb') as f:
            self._books_df = load(f)
        with open('./models/pt.pkl','rb') as f:
            self._pt = load(f)
        with open('./models/similarity_score.pkl','rb') as f:
            self._books_options = load(f)
        # self._books_df:pd.DataFrame = load()
        # self._pt:pd.DataFrame = load()
        # self._similarity_score:pd.DataFrame = load()
        self._books_options:list = self._pt.index.tolist()

    def get_book_list(self)->list:
        """returns the book options to display to the user"""
        self._books_options.insert(0,None)
        return self._books_options

    def get_popular_books(self):
        """Returns the list of all the values required to display on main page"""
        book_name:list = self._popular_df_books['Book-Title'].tolist() 
        author:list = self._popular_df_books['Book-Author'].tolist() 
        image:list = self._popular_df_books['Image-URL-M'].tolist() 
        votes:list = self._popular_df_books['num_ratings'].tolist() 
        rating:list = self._popular_df_books['avg_ratings'].tolist() 
        return (book_name,author,image,votes,rating)  
    
    def recommend_books(self,book_name:str):
        "recommends the similar books"
        index = np.where(self._pt.index==book_name)[0][0]
        similar_items = sorted(list(enumerate(self._similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]
        data = list(list())
        for i in similar_items:        
            item = list()
            temp_df = self._books_df[self._books_df['Book-Title']==self._pt.index[i[0]]]
            item.extend(temp_df.drop_duplicates('Book-Title')['Book-Title'].tolist())
            item.extend(temp_df.drop_duplicates('Book-Title')['Book-Author'].tolist())
            item.extend(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].tolist())
            data.append(item)
        return data

