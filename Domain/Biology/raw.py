import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
"Biology": [
        "Genomic Sequencing and Comparative Genomics",
        "Neurobiology of Learning and Memory",
        "Evolutionary Genetics and Phylogenetics",
        "Stem Cell Research and Regenerative Medicine",
        "Ecological Modeling and Biodiversity Conservation",
        "Bioinformatics and Computational Biology",
        "Immunotherapy and Cancer Immunology",
        "Molecular Biology of Gene Expression",
        "Marine Ecology and Conservation",
        "Zoological Behavior and Conservation",
        "Microbiome and Human Health",
        "Epigenetics and Epigenomics",
        "Evolutionary Developmental Biology (Evo-Devo)",
        "Population Genetics and Speciation",
        "Synthetic Biology and Genetic Engineering",
        "Plant Molecular Biology and Crop Improvement",
        "Behavioral Neuroscience and Neuropsychology",
        "Environmental Microbiology and Biogeochemistry",
        "Cell Signaling and Signal Transduction",
        "Biomaterials and Tissue Engineering",
        "Biophysics and Computational Modeling",
        "Toxicology and Environmental Health",
        "Agricultural Genetics and Crop Protection",
        "Comparative Anatomy and Morphology",
        "Neuropharmacology and Drug Development",
        "Neuroimaging and Brain Connectivity",
        "Evolutionary Ecology and Adaptation",
        "Proteomics and Protein Structure",
        "Immunogenetics and Autoimmune Diseases",
        "Conservation Genetics and Endangered Species",
        "Functional Genomics and Gene Regulation",
        "Microbial Ecology and Symbiosis",
        "Neurodevelopmental Disorders",
        "Plant Physiology and Stress Responses",
        "Molecular Epidemiology and Disease Surveillance",
        "Virology and Viral Pathogenesis",
        "Biomedical Engineering and Medical Devices",
        "Bioinformatics Tools and Software Development",
        "Cancer Genetics and Therapeutics",
        "Behavioral Ecology and Animal Communication",
        "Genome Editing Technologies (CRISPR/Cas9)",
        "Aquatic Ecology and Limnology",
        "Structural Biology and Protein Folding",
        "Pharmacogenomics and Personalized Medicine",
        "Neuroendocrinology and Hormone Regulation",
        "Plant Genetics and Breeding Programs",
        "Ecotoxicology and Pollutant Impact on Ecosystems",
        "Neurodegenerative Diseases",
        "Molecular Evolution and Adaptation",
        "Comparative Genomics of Model Organisms",
        "Metagenomics and Microbial Communities",
        "Host-Pathogen Interactions",
        "Stem Cell-Based Therapies"
        ]
}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/Biology/raw_semantic_Biology.csv", index=False)

