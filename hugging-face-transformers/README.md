## Hugging Face Transformers Samples

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

The pretrained models are downloaded and locally cached at: ```~/.cache/huggingface/hub``` (macOS, Linux). This is the default directory given by the shell environment variable TRANSFORMERS_CACHE. On Windows, the default directory is given by ```C:\Users\%USERNAME%\.cache\huggingface\hub```.  

### 7. Start transformers_offline.py

If you want to explicitly specify the path to the transformer model files and don't want the Transformers library to download and cache them automatically for you, then you can:

Option A:  

7.1. Download the [files](https://drive.google.com/drive/folders/14pT_IRs4HCvfpjfitGE6dpRHjvIz0bZa?usp=sharing) folder from my Google Drive.  

7.2. Move the 'files' folder into [src](src/) folder  

Option B:  

You can download each model corresponding files by yourself from Hugging Face Hub by looking below at the model details (revision used, commit URL, required files). Then put the files in Local folder with specific name (see: 'Local folder')

Open Terminal and execute the command: ```make run-offline```


-------------------------

## Models:


task: summarization  
model: facebook/bart-large-cnn  
revision: 3d22493  
commit URL: https://huggingface.co/facebook/bart-large-cnn/tree/3d224934c6541b2b9147e023c2f6f6fe49bd27e1  
my Google Drive URL: [facebook-bart-large-cnn-revision-3d22493](https://drive.google.com/drive/folders/1X-8OI3_7jCpuZsHjS7fMwvT12EsiU9Kt?usp=drive_link)  

Required files:  

config.json  
generation_config.json  
merges.txt  
pytorch_model.bin  
tokenizer.json  
vocab.json  

Local folder: hugging-face-transformers/src/files/facebook-bart-large-cnn-revision-3d22493  


*Note:* Keep in mind that the 'files' folder is excluded from tracking and is not in the GitHub repository due to large file sizes. 

--------------------------

## Example (Sentiment analysis)

### Model download and caching (by Hugging Face Transformers library)

```Python
sentiment_classifier: Pipeline = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    revision="3d65bad")
```

### Model files downloaded manually to a folder and folder path explicitly declared

```Python
distilbert_folder_path: str = "src/files/distilbert-base-uncased-finetuned-sst-2-english-revision-3d65bad"
tokenizer = AutoTokenizer.from_pretrained(distilbert_folder_path)
model = AutoModelForSequenceClassification.from_pretrained(distilbert_folder_path)
sentiment_classifier = pipeline(
    task="sentiment-analysis",
    model=model,
    tokenizer=tokenizer)
```

--------------------------

## Debugging / Troubleshooting

### A. Uninstall Poetry
If you would like to uninstall Poetry for testing / debugging purposes, then in Terminal navigate to the scripts folder and type: ```sudo sh poetry-remove.sh```.  

### B. Uninstall all Python versions
(excluding the default one)  

You can uninstall all Python versions from your Mac (excluding the one used by MacOS) by opening Terminal and navigating to the Project's scripts folder, then typing: ```sudo sh python-remove.sh```. On the Password prompt, please type your Mac user account (login) password.