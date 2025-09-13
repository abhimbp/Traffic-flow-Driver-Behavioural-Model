import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# STEP 1: Synthetic Traffic Dataset (arrivals per minute for 60 minutes)
# -------------------------
arrivals = np.array([
    5, 6, 8, 7, 9, 7, 6, 8, 10, 9,
    12, 11, 10, 9, 8, 7, 6, 7, 8, 9,
    10, 11, 12, 13, 12, 11, 10, 9, 8, 7,
    6, 7, 8, 9, 10, 11, 10, 9, 8, 7,
    6, 5, 7, 8, 9, 10, 11, 12, 11, 10,
    9, 8, 7, 6, 7, 8, 9, 10, 9, 8
])

# Average vehicles per minute (λ)
lambda_rate = np.mean(arrivals)
print("Average vehicles/minute (λ):", round(lambda_rate, 2))

# Plot arrivals per minute
plt.figure(figsize=(10,4))
plt.plot(range(1,61), arrivals, marker='o', label="Vehicles per minute")
plt.axhline(y=lambda_rate, color='r', linestyle='--', label=f"Mean λ={lambda_rate:.2f}")
plt.xlabel("Minute")
plt.ylabel("Number of Vehicles")
plt.title("Observed Vehicle Arrivals at Intersection (60 min)")
plt.legend()
plt.show()


# -------------------------
# STEP 2: Queueing Model (M/M/1 Queue at Traffic Signal)
# -------------------------
# Assume service rate μ = 10 vehicles/minute
mu = 10

if lambda_rate < mu:
    rho = lambda_rate / mu   # traffic intensity
    Lq = (rho**2) / (1-rho)  # average length of queue
    Wq = Lq / lambda_rate    # average waiting time (in minutes)

    print("\nQueue analysis at signal:")
    print(f"- Arrival rate λ: {lambda_rate:.2f} vehicles/min")
    print(f"- Service rate μ: {mu} vehicles/min")
    print(f"- Utilization (ρ): {rho:.2f}")
    print(f"- Avg. queue length: {Lq:.2f} vehicles")
    print(f"- Avg. waiting time per vehicle: {Wq*60:.2f} seconds")
else:
    print("\nSystem unstable: λ >= μ (Traffic jam occurs!)")


# -------------------------
# STEP 3: Fundamental Traffic Flow Model (Greenshields)
# -------------------------
density = np.linspace(0, 200, 50)   # density: vehicles/km
v_free = 60                         # free flow speed (km/h)
jam_density = 180                   # jam density (veh/km)

# Greenshields Model: Speed-Density relationship
speed = v_free * (1 - density/jam_density)

# Flow = Density × Speed
flow = density * speed

# Plot Speed-Density & Flow-Density curves
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(density, speed, 'b-', lw=2)
plt.xlabel("Density (veh/km)")
plt.ylabel("Speed (km/h)")
plt.title("Speed vs Density (Greenshields Model)")

plt.subplot(1,2,2)
plt.plot(density, flow, 'g-', lw=2)
plt.xlabel("Density (veh/km)")
plt.ylabel("Flow (veh/hour)")
plt.title("Flow vs Density (Fundamental Diagram)")

plt.tight_layout()
plt.show()