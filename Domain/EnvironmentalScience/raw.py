import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
"Environmental Science":[
        "Climate Change Mitigation and Adaptation",
        "Ecological Restoration and Conservation",
        "Ecosystem Services and Biodiversity Conservation",
        "Sustainable Agriculture and Food Systems",
        "Environmental Policy and Governance",
        "Hydrology and Watershed Management",
        "Urban Ecology and Green Infrastructure",
        "Environmental Impact Assessment",
        "Environmental Economics and Valuation",
        "Waste Management and Recycling",
        "Air Quality Monitoring and Control",
        "Soil Remediation and Land Reclamation",
        "Environmental Toxicology and Risk Assessment",
        "Renewable Energy and Green Technologies",
        "Environmental Education and Outreach",
        "Remote Sensing in Environmental Science",
        "Wildlife Ecology and Conservation",
        "Marine and Coastal Ecology",
        "Environmental Health and Epidemiology",
        "Climate Modeling and Prediction",
        "Environmental Law, Policy and Management",
        "Cleaner Production and Pollution Prevention",
        "Environmental Sociology and Communication",
        "Corporate Sustainability and Social Responsibility",
        "Natural Resources Management and Conservation",
        "Environmental Risk and Impact Analysis",
        "Life Cycle Assessment and Carbon Footprinting",
        "Remediation of Contaminated Environments",
        "Ecohydrology and Water Sustainability",
        "Environmental Microbiology and Biotechnology",
        "Ecological Modeling and Systems Analysis",
        "Green Chemistry and Sustainable Materials",
        "Circular Economy and Waste Valorization",
        "Environmental Justice and Social Movements",
        "Landscape Ecology and Habitat Fragmentation",
        "Sustainability Science and Green Technology",
        "Climate Modeling and Prediction",
        "Environmental Health and Epidemiology",
        "Marine and Coastal Ecology",
        "Wildlife Ecology and Conservation",
        "Remote Sensing in Environmental Science",
        "Environmental Education and Outreach",
        "Renewable Energy and Green Technologies",
        "Environmental Toxicology and Risk Assessment",
        "Soil Remediation and Land Reclamation",
        "Air Quality Monitoring and Control",
        "Waste Management and Recycling",
        "Environmental Economics and Valuation",
        "Environmental Impact Assessment",
        "Urban Ecology and Green Infrastructure",
        "Hydrology and Watershed Management",
        "Environmental Policy and Governance",
        "Sustainable Agriculture and Food Systems",
        "Ecosystem Services and Biodiversity Conservation",
        "Ecological Restoration and Conservation",
        "Climate Change Mitigation and Adaptation"
        ]
}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/EnvironmentalScience/raw_semantic_EnvironmentalScience.csv", index=False)

