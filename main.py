import streamlit as st
import Backend
from LinkScrapeData import ScrapeSite,extract_text_from
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os
import keyring
import json
import pickle
from Backend import llm
from langchain import PromptTemplate

#vector store is contained within Main.py and not backend.py

#------------------------------------------STREAMLIT APPLICATION------------------------------------------
# Set page title and icon
st.set_page_config(page_title="Mitre-Tcode ProcedureGPT App", page_icon="🛡️")

# Add a cool title header
st.title("🛡️ Welcome to the Mitre-Tcode ProcedureGPT App 🛡️")

# Add some description text
st.write("This app allows you to explore Mitre-Tcodes procedures using the power of GPT-3.5.")

# Input for article links as a text box
st.write("Enter article link")
article_links_text = st.text_area("Article Link")

# Input for Mitre T-code varaible
t_code = st.text_input("Enter a Mitre T-code:")

# Initialize a list to store entered article links
article_links = []

# Check if both article links and T-code are empty
if not article_links_text.strip() and not t_code.strip():
    st.warning("Please enter at least one article link and Mitre T-code.")
else:
    # Submit button to save the entered data into variables
    if st.button("Submit"):
        # Split the article links by line breaks and save them into the list
        article_links = article_links_text.split("\n")

        # Print entered article links
        st.subheader("Procedure TTP")
        #Article link Dictionary and it's HTML codes
        LinkDataSet = {link: extract_text_from(ScrapeSite(link)) for link in article_links}

        #format dataset to fit lanchain and chunkdata for embedding
        Total_chuncked_data = []
        for link, info in LinkDataSet.items():
            title = info['title']
            pagecontent = info['pagecontent']
            #calling function to format Langchain Data
            formatted_langchainChunkingData=Backend.get_text_chunks_langchain(pagecontent,link,title)
            Total_chuncked_data.append(formatted_langchainChunkingData)
        #stat the embedding process by ingesting all the data
        # --------------------storing embeddings in vectorStore--------------------------------
        embeddings =OpenAIEmbeddings()
        vectorStore_openAI = FAISS.from_documents(Total_chuncked_data[0], embeddings)
        with open("faiss_store_openai.pkl", 'wb') as f:
            pickle.dump(vectorStore_openAI, f)
        with open("faiss_store_openai.pkl", 'rb') as f:
            VectorStore = pickle.load(f)
        #questions asking
        # Prompt_template.format( Tcode="T1566")


        #question='What are the various methods and tactics used by adversaries in phishing attacks, including targeting individuals or organizations, using malicious attachments or links, and employing social engineering techniques?'
        answer = Backend.QARetrieval(llm,VectorStore,t_code.upper())
        st.write(answer)

#---------------------You can add more cool features and components here!---------------------------------------------------

        #st.subheader("Detection Rule")
        #Write Detection rule -> enalbe optional by uncommenting
        #RuleType = 'YARA'
        #DetectRule = Backend.DetectRuleCreate(llm, RuleType, t_code.upper(),answer)
        #st.code(DetectRule,language='python')
