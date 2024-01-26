from semanticscholar import SemanticScholar
import pandas as pd
import numpy as np
import datetime
import logging
import time
import ast
import json

def raw_empty_dataset():
    column_names = [
        "paperId",
        "corpusId",
        "url",
        "title",
        "venue",
        "publicationVenue",
        "year",
        "authors",
        "externalIds",
        "abstract",
        "referenceCount",
        "citationCount",
        "influentialCitationCount",
        "isOpenAccess",
        "openAccessPdf",
        "fieldsOfStudy",
        "s2FieldsOfStudy",
        "publicationTypes",
        "publicationDate",
        "journal",
        "citationStyles",
        "embedding",
        "tldr",
        "citations",
        "references",
        "domain",
        "subtopic",
        "date_retrieval"
    ]

    data_types = [
        str,            # paperId
        int,            # corpusId
        str,            # url
        str,            # title
        str,            # venue
        str,            # publicationVenue
        int,            # year
        str,           # authors
        str,           # externalIds
        str,            # abstract
        int,            # referenceCount
        int,            # citationCount
        int,            # influentialCitationCount
        bool,           # isOpenAccess
        str,            # openAccessPdf
        str,           # fieldsOfStudy
        str,           # s2FieldsOfStudy
        str,           # publicationTypes
        str,            # publicationDate
        str,            # journal
        str,           # citationStyles
        str,            # embedding
        str,            # tldr
        str,           # citations
        str,            # references
        str,            # domain
        str,             # subtopic
        str             # date of data retrieval
    ]
    # Initialize an empty DataFrame with specified columns
    raw_df = pd.DataFrame(columns=column_names)
    # Create a dictionary that maps column names to data types
    column_data_types = dict(zip(column_names, data_types))
    # Set data types for the columns
    raw_df = raw_df.astype(column_data_types)
    print(raw_df)


def get_papers(research_topics):
    raw_df = raw_empty_dataset()
    sch = SemanticScholar(timeout=36000)
    max_runtime = 7 * 60 * 60
    start_time = time.time()
    for domain in research_topics:
      for subtopic in research_topics[domain]:
        Iterator = 0
        logging.info("Info log")
        print("Getting Results")
        try:
          results = sch.search_paper(subtopic, year=2015-2020, fields_of_study=[domain], fields=["paperId","corpusId","url","title","venue","publicationVenue","year","authors","externalIds","abstract","referenceCount","citationCount","influentialCitationCount","isOpenAccess","openAccessPdf","fieldsOfStudy","s2FieldsOfStudy","publicationTypes","publicationDate","journal","citationStyles","embedding","tldr","authors","citations","references"], limit=10)
          print("Progress of subtopic: "+subtopic)
          for result in results:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time > max_runtime:
              print("Maximum runtime exceeded. Stopping the script.")
              return raw_df
            if(Iterator == 2000):
              break
            try:
              paper_info = {
                'paperId': str(result.paperId),
                'corpusId': str(dict(result)["corpusId"]),
                'url': str(result.url),
                'title': str(result.title),
                'venue': str(result.venue),
                'publicationVenue': str(dict(result)["publicationVenue"]),
                'year': int(result.year) if(result.year) else None,
                'authors': str(result.authors),
                'externalIds': str(result.externalIds),
                'abstract': str(result.abstract),
                "referenceCount": str(result.referenceCount),
                "citationCount": str(result.citationCount),
                "influentialCitationCount": str(result.influentialCitationCount),
                'isOpenAccess': bool(result.isOpenAccess),
                "openAccessPdf": str(dict(result)["openAccessPdf"]),
                "fieldsOfStudy": str(result.fieldsOfStudy),
                "s2FieldsOfStudy": str(result.s2FieldsOfStudy),
                "publicationTypes": str(result.publicationTypes),
                "publicationDate": str(result.publicationDate),
                'journal':str(result.journal),
                "citationStyles":dict(result)["citationStyles"],
                "embedding":str(result.embedding),
                "tldr":str(result.tldr),
                "citations":str(result.citations),
                "references":str(result.references),
                'domain': domain,
                'subtopic': subtopic,
                'date_retrieval': datetime.datetime.now()
              }
              raw_df = pd.concat([raw_df, pd.DataFrame([paper_info])], ignore_index=True)
              Iterator += 1
              print(" "+str(Iterator)+" ")
            except Exception as re:
              print("Record level error: "+str(re))
        except Exception as pe:
          print("Pagination error: "+str(pe))
    return raw_df


