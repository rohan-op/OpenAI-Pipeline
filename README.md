# OpenAI-Pipeline

OpenAI-Pipeline is a data pipeline designed to fetch publicly available research papers from various domains such as Biology, Computer Science, Physics, Geology, and more, using the Semantic Scholar API. By leveraging Semantic Scholar, the pipeline retrieves papers based on different subtopics specified for each domain. These papers are then preprocessed to remove redundant attributes and simplify complex nested JSON data structures.

## Overview

- **Data Retrieval**: OpenAI-Pipeline fetches research papers using subtopics as queries for different domains from the Semantic Scholar API.

- **Data Preprocessing**: The retrieved raw data undergoes preprocessing to remove redundant attributes and simplify complex nested JSON data structures for better analysis.

- **AI-Generated Summaries**: Using the titles of research papers from the clean dataset, the pipeline prompts ChatGPT 3.5 to generate summaries and metadata.

- **Credibility Assessment**: By comparing the AI-generated responses with the actual content, users can assess the credibility of the information provided by the large language model.

## Workflow

1. **Data Retrieval**: Fetch publicly available research papers using subtopics as queries for different domains from the Semantic Scholar API.

2. **Data Preprocessing**: Clean and preprocess the retrieved data to remove redundancy and simplify complex nested JSON structures.

3. **Prompt Generation**: Use the titles of research papers from the clean dataset to prompt ChatGPT 3.5 to generate summaries and metadata.

4. **Response Comparison**: Compare the AI-generated responses with the actual content to assess credibility and reliability.

## Usage

1. **Fetch Research Papers**: Use the Semantic Scholar API to fetch research papers based on specified subtopics for various domains.

2. **Preprocess Data**: Clean and preprocess the retrieved data to remove redundancy and simplify complex structures.

3. **Generate Prompts**: Utilize the titles of research papers to prompt ChatGPT 3.5 to generate summaries and metadata.

4. **Assess Credibility**: Compare the AI-generated responses with the actual content to determine credibility and reliability of the information.
