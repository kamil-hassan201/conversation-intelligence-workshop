# Conversational Intelligence: Chat with Your Document

Welcome to the Conversational Intelligence project, where you can have interactive chats with your document!

## Prerequisites

-   Python version 3.8, 3.9, or 3.10

## Setup and Installation

1. Install the required libraries:

    ```bash
    pip install openai llama-index pypdf sentence_transformers streamlit
    ```

2. Open `engine.py` and on line 6, replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

3. To chat with a new document:

-   First, delete the `index_data` folder.
-   Upload your desired file into the `data` folder.
-   Run the app again.

### How to get an OpenAI API Key?

Anyone with a new account associated with a new number at [OpenAI](https://platform.openai.com/account/api-keys) will receive a $5 free credit. If you're unfamiliar with how to get an API key, watch this [tutorial video](https://youtu.be/lnQsO-2MwXM?si=bg8w5FKWNmffBMpH).

4. Once everything is set up, run the app using:

    ```
    streamlit run app.py
    ```
