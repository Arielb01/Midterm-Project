import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EV Data Explorer", layout="wide")
st.title("🔌 Electric Vehicle Dataset Explorer")

# Load the dataset
@st.cache_data
def load_data():
    url = "https://www.dropbox.com/scl/fi/xp42e098kmv4fsuwku49u/ElectricCarData_Clean.csv?rlkey=vyq99aaowbc9ivfz5m9gjegop&st=d6o043rx&dl=1"
    df = pd.read_csv(url)
    df['FastCharge_KmH'] = pd.to_numeric(df['FastCharge_KmH'].replace('—', None), errors='coerce')
    return df

df = load_data()

# Show dataset dimensions and preview
st.subheader("Dataset Overview")
st.write(f"Number of rows: {df.shape[0]}")
st.write(f"Number of columns: {df.shape[1]}")
st.dataframe(df.head())

# Show variable types
st.subheader("Column Types and Data Overview")
st.text(str(df.dtypes))

# Numeric variable selection for histogram
st.subheader("Distribution of Numeric Variables")
numeric_columns = ['AccelSec', 'TopSpeed_KmH', 'Range_Km', 'Efficiency_WhKm',
                   'FastCharge_KmH', 'Seats', 'PriceEuro']
selected_numeric = st.selectbox("Choose a numeric variable:", numeric_columns)

fig1, ax1 = plt.subplots()
sns.histplot(df[selected_numeric], kde=True, ax=ax1, color="skyblue")
ax1.set_title(f"Distribution of {selected_numeric}")
ax1.set_xlabel(selected_numeric)
ax1.set_ylabel("Frequency")
st.pyplot(fig1)

# Relationship: Range vs Price
st.subheader("Relationship: Range vs Price")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x='Range_Km', y='PriceEuro', hue='Brand', ax=ax2)
ax2.set_title("Range vs Price")
ax2.set_xlabel("Range (Km)")
ax2.set_ylabel("Price (Euro)")
st.pyplot(fig2)

# Comparison: Efficiency by Segment
st.subheader("Comparison: Efficiency by Segment")
fig3, ax3 = plt.subplots()
sns.boxplot(data=df, x='Segment', y='Efficiency_WhKm', ax=ax3)
ax3.set_title("Efficiency by Segment")
ax3.set_xlabel("Segment")
ax3.set_ylabel("Efficiency (Wh/Km)")
st.pyplot(fig3)

# Trend: Acceleration vs Price colored by PowerTrain
st.subheader("Trend: Acceleration Time vs. Price by PowerTrain")
fig4, ax4 = plt.subplots()
sns.scatterplot(data=df, x='AccelSec', y='PriceEuro', hue='PowerTrain', ax=ax4)
ax4.set_title("Acceleration vs Price")
ax4.set_xlabel("0-100 km/h Acceleration (Seconds)")
ax4.set_ylabel("Price in Euros")
st.pyplot(fig4)

# Footer
st.markdown("---")
st.markdown("Developed by [Ariel Ben Moshe] | Dataset: ElectricCarData_Clean.csv")
