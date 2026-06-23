from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
import warnings
warnings.filterwarnings('ignore')


loader = DirectoryLoader(
    path=r'C:\Users\Subham Pathak\Documents\ACADEMICS\NOTES\JAVA',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()
# docs2 = loader.lazy_load()         ------> Use when the documents are in large number     

print((docs[0].page_content))
print((docs[0].metadata))