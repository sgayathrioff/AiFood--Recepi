import streamlit as st
from core.recipeGen import generate_recipe
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# --- Page Configuration ---
st.set_page_config(page_title="AI Food Recipe Generator", page_icon="🍳")

# --- Initialize Session State ---
if "generated_recipe" not in st.session_state:
    st.session_state.generated_recipe = None

# --- Robust PDF Function ---
@st.cache_data
def create_pdf(recipe_text: str) -> bytes: 
    pdf = FPDF() 
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Header
    pdf.set_fill_color(46, 125, 50) 
    pdf.rect(0, 0, 210, 40, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", 'B', 24)
    pdf.set_y(15)
    pdf.cell(0, 10, text="AI GENERATED RECIPE", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    # Body Text
    pdf.set_y(50)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", size=12)
    
    # Character Sanitization (prevents crash on emojis/special chars)
    clean_text = recipe_text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(w=0, h=9, text=clean_text)

    return bytes(pdf.output())

# --- User Interface ---
st.title("AI Food Recipe Generator 🍳")
st.write("Enter your ingredients to generate a structured, step-by-step recipe.")

# Input Section
ingredients = st.text_area("Enter ingredients (comma-separated):", "chicken, rice, tomatoes")

with st.expander("Recipe Options", expanded=False): 
    col1, col2 = st.columns(2)
    with col1:
        cuisine = st.selectbox("Select Cuisine", ["Any", "Indian", "Italian", "Chinese", "Mexican", "French", "Mediterranean"]) 
        meal_type = st.selectbox("Select Meal Type", ["Any", "Breakfast", "Lunch", "Dinner", "Snack"]) 
    with col2:
        prep_time = st.selectbox("Select Prep Time", ["Any", "< 15 minutes", "15-30 minutes", "30-60 minutes", "> 60 minutes"]) 
        veg_option = st.radio("Dietary Preference", ["Any", "Vegetarian", "Non-Vegetarian"])

# --- Helper Function ---
def clean_ingredients(raw_text: str):
    return [item.strip() for item in raw_text.split(",") if item.strip()]

# --- Main Generation Logic ---
if st.button("Generate Recipe", type="primary", use_container_width=True):
    ingredient_list = clean_ingredients(ingredients)

    if not ingredient_list:
        st.error("Please enter at least one ingredient!")
    else:
        try:
            with st.spinner("🍳 Chef is crafting your instructions..."):
                st.session_state.generated_recipe = generate_recipe(
                    ingredient_list,
                    cuisine=cuisine,
                    meal_type=meal_type,
                    prep_time=prep_time,
                    veg_option=veg_option
                )
        except Exception as e:
            st.error(f"Recipe generation failed: {e}")

# --- Clean Display Section ---
if st.session_state.generated_recipe:
    st.divider()
    
    # 1. Download Button at the top of the result for convenience
    pdf_bytes = create_pdf(st.session_state.generated_recipe)
    st.download_button(
        label="📥 Download this Recipe (PDF)", 
        data=pdf_bytes, 
        file_name="recipe.pdf", 
        mime="application/pdf",
        use_container_width=True
    )

    st.success("Recipe Successfully Generated!")
    
    # 2. Display the Recipe
    # This renders Markdown, so ensure your core/recipeGen.py returns 
    # structured text like "### Ingredients" and "### Steps"
    st.markdown(st.session_state.generated_recipe)