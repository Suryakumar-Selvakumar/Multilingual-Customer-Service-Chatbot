# Importing needed libs
import gradio as gr
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch
import langid  # Library for language detection
import re

# Load the model and tokenizer from the directory
model_dir = "models/final_mbart_model"
model = MBartForConditionalGeneration.from_pretrained(model_dir).to('cuda')  # Move model to GPU
tokenizer = MBart50TokenizerFast.from_pretrained(model_dir)

# Function to generate a response
def generate_response(input_text, max_length=256, num_beams=5, min_length=125):
    # Detect language of input text using langid
    detected_lang, _ = langid.classify(input_text)

    # Set language code for mBART
    language_code = {
        "en": "en_XX",
        "fr": "fr_XX",
        "es": "es_XX"
    }.get(detected_lang, "en_XX")  # Default to English if language is not recognized

    # Set the source language token
    tokenizer.src_lang = language_code

    model_inputs = tokenizer(input_text, return_tensors="pt", padding=True)
    model_inputs = {key: value.to('cuda') for key, value in model_inputs.items()} 

    # Generate response
    generated_tokens = model.generate(
        input_ids=model_inputs['input_ids'],
        attention_mask=model_inputs['attention_mask'],
        forced_bos_token_id=tokenizer.lang_code_to_id[language_code],
        eos_token_id=tokenizer.eos_token_id,
        min_length=min_length,
        max_length=max_length,
        num_beams=num_beams,
        no_repeat_ngram_size=2,
        early_stopping=True
    )

    # Decode the response
    response = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

    # Add line breaks before numbers followed by a dot
    response = re.sub(r'(?<!\d)(\b\d{1,2}\.\s)', r'\n\t\1', response)

    # Remove unnecessary asterisks
    response = re.sub(r'\*', '', response)
    return response

# Define a function for Gradio to handle input/output
conversation_history = []

def chatbot_interface(user_input):
    global conversation_history

    # Generate response
    response = generate_response(user_input)

    # Update conversation history with user input and chatbot response
    conversation_history.append((user_input, response))

    # Generate HTML for the formatted conversation
    conversation_display = ""
    for user, bot in conversation_history:
        conversation_display += f"""
        <div class="user-name">You</div>
        <div class="user-message">{user}</div>
        <div class="bot-name">Chatbot</div>
        <div class="bot-message">{bot}</div>
        """

    return conversation_display

def clear_chat():
    global conversation_history
    conversation_history = []
    return ""

# Create the Gradio interface
with gr.Blocks() as demo:
    # Add custom CSS
    demo.css = """
    .user-name {
        text-align: right;
        padding-right: 10px;
        font-style: italic;
        font-weight: 550;
    }
    .bot-name {
        text-align: left;
        padding-left: 10px;
        font-style: italic;
        font-weight: 550;
    }
    .user-message {
        background-color: #fde68a;  /* Soft yellow/orange for user */
        text-align: right;  /* Align user messages to the right */
        padding: 10px;
        margin: 5px;
        border-radius: 10px;
        max-width: max-content;
        margin-left: auto;
    }
    .bot-message {
        background-color: #e0f7fa;  /* Light blue for bot */
        text-align: left;  /* Align bot messages to the left */
        padding: 10px;
        margin: 5px;
        border-radius: 10px;
        max-width: 70%;
        margin-right: auto;
        white-space: pre-wrap; /* Maintain line breaks */
    }
    #chat-container {
        border: 1px solid #cccccc;
        min-height: 65vh;
        max-height: 65vh;
        overflow-y: scroll;
        padding: 15px;  /* Space inside chat window for neatness */
        background-color: #ffffff;  /* White background for chat window */
        margin-bottom: 15px;  /* Space between chat window and user input area */
        border-radius: 10px;
    }
    #user-input {
        width: 100%;
        padding: 10px;
    }
    .center-text {
        text-align: center;
    }
    #main-container {
        width: 50%;  
        margin: 0 auto;  /* Center the container horizontally */
    }
    #user-container {
        display: grid;
        grid-template-columns: 1fr 10rem
    }
    #btns {
        max-width: 10rem;
    }
    #submit-btn, #clear-btn {
        max-width: 10rem;
    }
    """

    # Main container to control the overall layout width
    with gr.Row(elem_id="main-container"):
        with gr.Column(scale=3):
            gr.Markdown("<div class='center-text'><h1>Multilingual Customer Service Chatbot - Suryakumar Selvakumar</h1></div>")
            gr.Markdown("<div class='center-text'>Interact with the multilingual chatbot in your preferred language (English, French, or Spanish).</div>")

            # Chat Window to see the user and chatbot conversation
            with gr.Column(elem_id="chat-container"):
                chatbot_output = gr.HTML(label="Chatbot Conversation")

            # Text-Box for user-input and Buttons for submitting or clearing the chat 
            with gr.Row(elem_id="user-container"):
                user_input = gr.Textbox(lines=1, placeholder="Enter your question here...", label="", elem_id="user-input")
                
                with gr.Column(elem_id="btns"):
                    submit_button = gr.Button("Submit", elem_id="submit-btn")
                    clear_button = gr.Button("Clear Chat", elem_id="clear-btn")

    # Logic for the buttons when clicked
    submit_button.click(fn=chatbot_interface, inputs=user_input, outputs=chatbot_output).then(lambda: "", inputs=None, outputs=user_input)
    clear_button.click(fn=clear_chat, inputs=None, outputs=chatbot_output)

# Launch the interface
demo.launch()
