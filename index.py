import streamlit as st
from firstpage import *
from opencv import *
st.set_page_config(page_title="YSU-农作物健康识别系统",layout="wide")


def main():
    menu = ["首页","登录","注册", "注销"]

    if 'count' not in st.session_state:
        st.session_state.count = 0
    choice = st.sidebar.selectbox("选项",menu)
    st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 250px;
        margin-left: -250px;
    }
     </style>
     """,
    unsafe_allow_html=True,)

    if choice =="首页":
        #st.subheader("YSU农作物健康识别系统")
        #st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')
        show();

       # c1, c2 = st.columns(2)
       # with c1:
       #     st.success("首页1")
       #     st.image("testimage.jpg")
       # with c2:
       #     st.success("首页2")
        #    st.image("testimage.jpg")
    elif choice =="登录":
        backimage = Image.open('glod.jpg')
        st.image(backimage, caption='Sunrise by the mountains',use_column_width = True)
        st.sidebar.subheader("登录区域")
        username = st.sidebar.text_input("用户名")
        password = st.sidebar.text_input("密码",type = "password")
        if st.sidebar.checkbox("开始登录"):
            dname1=str(main_loop())
            print("名称是",dname1)
                    #dname=main_loop()

      #              c1, c2 = st.columns(2)
       #             with c1:
        #                st.success()
         #               st.image()
          #          with c2:
           #             st.success()
            #            st.image()
    elif choice =="注册":
        #st.subheader("注册")
        backimage = Image.open('sunrise.jpg')
        st.image(backimage, caption='Sunrise by the mountains',use_column_width = True)
        new_user = st.sidebar.text_input("用户名")
        new_password = st.sidebar.text_input("密码",type = "password")
        new_password1 = st.sidebar.text_input("确认密码",type = "password")
        if st.sidebar.button("注册"):
            if(new_password==new_password1):
                st.info("注册成功。")
            else:
                st.sidebar.warning("两次密码不正确，请检查后重试。")
    elif choice =="注销":
        st.session_state.count = 0
        if st.session_state.count == 0:
            st.info("您已成功注销，如果需要，请选择左侧的登录按钮继续登录。")
if __name__=="__main__":
    main()