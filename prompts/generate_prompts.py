from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    
template = """

You are an expert academic writer and formatter.

Generate a {style_input} style answer for the following paper/question.

Question/Paper:
{paper_input}

Requirements:
- The answer length should be approximately {len_input}.
- Maintain a clean, human-written style.
- Use simple but effective language.
- Keep the structure organized with proper paragraphs and headings if needed.
- Avoid unnecessary repetition.
- Make the response accurate, natural, and exam-friendly.
- If the question requires examples, include relevant examples.
- If definitions are asked, make them concise and clear.
- If the question is theoretical, explain step-by-step in an understandable way.

Output only the final answer without extra explanations.    
    """
    
, input_variables=['style_input', 'paper_input', 'len_input'],

validate_template=False
    
)


template.save('template.json')