#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/1 20:24
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   simple_test.py
# @Desc     :   

from pandas import DataFrame
from streamlit import (empty, sidebar, subheader, session_state, number_input,
                       caption, button, columns, metric)

from utils.helper import Timer, scatter_2d_with_category

empty_messages: empty = empty()
left, _ = columns(2, gap="large")
empty_chart: empty = empty()

if "data" not in session_state:
    session_state["data"] = None
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
        if session_state["simple"] is None:
            empty_messages.error("Please train the model in the Simple KMeans - Train page first.")
        else:
            empty_messages.info("KMeans model has been trained.")
            subheader("Testing Settings")

            cols: list[str] = session_state["X"].columns.tolist()
            first_min: int = int(session_state["X"].iloc[:, 0].min())
            first_max: int = int(session_state["X"].iloc[:, 0].max())
            first_mean: int = int(session_state["X"].iloc[:, 0].mean())
            x: int = number_input(
                f"Select **{cols[0]}**  for scatter plot",
                min_value=first_min,
                max_value=first_max,
                value=first_mean,
                step=max(1, int((first_max - first_min) / len(session_state["X"].iloc[:, 0]))),
                help="Select the first feature for the scatter plot.",
            )
            caption(f"The axis x is set to {cols[0]}.")
            second_min: int = int(session_state["X"].iloc[:, 1].min())
            second_max: int = int(session_state["X"].iloc[:, 1].max())
            second_mean: int = int(session_state["X"].iloc[:, 1].mean())
            y: int = number_input(
                f"Select **{cols[1]}**  for scatter plot",
                min_value=second_min,
                max_value=second_max,
                value=second_mean,
                step=max(1, int((second_max - second_min) / len(session_state["X"].iloc[:, 1]))),
                help="Select the second feature for the scatter plot.",
            )
            caption(f"The axis y is set to {cols[1]}.")

            fig = scatter_2d_with_category(
                data=session_state["data"],
                x_name=cols[0],
                y_name=cols[1],
                category="Cluster"
            )
            empty_chart.plotly_chart(fig, use_container_width=True)

            if button(
                    "Test KMeans Model",
                    type="primary",
                    use_container_width=True,
                    help="Test the trained KMeans model with selected features.",
            ):
                with Timer("KMeans Testing") as timer:
                    X = session_state["scaler"].transform(DataFrame([[x, y]], columns=cols))
                    prediction = session_state["simple"].predict(X)
                    # print(prediction)

                    fig.add_scatter(
                        x=[x],
                        y=[y],
                        name="Test Point",
                        mode="markers",
                        marker=dict(color="red", size=15, symbol="x"),
                    )
                    empty_chart.plotly_chart(fig, use_container_width=True)

                    with left:
                        metric(label=f"Predicted Cluster", value=int(prediction[0]), delta=None, delta_color="off", )
                empty_messages.success(f"{timer} KMeans Test has completed successfully.")
