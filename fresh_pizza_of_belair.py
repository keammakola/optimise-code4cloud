import random

class KitchenDemo:
    def __init__(self):
        self.orders_completed = 0
        self.total_cost_zar = 0  
        self.cpu_operations = 0
        self.memory_allocations = 0
        self.storage_trips = 0
        
        # Costs converted to ZAR (R18.00 / $1.00)
        self.ZAR_PER_USD = 18.00
        self.cost_per_cpu_op_zar = 0.000000005 * self.ZAR_PER_USD
        self.cost_per_memory_mb_zar = 0.00000001 * self.ZAR_PER_USD
        self.cost_per_storage_trip_zar = 0.000004 * self.ZAR_PER_USD # The primary expense
    
    def reset_stats(self):
        self.orders_completed = 0
        self.total_cost_zar = 0
        self.cpu_operations = 0
        self.memory_allocations = 0
        self.storage_trips = 0

def simulate_storage_trip():
    """Simulate expensive storage access (I/O) with associated CPU overhead."""

    storage_data = [random.randint(1, 1000) for _ in range(1000)]
    return storage_data, 1100 

def simulate_ingredient_processing(ingredient_data):
    """Simulate processing ingredients - more CPU work"""
    processed = []
    for item in ingredient_data:
        result = item * 2 + random.randint(1, 10)
        processed.append(result)

    return processed, len(ingredient_data) + 1
 

def optimised_kitchen_demo(num_orders_to_show):
    """
    Optimised function that minimises storage trips and reuses processed ingredients.
    """
    demo = KitchenDemo()
    print("--- OPTIMISED KITCHEN IS STARTING (Costs in ZAR) ---")
    print("Implementing batching and caching for maximum efficiency.\n")
    
    # --- PHASE 1: BATCHING & PRE PROCESSING (Runs only ONCE) ---
    print("1. Initialising Kitchen (Batching Common Ingredients)...")
    
    common_ingredients_processed = {}
    
    for ingredient_name in ["dough", "sauce", "cheese"]:
        # 1. Fetch from Storage (Once)
        data, cpu_ops_fetch = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops_fetch
        demo.memory_allocations += len(data) / 1000
        
        # 2. Process Ingredient (Once)
        processed_data, cpu_ops_proc = simulate_ingredient_processing(data)
        demo.cpu_operations += cpu_ops_proc
        
        common_ingredients_processed[ingredient_name] = processed_data
        
        # Update cost after batch operations
        step_cost_zar = demo.cost_per_storage_trip_zar + \
                        (cpu_ops_fetch * demo.cost_per_cpu_op_zar) + \
                        (len(data) / 1000 * demo.cost_per_memory_mb_zar) + \
                        (cpu_ops_proc * demo.cost_per_cpu_op_zar)
        demo.total_cost_zar += step_cost_zar
        print(f"   ✅ Fetched & processed **{ingredient_name}** once. Cost: R{step_cost_zar:.6f}")

    # --- PHASE 2: ORDER FULFILMENT (The main efficient loop) ---
    print(f"\n2. Starting Order Fulfilment (Showing first {num_orders_to_show} orders)...")
    
    for order in range(num_orders_to_show):
        order_cost_start = demo.total_cost_zar 
        
        # We only perform the single expensive, non reusable task inside the loop.
        
        # 1. Unique Ingredient Fetch (Pepperoni)
        pepperoni_data, cpu_ops_fetch = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops_fetch
        
        # 2. Unique Ingredient Processing
        processed_pepperoni, cpu_ops_proc = simulate_ingredient_processing(pepperoni_data)
        demo.cpu_operations += cpu_ops_proc
        
        # Calculate cost for this order
        step_cost_zar = demo.cost_per_storage_trip_zar + \
                        (cpu_ops_fetch * demo.cost_per_cpu_op_zar) + \
                        (len(pepperoni_data) / 1000 * demo.cost_per_memory_mb_zar) + \
                        (cpu_ops_proc * demo.cost_per_cpu_op_zar)
        demo.total_cost_zar += step_cost_zar
        
        demo.orders_completed += 1
        
        order_total_cost = demo.total_cost_zar - order_cost_start
        print(f"   🍕 Order #{order + 1} Complete. Only 1 storage trip. Cost: **R{order_total_cost:.6f}**")
        

    
    print("\n-------------------------------------------------------------")
    print("OPTIMISED KITCHEN :")
    print(f"Total Orders: {num_orders_to_show:,}")
    print(f"Total Storage Trips: **{num_orders_to_show:,} trips**")
    print(f"💰 Final Estimated Cost (Scaled): **R{order_total_cost:.4f}**")
    print("-------------------------------------------------------------")

    return demo

optimised_kitchen_demo(1000)