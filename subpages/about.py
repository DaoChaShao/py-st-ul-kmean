#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/31 22:52
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   about.py
# @Desc     :

from streamlit import title, expander, caption

title("**Application Information**")
with expander("About this application", expanded=True):
    caption("- **Data Upload & Preview**: Upload CSV files and inspect data in an interactive table.")
    caption("- **Automatic Cluster Selection**: Optimal number of clusters calculated using silhouette score.")
    caption("- **Feature Selection**: Choose which features to include or exclude for clustering.")
    caption("- **2D & 3D Visualization**: Scatter plots show clusters and their centers.")
    caption("- **Easy Model Management**: Clear models and retry training as needed.")
    caption("**Designed for Learning & Exploration**: Perfect for students and data enthusiasts to experiment with KMeans clustering.")
