#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/1 23:14
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   advanced_train.py
# @Desc     :

from pandas import DataFrame
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from streamlit import (empty, sidebar, subheader, session_state, number_input,
                       caption, selectbox, multiselect, button, rerun,
                       columns, metric)

from utils.helper import scatter_3d_without_category, Timer, scatter_3d_with_category

empty_messages: empty = empty()
left, _ = columns(2, gap="large")
empty_chart: empty = empty()

if "data" not in session_state:
    session_state["data"] = None
if "simple" not in session_state:
    session_state["simple"] = None
if "scaler" not in session_state:
    session_state["scaler"] = None
if "X" not in session_state:
    session_state["X"] = None
if "advanced" not in session_state:
    session_state["advanced"] = None
if "timer" not in session_state:
    session_state["timer"] = ""
if "pca" not in session_state:
    session_state["pca"] = None
if "advanced_df" not in session_state:
    session_state["advanced_df"] = None
if "centres" not in session_state:
    session_state["centres"] = None
if "select" not in session_state:
    session_state["select"] = None

with sidebar:
    if session_state["data"] is None:
        empty_messages.error("Please upload a dataset in the Home page first.")
    else:
        if session_state["simple"] is not None:
            empty_messages.warning("Simple KMeans model has been trained. You must delete it first.")
        else:
            empty_messages.info(f"Dataset has been loaded successfully.")
            subheader("Training Settings")

            # Encode categorical features
            encoder = LabelEncoder()
            session_state["data"]["Gender"] = encoder.fit_transform(session_state["data"]["Gender"])

            seed: int = number_input(
                "Select Random Seed",
                min_value=0,
                max_value=10000,
                value=9527,
                step=1,
                help="Select a random seed for reproducibility.",
            )
            caption(f"The random seed is set to {seed}.")

            cols: list[str] = session_state["data"].columns.tolist()
            drop: str = selectbox(
                "Select feature to drop (optional)",
                options=cols,
                index=0,
                disabled=True,
                help="You should select a feature to drop from the dataset.",
            )
            caption(f"The {drop} will not be used in the model training.")
            cols.remove(drop)

            selection: list[str] = multiselect(
                "Select feature to drop (optional)",
                options=cols,
                default=session_state["select"],
                placeholder="Select features to train",
                help="You should select a feature to drop from the dataset.",
            )
            session_state["select"] = selection
            caption(f"{len(selection)} features will be used in the model training.")

            if not selection:
                empty_messages.error("Please select at least one feature to train the model.")
            elif len(selection) < 3:
                empty_messages.warning("Please select at least three feature to train.")
            else:
                # Standardise the features
                session_state["scaler"] = StandardScaler()
                session_state["X"] = session_state["data"][selection]
                X = session_state["scaler"].fit_transform(session_state["X"])

                # Fit K-Means model and find the best clusters
                k_values: list[int] = list(range(2, 11))
                scores: list[float] = []
                for k in k_values:
                    trier = KMeans(n_clusters=k, random_state=seed, n_init="auto")
                    label = trier.fit_predict(X)
                    score = silhouette_score(X, label)
                    scores.append(score)
                best_k = k_values[scores.index(max(scores))]

                # Initialise PCA for 3D visualisation
                session_state["pca"] = PCA(n_components=3)
                transform = session_state["pca"].fit_transform(X)

                if session_state["advanced"] is None:
                    session_state["advanced_df"] = DataFrame(transform, columns=["PCA-X", "PCA-Y", "PCA-Z"])
                    fig = scatter_3d_without_category(session_state.advanced_df)
                    empty_chart.plotly_chart(fig, use_container_width=True)

                    if button(
                            "Run KMeans Clustering", type="primary", use_container_width=True,
                            help="Run KMeans clustering on the selected features."
                    ):
                        with Timer("KMeans Clustering") as t:
                            session_state["advanced"] = KMeans(n_clusters=best_k, random_state=seed, n_init="auto")
                            session_state["advanced"].fit(X)
                        session_state["timer"] = repr(t)
                        rerun()
                else:
                    with left:
                        metric("Best K Value", best_k, delta=f"{max(scores):.4f}", delta_color="normal", )

                    transform = session_state["pca"].transform(session_state["advanced"].cluster_centers_)
                    session_state["centres"]: DataFrame = DataFrame(transform, columns=["PCA-X", "PCA-Y", "PCA-Z"])

                    category_name: str = "Cluster"
                    cluster = session_state["advanced"].predict(X)
                    session_state["advanced_df"][category_name] = cluster

                    # Show the clustering results
                    fig = scatter_3d_with_category(
                        data=session_state["advanced_df"],
                        x_name="PCA-X",
                        y_name="PCA-Y",
                        z_name="PCA-Z",
                        category_name=category_name
                    )
                    fig.add_scatter3d(
                        x=session_state.centres["PCA-X"],
                        y=session_state.centres["PCA-Y"],
                        z=session_state.centres["PCA-Z"],
                        name="Centres",
                        mode="markers",
                        marker=dict(color="red", size=10, symbol="circle")
                    )
                    empty_chart.plotly_chart(fig)

                    if button(
                            "Clear Clustering Model and Retry", type="primary", use_container_width=True,
                    ):
                        session_state["advanced"] = None
                        session_state["select"] = None
                        if category_name in session_state["data"].columns:
                            session_state["data"].drop(columns=[category_name], inplace=True)
                        rerun()

                    empty_messages.success(f"{session_state.timer} KMeans clustering has been completed.")
