# RAG Evaluation

The RAG evaluation flow will evaluate the Q&A Retrieval Augmented Generation systems by leveraging the state-of-the-art Large Language Models (LLM) to measure the quality and safety of your responses. Utilizing GPT as the Language Model to assist with measurements aims to achieve a high agreement with human evaluations compared to traditional mathematical measurements.

## What you will learn

The Similarity evaluation flow allows you to assess and evaluate your model with the LLM-assisted Similarity metric.

  1. **ground_truth**: Only evaluate the similarity between the rag answer and the standard answer, determining whether they express the same meaning. Assign a score between 0 and 1, rounded to two decimal places, such as 0.75; the higher the similarity, the higher the score.

  2. **context_question_relevance**: Evaluate only the relevance between the question and the context, determining whether the content in the context can be used to answer the question. Assign a score between 0 and 1, rounded to two decimal places, such as 0.63; the higher the relevance, the higher the score.

  3. **answer_question_relevance**: Evaluate only the relevance between the question and the rag answer, determining whether the rag answer addresses the question. Assign a score between 0 and 1, rounded to two decimal places, such as 0.91; the higher the relevance, the higher the score.

Metrics are scored on a scale of 0 to 1, with 0 being the worst and 1 being the best.

## Prerequisites

- Connection: Azure OpenAI or OpenAI connection.
- Data input: Evaluating the Similarity metric requires you to provide data inputs including a question, a standard answer, a rag answer and the context. 

## Tools used in this flow
- LLM tool
- Python tool
