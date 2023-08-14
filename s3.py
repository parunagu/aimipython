import pandas as pd
import numpy as np

data=pd.DataFrame([[10,11,12,13],[10,11,12,13]] ,columns=["maths","science","kannada","pms"])
print(data)


import pandas as pd
import numpy as np

data={"nagu":[18],"paru":[18],"racchu":[18],"acchu":[18] }
df=pd.DataFrame(data)
print(df)


import pandas as pd
import numpy as np

data2={"name":['racchu','acchu' ], "age":[18,18]}
p=pd.DataFrame(data2)
print(p)
