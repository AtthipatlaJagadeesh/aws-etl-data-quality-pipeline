import boto3, pandas as pd, io, logging, json
from data_quality import run_data_quality_checks
import config

s3 = boto3.client('s3', region_name=config.AWS_REGION)
logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO)

def lambda_handler(event=None, context=None):
    try:
        logging.info("Starting ETL pipeline...")

        # Extract
        obj = s3.get_object(Bucket=config.RAW_BUCKET, Key=config.RAW_FILE)
        df = pd.read_csv(io.BytesIO(obj['Body'].read()))

        # Transform
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df.dropna(subset=['product', 'price'], inplace=True)
        df['total'] = df['quantity'] * df['price']

        # Validate
        dq_report = run_data_quality_checks(df)
        logging.info(f"Data quality report: {dq_report}")

        # Load
        out_buffer = io.StringIO()
        df.to_csv(out_buffer, index=False)
        s3.put_object(Bucket=config.PROCESSED_BUCKET, Key=config.PROCESSED_FILE, Body=out_buffer.getvalue())

        # Save DQ Report
        s3.put_object(Bucket=config.PROCESSED_BUCKET, Key='data_quality_report.json', Body=json.dumps(dq_report, indent=2))

        logging.info("ETL pipeline completed successfully.")
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        raise e

if __name__ == "__main__":
    lambda_handler()
