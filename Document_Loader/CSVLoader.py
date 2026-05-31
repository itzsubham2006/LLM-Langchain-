from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path=r'C:\Users\Subham Pathak\Desktop\AI\LANGCHAIN\datasets\Churn_Modelling.csv'
)

docs = loader.load()

print(docs[0].page_content)