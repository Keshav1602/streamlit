import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
def load_data():
    data = pd.read_csv(r"C:\Users\kesha\Downloads\final_df.csv")
    data.drop(columns=["Unnamed: 0"], inplace=True)  # Remove unnecessary column
    return data

data = load_data()

# Streamlit app
st.title("Question Analysis Dashboard")
st.title("Project Management and Enterpreneaurship")

# Show dataset
if st.checkbox("Show Raw Data"):
    st.subheader("Dataset")
    st.dataframe(data)

# Analyze question types with improved aesthetics
st.subheader("Question Type Distribution")
type_counts = data["type"].value_counts()

# Define custom colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#ff6666']

# Create the pie chart
fig1, ax1 = plt.subplots(figsize=(8, 6))

# Exploding the largest slice
explode = [0.1 if x == type_counts.max() else 0 for x in type_counts.values]

# Create pie chart with rotation for labels and percentages
wedges, texts, autotexts = ax1.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%', 
                                   startangle=90, colors=colors, explode=explode, 
                                   textprops={'fontsize': 12, 'fontweight': 'bold', 'color': 'black'})

ax1.set_title("Distribution of Question Types", fontsize=14, fontweight='bold')
ax1.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

# Rotate the labels and percentages
for i, text in enumerate(texts):
    text.set_rotation(45)  # Rotate labels
    text.set_fontsize(12)
    text.set_fontweight('bold')

for i, autotext in enumerate(autotexts):
    autotext.set_rotation(45)  # Rotate percentages
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Display the pie chart in Streamlit
st.pyplot(fig1)

# Analyze marks distribution
st.subheader("Marks Distribution")
fig2, ax2 = plt.subplots()
ax2.hist(data["Marks"], bins=10, color="skyblue", edgecolor="black")
ax2.set_title("Marks Distribution")
ax2.set_xlabel("Marks")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# Filter questions by type
st.subheader("Filter Questions by Type")
selected_type = st.selectbox("Select Question Type:", data["type"].unique())
filtered_data = data[data["type"] == selected_type]
st.write(f"Total questions of type '{selected_type}': {len(filtered_data)}")
st.dataframe(filtered_data)

# Filter questions by marks
st.subheader("Filter Questions by Marks")
selected_marks = st.slider("Select Marks Range:", int(data["Marks"].min()), int(data["Marks"].max()), (2, 5))
filtered_marks_data = data[(data["Marks"] >= selected_marks[0]) & (data["Marks"] <= selected_marks[1])]
st.write(f"Total questions in marks range {selected_marks}: {len(filtered_marks_data)}")
st.dataframe(filtered_marks_data)
