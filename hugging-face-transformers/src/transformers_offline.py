"""This module contains functions invoking offline transformer models."""

from transformers import (
    AutoTokenizer,
    AutoModelForQuestionAnswering,
    AutoModelForSequenceClassification,
    AutoModelForSeq2SeqLM,
    AutoModelForTokenClassification,
    pipeline,
    Pipeline
)


def perform_sentiment_analysis_offline(text: str) -> Pipeline:
    """Takes text as input and returns the sentiment analysis result."""
    # files downloaded from:
    # https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english/tree/3d65bad49c7ba6f71920504507a8927f4b9db6c0
    distilbert_folder_path: str = "src/files/distilbert-base-uncased-finetuned-sst-2-english-revision-3d65bad"
    tokenizer = AutoTokenizer.from_pretrained(distilbert_folder_path)
    model = AutoModelForSequenceClassification.from_pretrained(distilbert_folder_path)
    sentiment_classifier = pipeline(
        task="sentiment-analysis",
        model=model,
        tokenizer=tokenizer)
    result = sentiment_classifier(text)
    return result


def perform_named_entity_recognition_offline(text: str) -> Pipeline:
    """Takes text as input and returns the named entity recognition result of the offline model."""
    # files downloaded from:
    # https://huggingface.co/dbmdz/bert-large-cased-finetuned-conll03-english/tree/f2482bf01f5da0f0eb8e183ffd8cc3885aa90b14
    bert_folder_path: str = "src/files/dbmdz-bert-large-cased-finetuned-conll03-english-revision-f2482bf"
    tokenizer = AutoTokenizer.from_pretrained(bert_folder_path, return_offsets_mapping=True)
    model = AutoModelForTokenClassification.from_pretrained(bert_folder_path)
    ner_tagger = pipeline(
        task="ner",
        model=model,
        tokenizer=tokenizer,
        aggregation_strategy="simple")
    result = ner_tagger(text)
    return result


def perform_question_answering_offline(question: str, context: str) -> Pipeline:
    """Takes question and context as input and returns the question answering result of the offline model."""
    # files downloaded from:
    # https://huggingface.co/distilbert-base-cased-distilled-squad/tree/50ba811384f02cb99cdabe5cdc02f7ddc4f69e10
    model_folder_path: str = "src/files/distilbert-base-cased-distilled-squad-revision-50ba811"
    model = AutoModelForQuestionAnswering.from_pretrained(model_folder_path)
    tokenizer = AutoTokenizer.from_pretrained(model_folder_path)
    reader = pipeline(
        task="question-answering",
        model=model,
        tokenizer=tokenizer)
    outputs: Pipeline = reader(question=question, context=context)
    return outputs


def perform_summarization_offline(text: str) -> str:
    """Takes text as input and returns the summarization result of the sshleifer-distilbart-cnn-12-6 offline model."""
    # files downloaded from:
    # https://huggingface.co/sshleifer/distilbart-cnn-12-6/tree/a4f8f3ea906ed274767e9906dbaede7531d660ff
    model_folder_path: str = "src/files/sshleifer-distilbart-cnn-12-6-revision-a4f8f3e"
    tokenizer = AutoTokenizer.from_pretrained(model_folder_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_folder_path)
    summarizer = pipeline(
        task="summarization",
        model=model,
        tokenizer=tokenizer)
    outputs: Pipeline = summarizer(text, max_length=45, min_length=20, clean_up_tokenization_spaces=True)
    return outputs[0]['summary_text']


def perform_summarization_offine_detailed_facebook_bart_large(text: str) -> Pipeline:
    """Takes text as input and returns the summarization result of the facebook-bart-large-cnn offline model."""
    # files downloaded from:
    # https://huggingface.co/facebook/bart-large-cnn/tree/3d224934c6541b2b9147e023c2f6f6fe49bd27e1
    model_folder_path: str = "src/files/facebook-bart-large-cnn-revision-3d22493"
    tokenizer = AutoTokenizer.from_pretrained(model_folder_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_folder_path)
    summarizer = pipeline(
        task="summarization",
        model=model,
        tokenizer=tokenizer)
    outputs: Pipeline = summarizer(text, max_length=45, min_length=20, clean_up_tokenization_spaces=True)
    return outputs[0]['summary_text']


sentiment_analysis_input: str = "You are so smart and beautiful"

sentiment_analysis_result_offline: Pipeline = perform_sentiment_analysis_offline(sentiment_analysis_input)
print(sentiment_analysis_result_offline)

customer_product_review: str = """Dear Amazon, last week I ordered an Optimus Prime action figure
from your online store in Germany. Unfortunately, when I opened the package,
I discovered to my horror that I had been sent an action figure of Megatron 
instead! As a lifelong enemy of the Decepticons, I hope you can understand my
dilemma. To resolve the issue, I demand an exchange of Megatron for the
Optimus Prime figure I ordered. Enclosed are copies of my records concerning
this purchase. I expect to hear from you soon. Sincerely, Bumblebee."""

ner_result_offline: Pipeline = perform_named_entity_recognition_offline(customer_product_review)
print(ner_result_offline)

user_question: str = "What does the customer want?"

question_answer_offline: Pipeline = perform_question_answering_offline(user_question, customer_product_review)
print(question_answer_offline)

summarized_text_offline: str = perform_summarization_offline(customer_product_review)
print(summarized_text_offline)

summarized_text_offline_detailed_facebook_bart_large: Pipeline = perform_summarization_offine_detailed_facebook_bart_large(
    customer_product_review
)
print(summarized_text_offline_detailed_facebook_bart_large)
