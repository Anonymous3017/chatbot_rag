import json
import requests
import markdown
import re
from flask import render_template, request,jsonify
import torch
import huggingface_hub
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import PromptTemplate
from llama_index.core import Settings
from app.config import Config

# Initialize HuggingFace Hub
huggingface_hub.login(token=Config.HF_HUB_TOKEN)

# Load documents
documents = SimpleDirectoryReader("data").load_data()

# System prompt for LLMS
system_prompt = Config.SYSTEM_PROMPT

query_wrapper_prompt = PromptTemplate("<|USER|>{query_str}<|ASSISTANT|>")

# LLMS settings
llm2 = HuggingFaceLLM(
    context_window=8192,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0, "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt="{query_str}",
    tokenizer_name=Config.MODEL_NAME,
    model_name=Config.MODEL_NAME,
    device_map="auto",
    tokenizer_kwargs={"max_length": 4096},
    model_kwargs={"torch_dtype": torch.bfloat16}
)

# Embedding model
embed_model = HuggingFaceEmbedding(model_name=Config.EMBED_MODEL_NAME, trust_remote_code=True)

# Set settings
Settings.llm = llm2
Settings.embed_model = embed_model
Settings.chunk_size = 1024

# Index documents
index = VectorStoreIndex.from_documents(documents)
retrieval = index.as_retriever()

# Chat memory buffer
memory = ChatMemoryBuffer.from_defaults(token_limit=20000)
chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=system_prompt,
    llm=llm2,
    verbose=False
)

def gen_response(question):
    response = chat_engine.chat(question)
    return str(response)

def clean_response(response):
    pattern = r'^\s*assistant\s*'
 
    # Use re.sub to replace the pattern with an empty string
    cleaned_response = re.sub(pattern, '', response)
    return cleaned_response

def load_suggestions_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        suggestions = json.load(file)
    return suggestions

predefined_suggestions = load_suggestions_from_json('suggestions.json')

def get_suggestions(input_text):
    return [suggestion for suggestion in predefined_suggestions if input_text.lower() in suggestion.lower()]

def send_email(email, category, query):
    subject = f'New query from {category} category'
    sender_name = "User"
    sender_email = email
    recipient_email = "bigsecxxv@gmail.com"
    body = f'New query from {category} category: {query}'

    payload = {
        "sender": {
            "name": sender_name,
            "email": sender_email
        },
        "to": [
            {
                "email": recipient_email
            }
        ],
        "subject": subject,
        "htmlContent": body
    }

    api_key = Config.SENDINBLUE_API_KEY
    api_url = "https://api.sendinblue.com/v3/smtp/email"

    response = requests.post(api_url, headers={"api-key": api_key}, json=payload)
    if response:
        scroll_to_contact = True if request.path.endswith('/sent') else False
        return render_template("chat.html", status="Successfully", scroll_to_contact=scroll_to_contact)
    else:
        scroll_to_contact = True if request.path.endswith('/sent') else False
        return render_template("chat.html", status="Successfully", scroll_to_contact=scroll_to_contact)

