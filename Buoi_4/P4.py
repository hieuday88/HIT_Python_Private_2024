import random
import numpy as np

def generate_samples(num_samples):
    y = [random.uniform(0, 10) for _ in range(num_samples)]
    y_hat = [random.uniform(0, 10) for _ in range(num_samples)]
    return y, y_hat

def calculate_loss(y, y_hat, loss_name):
    n = len(y)
    if loss_name == "MAE":
        mae = sum(abs(y[i] - y_hat[i]) for i in range(n)) / n
        return mae

    elif loss_name == "MSE":
        mse = sum((y[i] - y_hat[i]) ** 2 for i in range(n)) / n
        return mse

    elif loss_name == "RMSE":
        mse = sum((y[i] - y_hat[i]) ** 2 for i in range(n)) / n
        rmse = np.sqrt(mse)
        return rmse

    elif loss_name == "Huber_Loss":
        delta = 0.5
        huber_loss = sum(
            0.5 * (y[i] - y_hat[i]) ** 2 if abs(y[i] - y_hat[i]) <= delta
            else delta * abs(y[i] - y_hat[i]) - 0.5 * delta for i in range(n)
        ) / n
        return huber_loss

try:
    num_samples = int(input("Input number of samples (positive integer number) which are generated: "))
    if num_samples <= 0:
        print("number of samples must be a positive integer number")
        exit()
except ValueError:
    print("number of samples must be a positive integer number")
    exit()

loss_name = input("Input loss name: ").strip()
valid_losses = ["MAE", "MSE", "RMSE", "Huber_Loss"]
if loss_name not in valid_losses:
    print(f"{loss_name} loss is not supported")
    exit()

y, y_hat = generate_samples(num_samples)
if len(y) != num_samples or len(y_hat) != num_samples:
    print("The number of samples is incorrect")
    exit()

print("target:", y)
print("predict:", y_hat)

loss_value = calculate_loss(y, y_hat, loss_name)
print(f"{loss_name}: {loss_value}")
