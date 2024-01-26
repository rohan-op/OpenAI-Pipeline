import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {
"Mathematics":[
    "Combinatorial Optimization",
    "Algebraic Geometry",
    "Mathematical Logic and Proof Theory",
    "Number Theory and Cryptography",
    "Graph Theory and Network Analysis",
    "Mathematical Modeling of Biological Systems",
    "Harmonic Analysis and Wavelets",
    "Non-Euclidean Geometry",
    "Statistical Inference and Bayesian Analysis",
    "Mathematics Education and Pedagogy",
    "Topology and Knot Theory",
    "Quantum Information and Quantum Computing",
    "Mathematical Physics and Quantum Field Theory",
    "Applied Algebra and Coding Theory",
    "Fractal Geometry and Complex Dynamics",
    "Mathematics of Artificial Intelligence",
    "Mathematical Economics and Game Theory",
    "Numerical Analysis and Scientific Computing",
    "Mathematics of Climate Modeling",
    "Discrete Mathematics and Combinatorics",
    "Biomathematics","Mathematical Logic","Set Theory",
    "Operations Research","Decision Science",
    "Mathematics of Machine Learning ","Fluid Dynamics ",
    "Mathematical Physics","Information Theory",
    "Signal Processing","Control Theory and Optimization",
    "Computational Geometry","Topology","Financial Mathematics",
    "Quantitative Finance","Abstract Algebra","Calculus",
    "Numerical Linear Algebra","Matrix Analysis",
    "Probability Theory","Stochastic Processes",
    "Functional Analysis","Operator Theory",
    "Differential Equations","Dynamical Systems",
    "Discrete Mathematics ","Combinatorics",
    "Mathematics of Climate Modeling",
    "Numerical Analysis",
    "Scientific Computing","Mathematical Economics",
    "Mathematics of Artificial Intelligence","Applied Algebra and Coding Theory",
    "Quantum Information and Quantum Computing",
    "Mathematics Education and Pedagogy",
    "Statistical Inference and Bayesian Analysis"
    ]
}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/Mathematics/raw_semantic_Mathematics.csv", index=False)

