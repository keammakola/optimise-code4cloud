import random

class KitchenDemo:
    def __init__(self):
        self.orders_completed = 0
        self.total_cost_zar = 0  
        self.cpu_operations = 0
        self.memory_allocations = 0
        self.storage_trips = 0
        
        self.ZAR_PER_USD = 18.00 
        
        self.cost_per_cpu_op_usd = 0.000000005      
        self.cost_per_memory_mb_usd = 0.00000001    
        self.cost_per_storage_trip_usd = 0.000004   
        
        self.cost_per_cpu_op_zar = self.cost_per_cpu_op_usd * self.ZAR_PER_USD
        self.cost_per_memory_mb_zar = self.cost_per_memory_mb_usd * self.ZAR_PER_USD
        self.cost_per_storage_trip_zar = self.cost_per_storage_trip_usd * self.ZAR_PER_USD
    
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

def chaotic_kitchen_demo(num_orders_to_show):

    demo = KitchenDemo()
    print("CHAOTIC KITCHEN IS STARTING (Costs in ZAR)...")
    print(f"Showing the first {num_orders_to_show} orders at approx. R18.00 / \$1.00.\n")
    
    
    for order in range(num_orders_to_show):
        order_cost_start = demo.total_cost_zar
        
        print(f"🍕 Order #{order + 1}: Starting preparation...")
        
        
        # 1. Fetching Dough
        dough_data, cpu_ops = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(dough_data) / 1000  
        step_cost = demo.cost_per_storage_trip_zar + (cpu_ops * demo.cost_per_cpu_op_zar) + (len(dough_data) / 1000 * demo.cost_per_memory_mb_zar)
        demo.total_cost_zar += step_cost
        print(f"   - 🚶 Fetched Dough (Cost: R{step_cost:.6f})")
        
        # 2. Fetching Sauce
        sauce_data, cpu_ops = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(sauce_data) / 1000
        step_cost = demo.cost_per_storage_trip_zar + (cpu_ops * demo.cost_per_cpu_op_zar) + (len(sauce_data) / 1000 * demo.cost_per_memory_mb_zar)
        demo.total_cost_zar += step_cost
        print(f"   - 🚶 Fetched Sauce (Cost: R{step_cost:.6f})")
        
        # 3. Fetching Cheese
        cheese_data, cpu_ops = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(cheese_data) / 1000
        step_cost = demo.cost_per_storage_trip_zar + (cpu_ops * demo.cost_per_cpu_op_zar) + (len(cheese_data) / 1000 * demo.cost_per_memory_mb_zar)
        demo.total_cost_zar += step_cost
        print(f"   - 🚶 Fetched Cheese (Cost: R{step_cost:.6f})")
        
        # 4. Fetching Pepperoni
        pepperoni_data, cpu_ops = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        step_cost = demo.cost_per_storage_trip_zar + (cpu_ops * demo.cost_per_cpu_op_zar) + (len(pepperoni_data) / 1000 * demo.cost_per_memory_mb_zar)
        demo.total_cost_zar += step_cost
        print(f"   - 🚶 Fetched Pepperoni (Cost: R{step_cost:.6f})")
        
        # 1. Using Dough
        processed_dough, ops = simulate_ingredient_processing(dough_data)
        demo.cpu_operations += ops
        demo.total_cost_zar += (ops * demo.cost_per_cpu_op_zar)
        
        # 2. Using Sauce
        processed_sauce, ops = simulate_ingredient_processing(sauce_data)
        demo.cpu_operations += ops
        demo.total_cost_zar += (ops * demo.cost_per_cpu_op_zar)
        
        # 3. Using Cheese
        processed_cheese, ops = simulate_ingredient_processing(cheese_data)
        demo.cpu_operations += ops
        demo.total_cost_zar += (ops * demo.cost_per_cpu_op_zar)
        
        # 4. Using Pepperoni
        processed_pepperoni, ops = simulate_ingredient_processing(pepperoni_data)
        demo.cpu_operations += ops
        demo.total_cost_zar += (ops * demo.cost_per_cpu_op_zar)
        
        demo.orders_completed += 1
        
        order_total_cost = demo.total_cost_zar - order_cost_start
        print(f"   ✅ **Order #{order + 1} Complete.** Total cost for this order: **R{order_total_cost:.6f}**\n")
        
    
    print("-------------------------------------------------------------")
    print("CHAOTIC KITCHEN SUMMARY (Costs in ZAR):")
    print(f"Total Orders: {demo.orders_completed}")
    print(f"Total Storage Trips: {demo.storage_trips}")
    print(f"💰 Total Estimated Cost: **R{demo.total_cost_zar:.4f}**")
    print("-------------------------------------------------------------")

    return demo

chaotic_kitchen_demo(1000)