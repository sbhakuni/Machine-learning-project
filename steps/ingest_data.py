import logging

import pandas as pd
from zenml import step

class IngestData:
    def __init__(self, data_path:str):
        self.data_path = data_path
    
    def get_data(self):
        logging.info(f"Ingesting data from {self.data_path}"
                     )
        return pd.read_csv(self.data_path)
    
@step
def ingest_df(data_path:str) -> pd.DataFrame:
    """
    Ingesting the data from data_path

    Args:
        data_path:paht to the data

    Returns:
        pd.DataFrame: the ingested data
    """
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error whiile ingesting the data: {e}")
        raise e
