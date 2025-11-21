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

encrypted_list = b'gAAAAABpIJpP9ZFgxrZRdKClowDRNPi8qc-Nz_qCMWVzaQ76vATwJzfP52J9ffIEUftZmUb04JH9mcYGuhv-qwD4rjORka8e-qcVleiBf02DEvhZq8JJCwr1hfrJJj7Fz2T9jN_meLglaLdqMgq8wo6y4n6U6bKYp5qABMKtR7vDEqkgh9lwS4WuxlDhmmVPan5HOYVeTykOSwa83Vmsbj0wc3Elmiees-RXBMAZiYBk_tJKCiANCCudUHsWKiIvhN0GsooqDD8WlykEWQvkD97eXhjAdDYpw_Ol0elzXvjVb5CMZhYX9CGpOL46BEP7B5g793JOfEBB3l3Oo5In5Lj7TXpQVLfxpitLsXzZiH_Kk0bE6YSJ-y4Tb-LL62brQMn1NXxFLEdkkO2Cxus8lO6kayhBgjDD28SxBPIKHqwDvMZjUxcnI7HSrfWK7l7WxwwegrK2It7vNvfcfs3xwGJhftUAuBpnpOXANIKFEAyYb8wG01YySHdE6OIsuTYRSDZoA-ZxhP8gWneRC360PzTRUg_UhVosxt0i4oob1EgITpz6P41aKJ7MPE9V4doMurfW5VTQe58hbYVqkuzjIFRClixtVs4XJ5Yb2hm6KRi6TKZZs_DE0bO2OXtlksmrW7arGgeH9_5Y0nq4YmqABNd7AHsnv9g5LUaHuCA65kjcISTGmS1Zh9EJ4_O-CxOqmx-R1kVpD1OwKe1PlTFfn1Wi8Zmra7cvOM3pQc44IySvMpP_l1hvRDCVbqQdqDZKxGQNqj_9zUrFcUY-KzfbTZpAivOkGPRNxN8orBQ6ODufW1YFU7tq6B1t77U1dNZHG8bdW_Kwc1W-BpsFr2QPaUh-t9n05nW23jVNdqk635F-voztISMQmRnNrKWpf0L0GMVQC9PnCTagpg5PC6JPAfioLabP6b0lEoXjzfQzu_8CxlrP-MGEHy6r490KrFcmoMM4nbzDChP5YnB5wQLNWNz1UloYjw5_iZyqjGWbx620ZljMC3guu-jWLTodj6DNk4mfUd8F-kJ55EVljfUq7Cy-yCP3xsyy5vmkRRUeR7wJwgbXREDdAW3rU71rBPMwU9TVB0yFmUdscVU-FtMFsAfmn1CI-yMCmvJbEDNz4svrWpZ5JeJFrFFGuq73zbO2d_lZVhOOs89xUA3n_qicXXz4oGgsd5y29icaA1l9w2wX-1SjeSM0wfJjPZzLZl3k1oYbiLkP8Z5N_O8320Pk-Mq8Uer8WjEa3x_eKayafO6i0VmbdATRypX7klmIIn1pMO0tE3xDHQvsXIJ_Ggj0wQGCQ10QDSw-Gj1KvYW4GoSoPSY0iwgHQV7A9Hlro8EI2vKF18D1YLk61BRvLr58jLIarhr9cbgq_jBF_J5jKW-yDflNVr5cGe_U43pIG5xdeq0kmpvqMbgcepd-lgLr0iE3rH0z6IDAbTPhz9PpKE2Slt1mjTvxPc53W-PvGrZnIMA7NYqAE3YWmxZrHdR-7inn7b-Sgoslo5nISuKFa1LsIIX9AfBcxft2sSsTkc72V678b0A7SeQm56aktuWmA8UlbrB1Lph9aDJ0rGem8FvkBOqvW995OBRwKA2IgFN8aURIDrKoc_5UiGSsq6o_kDoGMVV5zvTUWW_4kX36cbBkKnjhA38LkeVmEyrzTyzJZwroLkIJvlXMisZx3V908zobhd5Ve_ciWahKiib2Ub-J8irqUbULYPgZEij0c0tKssTxh_yGZOjS4-gyapcrpAiH5KERuaSuHairKhNV0kscncfXX7ZGbGPAPrNEUGlk-DEBWLj8J18IGA9U9cLcXSYZR9OuiSkdzsiUHTJ9gfZbPB0RtPANXpWrVjeEMU_sFXL7MNACADDrM_wmcEQu5z5Q2QalKPo9LsfBD81e6AU51HKS1A8WQKGD_kn3LjFCetv1p2mJrven4AH8F4SHIcMzizs418GDBaO44rVVD_GZ8JuPPe4KeNmcaTWPqAi_2jU1f0U359UHj2mA62GamqvRv6uDgBBcpE5JA9XshV5LmQ9UjX0hEQ7fw3MA3fxP4UP_pKUKu9luz8OIdAZU8n0DVU-cGgXhTQfZu4Eq_7gsF_FAvbfpKrvXtf1fVyka773K_2sq2myC9678wjIXJUmDHtiqVGY89wgk6TLB829taYZ25AB9mkXeoxiMa0RiULuNoMDij3cxhmXZsZW3SIMWSywHsNiPbK5071A_PSqE5mKfKljEfQduTuNhN4K70iRTbKvP6cIhVRWW20eqj3ovArgXnflI2PYqEvM5Z2s5QP0n6HqMELRMifSrS_gaFp46L9v3-hV4aR3O23VQhxnX5hyP-YwZM9u-tI-PlqHISLpCRJUrcZpbxgtVePQsjKelvZjOgi96Xzdb1hJy50YOi44lnURF5bsvyUGPUE0RrjmUZ7Ysw3L7pjKYHxQjF2Ff1-ydPYzvGbsLdBoqRM2lp7kle75W-ytYmhlfY70PViMEhCoHR4KFfFxFwHA1Ue6KR7Es8p8ZHTJBpm1vqZby5Hg-CqAFVMrPN_b7b9t5EFOmudBoAc---SxehphWCbqosWBNsxlCvtYVWZIFF8AdPP_91t5xikJHVN_gpEZ2JQ0lrNw3vifulXjAESCGqpw59xDdcEEDxRTtak2SG42kPM1SKVNmNEkIgdZLbzauEpoBImOhiyAxHBnmG15EXdqJgPR8yCY_oz1AKIGPgeQCIuBtJ85BmzzdSFGkrulJykZzRaEdj5yqzG8gmw5Y_9SqjbhZkd9UCpcLUsWGrupuPE961JpKuy3jU6wksbLxoV4ZOiJ5A3fjfS1qSGp7MTBy5W5YINxr6FDpc_N90AP6YZYbxzEs0YAHhSQSStPDiuTMO80P3tF5Uu_wyVSQYRlLAa2UBok73-kSLg17cmeQi-t45wrldQ=='
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