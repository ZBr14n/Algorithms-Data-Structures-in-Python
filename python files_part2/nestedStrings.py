"""
{ [ (

-create hash table to find the corresponding right brackets for every left bracket   e.g.   }, ], )
-when theres a right parenth, we look back to check if it is valid. 
"""
def nestedString(s="{[()()]}"):
