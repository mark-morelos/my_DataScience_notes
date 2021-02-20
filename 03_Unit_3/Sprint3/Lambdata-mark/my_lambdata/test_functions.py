from my_lambdata.ds_utilities import address_column_split
from my_lambdata.ds_utilities import train_validation_test_split
from my_lambdata.ds_utilities import enlarge
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint

print(enlarge(5))

raw_data = load_wine()
df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
df['target'] = raw_data['target']

X_train, X_val, X_test, y_train, y_val, y_test = train_validation_test_split(
    df, features=['ash', 'hue'], target='target')

data = pd.DataFrame({
    'Address': ['xxx Antioch, CA',
                    'xxx Mobile, AL',
                    'xxx Wylie, TX WO-65758',
                    'zzz Waxahachie, TX WO-999786']})
print(data.join(data['Address'].apply(lambda x: pd.Series(
    address_column_split(x), index=["City", "State"]))))
