from langchain_community.document_loaders import WebBaseLoader
URL = "https://www.amazon.in/s?k=lenovo+ideapad+gaming+3+rtx+2050+ryzen+5+5500h"

loader = WebBaseLoader(URL)
docs = loader.load()

print(docs[0].page_content)