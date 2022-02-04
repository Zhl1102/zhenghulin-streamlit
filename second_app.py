import streamlit as st
import numpy
import pandas
import time

'Starting a long computation...'

# Add a placeholder
header_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
		header_iteration.text(f'Iteration {i + 1}')
		bar.progress(i + 1)
		time.sleep(0.1)

'...and now we\'re done!'