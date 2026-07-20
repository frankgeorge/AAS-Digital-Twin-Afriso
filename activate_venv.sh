#!/bin/bash

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
    echo "The VENV activated"
else
    echo "The VENV do not exist. Please run 'make venv' first."
fi
