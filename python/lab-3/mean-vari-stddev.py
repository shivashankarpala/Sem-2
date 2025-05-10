#Calculate the mean of a list of numbers
def mean(data_list):
    return sum(data_list) / len(data_list)

#Calculate the variance of a list of numbers
def variance(data_list):
    mean_value = mean(data_list)
    sumsq = 0
    for x in data_list:
        sumsq += (x - mean_value) ** 2
    return sumsq / len(data_list)

#Calculate the standard deviation of a list of numbers
def stddev(data_list):
    return variance(data_list) ** 0.5

# Example usage
data = [10, 20, 30, 40, 50]

mean_value = mean(data)  
variance_value = variance(data)
stddev_value = stddev(data)

print("Mean:", mean_value)
print("Variance:", variance_value)
print("Standard Deviation:", stddev_value)

# Expected Output:
# Mean: 30.0
# Variance: 200.0
# Standard Deviation: 14.14