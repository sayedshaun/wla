import streamlit as st
import base64

# Set the page title
st.set_page_config(page_title="Water Line Agency", layout="centered")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


hide_st_style = “”"

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

“”"
st.markdown(hide_st_style, unsafe_allow_html=True)


# Function to set a background image
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        encoded_image = base64.b64encode(data).decode()
    background_style = f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpeg;base64,{encoded_image}');
        background-size: cover;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Set the background image
set_background("assets/background.jpg")

# Add logos to the top of the page
# Add logos to the top of the page
def add_logos(logo_image):
    st.markdown(
        f"""
        <style>
        .center-logo {{
            display: block;
            margin-left: auto;
            margin-right: auto;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(f'<img src="data:image/jpeg;base64,{base64.b64encode(open(logo_image, "rb").read()).decode()}" alt="Logo" class="center-logo" width="200">', unsafe_allow_html=True)


# Add logos
add_logos("assets/logo.jpg")

# Main heading
title_alignment="""
<style>
#the-title {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)


# Create tabs
tabs = st.tabs(["Application", "Our Service", "About Company"])

# Tab 1: Application
with tabs[0]:
    st.header("Apply Now")
    st.write("Come to us for the best-in-class agency experience. Apply to us; we are a name you can trust!")
    
    # Add a form
    with st.form(key="application_form"):
        st.text_input("Name", placeholder="Enter your full name")
        st.text_input("Email", placeholder="Enter your email address")
        st.text_area("Message", placeholder="Write your message here")
        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            st.success("Your application has been submitted successfully!")

# Tab 2: Our Service
with tabs[1]:
    st.header("Our Service")
    st.write("WLA provides step-by-step guidance from application to enrolment to make dreams of higher study abroad a reality for genuine students. Book your FREE Consultation with us now to find out why more than five thousand students consider us the best education consultancy in Bangladesh. Our team of expert counselors is happy to assist you with the following services without ANY FEES when you apply to our partner universities.")
    st.markdown(
        """
        <div style="font-size:18px; color: #f8f8f2;"><b>Services Included:</b></div>
        <div style="border: 1px solid #44475a; padding: 10px; margin: 5px; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
            <b>Career Counseling</b>
        </div>
        <div style="border: 1px solid #44475a; padding: 10px; margin: 5px; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
            <b>Education Counseling</b>
        </div>
        <div style="border: 1px solid #44475a; padding: 10px; margin: 5px; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
            <b>University & Course Selection</b>
        </div>
        <div style="border: 1px solid #44475a; padding: 10px; margin: 5px; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
            <b>Application Placement</b>
        </div>
        <div style="border: 1px solid #44475a; padding: 10px; margin: 5px; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
            <b>Guidance on SOP/Personal Statement/Scholarship Essay Writing</b>
        </div>
        <div style="border: 1px solid #44475a; padding: 10px; margin: 5px; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
            <b>English Proficiency Tests</b>
        </div>
        <div style="border: 1px solid #44475a; padding: 10px; margin: 5px; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
            <b>Pre-Visa Assistance</b>
        </div>
        <div style="border: 1px solid #44475a; padding: 10px; margin: 5px; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
            <b>Expert Visa Services</b>
        </div>
        <div style="border: 1px solid #44475a; padding: 10px; margin: 5px; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
            <b>Travel Assistance</b>
        </div>
        """,
        unsafe_allow_html=True
    )



# Tab 3: About Company
with tabs[2]:
    st.header("About Company")
    st.write("Water Line Agency is a trusted student counseling firm; based in Dhaka, Bangladesh. It has been serving educational consultancy for Bangladeshi students for less than a years. Started the agency journey in the year 2024 and managed numerous students to study abroad at top-ranked global universities with the right set of scholarships and financial aid. Our success in the foreign admission process helped us achieve the Best Educational Consultant Award. Besides that, our Bangladesh government registration and well-acclaimed track record are evidence that we’re one of the best in finding and admitting students to the best universities. We are actively working with 300+ universities across the United Kingdom, China, the United States of America, Canada, Australia, New Zeland, Denmark, Malta, Malaysia, Dubai and other European and Asian countries. If you are one of the big dreamers who want to get higher degrees from abroad then you have come to the right place.")
    
    # Add top 3 images of CEO, CTO, and GM
    st.subheader("Our Leadership Team")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("assets/ceo.jpg", caption="CEO", use_container_width=True)
    with col2:
        st.image("assets/cto.jpg", caption="CTO", use_container_width=True)
    with col3:
        st.image("assets/gm.jpg", caption="GM", use_container_width=True)



def add_social_media():
    st.markdown(
        """
        <hr>
        <div style="text-align: center;">
            <a href="https://www.facebook.com" target="_blank">Facebook</a> |
            <a href="https://www.twitter.com" target="_blank">Twitter</a> |
            <a href="https://www.instagram.com" target="_blank">Instagram</a> |
            <a href="https://www.linkedin.com" target="_blank">LinkedIn</a>
        </div>
        <hr>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="text-align: center;">
            <p>&copy; 2024 Water Line Agency. All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Add social media section
add_social_media()
