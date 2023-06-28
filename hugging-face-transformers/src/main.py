"""Hello Transformers!"""

from transformers import (
    pipeline,
    Pipeline
)


def perform_sentiment_analysis_online(text: str) -> Pipeline:
    """Takes text as input and returns the sentiment analysis result."""
    sentiment_classifier: Pipeline = pipeline(
        task="sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        revision="3d65bad")
    result: Pipeline = sentiment_classifier(text)
    return result


def perform_named_entity_recognition_online(text: str) -> Pipeline:
    """Takes text as input and returns the named entity recognition result of the online model."""
    ner_tagger = pipeline(
        task="ner",
        model="dbmdz/bert-large-cased-finetuned-conll03-english",
        revision="f2482bf",
        aggregation_strategy="simple")
    outputs = ner_tagger(text)
    return outputs


def perform_question_answering_online(question: str, context: str) -> Pipeline:
    """Takes question and context as input and returns the question answering result of the online model."""
    reader = pipeline("question-answering")
    outputs: Pipeline = reader(question=question, context=context)
    return outputs


def perform_question_answering_online_detailed(question: str, context: str) -> Pipeline:
    """Takes question and context as input and returns the question answering result of the online model."""
    reader = pipeline(
        task="question-answering",
        model="distilbert-base-cased-distilled-squad",
        revision="50ba811",
        framework="pt")
    outputs: Pipeline = reader(question=question, context=context)
    return outputs


def perform_summarization_online(text: str) -> str:
    """Takes text as input and returns the summarization result of the online model."""
    summarizer = pipeline("summarization")
    outputs: Pipeline = summarizer(text, max_length=45, min_length=20, clean_up_tokenization_spaces=True)
    return outputs[0]['summary_text']


def perform_summarization_online_detailed(text: str) -> Pipeline:
    """Takes text as input and returns the summarization result of the online model. More pipeline parameters are explicitly set."""
    summarizer = pipeline(
        task="summarization",
        model="sshleifer/distilbart-cnn-12-6",
        revision="a4f8f3e",
        framework="pt")
    outputs: Pipeline = summarizer(text, max_length=45, min_length=20, clean_up_tokenization_spaces=True)
    return outputs[0]['summary_text']


def perform_summarization_online_detailed_facebook_bart_large(text: str) -> Pipeline:
    """Takes text as input and returns the summarization result of the online model. More pipeline parameters are explicitly set."""
    summarizer = pipeline(
        task="summarization",
        model="facebook/bart-large-cnn",
        revision="3d22493",
        framework="pt")
    outputs: Pipeline = summarizer(text, max_length=45, min_length=20, clean_up_tokenization_spaces=True)
    return outputs[0]['summary_text']


sentiment_analysis_input: str = "You are so smart and beautiful"

sentiment_analysis_result_online: Pipeline = perform_sentiment_analysis_online(sentiment_analysis_input)

print(sentiment_analysis_result_online)

customer_product_review: str = """Dear Amazon, last week I ordered an Optimus Prime action figure
from your online store in Germany. Unfortunately, when I opened the package,
I discovered to my horror that I had been sent an action figure of Megatron 
instead! As a lifelong enemy of the Decepticons, I hope you can understand my
dilemma. To resolve the issue, I demand an exchange of Megatron for the
Optimus Prime figure I ordered. Enclosed are copies of my records concerning
this purchase. I expect to hear from you soon. Sincerely, Bumblebee."""

ner_result_online: Pipeline = perform_named_entity_recognition_online(customer_product_review)
print(ner_result_online)

user_question: str = "What does the customer want?"

question_answer_online: Pipeline = perform_question_answering_online(user_question, customer_product_review)
print(question_answer_online)

question_answer_online_detailed: Pipeline = perform_question_answering_online_detailed(user_question, customer_product_review)
print(question_answer_online_detailed)

summarized_text_online: str = perform_summarization_online(customer_product_review)
print(summarized_text_online)

summarized_text_online_detailed: str = perform_summarization_online_detailed(customer_product_review)
print(summarized_text_online_detailed)

summarized_text_online_detailed_facebook_bart_large: str = perform_summarization_online_detailed_facebook_bart_large(
    customer_product_review
)
print(summarized_text_online_detailed_facebook_bart_large)
