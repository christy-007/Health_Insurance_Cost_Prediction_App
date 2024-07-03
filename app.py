


import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:center;">Health Insurance Cost Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    model=joblib.load('model_joblib_gr')
    p1=st.slider('Enter your Age',16,100)
    s1=st.selectbox('Sex',('Male','Female'))

    if s1=='Male':
        p2=1
    else:
        p2=0

    p3=st.number_input("Enter Your BMI Value")
    p4=st.slider('Enter Number Of Children',0,4)
    s3=st.selectbox('Smoker',('Yes','No'))

    if s3=='Yes':
        p5=1
    else:
        p5=0



    s2=st.selectbox('Region',('southwest', 'southeast', 'northwest', 'northeast'))

    if s2=='southwest':
        p6=1
    elif s2=='southeast':
        p6=2
    elif s2=='northwest':
        p6=3
    elif s2=='northeast':
        p6=4
    else:
        print("invalid")

    if st.button('predict'):
        pred=model.predict([[p1,p2,p3,p4,p5,p6]])

        st.balloons()

        st.success('Your Insurance Cost is {}'.format(pred[0]))


if __name__ == '__main__':
    main()

