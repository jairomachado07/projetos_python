#!/bin/bash

# Entra na pasta onde este arquivo está salvo
cd "$(dirname "$0")"

# Roda o comando do Streamlit
python3 -m streamlit run interface.py
