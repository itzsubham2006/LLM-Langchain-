from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline( 
    model_id='deepseek-ai/DeepSeek-V4-Flash',   
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is the president of America?")

print(result.content)