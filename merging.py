"""" Implementation of the coding task 2 """

class MergingFactory:
    def merge(self, intervals):
        """
        Merges a list of intervals by calculating overlapping regions.
        :param list intervals: The list of intervals to be merged
        :return The merged intervals
        """
        # Validate input and form of list
        intervals = self._validate_input(intervals)

        # Sort the list of intervals by the first entry
        intervals = self._sort_by_interval_start(intervals)
        merged_intervals = []

        # Building the merged list
        for interval in intervals:
            merged_intervals = merged_intervals or [interval]
            if interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            # Overlap with the current interval, increment the current end position
            else:
                merged_intervals[-1] = [merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1])]
        return merged_intervals

    def _sort_by_interval_start(self, intervals):
        """
        :param: list intervals: List to be sorted
        :return: Sorted list
        """
        # Assumption: It is allowed to use the sorted method
        # Otherwise I would implement a custom element-swapping method here
        intervals = sorted(intervals, key=lambda x: x[0])
        return intervals

    def _validate_input(self, intervals):
        """
        :param intervals: List to be validated according to shape and input
        :return: Unchanged intervals list in case no exceptions occured
        """
        # Validate if the list is numeric
        if not all(map(lambda x: all(map(lambda y: isinstance(y, (int, float)), x)), intervals)):
            raise Exception("This method does only support numeric interval borders but got: {}"
                            .format([type(j) for i in intervals for j in i if not isinstance(j, (int, float))]))

        # Validate if the intervals list contains only 2-tuples
        if any(map(lambda x: len(x) > 2, intervals)):
            raise Exception("The input list does not align with the expected shape of 2-tuples.")

        # Avoid undesired results from wrong user input
        if any(map(lambda x: x[0] > x[1], intervals)):
            raise Exception("Invalid interval format. The first entry needs to be smaller than the second.")

        return intervals