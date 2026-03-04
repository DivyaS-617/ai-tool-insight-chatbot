
import streamlit as st
import json

# Load dataset
with open("tools.json", "r") as file:
    tools = json.load(file)

st.title("AI Tool Insight Chatbot")

user_input = st.text_input("Enter AI Tool Name:")

if user_input:
    tool_name = user_input.lower()
    
    if tool_name in tools:
        tool = tools[tool_name]
        
        st.subheader("Used For:")
        for item in tool["used_for"]:
            st.write("- " + item)
        
        st.subheader("Advantages:")
        for item in tool["advantages"]:
            st.write("- " + item)
        
        st.subheader("Disadvantages:")
        for item in tool["disadvantages"]:
            st.write("- " + item)
    
    else:
        st.error("Tool not found in database.")