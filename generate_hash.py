import streamlit_authenticator as stauth


passwords = ['password123']
hashed_passwords = stauth.Hasher(passwords).generate()
print(hashed_passwords)
