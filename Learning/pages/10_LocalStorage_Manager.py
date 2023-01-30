import streamlit as st


def setLocalStorage(storage_string):
    code = """
    <script>
        var localStorage_string = localStorage.getItem("Chemical-Cookie");
        console.log(localStorage_string)
    </script>
    """
    st.components.v1.html(html=code, height=0)