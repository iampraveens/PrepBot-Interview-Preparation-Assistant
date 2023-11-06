# PrepBot - Interview Preparation Assistant <img src="https://cdn-icons-png.flaticon.com/512/3135/3135714.png" alt="Rule Based ChatBot For Retail" width="50" height="50">

PrepBot is a conversational document retrieval system designed to assist with interview preparation. It utilizes a combination of data ingestion, text embeddings, large language models, and memory management to provide responses to user queries.

## Note: Download any one the `Model` from the link given below and add to your working directory [Model](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/tree/main)

  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Run App](#run-ai)
  - [How to Use](#how-to-use)
  - [License](#license)

## Features

- **Data Ingestion**: Ingests and processes documents from a specified directory, extracts text from PDF files, and splits them into manageable chunks.
- **Text Embeddings**: Generates text embeddings using Hugging Face models.
- **Large Language Model (LLM)**: Configures a powerful LLM for conversational responses.
- **Memory Management**: Manages conversation history using a conversation memory buffer.
- **Conversational Retrieval**: Provides conversational responses to user queries about interview preparation.

## Getting Started

To get started with this project, you'll need Python and a few libraries installed. Follow these steps:

```bash
git clone https://github.com/iampraveens/PrepBot-Interview-Preparation-Assistant.git
```

```bash
cd PrepBot-Interview-Preparation-Assistant
```
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Run App
```bash
streamlit run app.py
```

## How to Use

- Open the application in your web browser.
- Enter your questions in the chat input field.
- PrepBot will generate responses based on the documents and models it has been configured with.


## License 
This project is licensed under the MIT License - see the [License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
