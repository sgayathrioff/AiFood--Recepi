import streamlit as st
import base64
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# --- Page Config ---
st.set_page_config(page_title="Recipe UI Tester", page_icon="🍳", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 1.8rem; color: #e67e22; }
    .recipe-card { border: 1px solid #ddd; padding: 20px; border-radius: 10px; background-color: #fdfdfd; }
    </style>
    """, unsafe_allow_html=True)

# --- Mock PDF Function ---
def create_pdf(recipe_text: str) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", 'B', 16)
    pdf.cell(0, 10, txt="AI Generated Recipe", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("helvetica", size=12)
    clean_text = recipe_text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(w=0, h=10, txt=clean_text)
    return bytes(pdf.output())

# --- Sample Data (Mocking the AI Response) ---
MOCK_RECIPE = """
### ITALIAN CHICKEN PARMESAN

**Ingredients:**
- 2 Chicken Breasts
- 1 cup Marinara Sauce
- 1/2 cup Mozzarella Cheese
- 1/4 cup Parmesan Cheese
- 1 tsp Italian Herbs
- Fresh Basil leaves

**Instructions:**
1. **Prep:** Flatten the chicken breasts to even thickness.
2. **Sear:** Brown the chicken in a pan for 3 minutes per side.
3. **Assemble:** Top with sauce and cheeses.
4. **Bake:** Bake at 200°C for 15 minutes until cheese bubbles.
5. **Serve:** Garnish with fresh basil.
"""

st.title("👨‍🍳 Recipe UI Dashboard")

# --- Sidebar for testing inputs ---
with st.sidebar:
    st.header("Settings")
    cuisine = st.selectbox("Cuisine", ["Italian", "Indian", "Mexican"])
    prep_time = st.select_slider("Prep Time", ["15 min", "30 min", "45 min", "60 min"])
    veg = st.toggle("Vegetarian Mode")

# --- Main UI Layout ---
tab1, tab2, tab3 = st.tabs(["📖 View Recipe", "🛒 Grocery List", "💾 Export"])

with tab1:
    # Top Metrics Bar
    m1, m2, m3 = st.columns(3)
    m1.metric("Prep Time", prep_time)
    m2.metric("Difficulty", "Medium")
    m3.metric("Calories", "450 kcal")
    
    st.divider()
    
    # Recipe Content in a "Card"
    st.markdown(MOCK_RECIPE)

with tab2:
    st.subheader("Smart Shopping List")
    st.write("Check items you already have in your pantry:")
    
    # Logic to extract list items and turn them into checkboxes
    lines = MOCK_RECIPE.split('\n')
    for line in lines:
        if line.strip().startswith("-"):
            item = line.replace("-", "").strip()
            st.checkbox(item, key=item)

with tab3:
    st.subheader("Save & Share")
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.info("Download this recipe as a high-quality PDF for offline cooking.")
        pdf_bytes = create_pdf(MOCK_RECIPE)
        st.download_button(
            label="📥 Download PDF",
            data=pdf_bytes,
            file_name="recipe.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    
    with col_right:
        st.warning("Print-friendly version also available.")
        if st.button("Print Version", use_container_width=True):
            st.toast("Sending to printer...")