#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/31 22:52
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :

from pandas import DataFrame
from plotly.express import scatter
from random import seed as random_seed, getstate as get_state, setstate as set_state
from time import perf_counter


class Timer(object):
    """ timing code blocks using a context manager """

    def __init__(self, description: str = None, precision: int = 5):
        """ Initialise the Timer class
        :param description: the description of a timer
        :param precision: the number of decimal places to round the elapsed time
        """
        self._description: str = description
        self._precision: int = precision
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        """ Start the timer """
        self._start = perf_counter()
        print("-" * 50)
        print(f"{self._description} has started.")
        print("-" * 50)
        return self

    def __exit__(self, *args):
        """ Stop the timer and calculate the elapsed time """
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        """ Return a string representation of the timer """
        if self._elapsed != 0.0:
            print("-" * 50)
            return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."
        return f"{self._description} has NOT started."


class SeedSetter(object):
    """ Set a random seed for reproducibility. """

    def __init__(self, seed: int = 9527):
        """ Initialise the RandomSeed class with a seed. """
        self._seed = seed
        self._state_random = None

    def __enter__(self):
        """ Enter the context manager and set the random seed. """
        # Store the current state of random and Faker
        self._state_random = get_state()
        # Set the random seed for reproducibility
        random_seed(self._seed)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Exit the context manager and reset the random seed. """
        # Reset the random and Faker states to their original values.
        set_state(self._state_random)
        return False

    def __str__(self):
        """ Return a string representation of the random seed. """
        return f"SeedSetter with seed {self._seed}"


def scatter_without_category(data: DataFrame, x_name: str, y_name: str):
    """ Get the unique categories in the target column.
    :param data: the DataFrame containing the data
    :param x_name: the name of the feature column (X)
    :param y_name: the name of the target column (Y)
    :return: a scatter plot with different colours and symbols for each category
    """
    return scatter(
        data,
        x=x_name,
        y=y_name,
        hover_data=[x_name, y_name]
    )


def scatter_with_category(data: DataFrame, x_name: str, y_name: str, category: str):
    """ Get the unique categories in the target column.
    :param data: the DataFrame containing the data
    :param x_name: the name of the feature column (X)
    :param y_name: the name of the target column (Y)
    :param category: the name of the category column
    :return: a scatter plot with different colours and symbols for each category
    """
    return scatter(
        data,
        x=x_name,
        y=y_name,
        color=category,
        symbol=category,
        hover_data=[x_name, y_name, category]
    ).update_layout(coloraxis_showscale=False)
