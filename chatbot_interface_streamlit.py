import streamlit as st
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# Load the model and tokenizer from the directory
model_dir = "models/final_mbart_model"
model = MBartForConditionalGeneration.from_pretrained(model_dir).to('cuda')  # Move model to GPU
tokenizer = MBart50TokenizerFast.from_pretrained(model_dir)

# Function to generate a response
def generate_response(input_text, source_lang, target_lang, max_length=256, num_beams=5, min_length=125):
    # Set the source language token
    tokenizer.src_lang = source_lang
    
    # Tokenize and move the inputs to the GPU
    model_inputs = tokenizer(input_text, return_tensors="pt", padding=True)
    model_inputs = {key: value.to('cuda') for key, value in model_inputs.items()}  # Move all inputs to GPU
    
    # Ensure the model and its inputs/outputs are on the same device
    generated_tokens = model.generate(
        input_ids=model_inputs['input_ids'],
        attention_mask=model_inputs['attention_mask'],
        forced_bos_token_id=tokenizer.lang_code_to_id[target_lang],
        eos_token_id=tokenizer.eos_token_id,  # Add end-of-sequence token to stop generation early
        min_length=min_length,
        max_length=max_length,
        num_beams=num_beams,
        no_repeat_ngram_size=2,  # Adjust this to prevent unwanted repetition
        early_stopping=True
    )

    # Decode and return the response
    return tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

# Streamlit App
st.set_page_config(page_title="Multilingual Customer Support Chatbot", layout="wide")
st.title("Multilingual Customer Support Chatbot")

# Language Selection
st.sidebar.header("Language Selection")
language = st.sidebar.radio("Select Language:", ("English", "French", "Spanish"))

# Map selected language to MBART codes
language_codes = {
    "English": "en_XX",
    "French": "fr_XX",
    "Spanish": "es_XX"
}

# Session state to keep track of conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Main Chat Interface
user_input = st.text_input("Message:", placeholder="How can I help?", key="user_input")
if st.button("Send", key="send_button"):
    if user_input:
        # Add user input to the conversation
        st.session_state.conversation.append(("user", user_input))

        # Generate chatbot response
        lang_code = language_codes[language]
        response = generate_response(input_text=user_input, source_lang=lang_code, target_lang=lang_code)
        
        # Add chatbot response to the conversation
        st.session_state.conversation.append(("bot", response))
        
        # Clear the input box after submission
        st.experimental_rerun()  # Rerun the script to clear the user input

# Display the conversation in a more interactive, chat-like interface
for speaker, text in st.session_state.conversation:
    if speaker == "user":
        st.markdown(f"<div style='text-align: right; background-color: #dcf8c6; padding: 10px; border-radius: 10px; margin: 5px 0;'>{text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color: #f1f0f0; padding: 10px; border-radius: 10px; margin: 5px 0;'>{text}</div>", unsafe_allow_html=True)

# Additional Styling
st.markdown(
    """
    <style>
    .css-1aumxhk {padding: 2rem 1rem;}
    .stTextInput > div > div > input {
        font-size: 18px;
        padding: 10px;
    }
    .stButton button {
        font-size: 16px;
        padding: 8px 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
