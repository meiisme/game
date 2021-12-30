#1A2B game
import random
import streamlit as st

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)
#st.write(answer)

answer=''

a_count=0 # initial A count
b_count=0 # initial B count

submit_button = st.button(label='確定')   
if submit_button:
    for i in range(4):
        answer+=str(items[i])
    st.session_state.answer=answer

number=st.sidebar.text_input('Enter the number: ')
#while(True):
    #number=st.text_input('Enter the number: ')
st.write(st.session_state.answer)
if not number.isdigit():  #cheak all input is digit
    pass
else:
    if number==st.session_state.answer:
        st.write('excellent you guess the correct number')
        #break
    for i in range(4):
        #st.session_state(st.session_state.answer)
        for j in range(4):
            if i==j and number[i]==st.session_state.answer[j]:
                a_count+=1
            elif number[i]==st.session_state.answer[j]:
                b_count+=1
            #    st.session_state(answer)
    st.write(a_count, 'A', b_count, 'B')
    a_count=0
    b_count=0
