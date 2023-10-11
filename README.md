# PrepBot - Interview Preparation Assistant <img src="https://cdn-icons-png.flaticon.com/512/3135/3135714.png" alt="Rule Based ChatBot For Retail" width="50" height="50">

  - [Features](#features)
  - [Getting Started](#getting-started)
  - [How to Use](#how-to-use)
  - [Customization](#customization)
  - [License](#license)
  - [Contributions](#contributions)
  - [Contact](#contact)
  - [Acknowledgments](#acknowledgments)

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

## Customization
You can customize by adding more intents to `intents.json` file. Feel free to adapt and extend the system to suit your specific use case.

## License 
This project is licensed under the MIT License - see the [License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
