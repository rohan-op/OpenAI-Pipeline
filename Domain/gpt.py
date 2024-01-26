from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
import pandas as pd
import json
import os
import time
def output_data(input,llm):
  output = llm(input.to_messages())
  out_string = output.content.replace("```json\n", "")
  out_string = out_string.replace("\n```", "")
  return json.loads(out_string)

def gpt_df_generator(df,key):
    #API key
    os.environ['OPENAI_API_KEY'] = key
    # Initializing llm
    llm = ChatOpenAI(temperature=0,model='gpt-3.5-turbo')
    template = """
    You are provided with a title of an open source research paper.
    TITLE: {title}
    Your task is to provide information about this research paper based on the intructions provide below.
    {format_instructions}
    Wrap your final output with closed and open brackets (a list of json objects)
    """
    # Input Schema
    response_schema = [
                  ResponseSchema(name='abstract_gpt', description='The abstract of the research paper'),
                  ResponseSchema(name='tldr_gpt', description='The summary of the research paper'),
              ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schema)
    prompt_abstract_tldr = ChatPromptTemplate(
        messages = [
            HumanMessagePromptTemplate.from_template(template)
        ],
        input_variables = ["title"],
        partial_variables = {'format_instructions' : output_parser.get_format_instructions()}
    )
    response_schema = [
                  ResponseSchema(name='venue_name_gpt', description='Specify the name of the publication venue for the provided research paper title'),
                  ResponseSchema(name='venue_type_gpt', description='Specify the type of the publication for the provided research paper title'),
                  ResponseSchema(name='venue_issn_gpt', description='Specify the International Standard Serial Number(issn) of the publication for the provided research paper title'),
                  ResponseSchema(name='venue_url_gpt', description='Specify the URL to the publication for the provided research paper title'),
              ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schema)
    prompt_venue = ChatPromptTemplate(
        messages = [
            HumanMessagePromptTemplate.from_template(template)
        ],
        input_variables = ["title"],
        partial_variables = {'format_instructions' : output_parser.get_format_instructions()}
    )
    response_schema = [
                  ResponseSchema(name='domain_gpt', description='Domains are as follows: [Biology, Chemistry, CompSci, Engineering, EnvironmentalScience, Geology, MaterialsScience, Mathematics, Physics, Psychology]. Specify the best suited domain for the provided research paper title.'),
                  ResponseSchema(name='subtopic_gpt', description='Considering the domain, specify the subtopic related to the povided research paper title'),
                  ResponseSchema(name='FieldsOfStudy_gpt', description='Specify a list of field of studies related to the research paper'),
              ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schema)
    prompt_fieldOfStudy = ChatPromptTemplate(
        messages = [
            HumanMessagePromptTemplate.from_template(template)
        ],
        input_variables = ["title"],
        partial_variables = {'format_instructions' : output_parser.get_format_instructions()}
    )
    response_schema = [
                  ResponseSchema(name='referenceCount_gpt', description='Specify the total count of papers referenced by the provided research paper title'),
                  ResponseSchema(name='citationCount_gpt', description='Specify the citation count of the provided research paper title'),
                  ResponseSchema(name='influentialCitationCount_gpt', description='Specify the influential count of the provided research paper title. Influential citations means citations where the cited publication has a significant impact on the citing publication')
              ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schema)
    prompt_count = ChatPromptTemplate(
        messages = [
            HumanMessagePromptTemplate.from_template(template)
        ],
        input_variables = ["title"],
        partial_variables = {'format_instructions' : output_parser.get_format_instructions()}
    )
    response_schema = [
                  ResponseSchema(name='publicationDate_gpt', description='Specify the publication date for the provided research paper title, date format: yyyy-mm-dd'),
                  ResponseSchema(name='journal_gpt', description='Specify the name of the journal for the provided research paper title'),
                  ResponseSchema(name='DOI_gpt', description='Specify the DOI for the provided research paper title'),
                  ResponseSchema(name='url_gpt', description='Specify the PDF URL for the provided research paper title'),
              ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schema)
    prompt_details = ChatPromptTemplate(
        messages = [
            HumanMessagePromptTemplate.from_template(template)
        ],
        input_variables = ["title"],
        partial_variables = {'format_instructions' : output_parser.get_format_instructions()}
    )
    response_schema = [
                  ResponseSchema(name='authors_gpt', description='Mention all the authors of the provided research paper, mention all the authors you know. Name format: first name initals followed by last name'),
                  ResponseSchema(name='citation_key_gpt', description='The citation key(unique identifier for this reference) from bibtex of the provided research paper title'),
              ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schema)
    prompt_authors_citekey = ChatPromptTemplate(
        messages = [
            HumanMessagePromptTemplate.from_template(template)
        ],
        input_variables = ["title"],
        partial_variables = {'format_instructions' : output_parser.get_format_instructions()}
    )
    # gpt df generation
    columns = [
    'title',
    'abstract_gpt',
    'publicationDate_gpt',
    'journal_gpt',
    'tldr_gpt',
    'domain_gpt',
    'subtopic_gpt',
    'venue_name_gpt',
    'venue_type_gpt',
    'venue_issn_gpt',
    'venue_url_gpt',
    'DOI_gpt',
    'url_gpt',
    'FieldsOfStudy_gpt',
    'citation_key_gpt',
    'authors_gpt',
    'referenceCount_gpt',
    'citationCount_gpt',
    'influentialCitationCount_gpt'
    ]
    # Create an empty DataFrame with the specified columns
    gpt_df = pd.DataFrame(columns=columns)
    #df = pd.read_csv(source_file_path)
    df = df['title']
    for index,row in enumerate(df):
        print(row)
        gpt_df.loc[index, 'title'] = row
        try:
          input = prompt_abstract_tldr.format_prompt(title=row)
          output = output_data(input,llm)
          gpt_df.loc[index, 'abstract_gpt'] = output[0]['abstract_gpt']
          gpt_df.loc[index, 'tldr_gpt'] = output[0]['tldr_gpt']
        except Exception as e:
          print(f"Abstracts catch {index}: {e}")
        try:
          input = prompt_venue.format_prompt(title=row)
          output = output_data(input,llm)
          gpt_df.loc[index, 'venue_name_gpt'] = output[0]['venue_name_gpt']
          gpt_df.loc[index, 'venue_type_gpt'] = output[0]['venue_type_gpt']
          gpt_df.loc[index, 'venue_issn_gpt'] = output[0]['venue_issn_gpt']
          gpt_df.loc[index, 'venue_url_gpt'] = output[0]['venue_url_gpt']
        except Exception as e:
          print(f"Venues catch {index}: {e}")
        time.sleep(30)
        try:
          input = prompt_fieldOfStudy.format_prompt(title=row)
          output = output_data(input,llm)
          gpt_df.loc[index, 'domain_gpt'] = output[0]['domain_gpt']
          gpt_df.loc[index, 'subtopic_gpt'] = output[0]['subtopic_gpt']
          gpt_df.loc[index, 'FieldsOfStudy_gpt'] = output[0]['FieldsOfStudy_gpt']
        except Exception as e:
          print(f"Fields catch {index}: {e}")
        try:
          input = prompt_count.format_prompt(title=row)
          output = output_data(input,llm)
          gpt_df.loc[index, 'referenceCount_gpt'] = output[0]['referenceCount_gpt']
          gpt_df.loc[index, 'citationCount_gpt'] = output[0]['citationCount_gpt']
          gpt_df.loc[index, 'influentialCitationCount_gpt'] = output[0]['influentialCitationCount_gpt']
        except Exception as e:
          print(f"Counts catch {index}: {e}")
        time.sleep(30)
        try:
          input = prompt_details.format_prompt(title=row)
          output = output_data(input,llm)
          gpt_df.loc[index, 'publicationDate_gpt'] = output[0]['publicationDate_gpt']
          gpt_df.loc[index, 'journal_gpt'] = output[0]['journal_gpt']
          gpt_df.loc[index, 'DOI_gpt'] = output[0]['DOI_gpt']
          gpt_df.loc[index, 'url_gpt'] = output[0]['url_gpt']
        except Exception as e:
          print(f"Details catch {index}: {e}")
        try:
          input = prompt_authors_citekey.format_prompt(title=row)
          output = output_data(input,llm)
          gpt_df.loc[index, 'authors_gpt'] = output[0]['authors_gpt']
          gpt_df.loc[index, 'citation_key_gpt'] = output[0]['citation_key_gpt']
        except Exception as e:
          print(f"Authors catch {index}: {e}")
        time.sleep(30)
    #gpt_df.to_csv(destination_file_path,index=False)
    return gpt_df