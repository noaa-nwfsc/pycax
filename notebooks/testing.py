import pyCAX
import pandas as pd
query = pyCAX.tables.get()
query = query.execute();
query.to_pandas()

args = {}
args['XApiKey']="a"