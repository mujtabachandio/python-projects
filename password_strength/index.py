import streamlit as st
import re


st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded",
)
# Function to evaluate password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Use special characters (!@#$%^&* etc.) for a stronger password.")

    return strength, feedback

# Streamlit UI
st.title("🔒 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)

    # Strength Indicator
    st.subheader("Password Strength:")
    if strength == 5:
        st.success("🟢 Strong Password")
    elif strength >= 3:
        st.warning("🟡 Medium Password")
    else:
        st.error("🔴 Weak Password")

    # Display Feedback
    if feedback:
        st.subheader("Suggestions to Improve:")
        for tip in feedback:
            st.write(f"✅ {tip}")
