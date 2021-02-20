from my_lambdata.ds_utilities import enlarge, get_business_info

def test_enlarge():
    assert enlarge(3) == 300

def test_business_info(self):
        test_df = get_business_info('fast_food', 'miami', 'FL')
        self.assertGreaterEqual(len(test_df.iloc[0]['Phone_No']), 10)