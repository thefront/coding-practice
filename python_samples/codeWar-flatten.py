#! /usr/bin/env python
#flatten up to one level only

def flatten(lst):
    result = []
    for thing in lst:
        if hasattr(thing, "__iter__"):
            result.extend(thing)
        else:
            result.append(thing)
    # this will flatten to all levels
    #for el in lst:
    #    if hasattr(el, "__iter__") and not isinstance(el, basestring):
    #        result.extend(flatten(el))
    #    else:
    #        result.append(el)
    return result
"""

#clever
def flatten(lst):
    return sum(([i] if not isinstance(i, list) else i for i in lst), [])
"""
print flatten([]) #, [], "[]")
print flatten([1,2,3])# , [1,2,3], "[1,2,3]")
print flatten([[1,2,3],["a","b","c"],[1,2,3]])
# , [1,2,3,"a","b","c",1,2,3], '[[1,2,3],["a","b","c"],[1,2,3]]')

print flatten([[1,2,3],["a","b","c"],[1,2,3],"a"])
# , [1,2,3,"a","b","c",1,2,3,"a"], '[[1,2,3],["a","b","c"],[1,2,3],"a"]')

print flatten([[3,4,5],[[9,9,9]],["a,b,c"]])
# , [3,4,5,[9,9,9],"a,b,c"], '[[3,4,5],[[9,9,9]],["a,b,c"]]')

print flatten([[[3],[4],[5]],[9],[9],[8],[[1,2,3]]])
# , [[3],[4],[5],9,9,8,[1,2,3]], '[[3,4,5],[[9,9,9]],["a,b,c"]]')
