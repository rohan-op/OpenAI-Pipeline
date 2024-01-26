import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
    "Computer Science": [
        "Natural Language Processing",
        "Computer Vision and Image Processing",
        "Cryptography and Network Security",
        "Machine Learning Algorithms and Applications",
        "Artificial Intelligence Ethics and Bias",
        "Human-Computer Interaction and User Experience",
        "Big Data Analytics and Data Mining",
        "Robotics and Autonomous Systems",
        "Computer Graphics and Virtual Reality",
        "Computer Architecture and Hardware Design",
        "Software Engineering Practices and Methodologies",
        "Cybersecurity Threat Analysis and Defense",
        "Reinforcement Learning and Robotics",
        "Deep Learning and Neural Networks",
        "Distributed Systems and Cloud Computing",
        "Quantum Computing and Quantum Algorithms",
        "Privacy-Preserving Data Analysis",
        "Social Media Analytics and Recommendation Systems",
        "Blockchain Technology and Applications",
        "Natural Language Generation and Conversational AI",
        "Computer Vision for Healthcare",
        "IoT (Internet of Things) and Edge Computing",
        "Graph Algorithms and Network Analysis",
        "Explainable AI (XAI)",
        "Federated Learning",
        "Bioinformatics and Computational Biology",
        "Autonomous Vehicles and Self-Driving Cars",
        "Human-Robot Interaction",
        "Emotion Recognition in AI",
        "Adversarial Machine Learning",
        "Edge AI and Edge Devices",
        "Computer-Aided Drug Design",
        "Game Development and AI",
        "Quantum Cryptography",
        "Augmented Reality (AR) Applications",
        "Natural Language Understanding",
        "Image and Video Forensics",
        "AI in Financial Services",
        "Virtual Reality (VR) for Therapy",
        "Exascale Computing",
        "Algorithmic Trading",
        "AI in Environmental Monitoring",
        "Quantum Machine Learning",
        "AI in Agriculture and Precision Farming",
        "Healthcare Informatics and AI",
        "Human-Centered AI",
        "AI for Education",
        "Cyber-Physical Systems",
        "AI in Music and Creativity",
        "Automated Theorem Proving",
        "Blockchain for Supply Chain Management"
    ]
}

raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/CompSci/raw_semantic_CompSci.csv", index=False)
