import streamlit as st

st.set_page_config(page_title="NivaraHealth", layout="wide")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"]  {
font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"]{
display:none;
}

[data-testid="stToolbar"]{
display:none;
}

/* Main layout */
.main-container{
display:flex;
height:100vh;
width:100%;
}

/* LEFT PANEL */

.left-panel{
flex:1.4;
background:linear-gradient(135deg,#2F80ED,#27AE60);
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
color:white;
text-align:center;
}

.left-panel h1{
font-size:44px;
font-weight:700;
margin-top:20px;
}

.left-panel p{
font-size:20px;
opacity:0.9;
}

/* RIGHT PANEL */

.right-panel{
flex:1;
background:#F4F5F7;
display:flex;
justify-content:center;
align-items:center;
}

/* LOGIN CARD */

.login-card{
background:white;
width:420px;
padding:40px;
border-radius:18px;
box-shadow:0px 20px 45px rgba(0,0,0,0.12);
}

/* Logo */

.logo{
display:flex;
align-items:center;
gap:10px;
justify-content:center;
margin-bottom:20px;
}

.logo-box{
width:42px;
height:42px;
border-radius:10px;
background:linear-gradient(135deg,#2F80ED,#27AE60);
display:flex;
align-items:center;
justify-content:center;
color:white;
font-weight:700;
}

/* Headings */

.secure{
text-align:center;
margin-top:10px;
}

.secure h3{
margin:0;
font-weight:600;
}

.secure p{
font-size:14px;
color:#6B7280;
margin-top:4px;
}

/* Inputs */

input, select{
width:100%;
padding:12px;
border-radius:8px;
border:1px solid #E5E7EB;
margin-top:6px;
margin-bottom:16px;
font-size:14px;
}

/* Button */

.login-btn{
width:100%;
padding:12px;
background:linear-gradient(to right,#2F80ED,#27AE60);
border:none;
color:white;
font-weight:600;
border-radius:8px;
cursor:pointer;
}

/* Forgot password */

.row{
display:flex;
justify-content:space-between;
align-items:center;
font-size:14px;
margin-bottom:16px;
}

.row a{
color:#2F80ED;
text-decoration:none;
}

.row a:hover{
text-decoration:underline;
}

.bottom{
text-align:center;
margin-top:20px;
font-size:14px;
color:#6B7280;
}

.bottom span{
color:#27AE60;
font-weight:500;
cursor:pointer;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div class="main-container">

<div class="left-panel">

<img src="https://cdn-icons-png.flaticon.com/512/3774/3774299.png" width="120">

<h1>Welcome to NivaraHealth</h1>

<p>Smart Healthcare, Simplified Management</p>

</div>


<div class="right-panel">

<div class="login-card">

<div class="logo">
<div class="logo-box">+</div>
<div>
<strong>NivaraHealth</strong><br>
<span style="font-size:12px;color:#6B7280;">Healthcare Management</span>
</div>
</div>

<div class="secure">
<h3>Secure Login</h3>
<p>Access your healthcare dashboard</p>
</div>

<label>Email Address</label>
<input placeholder="doctor@nivarahealth.com">

<label>Password</label>
<input type="password" placeholder="Enter your password">

<label>Select Role</label>
<select>
<option>Choose your role</option>
<option>Administrator</option>
<option>Doctor</option>
<option>Staff</option>
<option>Patient</option>
</select>

<div class="row">
<label><input type="checkbox"> Remember me</label>
<a href="#">Forgot password?</a>
</div>

<button class="login-btn">Sign In Securely</button>

<div class="bottom">
<hr>
<p>New to NivaraHealth?</p>
<p>Don't have an account? <span>Request Access</span></p>
</div>

</div>
</div>

</div>

""", unsafe_allow_html=True)
