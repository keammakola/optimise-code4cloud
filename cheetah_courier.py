import random
import time

def efficient_deliver(packages, houses):
    """
    EFFICIENT VERSION - O(n) complexity
    This saves significant cloud costs
    """
    houses_set = set(houses)  # O(m) - one-time cost
    return [pack for pack in packages if pack in houses_set]  # O(n)

def run_efficient_demo():
    """Run the efficient delivery demo"""
    print("RUNNING EFFICIENT CODE")
    print("=" * 50)
    
    # Configuration (same as inefficient demo)
    num_houses = 15000
    num_packages = 10000
    
    # Create data    
    houses  = []
    
    for i in range(num_houses):
        houses.append("house_{i}")
    packages = set()
    while len(packages) != num_packages:
        packages.add(f"house_{random.randrange(num_houses)}")
    
    # Run and time the efficient delivery
    start_time = time.perf_counter()
    result = efficient_deliver(packages, houses)
    end_time = time.perf_counter()
    
    duration = end_time - start_time
    cost = duration * 0.00002778  # Same cloud cost rate
    
    print(f"Completed in: {duration:.6f} seconds")
    print(f"Estimated cloud cost: ${cost:.6f}")
    print(f"Packages delivered: {len(result)}/{len(packages)}")
    print(" Efficient code saves money!")
    
    return duration, cost