import random
from colorama import Fore, Style, init

class KitchenDemo:
    def __init__(self):
        self.orders_completed = 0
        self.total_cost_zar = 0  
        self.cpu_operations = 0
        self.memory_allocations = 0
        self.storage_trips = 0
        
        # Exchange rate
        self.ZAR_PER_USD = 18.0
        
        # Cost constants in USD
        self.cost_per_cpu_op_usd = 0.000000005      # Cost per CPU operation
        self.cost_per_memory_mb_usd = 0.00000001    # Cost per MB of memory
        self.cost_per_storage_trip_usd = 0.000004   # Cost per storage access
        
        # Convert costs to ZAR
        self.cost_per_cpu_op_zar = self.cost_per_cpu_op_usd * self.ZAR_PER_USD
        self.cost_per_memory_mb_zar = self.cost_per_memory_mb_usd * self.ZAR_PER_USD
        self.cost_per_storage_trip_zar = self.cost_per_storage_trip_usd * self.ZAR_PER_USD
    
    def reset_stats(self):
        """Reset all counters and costs"""
        self.orders_completed = 0
        self.total_cost_zar = 0
        self.cpu_operations = 0
        self.memory_allocations = 0
        self.storage_trips = 0

def simulate_storage_trip():
    """🗄️ Simulate expensive storage access (I/O) with associated CPU overhead."""    
    storage_data = [random.randint(1, 1000) for _ in range(1000)]
    return storage_data, 1100 

def simulate_ingredient_processing(ingredient_data):
    """👨‍🍳 Simulate processing ingredients - more CPU work"""
    processed = []
    for item in ingredient_data:
        result = item * 2 + random.randint(1, 10)
        processed.append(result)
    return processed, len(ingredient_data) + 1

def chaotic_kitchen_demo(num_orders_to_show):
    """🏪 Main kitchen simulation demo"""

    init()
    
    demo = KitchenDemo()
    print(f"\n{Fore.YELLOW}🎉 CHAOTIC KITCHEN IS STARTING (Costs in ZAR)... 🎉{Style.RESET_ALL}")
    print(f"{Fore.CYAN}📋 Showing the first {num_orders_to_show} orders at approx. R18.00 / $1.00.{Style.RESET_ALL}\n")
    
    for order in range(num_orders_to_show):
        order_cost_start = demo.total_cost_zar
        print(f"\n{Fore.GREEN}🍕 Order #{order + 1}: Starting preparation...{Style.RESET_ALL}")
        
        # 1. Fetching Ingredients 
        ingredients = [
            ("Dough", "🥖", Fore.YELLOW), 
            ("Sauce", "🥫", Fore.RED),
            ("Cheese", "🧀", Fore.YELLOW),
            ("Pepperoni", "🥓", Fore.MAGENTA)
        ]
        
        for ingredient, emoji, color in ingredients:
            data, cpu_ops = simulate_storage_trip()
            demo.storage_trips += 1
            demo.cpu_operations += cpu_ops
            demo.memory_allocations += len(data) / 1000
            step_cost = (demo.cost_per_storage_trip_zar + 
                        (cpu_ops * demo.cost_per_cpu_op_zar) + 
                        (len(data) / 1000 * demo.cost_per_memory_mb_zar))
            demo.total_cost_zar += step_cost
            print(f"   {color}- {emoji} Fetched {ingredient} (Cost: R{step_cost:.6f}){Style.RESET_ALL}")
            
            # Process ingredient
            processed, ops = simulate_ingredient_processing(data)
            demo.cpu_operations += ops
            demo.total_cost_zar += (ops * demo.cost_per_cpu_op_zar)
        
        demo.orders_completed += 1
        order_total_cost = demo.total_cost_zar - order_cost_start
        print(f"\n   {Fore.CYAN}✨ Order #{order + 1} Complete! Total cost: R{order_total_cost:.6f} ✨{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}🎯 Dough Re Mi SUMMARY 🎯{Style.RESET_ALL}")
    print(f"{Fore.CYAN}📊 Total Orders Completed: {demo.orders_completed}")
    print(f"🚶 Total Storage Trips: {demo.storage_trips}")
    print(f"💰 Total Estimated Cost: R{demo.total_cost_zar:.2f}{Style.RESET_ALL}")
    
    print(f"To run this code 8 times a day for the whole year, it would cost the company R{(demo.total_cost_zar *8 * 365):.0f}!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 60}{Style.RESET_ALL}\n")

    return demo


chaotic_kitchen_demo(5000)
