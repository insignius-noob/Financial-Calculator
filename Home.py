import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(page_title='Financial Dashboard', layout='wide')

user_db = {
    'mutaal': {
        'name':"Abdul Mutaal Aashi",
        'password': "$2b$12$s3EdGLD/ExFt47JY1EmlIuaONGqSjN/iBnH/HQFA9ibN9bIMLTOk."
    }
}

option = st.sidebar.radio("Choose an option:", ["Login", "Sign Up"])

if option == "Sign Up":
    st.subheader('Create a New Account')
    new_name = st.text_input('Your full name')
    new_username = st.text_input('Choose a username')
    new_password = st.text_input('Choose a password', type='password')

    if st.button('Create Account'):
        if new_username in user_db:
            st.error('Username already exists')
        else:
            hashed_new_password = stauth.Hasher([new_password]).generate()[0]
            user_db[new_username] = {
                'name': new_name,
                'password': hashed_new_password
            }
            st.success('Account created successfully. Please switch to login')

if option == "Login":
    usernames = list(user_db.keys())
    names = [user_db[i]['name'] for i in usernames]
    hashed_passwords = [user_db[i]['password'] for i in usernames]

    credentials = {
        "usernames": {
            u: {
                "name": user_db[u]["name"],
                "password": user_db[u]["password"]
            } for u in usernames
        }
    }

    authenticator = stauth.Authenticate(
        credentials=credentials,
        cookie_name="finance_dashboard",
        key="mutaalrocks",
        cookie_expiry_days=1
    )

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status == False:
        st.error("Username or password is incorrect.")

    elif authentication_status == None:
        st.warning("Please enter your username and password.")

    elif authentication_status:
        authenticator.logout('Logout', 'sidebar')  
        st.title(f"💸 Welcome, {name}!")
        st.markdown("Use this tool to calculate your savings over time")

        st.markdown("### 👉 Choose a Calculator from the Sidebar:")
        st.write("- 📈 Annuity Calculator")
        st.write("- ♾️ Perpetuity Calculator")
        st.image("Home_Image.png", use_container_width=True)


