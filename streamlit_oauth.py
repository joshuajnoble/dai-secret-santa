import streamlit as st
import authlib

import json
from cryptography.fernet import Fernet
import base64

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Berkshire+Swash&display=swap');

    .berkshire-font {
        font-family: 'Berkshire Swash', cursive;
        font-size: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

encrypted_list = b'gAAAAABpIJl0Lyy_VrNkYuADRDER1L69pdwkDTp6cerj8k_fvESdhv9ik5VSeOlxBiBDBxXYVVbK8KroQyZLG7OZ5TjA5aqAuTSyAc193UAllmGRcHsJp6-o6vgObPISSgQdqJBXX5-WervgyyzgncxBl0ql6V9G9YZcqHz3lnMMT2diynxtLqJGmcO7kWo961fOoK0mkeDMww-Hdl-03uWW2PeItLvg4ojsy3NfiLt4yBofkA6YWpPk-7cUy9fieO-kuYNjsJn7rpVCxvFlXxKmIFOXs42xrZlTgk8jabr0F3FvyFiYO8eQqEYWpwFNPkzCZqNXgX2uq8SyVxIm9Y9TTgGtuMOJoBzpbjsLoucpfD07FrIxAGF9_ooyd17KmeRr0YWehVM3vR_Z55ldoW7UowwtzVp_Ylbcm_yo4T5nGD0UeS6Kho2WeLX_BduUXXKfq2gcmajhE-PERhUgsFuCKHBNUwuWdzxec2FoPw0EsQxJpernUwq_9_-FX3M7g4hrlbs2S96GVuONmCZrPlb5_lZPKArMK8d9dpVeA-qjBe9Egmj0YEl1dXXsz3QAMpGVUwgSHc-30nW1mCztxEERLtyW67t96nRVCPuauLCWJk6n3Tn_pGxzaytgD3jLjIshHN7gmDz6f7lSHutoS08o1fkVBxLAstd3YGN8vqusWksYzS4UYbYI7A1QAmyrQ8q9iqxeMCrfLVfbj8OHHJycjCmk15wxs_r8grNexUyIQmw6ZKcifl7MEt79XZfciFZESMJIznU8bUEpJQKAmYgXWhq4qnX1BWugVLxLqcaVGbB2uC86q7bQnKnUevVFa5Fj6L2cot3Xp5jCA0VYBPgs_579_1jXr4xNI9w-I4_ytVcBFwI2wNmV2UmIRchLlcOEoDtRG-IeupXsaoxhHe3uVFygOc7UrYHjxvBUzcRn8FQ5-z3T6-tzQfm2sp6B-FNrhQp3cb1Fcf2Z3XEVtDa-JXG7hUlDiyzP2sXf1fS2bWRehN25jojJkLMTKQ_4x9zCUb0g7LbNUS_Gl3VPkthQBEXKkCT2EXEvi77bvtKDodHuyxmTV2gRMZxkbmLQu2A5__6hAznih8hcv7_SCmB-ij9YpwBDgNt_jNoW-7l0ZsMyXHRyQzpJONOvMhjl3dcQ549W8mb5JdbKWZjbQBkOxnoEDX33riCS38uKapdAdeCgoXysk6JbOeh-nBdImzOyk7JgtxMo2-1HnOC2xUQb22wIrU2ZYvFRDBT5wixKp2Zf9G-Sa8osFdn7lcOcazoa6zX5JdI9Cis4j_kYXdAme1aI1gesOd0F2WpHENXJdi6vf5wXSMDwysim4N_hwHQmz2vrpsTFt322ns7x6KdFc0P6_n6Ax9i3eEt2Uv1MA33_3r2xe8LChGkLr3Jqgq25G3EzVnq3GBoOfI5_pkfg9MtGR_eP7qq3wNJsMBDKadp79G5bW2pQAh96Jy8NjvnWuul9ZZ5GJGAEUSfFx7LWAD84LiVkzyC8uTsu9YCVP2tgAYRPUe2IvoKeeTjlzVqgkXJ70DYzNqzS9fo7-oySHqrl7G6zkl0aOwsr6-G7PmAMajZziUDT8BT0xZR_fUnYul8idkpM_2yz2TGNWb8PfxHcOnBdJAbrjQbiH_wBcq5PEEmRphjHbCXEJkfGUqgpbgsT2sG93k_JABKSYGPVYkSU3_bw7IIMGkJMabxFc7lYgeLRHbm3iz9Uyt2LUKAYmdk9wv8AmVSEx1gMn5B_h2eS4CdRhrecb5Za990Qfxf5GaJ9cwb032XsAf0bCLmjup3dZgG5-gTSj5VuVpwpBkx93WVGXaoSTK5XU2F3_ZyjLxrlMXHOu_TgYH_KKmdfe9VQNJJxKYIGkqtZQ4pF5G5BO5Mj0c0B3AdYOAHsYJZHAPaUGixumGB_Qne17UIpJqNyvfkKyANBNDEFecZxXoUU-tyqaJyenowdGcjyHSJI82HFRIrsgXUNhhbGYodJV5cBeU0F7Pnm0S_J_b5uUw9VKa2NEfseh028dXsuIo2uSWLeww4j5uPjJxymstl9dyyV9Wy3FTCkm5ocGn5b5HgK2OikN3kseIy0cRHe0tCrQWIm72ijBNzEGWUfkEdqY3DbnEackKgjmn1BvAIa0Eh6xp4Og4B9FGVC0QOCuoTItBxHXSAkYTIh4phF0ZsHI-gz72MBEbqKgKarpQ29zHLSxEiW_BIhNFJaWgJ5flWPDJ20SD4Kbl_zkC6d_n1ay1tiiiqeRkKRHJebAXSi77tSAwRPK5xU7krr6cXFR_uDLW6mt98NCPIVnC5u58fRzZo0Ze2aia45vQgUFuVmCTX_b_dO5dkA5ze7R3E8bdeDmLVWGIBlUiDmARomVhDekxt7rj-fmcuNlvLXkcvuZUuWfpJBAcn9nvMMVn7oxtpOmsIn_PNM-cfizkuMxlD1Sehgc6XDdnHLTZMN0CKuCnLDQr_eldhS6opRYx7NBb795hNJbnwJcV0jmRZL6tpH-Sw7nX43fWcFP7_6KRf-PZbX730n3zBFSwWHakLtGXJjpLu3OiJcLAqhqtjWy7AT02zwUWnhuFjrzCvtSL-SsYFdPZl8lTpP6E2P9KbIwhWYB5_VIOdeDe43WmfmCOh1hmblJNvAVLGSjsdaEtB2uDVUmtfmxRtngW6GTTh8A4ZCDNEUALfMvTy-q528NssHvpymZ3tB5A9i5R6N5-prwmjoaycPdTlKPHN1c9B5HjhGJYFfAX5lSartP8d86-dR6V-EA3ymRAofPVryUdD3h36z9RRmPIB9i53kgKryeKdZRKcM8ck_73HlBYBA1yMP4PHhiL7t03Lesi3dwoR2HcrpWG2F3dwIH3A4G8tny14OmhLQNK4Q1_RC0VxQdLy6KDZWwB2wT9kv32k0ZzVzeCTOf-dqKg=='

st.html("<h1 class='berkshire-font'>Secret Santa Book Swap</h1>")
st.image('images/background.jpg')

# Button for Google login
if not st.user.is_logged_in:
    if st.button("Log in with Google", type="primary", icon=":material/login:"):
        st.login()
else:
    
    fernet_key = st.secrets["fernet"].encode('utf-8')
    f = Fernet(fernet_key)

    decrypted_message = f.decrypt(encrypted_list)
    gifting_list = json.loads(decrypted_message)

    for pair in gifting_list:
        if(pair['sender'] == st.user.email):
            st.html(f"You're sending to: <p><span style='color: orange; font-weight: bold;'>{pair['reciever'][0]}</span></p>")
            st.html(f"Their mailing address is: <p><span style='color: orange; font-weight: bold;'>{pair['reciever'][1]}</span></p>")
            if(pair['reciever'][2] != ""):
                st.html(f"Their preferred bookseller is <p><span style='color: orange;'><a href='http://{pair['reciever'][2]}'>{pair['reciever'][2]}</a></span></p>")

    if st.button("Log out", type="secondary", icon=":material/logout:"):
        st.logout()