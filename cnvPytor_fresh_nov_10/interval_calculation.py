def find_overlapping_intervals(intervals):
    # Sort intervals based on their start times
    intervals.sort(key=lambda x: x[0])

    overlapping_intervals = []
    overlap_sizes = []

    current_interval = intervals[0]
    for interval in intervals[1:]:
        # Check for overlap
        if interval[0] <= current_interval[1]:
            # Calculate overlap size
            overlap_size = min(current_interval[1], interval[1]) - interval[0] + 1

            # Add overlapping interval and its size to the lists
            overlapping_intervals.append((interval[0], current_interval[1]))
            overlap_sizes.append(overlap_size)

            # Update current interval if needed
            if interval[1] > current_interval[1]:
                current_interval = interval
        else:
            # No overlap, update current interval
            current_interval = interval

    return overlapping_intervals, overlap_sizes

# Example usage:
intervals = [(1, 3), (2, 6), (5, 8), (7, 10), (12, 15)]
overlapping_intervals, overlap_sizes = find_overlapping_intervals(intervals)

print("Overlapping Intervals:", overlapping_intervals)
print("Overlap Sizes:", overlap_sizes)
