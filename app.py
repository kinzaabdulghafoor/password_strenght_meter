import re
import streamlit as st

# page styling
st.set_page_config(page_title="password strength meter by kinza" , page_icon="🔐", layout="centered")

#custom css
st.markdown("""
<style>
    .main {text.align: center;}
    .st.textinput {width: 60% !important; margin: auto; }
    .st.button button {width: 50%; background-colour #4CAF50; color: white; font.size: 18x; }
    .st.button button:hover { background-color: #45a049;}
</style>
""", unsafe_allow_html=True)


#page title and decription


st.title("🔐password strength meter")
st.write("Enter your password below to check its security level,🔍")


#function to check password strength

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1    # increased score by 1
    else:
        feedback.append("❌password should be **atleast 8 character long** . ")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌password should include **both upper(A-Z) and lower case(a-z) letters**. ")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌password should include **at least one number (0-9)**. ")


    #special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌include ** at least one special character (!@#$%^&*)**.")


    #display password strength results
    if score == 4:
        st.success("✅**strong password** your password is secure.")
    elif score == 3 :
        st.info("⚠️**moderate password **- consider improving security by adding more feature ")
    else:
        st.error("❌ **week password** - follow the suggestion below to strength it. ") 


    #feedback 
    if feedback:
        with st.expander("🔍**improve your password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔏")

#button working 
if st.button("check strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ please enter a password first!") # show warning if password empty   


