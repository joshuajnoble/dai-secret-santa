import streamlit as st
import authlib

st.title("Streamlit OAuth Playground")
if not st.user.is_logged_in:
    if st.button("Log in with Google", type="primary", icon=":material/login:"):
        st.login()
else:
    print(st.user)
    st.html(f"Hello, <span style='color: orange; font-weight: bold;'>{st.user.email}</span>!")
    if st.button("Log out", type="secondary", icon=":material/logout:"):
        st.logout()

st.caption(f"Streamlit version {st.__version__}")
st.caption(f"Authlib version {authlib.__version__}")