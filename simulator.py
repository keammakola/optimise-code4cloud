"""
RESTAURANT KITCHEN DEMO


Interactive analogy: Bad code is like a chaotic restaurant kitchen!

Scenario: Making 100 orders of "Ultimate Pizza" 
Each pizza needs: dough, sauce, cheese, pepperoni

Watch the difference between a chaotic kitchen vs organised kitchen!
This demo uses REAL resource usage - no fake delays!
"""

import hashlib
import random
import json

class KitchenDemo:
    def __init__(self):
        self.orders_completed = 0
        self.total_cost = 0
        self.cpu_operations = 0
        self.memory_allocations = 0
        self.storage_trips = 0
        
        # Cloud costs (kitchen costs)
        self.cost_per_cpu_op = 0.000001      # Cost per CPU operation
        self.cost_per_memory_mb = 0.00001    # Cost per MB allocated
        self.cost_per_storage_trip = 0.02    # Cost per storage access
    
    def reset_stats(self):
        self.orders_completed = 0
        self.total_cost = 0
        self.cpu_operations = 0
        self.memory_allocations = 0
        self.storage_trips = 0

# Simulate resource-intensive operations
def simulate_storage_trip():
    """Simulate expensive storage access - like a database query"""
    # CPU-intensive: Generate random data and hash it
    data = ''.join([str(random.randint(0, 9)) for _ in range(1000)])
    
    # Multiple hash operations (CPU intensive)
    for i in range(100):
        hash_result = hashlib.md5(f"{data}{i}".encode()).hexdigest()
    
    # Memory allocation (simulate fetching data)
    storage_data = [random.randint(1, 1000) for _ in range(1000)]
    
    return storage_data, 100  # Return data and CPU op count

def simulate_ingredient_processing(ingredient_data):
    """Simulate processing ingredients - more CPU work"""
    # Process the ingredient data (CPU intensive)
    processed = []
    for item in ingredient_data:
        # Simulate complex processing
        result = item * 2 + random.randint(1, 10)
        processed.append(result)
    
    # More hashing (CPU work)
    data_str = json.dumps(processed)
    hash_result = hashlib.sha256(data_str.encode()).hexdigest()
    
    return processed, len(ingredient_data)  # Return processed data and ops count
