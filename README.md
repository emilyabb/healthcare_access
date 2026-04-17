# Healthcare Access Intelligence Platform

A Databricks-based data platform that analyzes healthcare provider supply, hospital facilities, and geographic access to identify care gaps and support network planning decisions.

## Overview

This project implements a medallion architecture (Bronze → Silver → Gold) to transform public healthcare data into actionable insights about:
* Provider coverage and density by geography
* Hospital facility access and ratings
* Patient travel burden estimates
* Network adequacy gaps

**Target Users:** Healthcare payers, digital health companies, care navigation teams, and network planning leaders.

- [View Project Charter](docs/PROJECT_CHARTER.md)
- [Architecture Overview](docs/ARCHITECTURE.md)

## Repository Structure
```
healthcare_access/
├── docs/                  # Project documentation
│   ├── PROJECT_CHARTER.md
│   ├── DATA_DICTIONARY.md   # (Coming soon)
│   └── ARCHITECTURE.md      # (Coming soon)
│
├── bronze/               # Raw data ingestion
│   └── ... (raw tables/files)
│
├── silver/               # Cleaned & standardized transformations
│   └── ... (cleaned tables)
│
├── gold/                 # Analytics-ready aggregations
│   └── ... (final models / BI-ready data)
```


## Prerequisites

### Required Access
* **Databricks Workspace** on AWS (Unity Catalog enabled)
* **Catalog Permissions:** `CREATE SCHEMA` on target catalogs (`bronze_dev`, `silver_dev`, `gold_dev`)
* **Serverless Compute:** No manual cluster setup required - runs on serverless

### Tools & Skills
* Basic SQL and Python knowledge
* Familiarity with Databricks notebooks
* (Optional) Power BI Desktop for dashboard development

## Setup Instructions

### 1. Clone Repository to Databricks Workspace

**Option A: Git Integration (Recommended)**
1. Navigate to your Databricks workspace
2. Go to **Repos** → **Add Repo**
3. Enter repository URL: `<your-git-url>/healthcare_access`
4. Click **Create Repo**

**Option B: Manual Upload**
1. Download repository as ZIP
2. Import notebooks into Workspace via **Import** button

### 2. Create Unity Catalog Schemas

Run this SQL in a Databricks SQL notebook or query editor:

```sql
-- Bronze layer (raw data)
CREATE SCHEMA IF NOT EXISTS bronze_dev.census_bureau;
CREATE SCHEMA IF NOT EXISTS bronze_dev.cms;
CREATE SCHEMA IF NOT EXISTS bronze_dev.economic_research_service;
CREATE SCHEMA IF NOT EXISTS bronze_dev.geo;
CREATE SCHEMA IF NOT EXISTS bronze_dev.nppes_npi_registry;
CREATE SCHEMA IF NOT EXISTS bronze_dev.ruca;

-- Silver layer (cleaned data)
CREATE SCHEMA IF NOT EXISTS silver_dev.demographics;
CREATE SCHEMA IF NOT EXISTS silver_dev.healthcare;
CREATE SCHEMA IF NOT EXISTS silver_dev.geo;

-- Gold layer (analytics-ready)
CREATE SCHEMA IF NOT EXISTS gold_dev.healthcare;
CREATE SCHEMA IF NOT EXISTS gold_dev.unified;
```

### 3. Configure Data Sources

Download public datasets and upload to  **Databricks Volumes**  or  **external storage**:


- **County Population Data**
  - Source: US Census Bureau 
  - Target Location: `/Volumes/bronze_dev/census_bureau/census_bureau_raw/co-est2025-pop.xlsx`
- **RUCA or Urban-Rural Classification Reference Data**
  - Source: Economic Research Service RUCA Data Products ([link](https://www-tx.ers.usda.gov/data-products/rural-urban-commuting-area-codes))
  - Target Location: `/Volumes/bronze_dev/ruca/ruca_raw/RUCA-codes-2020-tract.csv`
- **Poverty Estimates by State and County**
  - Source: Economic Research Service County-Level Datasets ([link](https://www.ers.usda.gov/data-products/county-level-data-sets/county-level-data-sets-download-data))
- **Hospital General Information**
  - Source: CMS Hospital Compare ([link](https://data.cms.gov/provider-data/dataset/xubh-q36u))
  - Target Location:  `/Volumes/bronze_dev/cms/cms_raw/Hospital_General_Information.csv`
- **Provider Data** (Optional)
  - Source: NPPES National Provider Identifier Registry ([link](https://download.cms.gov/nppes/NPI_Files.html))
  - Target Location: `/Volumes/bronze_dev/economic_research_service/ers_raw/Poverty2023.csv`

**Tip:**  Use  `dbfs:/`  paths or Unity Catalog Volumes for optimal performance.


###  4. Run Bronze Layer Ingestion

Navigate to `bronze/` and execute ingestion notebooks in order:

1.  01_ingest_hospitals.py  or  .sql
2.  02_ingest_counties.py  or  .sql
3.  (Optional)  03_ingest_providers.py

These create raw Delta tables in `bronze_dev.*` schemas.

### 5. Run Silver Layer Transformations

Navigate to `silver/`  and execute:

1.  01_clean_hospitals.sql  → Creates  silver_dev.healthcare.hospitals
2.  02_clean_counties.sql  → Creates  silver_dev.geo.counties

These apply data quality rules, standardize formats, and enrich data.

### 6. Run Gold Layer Aggregations

Navigate to  notebooks/gold/  and execute:

1.  01_county_hospital_summary.sql  → Creates  gold_dev.healthcare.county_hospital_summary
2.  02_access_metrics.sql  → Calculates provider density and gap indicators


### 7. Define Primary and Foreign Keys, and Validate Data Quality

Add primary and foreign keys:
 - Run `Add Keys.sql`

Run quality checks:


### 8. Connect Power BI (Optional)
Open Power BI Desktop
Get Data → Databricks
Enter workspace URL and connect using personal access token
Select tables from gold_dev.healthcare schema
Build visualizations using pre-aggregated metrics