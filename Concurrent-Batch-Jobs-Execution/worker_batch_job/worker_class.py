import pandas as pd
import awswrangler as wr

class WorkerClass:
    
    def __init__(self, 
                 country: str, 
                 column_1: str,
                 column_2: str,
                 column_3: bool,
                 df: pd.DataFrame):
        
        self.country = country
        self.column_1 = column_1
        self.column_2 = column_2
        self.column_3 = column_3
        self.df = df
              
    def processing_code(self) -> pd.DataFrame:
        
        """
        Write your processing code
        
        """
        pass
    
def main(country, column_1, column_2, column_3, df):
    
    # Create an instance of the TechVIO class and call its methods
    WC = WorkerClass(country = country,
                column_1 = column_1,
                column_2 = column_2,
                column_3 = column_3,
                df = df)

    print("TechVIO calculation method called.")
    # call the desired method
    wc_out = WC.processing_code()
    
    print("Saving parquet on S3.")
    wr.s3.to_parquet(df=wc_out, 
                     path=f"s3://path-to-save.parquet", 
                     index=False)
    print(f"{country} saved.")