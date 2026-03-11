import streamlit as st
import re

st.set_page_config(page_title="NivaraHealth", layout="wide")

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#2F80ED,#27AE60);
}

[data-testid="stHeader"]{
display:none;
}

/* LOGIN CARD */

.login-card{
background:white;
padding:40px;
border-radius:15px;
box-shadow:0 10px 30px rgba(0,0,0,0.2);
width:420px;
margin:auto;
}

/* BUTTON STYLE */

div[data-testid="stButton"] button{
width:100%;
background:linear-gradient(to right,#2F80ED,#27AE60);
color:white;
font-weight:600;
border:none;
border-radius:8px;
padding:10px;
}

/* FORGOT PASSWORD */

.forgot{
text-align:right;
font-size:14px;
}

.forgot a{
color:white;
text-decoration:none;
}

</style>
""", unsafe_allow_html=True)

left,right = st.columns([1.3,1])

# LEFT SIDE
with left:

    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=120)

    st.markdown(
        "<h1 style='color:white;'>Welcome to NivaraHealth</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:white;font-size:22px;'>Smart Healthcare, Simplified Management</p>",
        unsafe_allow_html=True
    )

# RIGHT SIDE
with right:

    st.markdown("<div class='login-card'>", unsafe_allow_html=True)

    st.markdown("### Secure Login")
    st.caption("Access your healthcare dashboard")

    email = st.text_input("Email Address", placeholder="doctor@nivarahealth.com")
    password = st.text_input("Password", type="password")

    role = st.selectbox(
        "Select Role",
        ["Choose role","Administrator","Doctor","Staff","Patient"]
    )

    remember = st.checkbox("Remember me")

    if st.button("Sign In Securely"):

        errors = []

        if not email:
            errors.append("Email required")

        elif not re.match(r"\S+@\S+\.\S+", email):
            errors.append("Invalid email")

        if not password:
            errors.append("Password required")

        elif len(password) < 8:
            errors.append("Password must be at least 8 characters")

        if role == "Choose role":
            errors.append("Please select role")

        if errors:
            for e in errors:
                st.error(e)
        else:
            st.success("Login successful")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='forgot'><a href='#'>Forgot password?</a></div>",
    unsafe_allow_html=True
)
