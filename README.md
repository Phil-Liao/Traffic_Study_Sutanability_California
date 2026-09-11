# Correlating Commuter Modal Share with Traffic Congestion Rates in California

This repository contains the research documentation, data processing scripts, and final analytical report for a quantitative investigation into urban traffic mitigation and commuter behavior across California.

## Project Overview
Urban traffic congestion remains a persistent challenge despite extensive public investments in alternative transportation systems. This project investigates the paradox of chronic urban traffic by analyzing whether providing non-driving commuting options correlates with reduced congestion. 

Specifically, the study addresses the core research question: *To what extent does the modal share of non-driving commute methods (Public Transit, Carpool, Walk, and Bicycle) correlate with the Aggregate Congestion Rate (ACR) across diverse California Caltrans districts?*

## Key Methodological Highlights
* **Geographical Scope:** Evaluates data across all Caltrans districts in California, distinguishing between *Densely Populated Districts (DPD)* and *Not Densely Populated Districts (NDPD)* to account for varied urban dynamics.
* **Statistical Analysis:** Employs both parametric (Pearson Product-Moment Correlation Coefficient) and nonparametric (Spearman's Rank Correlation Coefficient) tests alongside P-values for rigorous hypothesis validation.
* **Data Processing:** Utilizes custom Python scripts with the Pandas library to clean, filter, and aggregate multi-thousand-row datasets from statewide transportation portals.

## Repository Structure
* **`report/`**: Contains the complete written exploration report and documentation.
* **`code/`**: Python scripts used for data cleaning, filtering large-scale CSV/Excel datasets, and performing statistical regression processing.
* **`data/`**: Raw and processed datasets sourced from the California Open Data Portal and Caltrans, covering commuter habits (Transportation to Work) and traffic metrics (Average Transit Speeds by Route and Stop).

## References
ScienceDirect. Public transport. International Encyclopedia of Human Geography, 2009.

California State Government. California Open Data Portal. Caltrans Data Section, available at https://data.ca.gov/organization/caltrans.

Caltrans. Transportation to Work (T2W) Dataset. California Open Data Portal.

Caltrans. Average Transit Speeds by Route (ATSBR) Dataset. California Open Data Portal.

Caltrans. Average Transit Speeds by Stop (ATSBS) Dataset. California Open Data Portal.

---
*This repository is published for archival and informational display purposes.*