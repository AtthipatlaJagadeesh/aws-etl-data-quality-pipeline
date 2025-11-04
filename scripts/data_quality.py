def run_data_quality_checks(df):
    report = {}
    report['row_count'] = len(df)
    report['missing_values'] = df.isnull().sum().to_dict()
    report['duplicates'] = df.duplicated().sum()
    report['negative_prices'] = (df['price'] < 0).sum()
    report['schema_columns'] = list(df.columns)
    return report
