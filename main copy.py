import streamlit as st 
from PIL import Image
import pandas as pd

# Set up page configuration
st.set_page_config(page_title="Spiritual Wisdom", page_icon="🕉️", layout="wide")

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
    home_btn = st.button("Home")
with button_cols[1]:
    about_btn = st.button("About")
with button_cols[2]:
    teachings_btn = st.button("Teachings")
with button_cols[3]:
    ai_btn = st.button("AI & Spirituality")
with button_cols[4]:
    global_btn = st.button("Global Presence")
with button_cols[5]:
    contact_btn = st.button("Contact")
with button_cols[6]:
    donations_btn = st.button("Donations")

# Determine the selected page
if home_btn:
    choice = "Home"
elif about_btn:
    choice = "About"
elif teachings_btn:
    choice = "Teachings"
elif ai_btn:
    choice = "AI & Spirituality"
elif global_btn:
    choice = "Global Presence"
elif contact_btn:
    choice = "Contact"
elif donations_btn:
    choice = "Donations"
else:
    choice = "Home"  # Default to Home if no button is pressed

# Homepage
if choice == "Home":
    st.image(load_image("OIP.jpg"), use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Welcome to the Spiritual Renaissance</h2>", unsafe_allow_html=True)
    st.subheader("मानव सब एक हैं। ऊर्जा ही शक्ति है, शक्ति ही ब्रह्म है।")
    st.write("Experience the timeless wisdom of Guruji, where spirituality meets technology. Join us in spreading divine knowledge across the globe.")
    
    # Added OIP1.png image here to enhance aesthetics
    st.image(load_image("OIP1.png"), use_container_width=True)

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

# AI & Spirituality Page
elif choice == "AI & Spirituality":
    st.markdown("<h2>AI & Spirituality</h2>", unsafe_allow_html=True)
    st.write("Technology is a divine tool for spreading wisdom.")
    st.subheader("AI-powered Apps")
    df = pd.DataFrame({"App Type": ["Indian App", "Global App"], "Languages": ["10", "40"]})
    st.table(df)

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
