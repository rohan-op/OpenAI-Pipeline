import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
"Physics": [
    "Quantum Computing and Information",
    "Dark Matter and Dark Energy Studies",
    "Astrophysical Observations and Cosmology",
    "Particle Physics Experiments",
    "Condensed Matter Physics and Materials Science",
    "Nuclear Physics and Heavy Ion Collisions",
    "Plasma Physics and Fusion Research",
    "Gravitational Wave Detection and Research",
    "High-Energy Astrophysics",
    "Quantum Mechanics and Quantum Field Theory",
    "Astrobiology and Extraterrestrial Life",
    "Quantum Optics and Quantum Information",
    "String Theory and Fundamental Physics",
    "Particle Accelerators and Detectors",
    "Theoretical Astrophysics and Cosmology",
    "Quantum Materials and Superconductivity",
    "Quantum Entanglement and Quantum Computing Algorithms",
    "Experimental Techniques in Physics",
    "Dark Matter Detection Experiments",
    "Physics Education and Outreach",
    "Biophysics and Biological Physics",
    "Astroparticle Physics",
    "Quantum Sensors and Metrology",
    "Cosmic Microwave Background Radiation",
    "Advanced Materials for Energy Applications",
    "Optoelectronics and Photonics",
    "Astrochemistry and Planetary Science",
    "High-Performance Computing in Physics",
    "Quantum Communication and Cryptography",
    "Astroinformatics and Big Data Analysis",
    "Environmental Physics and Climate Modeling",
    "Neutrino Physics and Neutrino Oscillations",
    "Quantum Computing Hardware and Architectures",
    "Superfluidity and Bose-Einstein Condensates",
    "Magnetic Resonance Imaging (MRI) in Physics",
    "Astroengineering and Space Technology",
    "Renewable Energy and Sustainable Physics",
    "Quantum Many-Body Physics",
    "Accelerator-driven Subcritical Reactors (ADS)",
    "Quantum Error Correction",
    "Quantum Simulation and Quantum Algorithms",
    "High-Temperature Superconductors",
    "Atomic and Molecular Physics",
    "Quantum Nanophotonics",
    "Exotic Particles and Beyond the Standard Model",
    "Theoretical Condensed Matter Physics",
    "Quantum Cryptanalysis",
    "Quantum Hardware Benchmarking",
    "Quantum Internet and Quantum Key Distribution",
    "Quantum Metrology for Precision Measurements"
]
}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/Physics/raw_semantic_Physics.csv", index=False)

