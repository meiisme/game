import streamlit as st
import random
answer = random.sample(range(1, 10), 4)

a = b = n = 0     
while a!=4:       
  a = b = n = 0   
  user = st.number_input(label='輸入四個數字：') 
  submit_button = st.button(label='確定')                 
if (user[n]) == answer[n]:   
      a += 1                         
else:
    if (i) in answer:          
        b += 1                       
    n += 1                          
