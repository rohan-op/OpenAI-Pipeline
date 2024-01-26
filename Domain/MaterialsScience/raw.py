import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
"Materials Science": [
    "Nanomaterials and Nanotechnology",
    "Advanced Functional Materials",
    "Semiconductor Materials and Devices",
    "Biomaterials and Tissue Engineering",
    "Materials for Renewable Energy",
    "Polymer Science and Engineering",
    "Metallurgy and Alloys",
    "Superconducting Materials and Applications",
    "Materials Characterization and Testing",
    "Ceramics and Ceramic Engineering",
    "Composites and Hybrid Materials",
    "Materials Recycling and Sustainability",
    "Thin Films and Coatings",
    "Magnetic Materials and Spintronics",
    "Optical and Photonic Materials",
    "Electronic Materials and Devices",
    "Materials for Aerospace Applications",
    "Smart Materials and Responsive Structures",
    "Materials Informatics and Computational Design",
    "Materials Education and Outreach",
    "Nanocomposites and Nanomaterial Synthesis",
    "Biodegradable Polymers",
    "Hydrogels and Soft Materials",
    "Graphene and 2D Materials",
    "Biomineralization and Bioinspired Materials",
    "Materials for Drug Delivery",
    "Materials for Wearable Technology",
    "High-Temperature Materials",
    "Flexible Electronics and Flexible Materials",
    "3D Printing of Materials",
    "Materials for Biomedical Imaging",
    "Energy Storage Materials",
    "Quantum Materials",
    "Functional Coatings for Surface Modification",
    "Materials for Additive Manufacturing",
    "Structural Health Monitoring Materials",
    "Materials for Quantum Computing",
    "Organic Electronics and Conductive Polymers",
    "High-Performance Composites",
    "Bioactive Glasses and Ceramics",
    "Materials for Water Purification",
    "Materials for Space Exploration",
    "Nanostructured Surfaces and Interfaces",
    "Biofabrication and Bioprinting",
    "Materials for Renewable Energy Storage",
    "Self-Healing Materials",
    "Materials for Green Building",
    "Advanced Ceramics for Extreme Environments",
    "Materials for Energy Harvesting",
    "Materials for Microelectronics Packaging",
    "Sustainable Concrete and Construction Materials",
    "Materials for Robotics and Automation",
]
}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/MaterialsScience/raw_semantic_MaterialsScience.csv", index=False)

