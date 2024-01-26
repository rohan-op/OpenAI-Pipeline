import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
"Engineering":[
    "Aerospace Engineering and Space Exploration",
    "Biomedical Engineering and Medical Devices",
    "Civil Engineering and Infrastructure Development",
    "Mechatronics and Robotics Engineering",
    "Energy Systems and Renewable Energy",
    "Materials Engineering and Nanomaterials",
    "Transportation Engineering and Smart Cities",
    "Environmental Engineering and Sustainable Design",
    "Manufacturing Processes and Industry 4.0",
    "Electronics and Embedded Systems",
    "Data Science in Engineering",
    "Human Factors Engineering",
    "Geotechnical Engineering and Soil Mechanics",
    "Chemical Process Engineering and Petrochemicals",
    "Structural Health Monitoring and Maintenance",
    "Optical and Photonics Engineering",
    "Biomechanical Engineering and Prosthetics",
    "Water Resources Engineering and Management",
    "Cyber-Physical Systems and IoT",
    "Fire Safety Engineering and Disaster Resilience",
    "Engineering Economics and Cost Analysis",
    "Construction Engineering",
    "Computational Science and Engineering",
    "Mining and Geological Engineering",
    "Packaging Engineering and Logistics",
    "Ergonomics and Human Factors",
    "Additive Manufacturing and 3D Printing",
    "Engineering Ethics and Professionalism",
    "Sustainable and Green Engineering",
    "Engineering Education and STEM Learning",
    "Micro and Nanoelectronic Devices",
    "Software Engineering and Programming",
    "Communication Systems and Mobile Networks",
    "Computer Engineering and Processor Design",
    "Control Systems and Automation",
    "Engineering Management and Systems Engineering",
    "Thermal and Fluids Engineering",
    "Electrical Engineering and Power Systems",
    "Fire Safety Engineering and Disaster Resilience",
    "Cyber-Physical Systems and IoT",
    "Water Resources Engineering and Management",
    "Biomechanical Engineering and Prosthetics",
    "Optical and Photonics Engineering",
    "Structural Health Monitoring and Maintenance",
    "Chemical Process Engineering and Petrochemicals",
    "Geotechnical Engineering and Soil Mechanics",
    "Human Factors Engineering","Data Science in Engineering",
    "Electronics and Embedded Systems",
    "Environmental Engineering and Sustainable Design",
    "Transportation Engineering and Smart Cities",
    "Materials Engineering and Nanomaterials",
    "Energy Systems and Renewable Energy",
    "Mechatronics and Robotics Engineering"
    ]
}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/Engineering/raw_semantic_Engineering.csv", index=False)

