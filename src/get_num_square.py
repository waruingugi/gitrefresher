import os

num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    except Exception:
        exit('ERROR: the INPUT_NUM provided ("{}") is not an integer'.format(num))

else:
    num = 1

# To set output, print to shell in the following syntax
print(f"::set-ouput name=num_squared::{num ** 2}")