def filter_raw(source_file_path, destination_file_path):
    df = pd.read_csv(source_file_path)
    df.replace('None', np.nan, inplace=True)
    print("Original shape: ",df.shape)
    print("Distribution of Null Values BEFORE Filtering: \n",df.isna().sum())
    df = df.dropna(subset=['authors','title','abstract'])
    df['publicationDate'] = pd.to_datetime(df['publicationDate'], errors='coerce')
    filter_condition = df['publicationDate'] < '2021-09-01'
    df = df[filter_condition]
    df = df[df['isOpenAccess'] == True]
    print("Modified shape: ",df.shape)
    print("Distribution of Null Values AFTER Filtering: \n",df.isna().sum())
    df.to_csv(destination_file_path, index=False)

def extract_key_values(dictionary, key):
    try:
        parsed_dict = json.loads(dictionary.replace("'", "\""))
        if key in parsed_dict:
            return parsed_dict[key]
        else:
            return None
    except (json.JSONDecodeError, AttributeError):
        return None

def extract_doi(value):
    try:
        dictionary = ast.literal_eval(value)
        return dictionary.get('DOI', None)
    except (ValueError, SyntaxError, TypeError):
        return None

def extract_url(dictionary_str):
    try:
        dictionary = eval(dictionary_str)
        return dictionary.get('url', None)
    except (SyntaxError, TypeError):
        return None

def extract_unique_categories(field_str):
    field_dict = ast.literal_eval(field_str)
    categories = [category['category'] for category in field_dict]
    unique_categories = list(set(categories))
    return str(unique_categories)

def extract_unique_bibtexid(bibtex_string):
    start_index = bibtex_string.find('@Article{') + len('@Article{')
    end_index = bibtex_string.find(',', start_index)
    unique_id = bibtex_string[start_index:end_index]
    return unique_id

def extract_and_store_author_names(row):
    author_list = ast.literal_eval(row['authors'])
    author_names = [author['name'] for author in author_list]
    return ', '.join(author_names)

def transform(source_file_path, destination_file_path):
  # Removing irrelavant columns
  df = pd.read_csv(source_file_path)
  df = df.drop(columns=['paperId', 'corpusId', 'url', 'venue', 'year'])
  df['venue_name'] = df['publicationVenue'].apply(lambda x: extract_key_values(x, 'name'))
  df['venue_type'] = df['publicationVenue'].apply(lambda x: extract_key_values(x, 'type'))
  df['venue_issn'] = df['publicationVenue'].apply(lambda x: extract_key_values(x, 'issn'))
  df['venue_url'] = df['publicationVenue'].apply(lambda x: extract_key_values(x, 'url'))
  df['DOI'] = df['externalIds'].apply(extract_doi)
  df['url'] = df['openAccessPdf'].apply(extract_url)
  df['FieldsOfStudy'] = df['s2FieldsOfStudy'].apply(extract_unique_categories)
  df['bibtex_id'] = df['citationStyles'].apply(extract_unique_bibtexid)
  df['author_names'] = df.apply(extract_and_store_author_names, axis=1)
  df = df.drop(columns=['publicationVenue', 'externalIds', 'openAccessPdf', 's2FieldsOfStudy', 'fieldsOfStudy', 'isOpenAccess', 'citationStyles', 'embedding','citations','references','authors'])
  df.to_csv(destination_file_path, index=False)
