import os
import sys
import pandas as pd
sys.path.append("..")
from gpt import gpt_df_generator
chunk_size = 10
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

base_dir = "/N/u/shahrob/Carbonate/Research/Datasets/"
transformed_fname = "Transform/Domain/Biology/transform_semantic_Biology.csv"
generative_fname = "Generative/Domain/generative_Biology_100.csv"

df = pd.read_csv(os.path.join(base_dir,transformed_fname))
df = df[:100]

for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i:i + chunk_size]
    gpt_df = pd.concat([gpt_df,gpt_df_generator(chunk,os.environ.get('OPEN_KEY1'))], ignore_index=True)

gpt_df.to_csv(os.path.join(base_dir,generative_fname),index=False)