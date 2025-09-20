import streamlit as st

st.set_page_config(
    page_title="About the project",
    page_icon="ℹ"
)

st.title("Qilu Wang's Preject")
st.divider()

st.markdown("This project aims to develop a comprehensive analytical platform "
"" 
"for processing and analyzing spatial transcriptomics data.  " 
"" 
"Spatial transcriptomics is a revolutionary technology  " 
"" 
"that allows researchers to measure gene expression levels while preserving the spatial structure of tissues. " 
"" 
"" 


"This project employed a variety of bioinformatics and data analysis methods " 
"" 
"Such as Data processing, Spatial Cluster Analysis, Differential Expression Analysis " 
"" 
"Cell Type Deconvolution, and Spatial Pattern Recognition " 
"" 

"Key Findings:  " 
"" 
"Spatial Heterogeneity, Cell Communication, Biomarkers, Microenvironment Compartmentalization  " 
"" 

"Technology Stack " 
"" 
"Python: Use specialized libraries such as Scanpy, Squidpy, and Giotto to process spatial transcriptome data " 
"" 
"R: Use the Seurat and SPATA2 packages for specialized analyses " 
"" 
"Visualization Tools: Matplotlib, Seaborn, Plotly, and Napari for multidimensional data visualization " 
"" 
"Machine Learning: Apply various unsupervised and supervised learning methods to identify patterns in data. " 
""
, unsafe_allow_html=True)

st.divider()
st.caption("About | Spatial Transcriptomics Data Analysis")
