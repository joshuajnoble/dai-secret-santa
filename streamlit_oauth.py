import streamlit as st
import authlib

import json
from cryptography.fernet import Fernet

encrypted_list = b'gAAAAABpH6rsr9XJnb7-BQyXjVNS7gO8WzR72sY8cjbKXCHeD6E4EZsndPTHbycXqse_NxSNCDGgMlyhu3fdJIxv-2pBfgKQzjwSbW69ZnAjvMij5cgJmi8bQAPHDeoGTZYrsLoKsVcLO9umeyh-5pMl5TF_IkIVt4JFPF_IocZFZhgm7fIzvTu8L3RZ-bnQKTZmiezub5i_e69PBANgRyGYVdyOsDdhZj-sMAlNPli217oUhSIU5GFoEB2D9PJf7Gd6Tww8dX-zN8y56Zbva4nHWiF41htESyJO7hMGC5lHKCc3eDfWCu5AaIh3vpW9dYE0BN964CZca1jqFp_T0qKPy-lweHoKzDroE_lpaLo_4fWuuUMjHsCDn6FImMUpoBT6cslhJINZGwPWC1zn9RTyiP7PnFRYrsuorJfEBh6S-dqffilEHzfofBAwrcuuq0qJFhxIahDawBY6t22VwFbKrhFU-hIEWkFor0psN9YEIJ0wjgvlu7dYUA8Zgy6dwQZfsGAV5se7cqmcsxbfHeqbX7csuegmd5Z4VeIAP0yCXxaOmn7-ZDH1IkScGWwQBIkHQOlioAKHjLXRMF0ZUug_fDyhFdowgpzkfw9yBin0YZyVyUvbEH3CnqWQZ_VKOwQgjecnyq_2_hr1yVqLo7i2JGVvZfSbRR-e9gfe6l8h9_smo6z4IkHvHpuAWqzu9239tZjAS2DRnLYj_Uq-PR-MwwyAmRwRv3uDymFcWulNZm-Rr6CFHiBe4JpCXj_Nbd-C9yx6ktTqzezTL_qQJcAMGYFPFJeIh3XKNTY_vupvmC8UOUA5DIQZ7yGO8ubI5tSLU43oQxDSzbeUsX_N7P_I9PDqgIW9WeJn5CLlpbyAufjcYxbk48WzzvZSPsgIDfJuSLRB5Px2lUGqEBtNRVGMwi-D5EH1b4ONMvp1KWdTkWKbZALIAxrggmwOO4uLqDMfP9nCFULNqpQff3MalTk0iOEl7Zse37f0Y0wox70rdu2vEBgEtDnKX0Ma-SJE9-moW2cVA_ZX8krbEI4QA2WApc26ZJVnpe9PV7QmNNT1Ch9V-SiKR_XqsHHGFV9_M3T7meZxUPNT7oebRaLgk9WfedSUnVfc4P4q7lhV8guGcOFALLESKeXiomkct9gSHwmSnfTrDyMS2Qhhm13g1RzdF2FkaKOmjKU2dRjiq2XHaqhJnB_kwfbL7J28kqqTicJt_8WNeAcbAEpxL5JoXJhmFEXdQcQtaFGJKm3uARUVIZzwpZ2asz2U6hwMu4kHvuuFQQdpwWgZ2MpYiSNX3OEzHD7kMo2gdoNt0nGjVgM_3ZgMvmKFZ2MzObFs0UUpK_du29NNhWkOv8mJ9iNSxXelocPXm5V-_bIquENgDBQyu4RtT18R3hQ91Yq5BrSsIWoETp5cjGWk1ozrdf70k4rZmGtFWh-S-23nF_OoJbLa_xemGLEgW0t_2uzAJ4GXm8qHFVNUbO5aT1ommIzDLJRGjdBHbn1lzezYTkMDH5xpmWqBRproGdg791QLI3xX9zU2CjOA5306wqwe8nBHkfrO3Nr5sy9h1FTpBNibq3qYbLCFUoojCpLtWmnS59syjRvK2nQxHR8Qn02IefGkYWXY4-P_SvX8YsseBmN_7Aqw0ONk6ei9n4jC2qvtXecoAIabMiKJuHwy6YMDpsPRtWXvSvXPe9evjp6XQLJJMovMLRktOWirLYhKUYD-U7rL6udEb-wMFakFosokD7Fi_CEfynDuq0N27EWFTeuGt1ndZgBsnPUgGxjGu5qroFyJW4tA6gRhmVy0G-eqPw2KHkiswm-_Mzk0pFgrE71F8DWElqg03Yc1hhIQRNC312Jv4f8T05qLf21KOb9wqSXVYmA-7wWG8oyGZ3arBLxPluRlMmy2y9X2dGkT11zRErh55Zpp-1fIeev-twoDtczVFjhKPJWwDt4TQWykbgZecPELia92YKWr1P9CKvP5D3KCO9hhbhRAAnIU2fTjfrA6jwVemnb8xfN3mPwIQZ99_E00MAgiwmfoe3xPV1P6Ryb_htmcpVqv8QSMULSbR94UaRwEVqDPJGpRxCZQd0lb5JxkcdlnHg3X_L1DS63Nsjy3EhY6YAf5O_p5BYRZFYtWhjb_qd_0lJCcVtSjcLHZOFvHh77gPTOQV535dF52sLy85gHs0r7XaornFYejFdfxpng2ZeJWDo3ps5W-3JJ1cNvKwvVDGlEeo1BF6IE38dit3PWj3ThsA6DG5nWh_-a4i7NTA-eQ-wHrxbhuSCgv1Wu0qUaafks_JjzXDJIN_1_dAoM8RBdEPbBfCf2DqY5zCNP9IHgHz6622UPeAZweefpYiOxZ6R2nFBLlhnJcldRbVU9UFW06tYBH9zVl6GDW12iBco1hsRjwA11tccJ9PKww7VFPC5IRf4ddJ_vzPuHwEW0bbKASZHjNKLp9jedxSEM7mxVGfz2MR02y1VDA4WIT5kZwTvDVQ-ymkmWPYholsj_6kq1MsYSIlVnRChDCGpxG4rph86FTA2sH1WKV6bIz_wzZ_Tz7uAkgW9EsdTrV26jRnQuLZpkDwKFn5hJ3UMu8c2vyGsd6X2siXf_ubnQdJJDUOKwBhGFNbIr17XCkvC76XNdcP6MKXXpJqPmJMkhfGOBs47Hq23AP5RXqJAdTWoAZn6iPNsoJP34r3BXt1q3I97n2BHdDyRzt9FK4n1PXQjrYf2K98JndRiFAVIMjoZ1LK51hsMMEQHC43QZ7rls7IExpICy49Nyn1zG4XzLPH9RS6MI4WUiO30cqdm1wiMsRt75LG_JXA3cBZwEG7di1NS_Cry7WPnfRiaz3aM09orVWGnPG7EwjoXtHQUhCYA_ntOSZLzGF88zecqHc-Uv9HsfkJoDk3wrHXr-CqYNNWxHzmbpJSM6p5iQw7FsAuh7kRArOrPcvWrNbRqdVShNFNirSjcg_Bv77n-Mn-B1IrzaCLyIN3JTmDM4TBNX312v8fqJIIKk8nFwydwVXQhVTv_xk5pcqMLqlg-4VPt9I-Be_AOgVqQ=='

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