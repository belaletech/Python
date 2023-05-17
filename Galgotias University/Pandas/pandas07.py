
"""To create Data frame from list and series
          constrain-nested list
"""

import pandas as pd
list=[[1,2,3],[4,5,6],['ram','shayam','mohandas']]
var=pd.DataFrame(list)
print(var)