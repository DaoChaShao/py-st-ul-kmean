<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**INTRODUCTION**
---
This project is a **Streamlit-based interactive K-Means** clustering application designed to simplify both training and
testing of clustering models. It supports **simple 2D K-Means clustering** as well as **advanced multi-feature 3D
clustering** with **PCA visualisation**. Users can upload their datasets, select features for clustering, visualize
clusters interactively, and test new points in real-time. The application emphasises **reproducibility**, **scalability
**, and **user-friendly** visualisation.

**DATASET INTRODUCTION**
---
Using the
classic [Mall Customer dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python),
containing basic information of 200 mall customers:

+ CustomerID - Unique identifier
+ Gender - Customer gender
+ Age - Customer age
+ Annual Income (k$) - Annual income in thousands
+ Spending Score (1-100) - Mall spending score

**LEARNING OBJECTIVES**
---
Through this application, you can:

+ Practice the K-Means clustering algorithm
+ Explore MeanShift density clustering
+ Visualise customer segmentation results
+ Understand applicable scenarios of different clustering algorithms
+ Analyse characteristic patterns of customer groups

**FEATURES**
---

1. **Data Upload & Preparation**
    + Load CSV files with automatic preview in an interactive table.
    + Supports clearing and re-uploading datasets.
    + Provides timing metrics for data loading.
2. **Simple K-Means Training**
    + Train K-Means on two selected features (2D).
    + Automatically identifies the optimal number of clusters using the silhouette score.
    + Standardises features automatically.
    + Visualises clusters in 2D scatter plots with cluster centres.
    + Supports clearing the trained model to retry.
3. **Advanced K-Means Training**
    + Train K-Means on multiple selected features.
    + Uses PCA to project high-dimensional data to 3D for visualisation.
    + Finds the optimal number of clusters automatically.
    + 3D scatter plot visualisation with cluster centres.
    + Supports selecting multiple features to include/exclude dynamically.
4. **Model Testing**
    + Test trained models interactively by selecting new input values.
    + Simple mode: 2D test points added to scatter plots.
    + Advanced mode: multi-feature test points projected in 3D with PCA.
    + Displays predicted cluster and relevant metrics.
5. **Reproducibility**
    + Random seed selection ensures consistent clustering results.
    + Standard scaling ensures numeric features are normalised.

Start your unsupervised learning journey now!

**WEB DEVELOPMENT**
---

1. Install NiceGUI with the command `pip install streamlit`.
2. Run the command `pip show streamlit` or `pip show streamlit | grep Version` to check whether the package has been
   installed and its version.

**PRIVACY NOTICE**
---
This application may require inputting personal information or private data to generate customised suggestions,
recommendations, and necessary results. However, please rest assured that the application does **NOT** collect, store,
or transmit your personal information. All processing occurs locally in the browser or runtime environment, and **NO**
data is sent to any external server or third-party service. The entire codebase is open and transparent — you are
welcome to review the code [here](./) at any time to verify how your data is handled.

**LICENCE**
---
This application is licensed under the [BSD-3-Clause License](LICENSE). You can click the link to read the licence.

**CHANGELOG**
---
This guide outlines the steps to automatically generate and maintain a project changelog using git-changelog.

1. Install the required dependencies with the command `pip install git-changelog`.
2. Run the command `pip show git-changelog` or `pip show git-changelog | grep Version` to check whether the changelog
   package has been installed and its version.
3. Prepare the configuration file of `pyproject.toml` at the root of the file.
4. The changelog style is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
5. Run the command `git-changelog`, creating the `Changelog.md` file.
6. Add the file `Changelog.md` to version control with the command `git add Changelog.md` or using the UI interface.
7. Run the command `git-changelog --output CHANGELOG.md` committing the changes and updating the changelog.
8. Push the changes to the remote repository with the command `git push origin main` or using the UI interface.
