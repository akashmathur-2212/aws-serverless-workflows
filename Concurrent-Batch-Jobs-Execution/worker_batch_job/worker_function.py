import os
import awswrangler as wr
import pandas as pd
from worker_class import main
   
if __name__ == "__main__":
    
    # Access job parameters from environment variables
    country = str(os.environ.get('country'))
    column_1 = int(os.environ.get('column_1'))
    column_2 = int(os.environ.get('column_2'))
    column_3 = bool(os.environ.get('column_3'))
    
    # read file for specific country
    print(f"Running {country}")
    df = wr.s3.read_parquet(path=f"s3://path-to-country-file/")
    
    main(country=country, 
         column_1=column_1, 
         column_2=column_2, 
         column_3=column_3,
         df=df)
    
    print(f"{country} Completed.")