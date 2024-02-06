# Fact or Fake Debunker

Get real-time debunking of fake or factual information using the Fake or Fact Debunker tool, which utilizes real-time document streaming and the RAG (Retrieval-Augmented Generation) framework using [Dropbox](https://dropbox.com/).

## Demo

See the tool in action:

https://github.com/harikris001/Fact-or-Fake-Debunker/assets/85405666/bba0b608-e681-45bd-8918-98c5e40ae099



The Fact or Fake Debunker empowers users to quickly verify the authenticity of information by leveraging real-time document streaming and the RAG model for accurate analysis.

The LLM App Pathway, An awesome package to handle real-time data streaming.

## How to run the tool

There are 2 ways to run the app:



### Run with Docker

1. Create `.env` file in the root directory of the project, copy and paste the below config. Replace the `OPENAI_API_TOKEN` configuration value with your key `{OPENAI_API_KEY}` and replace `DROPBOX_LOCAL_FOLDER_PATH` with a path where Dropbox folder is located `{REPLACE_WITH_DROPBOX_FOLDER_PATH}`. For example, if the current project folder is `DROPBOX-SEARCH-TOOL`, you navigate to the Dropbox path in the home directory: `../Dropbox/documents`. Other properties are optional to change and be default.

```bash
OPENAI_API_TOKEN={OPENAI_API_KEY}
EMBEDDER_LOCATOR=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
DROPBOX_LOCAL_FOLDER_PATH={REPLACE_WITH_DROPBOX_RELATIVE_PATH}
```

2. From the project root folder, open your terminal and run `docker compose up`.
3. Access the tool via localhost:8501 in your web browser upon successful installation.

### Run from the source

#### Prerequisites

1. Ensure [Python](https://www.python.org/downloads/) 3.10 or above is installed on your machine.
2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.
3. Create an [OpenAI](https://openai.com/) account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the [OpenAI website](https://openai.com/product) and navigating to the API Key management page.
4. Access to your Dropbox/OneDrive account.

Then, follow the easy steps to install and get started using the sample app.

#### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
git clone https://github.com/harikris001/fact-or-fake-debunker
```

Next,  navigate to the project folder:

```bash
cd fact-or-fake-debunker
```

#### Step 2: Set environment variables

Create `.env` file in the root directory of the project, copy and paste the below config, and replace the `{OPENAI_API_KEY}` configuration value with your key.

```bash
OPENAI_API_TOKEN={OPENAI_API_KEY}
HOST=0.0.0.0
PORT=8080
EMBEDDER_LOCATOR=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
DROPBOX_LOCAL_FOLDER_PATH="../../../mnt/c/Users/<username>/Dropbox/documents"
```

Replace DROPBOX_LOCAL_FOLDER_PATH with your local Dropbox folder path and optionally, you customize other values.

#### Step 3 (Optional): Create a new virtual environment

Create a new virtual environment in the same folder and activate that environment:

```bash
python -m venv pw-env && source pw-env/bin/activate
```

#### Step 4: Install the app dependencies

Install the required packages:

```bash
pip install --upgrade -r requirements.txt
```

#### Step 5: Run the Pathway API

You start the application by running `main.py`:

```bash
python main.py
```

#### Step 6: Run Streamlit UI

You can run the UI separately by running Streamlit app
`streamlit run ui.py` command. It connects to the Pathway's backend API automatically and you will see the UI frontend is running on your browser.


<hr>

Considering Giving me a star if u like my work. :)
