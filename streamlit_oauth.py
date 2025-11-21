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

encrypted_list = b'gAAAAABpIH0CwHAGT9_lw8KuvgaFz47GSIGyx66GmRr1nGflDTZUdsNqZCihCidJRLVXEpp1RiweNsMPub5mcxpzdVmaA0FZFpxjeiTQ56u8lXaEjds-uRZx6MgrWTzhWzdudDsrZTVhAmHqr8rhKKvj3e6FZ768VH7V2RrBWl2Ooh1quYOki7Yb-zp-4sUF51YmsKJpyY0jfby2tlHpLtLNqshL7-W-s85n1eoS5nE_kobvB1g4n75DS7yhXevfHTPbQcqQ8A61XHLcwjBqejER4mBHziVzuSGOdpdbO3wdRzbNnPX_yM8siJrp3WQTQdUX3qdECyAlEVhvfo_yEAc6VnrWk-GkGDSo25k3Gkae5jXnNxVDZlBLTFS6W3duvTNdmUC8fB-VOpcW331ewiebH3cNW1QeF49w5T8fL9WX5RDi45IRuJ93HZmIag7Q7QbgBWzP9a78WO75BYpay4BdoJgcORI_fjO-J5E7IpYK8ah4VHjmY2SybONJA_3Sgy_o5qxdcpjuyM-12-AJbFRHjlDiIeUY-V4q3NqfpAc8rwJ6uecZcA0p12mbM71-J30glo8byqGfIE9ZfRv5GcvQ52bN4Ht0hlAPlDYpwCno7vHV4ZBZr8wnqbpIsXVyiCaZA8FWZS7pX_EK7FrC4yxDPONM4aOju6JLjw72ulXjJ7u4MZ3MhRV2SkinBzI_gv0WW2BwtQLAHmpB8OPPp7Zr70pKYXiTCE4KVhJRvNov0mWwnTJ_dPhg78vyQrSrIwXYyEVg4q5VgLFgTxgOeG-DwT49i8uZsFid4aBmt_d_hNFBwFKoRPKKQDedrwKkFOIdZ5pnZZg4BJWMQwDt2pFSDaStRelc0IgOZPRmp9KnofOkjtO8G9jzYNaieKNHLcqavnQZe-X55Xhdyrv1QwDZ38xFT6kAroURCXKUr8CxEitKFV8Dl4naIOdoKX17RzNBuGd_qmBoGguGh8PtUPqBkq22vSz8A8z-0UPxu8ad3nE8cxkrGvelzLTUmpydoa1MtVZ41qLXc6_JwtE2sOYhOff4OkJeRgHObhxhJ7vOWlNEr6cLv01hWhHvL0PX4lV-xdNGb0LrPZdMNoKUJScAqvGndu11zYToe9LSf0PjTKFROwwAYILASzoJL3KuRU_sYaQEAzf3llcUiPdrjAzeXeuNKUPjhMsnGuxauTZBEcFkSpAg76BmjuDMDeC2ao9olHVYKrNLKQRbucY20lnBQNVsmPZFV9_rN5xzClELajFf9ed1aNOSoL9FJtW3aD11qkqMN8HW_Wuvkf3w5o6Tgphyb7eUv1YTNac9VedZOtStbDbkv4dk09iRoFtvl9JO-q8ezi5kfPRW1RIXJ_Mciq22lzOIuv4oO-1KeN6GzjzwAnWIkEggmgT_vNE19ezzn9E2FUoYGpvhezWM94-UDmOP8IQ1BfwE1ZbvHTs2ryvsngEOOEy9b_T7O2JGXWufXKcDbRrIwenvoXBeSCtGCsjzVHtfVA3N66Hp-0G53-jfWB6oI3_vkG0PgZoBmsinPgkZiIIbcbHoDwcaZC6AknJZ_LiSBD-PZ3ggGMH6OrANC1pGspBUZEbmOobwkABafYZaK8k76Skqtk-gP9qRG1kFGixJQTvnSPUDpfeMYfigPFuMZNsYKr3cb_gpaTxiUYdLHBn-Mn3nKZRnhZ5iK6NKCbWha2BlN1XNx0eVl-uB5eNBsvEVtGgfNQauxBau5OxpQqt8vSHMss7Vi_bz8_QdsemuSnOJn-k6w2tJhuMqvWabohDd4ngxN1EmJMPX0iunHB64m3T6_WwAcxTSOXchXYtofmKlzOmHWXTFwtz8qfYHhTy6d5vzy0hATurSs-Luo366iYRFfZycmBAN3r5dYvx_LDox2io5eeOruG0E6N0zUEpjuF6JfldL_Bzx8CRSMQ067hKCCvSBCY-pqOgpeJ4L7d7ytAdbvMqXejmJmaIbv1ZdjfJ2-6NaOOJ8VZB5IGMaQjL433VO1MDR1X0mrbSz0Fi_RdPBEVLzE9yYGpfcDzrbgqd2kaWpp1s7tySJlsPxKxZFSBEy-7C3YCwe1gWGy1JPFwqDadM463OFvKFvA5e7dylHpcey5YgU-_ZoRzopFFT-SQ561ltKBNBYwkQzTNyauUVszkR31dJxSa3vzydHAGboEWDXKU4kstpedGcTM_Qp-ojnCTM6Uy4UyAA1vYozYFb9SkunjzlWAuN68YLcXbp8qtqS89dmRELQ9lEuPYgR-xPFLdhl2N3ywCgUUAmBHnNy5353ZDWcdulaVYstrQsRgJ8tEgsJkFjD7f2AWkFvTktghZzSyETbn0Y7zodBbP9LeLSFb--zPHXfk02N8IxMsIBFgeE28fIdwJLcS70Xyn9gkNDpdg4mnf8ps40bMQpTYX5P5_S2Zk8_X4c0QN7h9N_7BMadVGdk-_2C34rDI9ncK8aERHZS7Pd-yv4lGiwlICdUUGPSP_rwv8O_eAJvsXz66siRvrJ9e8gbjD-kTgGoV-FXoHympl86PEaE5nLcvgXC12aO0eO0lDwOeVSq01jvvQGjdXYb458LaMAiyhhWmGow4ak6-C05A8rozd3kYBcOiwNgWVvQyLPLRL7x_NxfeG0pULzLwBKvYMpkAJFxcmZatQb3daFQnuY3Yt6n7cE2VoXt2zmGrV26cj3nhmYblI3s1Wfw2TEHBF4l0LbJKpdYDVAQ7FYREKEjF3-0WX4vG8MUVAxq3VgkvSqCXyz-plWJYHuGVlxeY_Y7gxT0htsuIOwe_F0XKa3RJYJn1gHRn4Mvp3gRY6F0WjTKDEaZSxrib-6IBbFZFCp7B-ycWvN4quI02eUjvjLzAN_lCHTDH28G3bEFhn6ypXYIpsc4vEbPm4cvaJfFfsuD6t6hKQmZAgpYQxbj-3aCf02QaUvLtJHlGqfeL_X-6XbWs2eZtQzW0F5fhIE4k2RNhiaPIUFEnrHVBEVr6WSMVuYPgZDxCVq_XTutSKz1mDC-8I38ZDEWm9Vu45Upf_-GpA6zpnEyqwEolY5U15vlvgh6ps-pGA5IhKFUXamtFJtRbKxIBmk8KdYVSlmP'

st.html("<h1 class='berkshire-font'>Secret Santa Book Swap</h1>")
st.image('background.jpg')

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