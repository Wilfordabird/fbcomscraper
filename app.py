import streamlit as st
import pandas as pd
import facebook_scraper

def scraping_comments(url):
    options={"comments": 1000}
    urls = [url]
    comment_text = []
    st.write(st.secrets["MY_USER"])
    st.write(st.secrets["MY_PASS"])
    
    posts = facebook_scraper.get_posts(options = options, post_urls=urls, credentials=tuple({"username": st.secrets["MY_USER"], "password": st.secrets["MY_PASS"]}.values()))
    for post in posts:
        comments = post["comments_full"]
        for comment in comments:
            comment_text.append([comment['commenter_name'], comment["comment_text"]])
            replies = comment["replies"]
            for reply in replies:
                comment_text.append([reply['commenter_name'], reply["comment_text"]])
    df = pd.DataFrame(comment_text, columns=["commenter_name", "comment_text"])
    return df

def main():
    st.image("YIGH-Blue.png")
    st.title("Facebook Scraper")
    url = st.text_input("Enter URL")
    if st.button("Scrape"):
        comment_text = scraping_comments(url)
        st.dataframe(comment_text)


if __name__ == "__main__":
    main()
    #example url: https://www.facebook.com/NBCNews/posts/pfbid02qzHYaSACV21AsHbzUDms5j51yQ18Bc2Xio6gjP1MDsFDVuv4w5yuh6dHMUBTEuEpl
    #unicef url: https://www.facebook.com/UNICEFSouthAfrica/posts/pfbid088DuwL5BhynA5r7X7DXCqFvCeneR4KtuXii3ARk1bGoK7bh6q7Rqn4PzR1JmJJA6l
    
