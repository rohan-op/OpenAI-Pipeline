import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
"Chemistry": [
        "Green Chemistry",
        "Computational Chemistry",
        "Drug Discovery and Development",
        "Catalysis and Reaction Mechanisms",
        "Nanomaterials and Nanotechnology",
        "Polymer Chemistry",
        "Chemical Engineering and Process Optimization",
        "Analytical Techniques and Instrumentation",
        "Supramolecular Chemistry",
        "Medicinal Chemistry and Drug Design",
        "Surface Chemistry",
        "Materials Synthesis and Characterization",
        "Chemical Education and Outreach",
        "Environmental Chemistry and Sustainability",
        "Bioinorganic Chemistry",
        "Chemical Kinetics and Thermodynamics",
        "Spectroscopy and Spectrometry",
        "Coordination Chemistry",
        "Theoretical Chemistry and Quantum Chemistry",
        "Industrial Chemistry and Manufacturing",
        "Chemoinformatics",
        "Chemical Biology",
        "Physical Organic Chemistry",
        "Organic Synthesis",
        "Inorganic Synthesis",
        "Analytical Chemistry for Environmental Monitoring",
        "Chemical Sensors and Biosensors",
        "Chemical Informatics",
        "Chemical Safety and Hazardous Materials Management",
        "Chemistry of Natural Products",
        "Chemistry of Food and Flavor",
        "Chemistry of Pharmaceuticals",
        "Chemistry of Polymers",
        "Chemistry of Dyes and Pigments",
        "Electrochemistry",
        "Solid-State Chemistry",
        "Chemical Nanosensors",
        "Green Solvents and Solvent Alternatives",
        "Chemistry of Renewable Energy",
        "Chemistry of Nanomedicine",
        "Quantum Dot Chemistry",
        "Photochemistry",
        "Chemical Synthesis of Nanoparticles",
        "Supramolecular Chemistry in Drug Delivery",
        "Chemical Vapor Deposition (CVD)",
        "Chemistry of Battery Materials",
        "Chemical Analysis of Air Pollutants",
        "Chemistry of Water Treatment",
        "Bioorganic Chemistry",
        "Chemistry of Coordination Compounds",
        "Chemistry of Metal-Organic Frameworks (MOFs)"
    ]
}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/Chemistry/raw_semantic_Chemistry.csv", index=False)

