import streamlit as st
import numpy
import pandas

if st.checkbox('show dataframe'):
		chart_data = pandas.DataFrame(
				numpy.random.randn(20, 3),
				columns=['a', 'b', 'c'])

		st.line_chart(chart_data)