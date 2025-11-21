import streamlit as st
import authlib

import json
from cryptography.fernet import Fernet

encrypted_list = b'gAAAAABpH7wNeiiiQED2snlzhf6jyH1JdY2tAWicJv6qrDtb7anEvVJNP8acvhvmZY7my-qB2iO8Zez1yOSSpyuEzjzUWJfFvXpiCkMyVeAY1dRR_c4cY240VFi41g0M5NXuLFfaov2tFLm5YCKAKKs30WxngRFU9aokO7rC4lB0E7ikeOMnnzh5vU-QxYO2off71LLtdF8LAxhML_EEclscRcEK8WUr3I-yw99HCGASPMYSEHSdJ_S8X--8YSoKap8jUy9vZQ_FmHSbbavHth4xjqRESz2i-rVcMGtaGVPtpjd-hMwoOVXohK6yhBAfZDvIQmgr0K-gwl3_zU2rr5ftJpbn1QTsA2Puyk8i9ay_4lkdfkx0XoqOryxrrmNaqNfKFNIMA_vG5NALPijcJh3saN7R13wyzbYzVfZ81dH03HZnPhy0Zrvf-AOOKlGxe3uIEeMleDBMlZv3LYm_LKdYiajDk70JharAFB3ojidUrPClMpTuuqbeJTh3QVEm_QD0IguwjSfsgbAFNKTFImxVeeOEZhAaSodbtZzKbf_r15vsfRdzc0J1dDlVGYRVdBMUy0W85pymYMiwz5y0WyWhWddmUKR4NKxmrmMU6_EoWSDSK-BieM_y5t-NeY6yZVdpyLhwlmSv07Fd1B84TYAPSNZPm0noHquLUKC17drVm25uoBN5Bin6Ga7-vG7QjqMkqjtwdmEEz6rX65mImrAUcOKObsCNqtydDBdds1srJzCN02hErArOSA1np5QfnBu9CzRpAMOCs_lg30SziwaMMxRQfU7jEAz_lulYKN_zjXHTZfD08Gs8lOwvf-S4Mp125gOGAxThzu9Ede2EmqkEL33q-Pj1nKXnHqQJpVk-mUNt3jyq_75udwH-WkUC1OClELDWs34nDRo_iCwHzmqkm0t2CNscuTezEzVsHHUdgnIBR7hLSWf54-rKmJlruP__7QXOtlwJf0n7RMcKMqjNgK_fPH0zmmahH5lR8JEMivbWLcRVTBM3jcbRjSEDMT748YxmQucJWHOFN0KYTBdsWeBxLT1K0vXVzo3bmSUL2nd-rbUulG4enPAPvE0X_9n3pnYU5z_ynUr_RlML3bi0B1VoNugLqzlZphbPdinWGGHCmYjM8ugdH7Vh1PE6fhtoHeGZTuS8_W4ofhTtQ_XhJPFu_LpYxNOpIRgjOB8Hstwne76zT6CWWL-33qK7bsRccIX9LugB7Ozc2UOcTPgwkmBza04K3OKOTmqQ-yqqYwGShyYlZ6flIJAb66xv1r2n4pxKjLMn0uk6Z3XpL18E3nPblCsrIBPAsq8Q0R38Bb1pg-e5WzNSPZbokhxN-mJJ9BkHAoTYlAvWxom4jHFFnYRujNSN7AiHHK0Wfxnpcz51lnrMDdy1Egrs8DVDRwRCLrbwIJrJM2y6_ZSQgjcCdN-aDttADnVNfMGvBVmgf9OhLy_7ZCNMsjD-1y0fKPv56OdbD7DM0GwhkdzXCHzQHJx_n5zHW3JCH4UAzMT2JhwgH7bwTbMtWOrsTJ8tFF3kigP0ThUdo-aCkWlrcyqM7IxBit3Y-824iR54rnLHlvopzFIFt-hZDfTpjxZLkf32FilfSPVkTt12inopKwZS5w8crG-DRhz4_J8J-LL-ge-6QRPLlHZ7zObcNlOzMM4sRuLWw4eiOgwLMOCI4bokMmrGYgi-CHq5KywOiHAArI8rhMWwcfucuawkohx1-sUdcH2JydqHHIKGsWkVAmCc89Gm6ZX9dXGtfjBl2VzZbfnTmB_7T9_iZu746FHQJwg5mZq7DDFW0RVsqgSpr-r-zMQr2zT7HlQBro_j1xva26kCQy6k_VFiAYq15aj7ENknYiuf02gX1ciiB9EQnBBaaSn18-8mo-VboCslO289eVOzpz9ll4f-3T0FjBgzpb-CahgMfAba8GZe98KCOBE9y9FqZxlwyF7Kf628ogo3Pnj5oQQmTyHizf-vdRLLdk3rf9238QtbuuJiU8RqPb-J8uWempxP1T3tl30vUd6h071dd0TwUn9wEP1Ry4caJoSMfYhYdkwGytggkFHaorkekFKR9abGdyaYDrvW0_C2ZZHOU_vm6KfrE-_zPWCNTJXe8k8GmVsUpUWFwD-LKf8JSPPTFheDXWV17sI11I59vVXZbT6NfDVn1pFSHryhxm3Nc2Ey9Q74Gh5NwK1eHrDBJIQGCu3-jx2GRPSiZLA920IXze_9q4Dx8JPBTdPuVKIso5gcq-udFVSCWYPhCf3AMFCCQZO4BhswIOwBl8cK0AgcHiR-ZT6N6JaetPN82gmseh-RmcFmaMXmVKIMTiS-2eekGsXD8cAN5KIVXmjyP499fy9ZAJH44tJi1x2rvBGvuiV6o7IJMFXwlx2s2-v9_jRoARVMuOGzqRHgzB-0_xV5Cwi9izrEJ3Uc2iv7I3U0hIG9OL53qFU1NpDTCFar4o9p2VBVB76vMN4QS5xt8SFZKwS-xDbfS5q-anyFCdea1vhN2fLKSvz2Psnmq4JD-VaE19kRoLDhQHl4QBjlOS2IO_Y8dEgN3Fyd71j_ZnwrMLa20kNqMThilJO7SzjS9K7PH25ODkPlTLUJXGM_fFtv_OceaM0I-uWnIW-0-lWmv4hYOoNF7Kgnmgln9ZiPEbuZO__374cYspQUoM65PE9vmvFBagqaO1MrV03qUPAFOvNBp_zq2WrfBcNA729mp8R7WZQktyr2qb-F7qRe7AHIfYURYbw6gFlXskKVTZyta-DU4fGa6ekTWHXTVz1wspWC5pQA2E28z2y2V7mR8ggl-9LVYm8iak-aaW90G8Xc3G_5UE-c5PfLy2JqnYr5RqAfrlto98b77cNcA44cEcK7WlTVUBlvf76VnU05q-KJKEZ3dHFolsK54H9IvjEK1Y_pFXmDtHLV4eEL1pYZ6rQtv0LkCfG1KCrcu9aAzBubvAxhGebiGMfDAWtPdagEN0P1jYQ4uqTUOFDS1UWpWiANjA2A75m82PsX7OJg84i4jV6hkeLZuHZNpZKbg67rTYQ47J6HkKWk2_zIDLd-vl0vo1st7sowmBzCz2nNfLFwupeDNZBH'

st.title("Streamlit OAuth Playground")
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
            st.html(f"You're giving to: <p><span style='color: orange; font-weight: bold;'>{pair['reciever'][0]}</span></p>")
            st.html(f"Their mailing address is {pair['reciever'][1]}</span></p>")
            if(pair['reciever'][2] != ""):
                st.html(f"Their preferred bookseller is {pair['reciever'][2]}</span></p>")

    if st.button("Log out", type="secondary", icon=":material/logout:"):
        st.logout()