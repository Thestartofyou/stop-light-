import random
import time

def simulate_traffic(stop_probability=0.2, simulation_duration=24 * 60 * 60):
    stop_count = 0
    start_time = time.time()

    while time.time() - start_time < simulation_duration:
        # Simulate a car approaching the intersection
        if random.random() < stop_probability:
            stop_count += 1
            print("Stop!")

        # Simulate time passing (adjust the sleep duration as needed)
        time.sleep(0.1)

    return stop_count

def main():
    street_corner = "Main St and Elm St"  # Replace with your specific street corner
    print(f"Tracking stop lights at {street_corner}")

    stops = simulate_traffic()

    print(f"\nSimulation finished for {street_corner}")
    print(f"Total stops: {stops}")

if __name__ == "__main__":
    main()
