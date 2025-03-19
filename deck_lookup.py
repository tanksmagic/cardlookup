import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("ACAANv5.csv")
    df = df.applymap(lambda x: str(x).upper())  # Ensure case insensitivity
    return df

df = load_data()

# Function to fetch the deck value
def get_deck_value(card, position):
    row_index = df[df.iloc[:, 0] == card].index
    if not row_index.empty and str(position) in df.columns:
        return df.loc[row_index[0], str(position)]
    else:
        return "Card or position not found"

# Streamlit App UI
st.title("Card Position Lookup")

# User inputs
card_input = st.text_input("Enter Card (e.g., 4D):").strip().upper()
position_input = st.number_input("Enter Position (1-52):", min_value=1, max_value=52, step=1)

# Button to get the result
if st.button("Find Deck Value"):
    if card_input and position_input:
        result = get_deck_value(card_input, position_input)
        st.success(f"Deck value for **{card_input}** at position **{position_input}** is: **{result}**")
    else:
        st.warning("Please enter a valid card and position.")
