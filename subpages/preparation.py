#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/1 14:00
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preparation.py
# @Desc     :   

from pandas import read_csv, DataFrame
from streamlit import (empty, sidebar, subheader, session_state, file_uploader,
                       rerun, button)

from utils.helper import Timer

empty_messages: empty = empty()
empty_table: empty = empty()

if "data" not in session_state:
    session_state["data"] = None
if "timer" not in session_state:
    session_state["timer"] = ""

with sidebar:
    if session_state["data"] is None:
        subheader("Data Preparation")
        uploaded_file = file_uploader(
            "Upload your CSV file",
            type=["csv"],
            help="Upload a CSV file. The first row should contain the column headers.",
        )
        if uploaded_file is None:
            empty_messages.error("Please upload a dataset in the Home page first.")
        else:
            with Timer("Data Loading") as t:
                session_state["data"]: DataFrame = read_csv(uploaded_file)
                empty_table.data_editor(
                    session_state["data"],
                    hide_index=True,
                    disabled=True,
                    use_container_width=True,
                )
            session_state["timer"] = repr(t)
            rerun()
    else:
        empty_table.data_editor(
            session_state["data"],
            hide_index=True,
            disabled=True,
            use_container_width=True,
        )
        empty_messages.success(f"{session_state.timer} You can clear it if needed.")

        if button("Clear Data", type="primary", use_container_width=True, help="Clear the uploaded dataset."):
            session_state.clear()
            rerun()
