# Lambdata-mark
A collection of data science utility functions.

## Installation

```
pip install -i https://test.pypi.org/simple/ Lambdata-mark==0.0.2
```

## Usage

```
from my_lambdata.ds_utilities import enlarge

print(enlarge(5))
```

```
from my_lambdata.ds_utilities import address_column_split
data = pd.DataFrame({
    'Address': ['xxx Antioch, CA',
                    'xxx Mobile, AL',
                    'xxx Wylie, TX WO-65758',
                    'zzz Waxahachie, TX WO-999786']})
print(data.join(data['Address'].apply(lambda x: pd.Series(
    address_column_split(x), index=["City", "State"]))))
```

```
from my_lambdata.ds_utilities import train_validation_test_split
raw_data = load_wine()
df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
df['target'] = raw_data['target']

X_train, X_val, X_test, y_train, y_val, y_test = train_validation_test_split(
    df, features=['ash', 'hue'], target='target')
```
