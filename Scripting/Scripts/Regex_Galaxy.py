import re

result = re.search(r'(NM_[0-9]{1,9}.[1-2])\1','NM_001243331.1_cds_0_0_chr18_25134033_f' )
print(result.group())