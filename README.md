<p align="center">
  <img src="https://img.shields.io/badge/AWS-Data%20Engineering-orange?style=for-the-badge&logo=amazonaws"/>
  <img src="https://img.shields.io/badge/Python-Automation-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/ETL-Data%20Pipeline-green?style=for-the-badge&logo=apacheairflow"/>
  <img src="https://img.shields.io/badge/Data%20Quality-Validation-brightgreen?style=for-the-badge&logo=pytest"/>
</p>

# AWS ETL Data Pipeline with Data Quality Validation

### Overview
This project demonstrates how to automate an ETL (Extract, Transform, Load) pipeline on AWS using Python and AWS services like S3, Glue, Athena, and Redshift.  
It also integrates **data quality checks** to validate data integrity before loading into the data warehouse.
---

## 🚀 Project Highlights

- Built an automated ETL pipeline using **AWS S3, Glue, and Redshift**.
- Implemented **data quality checks** for missing values, schema validation, and duplicates using **Python (pandas, boto3)**.
- Designed a reusable **ETL framework** with configurable parameters.
- Automated daily pipeline runs using **AWS Lambda + EventBridge**.
- Validated transformation accuracy through **Athena SQL queries**.


### 🧱 Architecture
1. Raw CSV files are uploaded to an S3 bucket.
2. A Python ETL script extracts, transforms, and validates the data.
3. Cleaned data is stored in another S3 bucket.
4. AWS Glue catalogs the processed data.
5. Athena queries validate the transformations.
6. The clean data is finally loaded into Amazon Redshift for analytics.

### 🧰 Tech Stack
- Python (pandas, boto3)
- AWS S3, AWS Glue, Athena, Redshift, Lambda (optional)
- SQL for transformation validation
- Logging & JSON reports for data quality metrics

### ⚙️ Setup Steps
1. Create two S3 buckets:
   - raw-sales-data
   - processed-sales-data
2. Upload `sales_data_sample.csv` to your `raw-sales-data` bucket.
3. Edit `config.py` with your AWS credentials and bucket names.
4. Run the ETL pipeline:
   ```bash
   python scripts/etl_pipeline.py
   ```
5. Validate Output:
   - Clean data in `processed-sales-data/sales_data_clean.csv`
   - Quality report in `processed-sales-data/data_quality_report.json`
6. (Optional) Configure AWS Glue & Athena to query processed data.
7. Load data into Redshift using COPY command.

### 🧪 Data Quality Checks
- Null or missing values  
- Duplicate records  
- Schema validation  
- Negative or invalid numerical values  
- Row count summary

### 📊 Example Report
```json
{
  "row_count": 1000,
  "missing_values": {"product": 0, "price": 2},
  "duplicates": 5,
  "negative_prices": 0,
  "schema_columns": ["sales_id", "product", "quantity", "price", "date", "total"]
}
```

### 🧠 Learning Outcomes
- Hands-on AWS data pipeline experience  
- ETL automation using Python & boto3  
- Data quality validation framework  
- Integration with Glue, Athena, and Redshift  
- Cloud-based data architecture fundamentals

### 👨‍💻 Author
**Jagadeesh Atthipatla**  
MS in Computer Science, University of Texas at Arlington  
Email: jagadeeshatthipatla01@gmail.com
