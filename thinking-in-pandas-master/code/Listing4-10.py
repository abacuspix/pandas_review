import io

import pandas as pd


data = io.StringIO(
"""
student_id, grade
1045,"a"
2391,"b"
8723,"c"
1092,"a'
"""
)

grades = pd.read_csv(data, nrows=3)
print (grades)
