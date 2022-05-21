#! /usr/bin/env bash

# Let the DB start
python pre_start.py

# Create initial data in DB
python initial_data.py

# Populate with test data
python test_population.py