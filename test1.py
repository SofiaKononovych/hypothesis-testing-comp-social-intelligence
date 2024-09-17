import numpy as np
import matplotlib.pyplot as plt

# Given data
observers_male = 57
observers_female = 63
number_callers = 60
number_receivers = 60
laughs_male = 0
laughs_female = 0
laughs_caller = 0
laughs_receiver = 0
durations_female = []
durations_male = []
durations_caller = []
durations_receiver = []

# Taking data from laugher-corpus.csv
with open("laughter-corpus.csv", 'r') as file:
    header = file.readline()
    for line in file:
        columns = line.strip().split(',')
        gender = columns[0]
        caller_receiver = columns[1]
        duration = float(columns[2])

        if gender == 'Male':
            laughs_male += 1
            durations_male.append(duration)
        elif gender == 'Female':
            laughs_female += 1
            durations_female.append(duration)

        if caller_receiver == "Receiver":
            laughs_receiver += 1
            durations_receiver.append(duration)
        elif caller_receiver == 'Caller':
            laughs_caller += 1
            durations_caller.append(duration)


def chi_square_male_female():
    # Calculate proportions
    p1 = laughs_male / observers_male
    p2 = laughs_female / observers_female

    # Calculate pooled sample proportion
    pooled_sample = (laughs_male + laughs_female) / (observers_male + observers_female)

    # Calculate expected frequencies
    expected_male = observers_male * pooled_sample
    expected_female = observers_female * pooled_sample

    # Calculate the chi-square test statistic
    chi_square = ((laughs_male - expected_male) ** 2 / expected_male) + ((laughs_female - expected_female) ** 2 / expected_female)

    # Degrees of freedom
    degrees_of_freedom = 1
    #Critical value corresponding to df from chi-square distibution table for alpha = 0,05
    critical_value = 3.841

    print(f"Chi-squared statistic: {chi_square}")
    print(f"Degrees of freedom: {degrees_of_freedom}")
    print(f"Proportions for male / female: {p1} / {p2}")

    if chi_square > critical_value:
        print(
            "Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")




# print(chi_square_male_female())


def chi_square_callers_receivers():
    # Calculate proportions
    p_caller = laughs_caller / number_callers
    p_receiver = laughs_receiver / number_receivers

    # Calculate pooled sample proportion
    pooled_sample = (laughs_caller + laughs_receiver) / (number_callers + number_receivers)

    # Calculate expected frequencies
    expected_callers = number_callers * pooled_sample
    expected_receivers = number_receivers * pooled_sample

    # Calculate the chi-square test statistic
    chi_square = ((laughs_caller - expected_callers) ** 2 / expected_callers) + (
                (laughs_receiver - expected_receivers) ** 2 / expected_receivers)

    # Degrees of freedom
    degrees_of_freedom = 1
    # Critical value corresponding to df from chi-square distibution table for alpha = 0,05
    critical_value = 3.841

    print(f"Chi-squared statistic: {chi_square}")
    print(f"Degrees of freedom: {degrees_of_freedom}")
    print(f"Proportions for caller / receiver: {p_caller} / {p_receiver}")

    # Make a decision
    if chi_square > critical_value:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")

# print(chi_square_callers_receivers())

def students_t_gender():
    male_mean = sum(durations_male) / len(durations_male)
    female_mean = sum(durations_female) / len(durations_female)

    #Calculate the variance of a list
    var_male = sum((x - male_mean) ** 2 for x in durations_male) / (len(durations_male) - 1)
    var_female = sum((x - female_mean) ** 2 for x in durations_female) / (len(durations_female) - 1)

    #Define number of elements in each list
    n_male = len(durations_male)
    n_female = len(durations_female)

    # Calculate the degrees of freedom
    df = n_male + n_female - 2

    #Process of calculating the t-statistic
    sp_squared = (((n_male - 1) * var_male + (n_female - 1) * var_female) / df)

    sum_of_sqrt = ((sp_squared / n_male) + (sp_squared / n_female)) ** 0.5

    t = abs((male_mean - female_mean) / sum_of_sqrt)

    #Find the critical t-value for a two-tailed test with significance level (alpha) = 0.05
    critical_t_value = 1.647   # For alpha = 0.05 and degrees of freedom = 840
    print(t)
    print(f"Degrees of freedom: {df}")
    # Compare the t-statistic to the critical value

    print(f"Average of laugher length for male/female subjects: {male_mean} / {female_mean}")
    print(f"Variance of laughter length for male/female subjects: {var_male} / {var_female}")

    # Make a decision
    if t > critical_t_value:
        print(
            "Reject the null hypothesis.")
    else:
        print(
            "Fail to reject the null hypothesis.")

print(students_t_gender())

def students_t_role():

    caller_mean = sum(durations_caller) / len(durations_caller)
    receiver_mean = sum(durations_receiver) / len(durations_receiver)

    # Calculate the variance of a list
    var_caller = sum((x - caller_mean) ** 2 for x in durations_caller) / (len(durations_caller) - 1)
    var_receiver = sum((x - receiver_mean) ** 2 for x in durations_receiver) / (len(durations_receiver) - 1)

    # Define number of elements in each list
    n1 = len(durations_caller)
    n2 = len(durations_receiver)

    # Calculate the degrees of freedom
    df = n1 + n2 - 2

    # Process of calculating the t-statistic
    sp_squared = (((n1 - 1) * var_caller + (n2 - 1) * var_receiver) / df)

    sum_of_sqrt = ((sp_squared / n1) + (sp_squared / n2)) ** 0.5

    t = abs((caller_mean - receiver_mean) / sum_of_sqrt)

    # Find the critical t-value for a two-tailed test with significance level (alpha) = 0.05
    critical_t_value = 1.647  # For alpha = 0.05 and degrees of freedom = 840

    print(t)
    print(f"Degrees of freedom: {df}")
    # Compare the t-statistic to the critical value
    print(f"Average of laughter length for caller/receiver subjects: {caller_mean} / {receiver_mean}")
    print(f"Variance of laughter length for caller/receiver subjects: {var_caller} / {var_receiver}")

    # Make a decision
    if t > critical_t_value:
        print(
            "Reject the null hypothesis.")
    else:
        print(
            "Fail to reject the null hypothesis.")

# print(students_t_role())
