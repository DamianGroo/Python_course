
import pandas as pd;
import numpy as np;

range = 10

dataframe = pd.DataFrame({
    'age': np.random.randint(15, 50, range),
    'weight': np.random.randint(50, 80, range),

})



print(dataframe)

