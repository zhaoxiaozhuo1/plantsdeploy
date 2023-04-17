import streamlit as st
import pymysql
from firstpage import *
from opencv import *
st.set_page_config(page_title="YSU-农作物健康识别系统",layout="wide")

con = pymysql.connect(host="10.51.105.79", user="root", password="zhaozhuo2001.", database="plants_disease", charset="utf8")

c = con.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')

def add_userdata(username, password):
    if c.execute('SELECT username FROM userstable WHERE username = %s',(username)):
        st.warning("用户名已存在，请更换一个新的用户名。")
    else:
        c.execute('INSERT INTO userstable(username,password) VALUES(%s,%s)',(username,password))
        con.commit()
        st.success("恭喜，您已成功注册。")
        st.info("请在左侧选择“登录”选项进行登录。")

def login_user(username,password):
    if c.execute('SELECT username FROM userstable WHERE username = %s',(username)):
        c.execute('SELECT * FROM userstable WHERE username = %s AND password = %s',(username,password))
        data=c.fetchall()
       # print("数据是",data)
        return data
    else:
        st.warning("用户名不存在，请先选择注册按钮完成注册。")

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data
def show_slove(dname1):
    c.execute('SELECT * FROM information WHERE dname= %s ',(dname1))
    data=c.fetchall()
    print("数据是",data)
    return data

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
            logged_user = login_user(username,password)
            if logged_user:
                st.session_state.count += 1

                if st.session_state.count >= 1:
                    st.sidebar.success("您已登录成功，您的用户名是 {}".format(username))
                    #st.title("成功登录后可以看到的内容")
                    st.balloons()
                    dname1=str(main_loop())
                    print("名称是",dname1)
                    #dname=main_loop()
                    slove_data=show_slove(dname1)
                    #print(type(slove_data))
                    #for row in slove_data:
                     #   print("ee12e")
                        #print("%d--%d" % (cloumn[0], cloumn[1]))
                    for i in slove_data:
                        #print(i)
                        dinfo=i[2]
                        dsolve=i[3]
                        st.success(dinfo)
                        st.success(dsolve)

      #              c1, c2 = st.columns(2)
       #             with c1:
        #                st.success()
         #               st.image()
          #          with c2:
           #             st.success()
            #            st.image()
                else:

                    st.sidebar.warning("用户名或者密码不正确，请检查后重试。")
    elif choice =="注册":
        #st.subheader("注册")
        backimage = Image.open('sunrise.jpg')
        st.image(backimage, caption='Sunrise by the mountains',use_column_width = True)
        new_user = st.sidebar.text_input("用户名")
        new_password = st.sidebar.text_input("密码",type = "password")
        new_password1 = st.sidebar.text_input("确认密码",type = "password")
        if st.sidebar.button("注册"):
            if(new_password==new_password1):
                create_usertable()
                add_userdata(new_user,new_password)
            else:
                st.sidebar.warning("两次密码不正确，请检查后重试。")
    elif choice =="注销":
        st.session_state.count = 0
        if st.session_state.count == 0:
            st.info("您已成功注销，如果需要，请选择左侧的登录按钮继续登录。")
if __name__=="__main__":
    main()
