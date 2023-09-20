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


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    df=pd.read_csv(r'toy_dataset.csv')
    print(df)

    """Bar Chart"""

    plt.rcParams["figure.figsize"] = (10,5)

    city_name = df['City']
    Income = df['Income']
    plt.bar(city_name,Income)
    plt.xlabel('City')
    plt.ylabel('Income')
    plt.title('Bar_Chart')
    plt.xticks(rotation=45,horizontalalignment='right' )
    plt.show()

    st.write("Here's our first attempt at using data to create a table:")
    st.write(df)
    st.write(plt.show())

    


if __name__ == "__main__":
    run()
