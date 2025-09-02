#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/1 23:15
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   advanced_test.py
# @Desc     :
from pyexpat import model

from pandas import DataFrame
from streamlit import (empty, sidebar, subheader, session_state, caption,
                       slider, button, columns, metric, selectbox)

from utils.helper import Timer, scatter_3d_with_category

empty_messages: empty = empty()
left, _ = columns(2, gap="large")
empty_chart: empty = empty()

if "data" not in session_state:
    session_state["data"] = None
if "advanced" not in session_state:
    session_state["advanced"] = None
if "X" not in session_state:
    session_state["X"] = None
if "scaler" not in session_state:
    session_state["scaler"] = None
if "advanced" not in session_state:
    session_state["advanced"] = None
if "advanced_df" not in session_state:
    session_state["advanced_df"] = None
if "centres" not in session_state:
    session_state["centres"] = None
if "pca" not in session_state:
    session_state["pca"] = None

with sidebar:
    if session_state["data"] is None:
        empty_messages.error("Please upload a dataset in the Home page first.")
    else:
        if session_state["advanced"] is None:
            empty_messages.error("Please train the model in the Advanced KMeans - Train page first.")
        else:
            empty_messages.success("KMeans model has been trained. You can click the button to test it now.")
            subheader("Testing Settings")

            cols: list[str] = session_state["X"].columns.tolist()
            # print(cols)

            values: list[float] = []
            names: list[str] = []
            for col in cols:
                if col == "Gender":
                    unique_values = sorted(session_state["X"][col].unique())
                    value = selectbox(
                        f"Select **{col}** for testing",
                        options=unique_values,
                        index=0,
                        help=f"Select the value for {col} (0=Female, 1=Male).",
                    )
                    values.append(value)
                    names.append(col)
                    caption(f"The {col} is set to {value} ({'Female' if value == 0 else 'Male'}).")
                else:
                    min_value: float = session_state["X"][col].min()
                    max_value: float = session_state["X"][col].max()
                    mean_value: float = session_state["X"][col].mean()
                    step_value: float = max(0.1, (max_value - min_value) / len(session_state["X"]))

                    value = slider(
                        f"Select **{col}** for testing",
                        min_value=float(min_value),
                        max_value=float(max_value),
                        value=float(mean_value),
                        step=float(step_value),
                        help=f"Select the value for {col}.",
                    )
                    values.append(value)
                    names.append(col)
                    caption(f"The {col} is set to {value}.")

            fig = scatter_3d_with_category(
                session_state["advanced_df"],
                x_name="PCA-X",
                y_name="PCA-Y",
                z_name="PCA-Z",
                category_name="Cluster"
            )
            fig.add_scatter3d(
                x=session_state.centres["PCA-X"],
                y=session_state.centres["PCA-Y"],
                z=session_state.centres["PCA-Z"],
                name="Centres",
                mode="markers",
                marker=dict(color="red", size=10, symbol="circle")
            )
            empty_chart.plotly_chart(fig, use_container_width=True)

            X = DataFrame([values], columns=names)
            if button(
                    "Test with current settings",
                    type="primary", use_container_width=True,
                    help="Test the model with the current settings."
            ):
                with Timer("Prediction") as t:
                    x_scaler = session_state["scaler"].transform(X)
                    # print(x_scaler)
                    prediction = session_state["advanced"].predict(x_scaler)
                    x_pca = session_state["pca"].transform(x_scaler)

                    fig.add_scatter3d(
                        x=[x_pca[0][0]],
                        y=[x_pca[0][1]],
                        z=[x_pca[0][2]],
                        name="Test Point",
                        mode="markers",
                        marker=dict(color="green", size=15, symbol="x"),
                    )
                    empty_chart.plotly_chart(fig, use_container_width=True)

                    with left:
                        metric("Categorised as", value=f"{prediction[0]}", delta=None, delta_color="off")
                empty_messages.success(f" {t} Prediction has been made.")
