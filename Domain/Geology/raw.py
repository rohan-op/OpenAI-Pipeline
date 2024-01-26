import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
"Geology":  [
        "Paleoclimatology and Climate Reconstructions",
        "Mineralogy and Mineral Exploration",
        "Sedimentology and Stratigraphy",
        "Structural Geology and Tectonics",
        "Geomorphology and Landscape Evolution",
        "Geophysics and Geophysical Surveys",
        "Volcanology and Volcanic Hazards",
        "Hydrogeology and Groundwater Resources",
        "Geochemistry and Isotope Geochemistry",
        "Petrology and Igneous Processes",
        "Seismology and Earthquake Studies",
        "Glaciology and Glacier Dynamics",
        "Remote Sensing in Geological Studies",
        "Environmental Geology and Hazard Assessment",
        "Geological Mapping and Cartography",
        "Mineral Resources and Economic Geology",
        "Geological Hazards and Risk Assessment",
        "Planetary Geology and Extraterrestrial Studies",
        "Geoarchaeology and Geohistorical Research",
        "Geological Education and Outreach","Geology and Society","Mining Geology",
        "Mapping Techniques","Geoscience Data Analysis","ModelingSpeleology","Natural Disaster",
        "Soil Genesis","Geohazards","Classification and Mapping","Geomatics","Geological Remote Sensing",
        "Planetology","Spatial Analysis","Quaternary Geology","Pollutant Transport",
        "Environmental Geochemistry","Geofluids","Hydrogeochemistry","Geomechanics",
        "Rock Mechanics","Petroleum","Ore Deposit Models","Economic Geology","Marine Geology ",
        "Ocean Floor Dynamics","Geomicrobiology","Microbial Processes","Geochronology",
        "Dating Methods","Plate Tectonics","Geomorphology","Fossil Studies","Paleontology",
        "Geological Education","Risk Assessment","Geological Hazards","Mineral Resources",
        "Economic Geology","Cartography","Remote Sensing in Geological Studies"
    ]
}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/Geology/raw_semantic_Geology.csv", index=False)

