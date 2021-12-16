import streamlit as st
import random
answer = random.sample(range(1, 10), 4)

a = b = n = 0     # 設定 a、b、n 三個變數，預設值 0
while a!=4:       # 使用 while 迴圈，直到 a 等於 4 才停止
  a = b = n = 0   # 每次重複時將 a、b、n 三個變數再次設定為 0
  user = st.text_input(label='輸入四個數字：')  # 讓使用者輸入數字，並透過 list 轉換成串列
  submit_button = st.button(label='確定')                 
if (user[n]) == answer[n]:    # 因為使用者輸入的是「字串」，透過 int 轉換成數字，和答案串列互相比較
      a += 1                         # 如果位置和內容都相同，就將 a 增加 1
else:
    if (i) in answer:           # 如果位置不同，但答案裡有包含使用者輸入的數字
        b += 1                       # 就將 b 增加 1
    n += 1                           # 因為輸入的每個數字都要判斷，將 n 增加 1
