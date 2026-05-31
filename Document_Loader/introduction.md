### **Document Loader** are components in Langchain used to load data from various sources into a standardized format usually document objects , which can be used for chunking, embedding, retrieving, and generation.

`Document` = {
    page_content = "The actual text content"
    metadata = { "source" : "filename.pdf",...}
}

-------------------------

## Type of Document Loader -->

1. `TextLoader` : Used to load text document (name.txt) for LLM's. 
2. `PyPDFLoader` : It is a document loader used to load content from PDF files and convert each page into a document object. 

    `Limitations` -> It used PyPDF library, not great with scanned pdf or with complex layout.

3. `DirectoryLoader` : It is a document loader which enables user to load the multiple documents/files from a directory.
4. `WebBaseLoader` : It is a document loader which is used to loads the content of web pages.
5. `CSVLoader` : Used to load CSV files.


# Document Loading Methods in LangChain

## 1. `load()`

### Eager Loading (loads everything at once)

- Returns a list of `Document` objects.
- Loads all documents immediately into memory.

### Best when:
- The number of documents is small.
- You want everything loaded upfront.

-------------------------------------------------------------

## 2. `lazy_load()`

### Lazy Loading (loads on demand)

- Returns a generator of `Document` objects.
- Documents are not all loaded at once; they are fetched one at a time as needed.

### Best when:
- You're dealing with large documents or lots of files.
- You want to stream processing (e.g., chunking, embedding) without using lots of memory.