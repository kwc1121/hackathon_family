import streamlit as st






def auth():
    st.title('로그인 / 회원가입')

    if 'auth_mode' not in st.session_state:
        st.session_state.auth_mode = 'login'

    if st.session_state.auth_mode == 'login':
        login_form()
    else:
        signup_form()

def login_form():
    st.header('로그인')
    username = st.text_input('아이디')
    password = st.text_input('비밀번호', type='password')

    

    if st.button('로그인'):
        if username in st.session_state.users and st.session_state.users[username]['password'] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f'{username}님 환영합니다! 메인 페이지로 이동합니다.')
            st.experimental_set_query_params(page="smalltalk")
            st.experimental_rerun()
        else:
            st.warning('아이디 또는 비밀번호가 일치하지 않습니다.')

    st.button('회원가입', on_click=switch_to_signup)
        
        

def signup_form():
    st.header('회원가입')
    name = st.text_input('이름')
    age = st.number_input('나이', min_value=0, max_value=120)
    username = st.text_input('아이디')
    password = st.text_input('비밀번호', type='password')
    password_confirm = st.text_input('비밀번호 확인', type='password')
    position = st.selectbox("관계를 선택해주세요",("아들","딸","엄마","아빠","할머니","할아버지"))

    if st.button('가입하기'):
        if username in st.session_state.users:
            st.warning('이미 존재하는 아이디입니다.')
        elif password != password_confirm:
            st.warning('비밀번호가 일치하지 않습니다.')
        else:
            st.session_state.users[username] = {'name': name, 'age': age, 'password': password}
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success('회원가입이 완료되었습니다. 메인 페이지로 이동합니다.')
            st.switch_page("pages/1smalltalk.py")

    # st.sidebar.button('로그인', on_click=switch_to_login)


def switch_to_signup():
    st.session_state.auth_mode = 'signup'

def switch_to_login():
    st.session_state.auth_mode = 'login'
