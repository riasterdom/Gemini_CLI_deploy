import streamlit as st
import random

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "Computer wins!"

st.title('Rock, Paper, Scissors')

st.write("Choose your weapon:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Rock'):
        user_choice = 'Rock'
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        st.write(f"You chose: {user_choice}")
        st.write(f"Computer chose: {computer_choice}")
        st.write(f"**{winner}**")

with col2:
    if st.button('Paper'):
        user_choice = 'Paper'
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        st.write(f"You chose: {user_choice}")
        st.write(f"Computer chose: {computer_choice}")
        st.write(f"**{winner}**")

with col3:
    if st.button('Scissors'):
        user_choice = 'Scissors'
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        st.write(f"You chose: {user_choice}")
        st.write(f"Computer chose: {computer_choice}")
        st.write(f"**{winner}**")
