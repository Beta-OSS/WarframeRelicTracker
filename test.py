import time

for i in range(1, 101):
    print(f"\rProgress: {i}%", end="")
    time.sleep(0.1)

print("\nDone!")