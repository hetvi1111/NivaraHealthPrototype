import streamlit as st
import re

st.set_page_config(page_title="NivaraHealth", layout="wide")

st.markdown("""
<style>

/* Remove top Streamlit header */
[data-testid="stHeader"]{
display:none;
}

/* Full page background */
[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#2F80ED,#27AE60);
}

/* LEFT SIDE */

.left-panel{
color:white;
padding-left:120px;
display:flex;
flex-direction:column;
justify-content:center;
height:100vh;
}

.left-panel h1{
font-size:46px;
font-weight:700;
margin-top:20px;
}

.left-panel p{
font-size:22px;
opacity:0.9;
}

/* RIGHT SIDE */

.right-panel{
background:white;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
}

/* LOGIN CONTENT */

.login-card{
width:420px;
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
margin-top:5px;
}

.forgot a{
color:#2F80ED;
text-decoration:none;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)


# Create layout
left, right = st.columns([1.2,1])


# LEFT PANEL
with left:

    st.markdown('<div class="left-panel">', unsafe_allow_html=True)

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3774/3774299.png",
        width=120
    )

    st.markdown("""
    <h1>Welcome to NivaraHealth</h1>
    <p>Smart Healthcare, Simplified Management</p>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)



# RIGHT PANEL
with right:

    st.markdown('<div class="right-panel">', unsafe_allow_html=True)

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    st.markdown("### Secure Login")
    st.caption("Access your healthcare dashboard")

    email = st.text_input("Email Address", placeholder="doctor@nivarahealth.com")

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    role = st.selectbox(
        "Select Role",
        ["Choose role","Administrator","Doctor","Staff","Patient"]
    )

    remember = st.checkbox("Remember me")

    st.markdown('<div class="forgot"><a href="#">Forgot password?</a></div>',
                unsafe_allow_html=True)

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

    st.markdown("---")
    st.markdown("New to NivaraHealth?")
    st.markdown("Don't have an account? **Request Access**")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
