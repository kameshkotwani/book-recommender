import copy
from socket import herror
import streamlit as st
from helper import Helper

# setting the page content
st.set_page_config(
    page_title="Book Recommender System",
    page_icon="assets/icon.png",
    menu_items={
        "about": "Hi there, thanks for checking out my app! feel free to checkout my [GitHub](https://www.github.com/kameshkotwani) page lets collaborate!"
    }
)

try:
    @st.cache()
    def load_popular_books():
        helper = Helper()
        return helper.get_popular_books()
    
    helper = Helper()
    

    books_name,author,image,votes,rating = load_popular_books()
    book_options = helper.get_book_list()
    book_options.insert(0,None)
    # creating the sidebar
    with st.sidebar:
        st.title("Collaborative Book Recommender System")
        user_option = st.selectbox(label="Start your search here!", options=(None, "Top 48 Books","Recommend"))

    # checking with all the options and if displaying as per the user
    if user_option ==None:
        st.header("Hi there, this is a collaborative book recommender system.")
        st.subheader("Feel free to explore the options from the sidebar.")
        st.title("[My GitHub Page](https://www.github.com/kameshkotwani)")
    
    elif user_option =="Top 48 Books":
        with st.spinner("loading top 48 books!"):
            st.header("Hi There, you are currently looking at top 48 most read books!")
                
            k:int = 0
            # had to use 12 rows and 4 rows to create a grid of 48 itmes, otherwise getting list index out of range error 
            for i in range(1, 12):
                cols = st.columns(4)
                for j in range(0,4):
                    with cols[j]:
                        st.image(image[k])
                        st.write(f"{books_name[k]}")
                        st.caption(f"Author: {author[k]}")
                        st.caption(f"Votes: {votes[k]}")
                        st.caption(f"Rating: {rating[k]}")
                        k+=1
    elif user_option =="Recommend":
        st.subheader("Displaying records across thousands of books!")
        user_option = st.selectbox(label="",options=book_options)
        if user_option:
            with st.spinner("Fetcing great books!"):
                recommended_books = helper.recommend_books(user_option)
                cols = st.columns(5)
                for i in range(0,5):
                    with cols[i]:
                        st.image(recommended_books[i][2])
                        st.write(recommended_books[i][0])
                        st.caption(f"Author: {recommended_books[i][1]}")
        else:
            st.subheader("Go ahead, search a book and read books similar to the one you loved!")            
except Exception as e:
    print(e)
    st.info("perhaps, you are a unique user and we were not able to find book similar to yours.")