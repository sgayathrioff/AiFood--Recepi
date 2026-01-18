import sys
from pathlib import Path
import logging

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from services.llmclient import LLMClient
llm = LLMClient()

def generate_recipe(ingredients: list, cuisine: str, meal_type: str, prep_time: str, veg_option: str  ) -> str:
    
    logging.info(f"Generating Recipe ({len(ingredients)} ingredients)")
    prompt = f"""You are a professional chef creating a delicious recipe.

Create a complete {veg_option.lower()} {meal_type.lower()} recipe in {cuisine} style using the following ingredients: {', '.join(ingredients)}.

Requirements:
- Start with a short, inviting introduction to the dish
- Provide a clear list of ingredients with quantities
- Write step-by-step cooking instructions in simple language
- Mention approximate cooking time ({prep_time}) and serving size
- Keep the recipe between 150-250 words
- Use a friendly, conversational tone
- Do NOT use markdown, emojis, or bullet points
- Write as continuous text suitable for text-to-speech
"""


    return llm.generate(prompt)
