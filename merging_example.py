import merging

# Instantiate merger class in order to use methods
mf = merging.MergingFactory()

example_intervals = [[25,30], [2,19], [14, 23], [4,8]]
print("The example list is: {}".format(example_intervals))
print("The merged list is: {}".format(mf.merge(example_intervals)))