#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/31 22:52
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :

from streamlit import title, expander, caption, empty

empty_message = empty()
empty_message.info("Please check the details at the different pages of core functions.")

title("Unsupervised Learning with KMeans Clustering")
with expander("**INTRODUCTION**", expanded=True):
    caption("- **Interactive KMeans Clustering App**: Train and test KMeans models with your dataset.")
    caption("- **Simple 2D Mode**: Select 2 features, visualize clusters in 2D scatter plots.")
    caption("- **Advanced 3D Mode**: Use multiple features, project data with PCA, visualize in 3D.")
    caption("- **Real-time Testing**: Test new points and see predicted clusters immediately.")
    caption("- **Reproducibility**: Set random seed and standardize features automatically.")
    caption("- **User-Friendly Visualization**: Hover, zoom, and explore clusters interactively.")
