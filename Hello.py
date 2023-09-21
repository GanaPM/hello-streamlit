# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from streamlit.logger import get_logger

LOGGER = get_logger(__name__)



    
df=pd.read_csv(r'Real_estate.csv')

"""Bar Chart Start"""
  

plt.rcParams["figure.figsize"] = (10,5)

Price = df['house_price_of_unit_area']
Age = df['house_age']
fig,ax=plt.subplots()
ax.bar(Price,Age)

plt.bar(Price,Age)
plt.xlabel('Price')
plt.ylabel('Age')
plt.title('Bar_Chart')

st.pyplot(fig)

"""Bar Chart End"""
