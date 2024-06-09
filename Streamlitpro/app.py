import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.express as px

conn = snowflake.connector.connect(
    user=st.secrets["snowflake"]["user"],
    password=st.secrets["snowflake"]["password"],
    account=st.secrets["snowflake"]["account"],
    warehouse=st.secrets["snowflake"]["warehouse"],
    database=st.secrets["snowflake"]["database"],
    schema=st.secrets["snowflake"]["schema"]
)

st.write("Hello sayani")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


query = "SELECT country, no_of_company FROM COUNTRYCOMPANY"
cur = conn.cursor()
cur.execute(query)
data = cur.fetchall()


# Convert to DataFrame
df = pd.DataFrame(data)

# Display DataFrame in Streamlit
st.write(df)




# Close the connection
cur.close()
conn.close()
