import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
"Psychology":[
    "Positive Psychology and Well-being",
    "Clinical Psychology and Psychotherapy",
    "Neuroimaging and Brain Connectivity",
    "Social Cognition and Empathy",
    "Cross-Cultural Psychology",
    "Child and Adolescent Development",
    "Behavioral Economics and Decision Making",
    "Health Psychology and Behavior Change",
    "Environmental Psychology and Sustainability",
    "Forensic Psychology and Criminal Profiling",
    "Emotion Regulation and Affective Science",
    "Sports Psychology and Performance Enhancement",
    "Psycholinguistics and Language Processing",
    "Evolutionary Psychology and Human Behavior",
    "Psychometrics and Psychological Testing",
    "Gender and Sexuality Studies",
    "Media Psychology and Media Effects",
    "Positive Youth Development",
    "Cognitive Aging and Memory Research",
    "Animal Behavior and Comparative Psychology",
    "Clinical Neuropsychology ","Mathematical Psychology",
    "Psychometrics","Psychology of Art","Aesthetics",
    "Psychology of Religion and Spirituality",
    "Addiction Psychology and Treatment",
    "Sleep and Biological Rhythms",
    "Sensation and Perception Research",
    "Neural Networks and Computational Models",
    "Counseling Psychology and Mental Health",
    "Consumer Psychology and Persuasion",
    "Community Psychology and Social Change",
    "Industrial-Organizational Psychology",
    "Educational Psychology and Learning Sciences",
    "Personality Psychology","Trait Theory",
    "Cognitive Psychology","Perception",
    "Animal Behavior","Comparative Psychology",
    "Cognitive Aging and Memory Research",
    "Positive Youth Development",
    "Media Psychology and Media Effects",
    "Gender and Sexuality Studies",
    "Psychometrics and Psychological Testing",
    "Evolutionary Psychology and Human Behavior",
    "Psycholinguistics and Language Processing",
    "Sports Psychology and Performance Enhancement",
    "Emotion Regulation and Affective Science",
    "Forensic Psychology and Criminal Profiling",
    "Environmental Psychology and Sustainability",
    "Health Psychology and Behavior Change",
    "Behavioral Economics and Decision Making",
    "Child and Adolescent Development"
    ]
}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/Psychology/raw_semantic_Psychology.csv", index=False)

