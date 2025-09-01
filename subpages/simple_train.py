#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/31 23:04
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   simple_train.py
# @Desc     :

from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score, silhouette_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from streamlit import (empty, sidebar, subheader, session_state, selectbox,
                       caption, number_input, button, columns, metric, rerun)

from utils.helper import Timer, scatter_2d_without_category, scatter_2d_with_category

empty_messages: empty = empty()
left, right = columns(2, gap="large")
empty_chart: empty = empty()
empty_table: empty = empty()

if "data" not in session_state:
    session_state["data"] = None
if "timer" not in session_state:
    session_state["timer"] = ""
if "simple" not in session_state:
    session_state["simple"] = None
if "X" not in session_state:
    session_state["X"] = None
if "scaler" not in session_state:
    session_state["scaler"] = None

with sidebar:
    if session_state["data"] is None:
        empty_messages.error("Please upload a dataset in the Home page first.")
    else:
        empty_messages.info("Dataset has been uploaded.")
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
        x_name = selectbox(
            "Select X-axis feature",
            options=cols,
            index=2,
            help="Select the feature for the X-axis.",
        )
        caption(f"The {x_name} will be used as the X-axis feature.")
        cols.remove(x_name)
        y_name = selectbox(
            "Select Y-axis feature",
            options=cols,
            index=2,
            help="Select the feature for the Y-axis.",
        )
        caption(f"The {y_name} will be used as the Y-axis feature.")

        # Standardise the features
        session_state["scaler"] = StandardScaler()
        session_state["X"] = session_state["data"][[x_name, y_name]]
        X = session_state["scaler"].fit_transform(session_state.X)
        # Fit K-Means model and find the best clusters
        k_values: list[int] = list(range(2, 11))
        scores: list[float] = []
        for k in k_values:
            trier = KMeans(n_clusters=k, random_state=seed, n_init="auto")
            label = trier.fit_predict(X)
            # score = calinski_harabasz_score(X, label)
            score = silhouette_score(X, label)
            scores.append(score)
        best_k = k_values[scores.index(max(scores))]

        if session_state["simple"] is None:
            empty_table.data_editor(
                session_state["data"][[x_name, y_name]],
                hide_index=True,
                disabled=True,
                use_container_width=True,
            )

            fig = scatter_2d_without_category(session_state["data"], x_name, y_name)
            empty_chart.plotly_chart(fig)

            if button(
                    "Run KMeans Clustering", type="primary", use_container_width=True,
                    help="Run KMeans clustering on the selected features."
            ):
                with Timer("KMeans Clustering") as t:
                    session_state["simple"] = KMeans(n_clusters=best_k, random_state=seed, n_init="auto")
                    session_state["simple"].fit(X)
                session_state["timer"] = repr(t)
                rerun()
        else:
            with left:
                metric("Best K Value", best_k, delta=f"{max(scores):.4f}", delta_color="normal", )

            centres = session_state["scaler"].inverse_transform(session_state["simple"].cluster_centers_)
            # print(centres)
            cluster = session_state["simple"].predict(X)
            session_state["data"]["Cluster"] = cluster

            # Show the clustering results
            category_name: str = "Cluster"
            empty_table.data_editor(
                session_state["data"][[x_name, y_name, category_name]],
                hide_index=True, disabled=True, use_container_width=True,
            )
            fig = scatter_2d_with_category(session_state["data"], x_name, y_name, category_name)
            fig.add_scatter(
                x=centres[:, 0],
                y=centres[:, 1],
                name="Centres",
                mode="markers",
                marker=dict(color="red", size=10, symbol="circle")
            )
            empty_chart.plotly_chart(fig)

            if button(
                    "Clear Clustering Model and Retry", type="primary", use_container_width=True,
            ):
                session_state["simple"] = None
                session_state["data"].drop(columns=["Cluster"], inplace=True)
                rerun()

            empty_messages.success(f"{session_state.timer} KMeans clustering has been completed.")
