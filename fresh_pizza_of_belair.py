import random
from colorama import Fore, Style, init

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
    init() # Initialize colorama
    demo = KitchenDemo()
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.WHITE}🏪 OPTIMISED KITCHEN SIMULATOR {Fore.YELLOW}(Costs in ZAR)")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}Implementing batching and caching for maximum efficiency...{Style.RESET_ALL}\n")
    
    # --- PHASE 1: BATCHING & PRE PROCESSING ---
    print(f"{Fore.YELLOW}📦 PHASE 1: Initializing Kitchen (Batching Common Ingredients)...{Style.RESET_ALL}")
    
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
        
        step_cost_zar = demo.cost_per_storage_trip_zar + \
                        (cpu_ops_fetch * demo.cost_per_cpu_op_zar) + \
                        (len(data) / 1000 * demo.cost_per_memory_mb_zar) + \
                        (cpu_ops_proc * demo.cost_per_cpu_op_zar)
        demo.total_cost_zar += step_cost_zar
        print(f"{Fore.GREEN}   ✅ Processed {Fore.CYAN}{ingredient_name:>6}{Fore.GREEN} | Cost: {Fore.YELLOW}R{step_cost_zar:.6f}{Style.RESET_ALL}")

    # --- PHASE 2: ORDER FULFILMENT ---
    print(f"\n{Fore.YELLOW}🔄 PHASE 2: Order Fulfillment (Processing {num_orders_to_show:,} orders)...{Style.RESET_ALL}")
    
    for order in range(num_orders_to_show):
        order_cost_start = demo.total_cost_zar 
        
        # 1. Unique Ingredient Fetch (Pepperoni)
        pepperoni_data, cpu_ops_fetch = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops_fetch
        
        # 2. Unique Ingredient Processing
        processed_pepperoni, cpu_ops_proc = simulate_ingredient_processing(pepperoni_data)
        demo.cpu_operations += cpu_ops_proc
        
        step_cost_zar = demo.cost_per_storage_trip_zar + \
                        (cpu_ops_fetch * demo.cost_per_cpu_op_zar) + \
                        (len(pepperoni_data) / 1000 * demo.cost_per_memory_mb_zar) + \
                        (cpu_ops_proc * demo.cost_per_cpu_op_zar)
        demo.total_cost_zar += step_cost_zar
        
        demo.orders_completed += 1
        
        order_total_cost = demo.total_cost_zar - order_cost_start
    print(f"{Fore.BLUE}All {num_orders_to_show} are processed!{Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.WHITE}📊 FINAL STATISTICS:")
    print(f"{Fore.CYAN}{'='*60}")
    print(f"{Fore.GREEN}📦 Total Orders Completed: {Fore.WHITE}{num_orders_to_show:,}")
    print(f"{Fore.GREEN}💾 Total Storage Trips:    {Fore.WHITE}{demo.storage_trips:,}")
    print(f"{Fore.GREEN}💰 Final Cost:             {Fore.YELLOW}R{demo.total_cost_zar:.4f}")
    print(f"To run this code 8 times a day for the whole year, it would cost the company R{(demo.total_cost_zar * 8 * 365):.0f}!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")

    return demo

optimised_kitchen_demo(5000)
