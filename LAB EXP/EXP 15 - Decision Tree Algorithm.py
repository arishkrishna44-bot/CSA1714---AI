
# Decision Tree Algorithm

def decision_tree(weather):
    if weather == "Sunny":
        return "Play"
    elif weather == "Rainy":
        return "Stay Home"
    elif weather == "Cloudy":
        return "Play"
    else:
        return "Invalid Input"

weather = input("Enter weather (Sunny/Rainy/Cloudy): ")

result = decision_tree(weather)

print("Decision:", result)
