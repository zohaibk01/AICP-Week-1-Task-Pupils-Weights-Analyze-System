class WeightTracker:
    def __init__(self):
        self.num_pupils = 30
        self.names = []
        self.weights_first_day = []
        self.weights_last_day = []
        self.weight_difference = []

    def validate_weight(self, weight):
        try:
            weight = float(weight)
            if weight <= 0 or weight > 300:  # Arbitrary weight limits
                return False
            return True
        except ValueError:
            return False

    def input_weights_and_names(self):
        print("Enter the weights of pupils (in kilograms) and their names:")
        for i in range(self.num_pupils):
            name = input(f"Enter name of pupil {i + 1}: ")
            weight_valid = False
            while not weight_valid:
                weight = input(f"Enter weight of {name}: ")
                if self.validate_weight(weight):
                    weight_valid = True
                    self.names.append(name)
                    self.weights_first_day.append(float(weight))
                else:
                    print("Invalid weight! Please enter a valid weight.")

    def calculate_weight_difference(self):
        for i in range(self.num_pupils):
            difference = self.weights_last_day[i] - self.weights_first_day[i]
            self.weight_difference.append(difference)

    def output_pupil_details(self):
        print("\nPupil details:")
        for i in range(self.num_pupils):
            print(f"Name: {self.names[i]}, "
                  f"First Day Weight: {self.weights_first_day[i]} kg, "
                  f"Last Day Weight: {self.weights_last_day[i]} kg, "
                  f"Weight Difference: {self.weight_difference[i]} kg")

    def output_weight_changes(self):
        print("\nWeight Changes:")
        for i in range(self.num_pupils):
            if abs(self.weight_difference[i]) > 2.5:
                change_type = "rise" if self.weight_difference[i] > 0 else "fall"
                print(f"{self.names[i]} has a {change_type} in weight "
                      f"by {abs(self.weight_difference[i])} kg.")


def main():
    tracker = WeightTracker()
    tracker.input_weights_and_names()

    # Simulate last day weights
    print("\nEnter the weights of pupils on the last day:")
    for i in range(tracker.num_pupils):
        weight_valid = False
        while not weight_valid:
            weight = input(f"Enter weight of {tracker.names[i]} on last day: ")
            if tracker.validate_weight(weight):
                weight_valid = True
                tracker.weights_last_day.append(float(weight))
            else:
                print("Invalid weight! Please enter a valid weight.")

    tracker.calculate_weight_difference()
    tracker.output_pupil_details()
    tracker.output_weight_changes()


if __name__ == "__main__":
    main()
