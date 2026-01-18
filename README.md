# AI Food Recipe Generator 🍳

This project is a Streamlit-based web application that generates AI-powered recipes based on user-provided ingredients. It uses the Groq API for large language model (LLM) capabilities to generate recipes. Users can customize their recipes by selecting cuisine type, meal type, preparation time, and dietary preferences. The app also allows users to download the generated recipes as PDF files.

## Features
- **AI Recipe Generation:** Generate recipes using the Groq API and user-provided ingredients.
- **Customizable Options:** Choose cuisine type, meal type, preparation time, and dietary preferences.
- **PDF Export:** Download the generated recipe as a PDF file.
- **Interactive UI:** User-friendly interface built with Streamlit.

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd AiFoodRecipe
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Groq API key:
   - Obtain your API key from the [Groq API website](https://groq.com/).
   - Create a `.env` file in the project directory and add your API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the app in your browser (usually at `http://localhost:8501`).
2. Enter a list of ingredients in the text area (comma-separated).
3. Customize the recipe by selecting options like cuisine type, meal type, preparation time, and dietary preferences.
4. Click the "Generate Recipe" button to create a recipe using the Groq API.
5. Download the recipe as a PDF using the provided button.

## Project Structure
```
AiFoodRecipe/
│
├── app.py                # Main Streamlit application file
├── core/
│   ├── recipeGen.py      # Core logic for generating recipes
│   └── llmclient.py      # Handles interactions with the Groq API
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── outputs/              # Folder for storing generated PDFs
```

## Dependencies
The project uses the following Python libraries:
- **Streamlit:** For building the web application.
- **FPDF:** For generating PDF files.
- **Groq API:** For AI-powered recipe generation.

Install all dependencies using the `requirements.txt` file.

## Example Recipe
### CLASSIC CHICKEN AND RICE

**Ingredients:**
- Chicken
- Rice
- Tomatoes

**Steps:**
1. Prepare the chicken by seasoning it with salt and pepper.
2. Cook the rice according to the package instructions.
3. Dice the tomatoes and sauté them in a pan with olive oil.
4. Combine the cooked chicken, rice, and tomatoes in a bowl.
5. Serve hot and enjoy your meal!
