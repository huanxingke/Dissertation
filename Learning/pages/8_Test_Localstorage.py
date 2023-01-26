import streamlit as st

from components.StreamlitLocalstorage import injectWebsocketCode, getOrCreateUID


with st.spinner("加载本地储存..."):
    # Main call to the api, returns a communication object
    conn = injectWebsocketCode(hostPort='linode.liquidco.in', uid=getOrCreateUID())

    st.write('setting into localStorage')
    ret = conn.setLocalStorageVal(key='k1', val='v1')
    st.write('ret: ' + ret)

    st.write('getting from localStorage')
    ret = conn.getLocalStorageVal(key='k1')
    st.write('ret: ' + ret)