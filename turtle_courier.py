import random
import time

def inefficient_deliver(packages, houses):
    """
    INEFFICIENT VERSION - O(n*m) complexity
    This will rack up huge cloud bills!
    """
    delivered = []
    for pack in packages:  # O(n)
        for house in houses:  # O(m) - nested loop = disaster!
            if pack == house:
                delivered.append(pack)
                break
    return delivered

def run_inefficient_demo():
    """Run the inefficient delivery demo"""
    print("RUNNING CODE ")
    print("=" * 50)
    
    # Configuration
    num_houses = 15000  # Reduced for demo purposes
    num_packages = 10000
    
    # Create data
    houses = []
    for i in range(num_houses):
        houses.append("house_{i}")
    packages = set()
    while len(packages) != num_packages:
        packages.add(f"house_{random.randrange(num_houses)}")
    
    # Run and time the inefficient delivery
    start_time = time.perf_counter()
    result = inefficient_deliver(packages, houses)
    end_time = time.perf_counter()
    
    duration = end_time - start_time
    cost = duration * 0.00002778  # Assuming $0.10/hour cloud cost
    
    print(f"Completed in: {duration:.4f} seconds")
    print(f"Estimated cloud cost: ${cost:.6f}")
    print(f"Packages delivered: {len(result)}/{len(packages)}")
    print("WARNING: This code would rack up huge cloud bills!")
    
    return duration, cost