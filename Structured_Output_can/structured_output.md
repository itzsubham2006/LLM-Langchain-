In langchain Structured Output refers to the practice of having language model return response in a 
well defined data format (example-> JSON), rather than free form text. This makes the model easier to parse
and work with programitaclly



LLMs which have capability to give structured output, in that situation we can use (with_structured_output) class, and which cannot give (Output_parser) class


Three ways to format in structured way-------> 1) TypedDict 2) Pydantic  3) JSON_Schema


----------------------------------------------------------------------------------------------------------------------------------------------

1. TypedDict

TypedDict is a way to define a dictionary in Python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure.

# Why use TypedDict?


It tells Python what keys are required and what types of values they should have.

It does not validate data at runtime (it just helps with type hints for better coding).