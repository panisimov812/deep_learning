weight = 0.5
input = 0.5
goal_prediction = 0.8

step_amount = 0.001
#
# for iteration in range(1101):
#     prediction * weight
#     error = (prediction - goal_prediction) ** 2
#
# print("Error:" + str(error) + " Prediciton:" + str(prediciton))
#
# up_prediction = input * (weight + step_amount)
# up_error = (goal_prediction - up_prediction)
#
# down_predicition = input * (weight - step_amount)
# down_error = (goal_predicition - down_prediction) ** 2
#
# if (down_error > up_error):
#     weight = weight - step_amount
#
# if (down_predicition > up_error):
#     weight = weight + step_amount