import streamlit as st
import streamlit.components.v1 as components

# Set Streamlit page configuration (only once, at the top)
st.set_page_config(
    page_title="Birthday Invitation",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# HTML content as a string
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formal 50th Birthday Invitation</title>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Great+Vibes&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
  <!-- Font Awesome for map pin -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <style>
    body {
      margin: 0;
      background: #f6f6f6;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
      font-family: 'Lato', sans-serif;
    }
    .invitation {
      max-width: 650px;
      background: #fff;
      border: 2px solid #d4af37;
      border-radius: 10px;
      box-shadow: 0 0 25px rgba(0,0,0,0.08);
      text-align: center;
      padding: 60px 45px;
      color: #333;
    }
    .invitation h1 {
      font-family: 'Great Vibes', cursive;
      font-size: 3em;
      color: #111;
      margin-bottom: 5px;
    }
    .invitation h2 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 1.4em;
      font-weight: 500;
      margin-bottom: 35px;
      color: #555;
    }
    .badge {
      font-family: 'Cormorant Garamond', serif;
      font-size: 2.6em;
      font-weight: 600;
      color: #111;
      background: linear-gradient(to right, #d4af37, #f7e9b2);
      display: inline-block;
      padding: 16px 42px;
      border-radius: 50px;
      margin-bottom: 30px;
      letter-spacing: 1px;
    }
    .details {
      font-size: 1.05em;
      line-height: 1.9;
      margin: 25px 0;
      color: #444;
    }
    .details strong {
      font-family: 'Great Vibes', cursive;
      font-size: 1.6em;
      font-weight: normal;
      color: #111;
      display: block;
      margin-top: 5px;
    }
    .address {
      margin-top: 15px;
      font-size: 1.05em;
      color: #444;
    }
    .address a {
      color: #444;
      text-decoration: none;
      transition: 0.3s;
    }
    .address a:hover {
      color: #d4af37;
      text-decoration: underline;
    }
    .address i {
      color: #d4af37;
      margin-right: 6px;
    }
    .line {
      height: 2px;
      width: 80px;
      background: #d4af37;
      margin: 25px auto;
    }
    .rsvp {
      margin-top: 30px;
      display: inline-block;
      padding: 14px 40px;
      background: #d4af37;
      color: #111;
      font-weight: bold;
      border-radius: 6px;
      text-decoration: none;
      font-size: 1.1em;
      transition: 0.3s;
      letter-spacing: 0.5px;
      font-family: 'Cormorant Garamond', serif;
    }
    .rsvp:hover {
      background: #b89128;
      color: #fff;
    }
    .respond {
      margin-top: 15px;  /* spacing below RSVP */
      font-size: 1em;
      color: #444;
      font-family: 'Lato', sans-serif;
    }
    @media (max-width: 600px) {
      .invitation {
        padding: 35px 20px;
      }
      .invitation h1 {
        font-size: 2.4em;
      }
      .badge {
        font-size: 2em;
        padding: 12px 28px;
      }
    }
  </style>
</head>
<body>
  <div class="invitation">
    <h1>Shhh... It’s a Surprise</h1>
    <h2>You're invited with your family to celebrate</h2>
    
    <div class="badge">Raj Kollu's 50th Birthday</div>
    
    <div class="line"></div>
    <div class="details">
      <br> September 28, 2025 at Noon
    </div>

    <div class="address">
      <i class="fas fa-map-marker-alt"></i>
      <a href="https://www.google.com/maps/place/655+John+Fitch+Blvd,+South+Windsor,+CT+06074" target="_blank">
        655 John Fitch Blvd <br> South Windsor, CT 06074 <br><br>
      </a>
    </div>
    <div class="line"></div>
    <div class="message">Join us as we surprise Raj with laughter, love, and memories to last a lifetime.</div>
    
    <a href="https://docs.google.com/forms/d/1oTxv2tut3US9gsxCQbJtDHWnh5AoI-etlJ2WkLiwWQ4/viewform?edit_requested=true" 
       class="rsvp" target="_blank">
       RSVP
    </a>

    <div class="respond">by September 23th!!!</div>
  </div>
</body>
</html>
"""

# Render HTML inside Streamlit
components.html(html_code, height=900, scrolling=False)
