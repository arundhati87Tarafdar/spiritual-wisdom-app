import streamlit as st
from PIL import Image
import pandas as pd
from deep_translator import GoogleTranslator

# Set up page configuration
st.set_page_config(page_title="Spiritual Wisdom", page_icon="🕉️", layout="wide")

# Initialize session state for navigation if not set
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def set_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# Custom CSS to change background, font colors, button spacing, and remove sidebar
st.markdown(
    """
    <style>
    body {
        background-color: #003366; /* Dark blue */
        color: white; /* White font */
    }
    .stApp {
        background-color: #003366;
    }
    .stMarkdown, .stTextInput, .stButton, .stTable {
        color: white !important;
    }
    .stButton button {
        background-color: white !important;
        color: #003366 !important;
        border-radius: 10px;
        font-weight: bold;
        width: 100%; /* Make buttons evenly spaced */
    }
    h1, h2, h3, h4 {
        color: #FFD700 !important; /* Yellow */
    }
    [data-testid="stSidebar"] { 
        display: none; /* Hide sidebar */
    }
    .translated-text { color: #FFD700; font-family: cursive; font-size: 18px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Load images (replace with actual images)
def load_image(image_path):
    return Image.open(image_path)

# Top Navigation with Buttons
st.markdown("<h1 style='text-align: center;'>Spiritual Wisdom</h1>", unsafe_allow_html=True)

# Use evenly spaced columns for buttons
button_cols = st.columns(7)
with button_cols[0]:
    if st.button("Home"): set_page("Home")
with button_cols[1]:
    if st.button("About"): set_page("About")
with button_cols[2]:
    if st.button("Teachings"): set_page("Teachings")
with button_cols[3]:
    if st.button("AI & Spirituality"): set_page("AI & Spirituality")
with button_cols[4]:
    if st.button("Global Presence"): set_page("Global Presence")
with button_cols[5]:
    if st.button("Contact"): set_page("Contact")
with button_cols[6]:
    if st.button("Donations"): set_page("Donations")


# Page Selection
choice = st.session_state.page



# Homepage
if choice == "Home":
    st.image(load_image("OIP.jpg"), use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Welcome to the Spiritual Renaissance</h2>", unsafe_allow_html=True)
    st.subheader("मानव सब एक हैं। ऊर्जा ही शक्ति है, शक्ति ही ब्रह्म है।")
    st.write("Experience the timeless wisdom of Guruji, where spirituality meets technology. Join us in spreading divine knowledge across the globe.")
    st.button("Join the Spiritual Movement")

# About Page
elif choice == "About":
    st.markdown("<h2>About Guruji's Vision</h2>", unsafe_allow_html=True)
    st.write("Guruji envisions a world where wisdom transcends borders. Through AI-driven platforms, his teachings reach millions worldwide.")
    st.image(load_image("OIP.jpg"), caption="Guruji's Journey", use_container_width=True)

# Teachings & Philosophy Page
elif choice == "Teachings":
    st.markdown("<h2>Divine Teachings & Philosophy</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style='font-size:18px;'>
    "सुनु सुत कहौं साधन भल तुम्हार जगिह भागु, सकल सुमंगल मूल सब मोर चरण अनुरागु।"
    <br>
    "The company of saints is the root of joy, removing all suffering."
    </p>
    """, unsafe_allow_html=True)
    st.subheader("AI as the Voice of the Divine")
    st.write("AI can amplify divine messages, making spirituality accessible worldwide.")
    
    # Translation Feature
    st.subheader("Translate Spiritual Teachings")
    user_input = st.text_area("Enter text to translate:", "")
    LANGUAGES = {"French": "fr", "Spanish": "es", "German": "de", "Hindi": "hi", "Bengali": "bn", "Chinese": "zh-CN", "Japanese": "ja", "Russian": "ru", "Arabic": "ar", "Portuguese": "pt"}
    target_language_name = st.selectbox("Select target language:", list(LANGUAGES.keys()))
    target_language = LANGUAGES[target_language_name]
    
    if st.button("Translate"):
        if user_input.strip():
            translator = GoogleTranslator(source='auto', target=target_language)
            translated_text = translator.translate(user_input)
            st.markdown(f"<p class='translated-text'>Translated Text ({target_language_name}): {translated_text}</p>", unsafe_allow_html=True)
        else:
            st.warning("Please enter text to translate.")


# AI & Spirituality Page
elif choice == "AI & Spirituality":
    st.markdown("<h2 style='color: white;'>AI & Spirituality</h2>", unsafe_allow_html=True)
    st.write("Technology is a divine tool for spreading wisdom.")
    st.subheader("AI-powered Apps")
    df = pd.DataFrame({"App Type": ["Indian App", "Global App"], "Languages": ["10", "40"]})
    st.markdown(df.style.set_table_styles(
        [{'selector': 'td', 'props': [('color', 'white')]}]
    ).to_html(), unsafe_allow_html=True)
    #st.table(df)
    # Added OIP1.png image here
    st.image(load_image("OIP1.png"), width=300)

# Global Presence Page
elif choice == "Global Presence":
    st.markdown("<h2>Guruji’s Teachings Across the World</h2>", unsafe_allow_html=True)
    st.write("""
    Phase 1: France, Germany, UK → Key spiritual hubs.
    Phase 2: Greater Europe, USA, Eastern Asia.
    """)
    st.map()

# Contact Page
elif choice == "Contact":
    st.markdown("<h2>Contact Us</h2>", unsafe_allow_html=True)
    st.write("Fill out the form below to reach us.")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.button("Send Inquiry"):
        st.success("Your message has been sent!")

# Donations Page
elif choice == "Donations":
    st.markdown("<h2>Support the Movement</h2>", unsafe_allow_html=True)
    st.write("Your contributions help sustain this global spiritual movement.")
    st.button("Donate Now")

# Footer
st.markdown("<hr><p style='text-align: center;'>© 2025 Spiritual Wisdom | Powered by AI & Guruji’s Vision</p>", unsafe_allow_html=True)