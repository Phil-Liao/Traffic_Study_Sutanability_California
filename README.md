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

## Acknowledgments & Honorable Mention
* **Dr. Mintu Miah:** Chief Data Scientist at Caltrans, for invaluable guidance regarding data dictionaries, metadata XML structures, and programmatic access methods via ArcGIS endpoints.

## References
* “California’s Population Drain.” Stanford Institute for Economic Policy Research (SIEPR), siepr.stanford edu/publications/policy-brief/californias-population-drain#:~:text=California%20is%20still%20the%20largest,percent%20of%20the%20U.S.%20population. Accessed 20 June 2025.
* “Public Transport.” Public Transport - an Overview | ScienceDirect Topics, www.sciencedirect.com/topics/social-sciences/public-transport. Accessed 23 June 2025.
* Transportation to Work - Dataset - California Open Data - ca.Gov, data.ca.gov/dataset/transportation-to-work. Accessed 11 July 2025.
* “Average Transit Speeds by Route.” California Open GeoPortal, data.ca.gov/dataset/average-transit-speeds-by-route. Accessed 11 July 2025.
* “Average Transit Speeds by Stop.” California Open GeoPortal, data.ca.gov/dataset/average-transit-speeds-by-stop. Accessed 11 July 2025.
* District Map and County Chart, cwwp2.dot.ca.gov/documentation/district-map-county-chart.htm. Accessed 16 July 2025.
* Tu, Anh Trinh, and Thi Phuong Linh Le Le. “Encouraging Public Transport Use to Reduce Traffic Congestion and Air Pollutant: A Case Study of Ho Chi Minh City, Vietnam - Sciencedirect.” Encouraging Public Transport Use to Reduce Traffic Congestion and Air Pollutant: A Case Study of Ho Chi Minh City, Vietnam, 14 Mar. 2016, www.sciencedirect.com/science/article/pii/S187770581600401X.
* California. Vehicle Code, § 21200 (2024).
---
*This repository is published for archival and informational display purposes.*