# it is mainly used to split the document which is not normal text, example coding language etc.

from langchain_text_splitters import RecursiveCharacterTextSplitter

code = """ def linear_search(item, arr):
    
    for i in range(0, len(arr)):
        if(arr[i]==item):
            return f'Item found at idx {i}..!!'
        else: 
            continue
    if(i==len(arr)-1 and arr[i]!=item):
        return 'Item is not present in the list'
        
arr = [1,4,7,3,89]  
a= linear_search(4, arr)
print(a)



linear_search =lambda item, arr: (f"Item found at idx {arr.index(item)}..!!" if item in arr else "Item is not present in the list"
)

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language="python",
    chunk_size = 100,
    chunk_overlap = 0
)

chunks = splitter.split_text(code)
print(chunks)