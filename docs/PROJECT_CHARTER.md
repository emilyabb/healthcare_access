
# Healthcare Access Intelligence Platform - Project Charter
## Project Overview
Project Name: Healthcare Access Intelligence Platform
Repository: healthcare_access

## Executive Summary
This initiative will deliver a Databricks-based healthcare access intelligence platform that transforms public provider, hospital, and geographic data into actionable insights about care access gaps, provider coverage, and patient travel burden. The platform will serve as a strategic decision-making tool for network planning, expansion prioritization, and care navigation optimization.

## Business Problem
Healthcare organizations lack visibility into the relationship between facility and provider supply and population demand across geographic regions. This information gap results in:

- Extended patient travel times to access care
- Delayed treatment and suboptimal health outcomes
- Lower member satisfaction and increased churn risk
- Network adequacy compliance risks for payers
- Avoidable operational costs from inefficient provider networks
Stakeholders require a trusted, scalable data product that integrates provider, facility, and population datasets to systematically identify underserved areas and guide strategic interventions.

## Objectives
- **Data Integration**: Ingest and harmonize public healthcare provider, hospital, and geographic datasets into a medallion architecture (Bronze/Silver/Gold)
- **Access Metrics**: Calculate standardized metrics for provider density, facility coverage, and estimated travel burden by geography
- **Gap Identification**: Identify underserved regions where supply fails to meet population need
- **Public-Facing Visibility**: Deliver an interactive Power BI dashboard enabling stakeholders to explore access patterns and prioritize interventions
- **Scalability**: Establish a maintainable, production-grade platform that supports ongoing data refresh and expansion

## Scope

### In Scope
- Ingestion of public provider directories, hospital data, and census/geographic datasets
- Implementation of Bronze → Silver → Gold medallion architecture in Databricks
- Data quality validation and transformation logic
- Calculation of access metrics: provider-to-population ratios, facility proximity, travel time estimates
- Power BI dashboard development with geographic visualizations and tooltip capabilities
- Documentation of data lineage, transformation logic, and metric definitions
- Initial deployment to _dev environment with promotion path to production

### Out of Scope
- Real-time alerting or operational workflows
- Integration with proprietary claims or EMR systems (phase 2)
- Predictive modeling or ML-based demand forecasting (future phase)
- Mobile applications or patient-facing interfaces
- Direct integration with provider credentialing systems

## Key Deliverables
1. Bronze Layer: Raw data ingestion pipelines for all source datasets
2. Silver Layer: Cleaned, standardized tables including:
   - silver_dev.healthcare.hospitals
   - silver_dev.healthcare.providers (if applicable)
   - silver_dev.geo.counties
3. Gold Layer: Analytics-ready aggregations including:
   - gold_dev.healthcare.county_hospital_summary
   - Provider density metrics by geography
   - Access gap indicators
4. Power BI Dashboard: Interactive executive dashboard with:
   - Geographic heat maps of access gaps
   - Provider coverage metrics by region
   - Travel burden estimates
   - Trend analysis capabilities
5. Documentation: Data dictionary, metric definitions, architecture diagrams, and operational runbook


## Risks & Assumptions
### Risks:

 - Data source availability or quality issues from public datasets
 - Scope creep from additional metric requests
 - Power BI licensing or connectivity constraints
 - Resource availability conflicts

### Assumptions:
 - Public healthcare datasets are accessible and legally compliant for use
 - Databricks workspace and Unity Catalog are provisioned
 - Power BI infrastructure is available
