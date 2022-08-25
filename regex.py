import re
txt="Rashad k"
x=re.search("^Rashad.*k$",txt)
if x:
    print("Found")
else:
    print("Not Found")
    