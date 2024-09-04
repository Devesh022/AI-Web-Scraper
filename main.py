import streamlit as st
from app_srape import scrape_website,split_dom_content,clean_body_content,extract_body_content
from app_parse import parse_with_ollama
st.title("AI web scraper")

url =st.text_input("enter a website url")

if st.button("scrape site"):
    st.write("scarping the website")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content

    with st.expander("view DOM content"):
        st.text_area("DOM Content", cleaned_content,height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse_Content"):
        if parse_description:
            st.write("parsinh the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks,parse_description)
            st.write(result)