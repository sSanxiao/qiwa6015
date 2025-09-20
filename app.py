import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Spatial Transcriptomics Analysis Platform",
    page_icon="🧬",
    layout="wide"
)

st.title("Spatial Transcriptomics Data Analysis Dashboard")

# Create three-column layout
col1, col2, col3 = st.columns(3)

# First input widget - Gene selection
with col1:
    st.subheader("Gene Selection")
    gene_options = ["TP53", "EGFR", "MYC", "BRCA1", "BRCA2", "ACTB", "GAPDH"]
    selected_gene = st.selectbox(
        "Select a gene for analysis",
        options=gene_options,
        index=0,
        help="Choose a gene from the list for analysis"
    )

# Second input widget - Clustering parameters
with col2:
    st.subheader("Clustering Parameters")
    n_clusters = st.slider(
        "Number of clusters",
        min_value=2,
        max_value=10,
        value=5,
        help="Set the number of clusters for clustering analysis"
    )

# Third input widget - Visualization settings
with col3:
    st.subheader("Visualization Settings")
    color_scheme = st.selectbox(
        "Color scheme",
        options=["viridis", "plasma", "inferno", "magma", "cividis"],
        index=0,
        help="Select the color scheme for visualization"
    )

# Divider
st.divider()

# Data display section
st.header("Gene Expression Data")
st.write("Below is simulated spatial transcriptomics data:")

# Generate simulated spatial transcriptomics data
np.random.seed(42)
n_spots = 100
data = pd.DataFrame({
    'spot_id': range(1, n_spots+1),
    'x_coordinate': np.random.uniform(0, 10, n_spots),
    'y_coordinate': np.random.uniform(0, 10, n_spots),
    'cluster': np.random.randint(1, n_clusters+1, n_spots),
    selected_gene: np.random.lognormal(mean=2, sigma=1.5, size=n_spots)
})

# Show data table
st.dataframe(data.head(10), use_container_width=True)

# Divider
st.divider()

# Charts section
st.header("Spatial Expression Visualization")

# Create two charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Spatial Distribution of Gene Expression")
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    scatter = ax1.scatter(
        data['x_coordinate'], 
        data['y_coordinate'], 
        c=data[selected_gene], 
        cmap=color_scheme,
        s=100,
        alpha=0.7
    )
    ax1.set_xlabel("X Coordinate")
    ax1.set_ylabel("Y Coordinate")
    ax1.set_title(f"Spatial Distribution of {selected_gene} Expression")
    plt.colorbar(scatter, ax=ax1, label="Expression Level")
    st.pyplot(fig1)

with chart_col2:
    st.subheader("Clustering Results Visualization")
    fig2, ax2 = plt.subplots(figsize=(10, 8))
    scatter = ax2.scatter(
        data['x_coordinate'], 
        data['y_coordinate'], 
        c=data['cluster'], 
        cmap='tab10',
        s=100,
        alpha=0.7
    )
    ax2.set_xlabel("X Coordinate")
    ax2.set_ylabel("Y Coordinate")
    ax2.set_title("Spatial Clustering Results")
    legend = ax2.legend(*scatter.legend_elements(), title="Cluster")
    ax2.add_artist(legend)
    st.pyplot(fig2)

# Interactive chart
st.subheader("Interactive Gene Expression Analysis")
fig = px.scatter(
    data, 
    x='x_coordinate', 
    y='y_coordinate', 
    color=selected_gene,
    size=selected_gene,
    hover_data=['spot_id', 'cluster'],
    title=f"Interactive Visualization of {selected_gene} Expression",
    color_continuous_scale=color_scheme
)
st.plotly_chart(fig, use_container_width=True)

# Footer
st.divider()
st.caption("Spatial Transcriptomics Analysis Platform | Built with Streamlit")