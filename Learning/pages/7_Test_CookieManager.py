from components.CookieManager import CookieManager
import streamlit as st


cm = CookieManager()

all_cookie = cm.getAll()
st.write(all_cookie)

remove_starting = cm.delete("starting")
st.write(remove_starting)

set_test_cookie = cm.set("test-cookie", "ok")
st.write(set_test_cookie)

get_test_cookie = cm.get("  test-cookie")
st.write(get_test_cookie)

get_test_cookie1 = cm.get("  -cookie")
st.write(get_test_cookie1)

get_test_cookie2 = cm.get("  ")
st.write(get_test_cookie2)