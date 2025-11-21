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

encrypted_list = b'gAAAAABpIJYrmgRXlDN2HVS_lTk7IKy0jsmMWmzL8S9styDOXcClGTWp_Wl9196u1Fe6l8DTq0upO-84BN0YGKi79LjvCTTdH2w9SizhWtWZx7jffVsDuNpHVEAc9IIJ1i2d95ynbhD7oDkaW4xTQfE91p3zYLuKOPt3KHkUp1bkivv00r7Yan2tZySqisvdS8GEMof8syKD9NOKRf9C1haGjSNB3O-b7kuE72ADtQIMBH9IzzAOKXizdBLiMXv6ueNpJswC1I7HCW83udew78dUKa8RejJeJNiDHNJTac7v1_b3bIyXgz3uBrziaqShdMBSg3Y0uJ2vysSJVrjROzjP77U3DmWn1xk3ZCzkCZ_fhdex2sR1BMdtVqAXFCVk5pLpsVFLz0842gQ3uk_mkicWsBkluTrzBQwL3KMflYQgZC6oLSDtD8NKB1D-yODzbttB4-POylNSe8wWk4BRe9VtFTaKlcPEgVGIJHK_EnbZibOhzBSYUYxB8IvqLMVMeGXQSOgJvR88AARoBRCcf-jMiXRfnN_3RikxYjGAhk2dgT86cXsc7jwzNmOmVjYnKx3vuJktKMzElkNsiIJqVnNdPydwJmaY4_Ef9Q-f7KRmZeLHYwJA9PTO7V89lcxh5AFXCDcQL9SUP538QNa3jVhnghYsehp8AcDdU5r0b4BwSvWt7MhKPPHgFWdoxGdOUv1KH1axxP_WXolyZV6yLHdxtI1MwwpkRnfFaeLmue5nNlW2wBpo-tI9b-hOUn1Mu_vqcmQXCkLUas3Su2RqJT9owP9A85UX4iXqpsov_1b7-mHumkxtrR4EmbqQdDKup73aE0Uqa2X19JRS_KQagjMbP2DBmxe4aGbnizWEl8yVTNMPrvibLGdgbt5vevyuBeHqF5emdFbXSdjhz-WweCDK_wObYZYKkqQ-0bPdtgcaAhubWft3daL_nXAJ6Bx2Dny0x3LbOC3G-ebeSVKM94ZLRcGxq60A3Rujm79OBhDg-Ylapzor9aLeLcUnCEo_mjdJdAe_QkKeeJNOOZDCGZz0WsS7cKXsiHRLOA_gbz5rabrnOgUHw5o4mJpWa8dIPz9qv0k5_Z6Kst-EBwDOfJJJHy9BhCZKNcLEe447I8QU9uen-8Dp-xu7caDWdk7jYUaoNuNH2QFOrCS76BvYd2K9ukQ5T8O0anE-HftQGDJCDaQzc4BCiuJYnz7rVqR7cC4IFAL4SqfeEnKyw3IqD7E8myNlobmOjbo10wbB1ynt9GukNI5YfBZ3HBx_eraEv6bTr-y7Iwtg6kgcdHaeIlEKNQtjLy4ZLL5q_jbRkSkOq1fTf12hg0HRLrHwlntkLR1h4bJBaPpVofWr7mM1ZqepNlAKVJIYX8mHhmpPxY0DR3ZQCh5ZHX5t0pHT2RCgTMpt99zsarzx58oXv91eO631tt6MGRjF_LiqI5V6uFJs8maibBuA_nFc0xRkjciol9Ze4jM4Bb5McOerKRan93Wg96yVY2n7tfimZrTDhXL3fEKnecZtt59KwbdO-sbo-S8oyOwkww9vDhGSeUF888HCfnIiDkG_Cw13vRlcy-NdXREIYDCMHApUCRrbV1NpWc_fa82H_Dq4U2G0hENr95oBq9Az1pH0LfFd6GuSdhSC-9Ci5LAPqAwj7RB9SCdRfzLN99Xi-BVC-8hzkWXYI-YDzeV8tyMycIigMpreLUin-c_LCgnidwnoupZjSp3o7rN_fU-QhZ2JMOaSoaFAWsqPPDEAdsY6NJfYBUmSGlrZIhKlNwVCjW-ST5X6E4xjZ4219dz3cjDdf0S-2Agfva_HB04qmL_yuGnTsHZMR3qxzF6ilQ41Ujo3cfOPvs7ESZJsLGIVGsbKnyvC3FKYz6jmW0Wx8jnKfrnd-QR9dx9GzhXE913GiYkP1vkbP4IJQUX8pYfY0RIpFsyq3fyQSuJm3yAJXIgJuT_DPw3PGbu45eys-uF7XtTcUfl7rq5fmXNL5eNagqO8AWiquT91M26xhyA1M96tdrGhKBFn2GKqNiRhhWsYwhk79uwCT3OntV4zO0maqRDgztsTFbMfAkMEImZAylMwbtOq6g2g4SdDpEQDt4ELCpJy1a_JNZRe7LXggUtqH9DuNAplS7K9qFiiyiWAi40LkKj98HdEy_V7s-i1fJ5-wejCLU2CLCd06dXSaQ2e1vGd3vb57m0sFM21Ta-cadoY66X1HCG1IjzhU4dUI9vyhX0COX7c7yyAncX81TR1s37bRnbSnLjk5_CzQhoWKKYbQHWHnDdqIje4FX0aFIwDtPLhV61Zcu2Cwp1CjftWltdD2fYvRL9D_Dgx1E44GhoYVYy7Znn8GE9nOqrg2aj4FDp0MD8d10rgAdbppPcuyI3D8jmieMq3h18fLEcdpqxcLkFu19LDba5veNUpY1kJ7y-CEXxxb-AM5-Fe0f4etDhpB106rMdE6QrKZ1bpxjo9Wjt5P-psTwscoqlyWaFpjOJ3MBSAChBVmhAPVSMFM0YZANB6nNr_wXeShoaK4udIOGMO8j_ALradLHJybar5f_3l2LF9YC0HhD31PnIpgBNy7dujCdjsixE8r6hTMn2WxYZHmHZ9nuBze8uAayHhcNolOv9Li-ZFVJvwTvNkRgi3xWhkOzX3T7hpf_Itu9wGrsrQCALGPeCxpg_6Ch1apzPGdYRbH4WblJrE6TEoMFD3igAvY5n7mKDazOerCUR0ZxFQFXau6yV4nyWatnJYEgQcIGLNlbBer9Ylj8_-MvajZLByHbPOySp8UDr2yzGnPhKj1duEJrEYm5CAn-ITZcokF6gEWnN1x__8m_pD5CoLn8q4Ms2idZYLvbZF5H930twxggA0euhUGbZnu6TEDc-OvhHpaK6Sg2lOYql3N4vD5JCJuJFb-Rug_gL30i1IHCt5ps9n20UMAWwkkI0MbSK7LUfkdhBzKZ5vMBXlSpP8aX_N4WMqeeDWjrBp74j5OwH_Ccnzz_mnkC_kOlJ-gXKGgaDMDFpAhFOtDwvEHj0Fiu3Q9d8xb8XWOljj-39k05Y7jFRp4vREBK52GdKlO1qWORqthX735BEZzQuh2vGF3YU49xqElQLszslycUlOBoocwh6AQOalzxtY2zX4BV4='

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