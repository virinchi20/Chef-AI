from openai import OpenAI
from pydantic import BaseModel, Field
import logging
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
model = "gpt-4o"

class FoodNameExtraction(BaseModel):
    """first llm call for getting input on what the user wants to cook"""

    food_to_cook: str = Field(description="name of the food recipe to cook")
    is_valid_food: bool = Field(description="Weather this text describes a valid food itme that can be cooked")
    confidence_score: float = Field(description="Confidence score between 0 and 1")

def extract_food_name(user_input: str) -> FoodNameExtraction:

    completion = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Analyze the text for extracting the food name to cook and get the recipe for",
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
        response_format=FoodNameExtraction,
    )
    result = completion.choices[0].message.parsed
    return result


class IngredientList(BaseModel):
    """second llm call to get the list of recipe"""
    ingrediends: list[str] = Field(description="list of all the ingredients required to make this food")


def start():

    food_to_make = input("What would you like to make today")
    first_response = extract_food_name(food_to_make)
    print(first_response.food_to_cook, first_response.is_valid_food, first_response.confidence_score)

if __name__ == "__main__":
    start()
