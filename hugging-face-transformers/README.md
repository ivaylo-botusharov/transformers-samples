## Hugging Face Transformers Demos

Description: This is a Python Demo Project using [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) for Natural language processing (NLP).  

### Prerequisites

### 1. Install Python 3.10.11

You can install Python by opening Terminal and navigating to the Project scripts folder, then typing: ```sudo sh python-install.sh```  

Or you can download the Python official installer from: [Python 3.10.11 (Release Date: April 5, 2023)](https://www.python.org/downloads/release/python-31011/) and run it on your computer  

### 2. Install Poetry

You can install Poetry by running: ```sudo sh poetry-install.sh``` from the scripts folder within the Project.  

Then you can verify if Poetry is successfully installed by reopening the Terminal and typing: poetry --version  

--------------------------

### Project Setup

### 3. Create virtual environment (using Poetry)

Open terminal in Project folder and run: ```poetry env use /usr/local/bin/python3.10```

### 4. Select Python interpreter for the Project (Workspace)

Reopen project in VS Code

Go to: View - Command pallete (Command + Shift + P) - Python: Select interpreter - Select at workspace level - make sure the Python 3.10.11 (Poetry) interpreter is selected  

### 5. Install Python packages  

In terminal type:

```poetry lock```  
```poetry install```   

### 6. Start main.py

In Terminal navigate to the Project folder (where also the MakeFile is located) and start the project by typing: ```make run```.    

Several Hugging Face Transformers pipelines will be executed sequentially:

* sentiment-analysis
* named-entity recognition (NER)
* question answering
* summarization

The pretrained models are downloaded and locally cached at: '~/.cache/huggingface/hub'. This is the default directory given by the shell environment variable TRANSFORMERS_CACHE. On Windows, the default directory is given by 'C:\Users\%USERNAME%\.cache\huggingface\hub'.  

### 7. Start transformers_offline.py

Prerequisites:  

* Download the [files](https://drive.google.com/drive/folders/14pT_IRs4HCvfpjfitGE6dpRHjvIz0bZa?usp=sharing) folder from my Google Drive.  

* Move the files folder into ```hugging-face-transformers/src``` folder  

Open Terminal and execute the command: ```make run-offline```

--------------------------

## Debugging / Troubleshooting

### A. Uninstall Poetry
If you would like to uninstall Poetry for testing / debugging purposes, then in Terminal navigate to the scripts folder and type: ```sudo sh poetry-remove.sh```.  

### B. Uninstall all Python versions
(excluding the default one)  

You can uninstall all Python versions from your Mac (excluding the one used by MacOS) by opening Terminal and navigating to the Project's scripts folder, then typing: ```sudo sh python-remove.sh```. On the Password prompt, please type your Mac user account (login) password.


--------------------------

In order to use the model and tokenizer offline, I went to the [model card](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) for "distilbert-base-uncased-finetuned-sst-2-english" - Files and Versions tab and manually downloaded the below files into folder ```hugging-face-transformers/src/files```  

* config.json file - contains the configuration of the model, such as the number of layers and the size of the hidden layer.  

* pytorch_model.bin - contains the weights of the model.  

* vocab.txt - contains the vocabulary of the tokenizer.  

Then in main.py I updated the model and tokenizer references from:

```Python
sentiment_classifier: Pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english", revision="3d65bad")
```
to:

```Python
distilbert_folder_path: str = "src/files/distilbert-base-uncased-finetuned-sst-2-english-revision-3d65bad"
tokenizer = AutoTokenizer.from_pretrained(distilbert_folder_path)
model = AutoModelForSequenceClassification.from_pretrained(distilbert_folder_path)
sentiment_classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
```