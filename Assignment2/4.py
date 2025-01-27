import numpy as np
import matplotlib.pyplot as plt

file_path = "C:/Users/Administrator/PycharmProjects/pythonProject4/weight-height.csv"  # Update with the full file path if necessary
data = np.genfromtxt(file_path, delimiter=',', skip_header=1)


Height_in_inches = data[:, 0]  # Assuming the first column is Length
Weight_in_pounds = data[:, 1]  # Assuming the second column is Weight


Height_in_cm = Height_in_inches * 2.54  # 1 inch = 2.54 cm
Weight_in_kg = Weight_in_pounds * 0.453592  # 1 pound = 0.453592 kg


mean_Height = np.mean(Height_in_cm)
mean_Weight = np.mean(Weight_in_kg)


print(f"Mean Height (cm): {mean_Height:.2f}")
print(f"Mean Weight (kg): {mean_Weight:.2f}")


plt.figure(figsize=(8, 6))
plt.hist(Height_in_cm, bins=8, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Height (in cm)', fontsize=14)
plt.xlabel('Height (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

