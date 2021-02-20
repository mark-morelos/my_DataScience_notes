import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint

# Import libraries needed:
import requests
from bs4 import BeautifulSoup

def get_business_info(business, city, state):
    '''
    This function  will scrape the yellowpages website and
    will return a list of the information, such as name, phone number,
    street address, city, state, and zip code for those businesses.
    Parameters:
    -----------
      business : type or name of business
      city : name of the city where the business is located
      state : the 2 character abbrivation for the state in which the
        business is located.
    Returns:
    --------
      DataFrame with information scraped from the yellowpages website,
        based on the parameters entered into the function.
    '''

    # Set the url to pull the data from:
    url = f'https://www.yellowpages.com/search?search_terms={business}&geo_location_terms={city}%2C+{state}&s=distance'
    
    # Create a get request:
    response = requests.get(url)
    
    # Check the status code to verify it is 200. This lets you know if there is
    #   an error reaching the website based on the code:
    if response.status_code == 200:
        # Use beautiful soup to parse everything:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Get the data from the location within the webpage:
        information = soup.find_all('div', class_="info")
        data = {'Name': [], 'Phone_No': [], 'Street': [], 'City_State_Zip': []}
        for info in information:
            # Get all the attribrutes we need:
            name = info.find('a', class_="business-name").span
            name = name.text if name else None
            phone = info.find('div', class_='phones phone primary')
            phone = phone.text if phone else None
            street = info.find('div', class_='street-address')
            street = street.text if street else None
            area = info.find('div', class_='locality')
            area = area.text if area else None
            # Store the values in a data object:
            data['Name'].append(name)
            data['Phone_No'].append(phone)
            data['Street'].append(street)
            data['City_State_Zip'].append(area)
    else:
        print('There is an error, the website can not be reached.')
    # Turn data collected into a pandas dataframe:
    business_info = pd.DataFrame(data, columns=['Name', 'Phone_No', 'Street',
                                                'City_State_Zip'])
    
    return business_info

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100


class My_Data_Splitter():
    def __init__(self, df, features, target):
        self.df = df
        self.features = features
        self.target = target
        self.X = df[features]
        self.y = df[target]

def train_validation_test_split(df, features, target,
                                train_size=0.7, val_size=0.1,
                                test_size=0.2, random_state=None,
                                shuffle=True):
    '''
    This function is a utility wrapper around the Scikit-Learn train_test_split that splits arrays or 
    matrices into train, validation, and test subsets.
    Args:
        df (Pandas DataFrame): DataFrame with code.
        X (list): A list of features.
        y (str): A string with target column.
        train_size (float or int): Proportion of the dataset to include in the train split (0 to 1).
        val_size (float or int): Proportion of the dataset to include in the validation split (0 to 1).
        test_size (float or int): Proportion of the dataset to include in the test split (0 to 1).
        random_state (int): Controls the shuffling applied to the data before applying the split for reproducibility.
        shuffle (bool): Whether or not to shuffle the data before splitting
    Returns:
        Train, test, and validation dataframes for features (X) and target (y). 
    '''

    X = df[features]
    y = df[target]

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size / (train_size + val_size),
        random_state=random_state, shuffle=shuffle)

    return X_train, X_val, X_test, y_train, y_val, y_test


if __name__ == '__main__':
    # Simple test for enlarge function
    # print (enlarge(5))

    # Test for train_validation_test_split function
    raw_data = load_wine()
    df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
    df['target'] = raw_data['target']

    X_train, X_val, X_test, y_train, y_val, y_test = train_validation_test_split(df, features=['ash', 'hue'], target='target')

    # breakpoint()


def address_column_split(a):
    """
    Extracts city and state in an address and provides separate columns for each
    """
    asplit = a.split(",")
    city = asplit[0].split()[-1]
    state = asplit[1].split()[0]
    return city, state

if __name__ == '__main__':

    data = pd.DataFrame({
        'Address': ['xxx Antioch, CA',
        'xxx Mobile, AL',
        'xxx Wylie, TX WO-65758',
        'zzz Waxahachie, TX WO-999786']})
    print(data.join(data['Address'].apply(lambda x: pd.Series(address_column_split(x), index=["City", "State"]))))

    # breakpoint()