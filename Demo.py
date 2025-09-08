
# INTERACTIVE DEMO RUNNER

from cheetah_kitchen import organised_kitchen_demo
from turtle_kitchen import chaotic_kitchen_demo


def run_restaurant_demo():
    """
    Run the interactive restaurant demo with REAL resource usage
    Perfect for explaining inefficient code to anyone!
    """
    print("\n")
    print("WELCOME TO THE RESTAURANT KITCHEN EFFICIENCY DEMO!\n")
    print("\nToday we're comparing two kitchens making 1000 Ultimate Pizzas...")
    print("Each pizza needs: dough, sauce, cheese, pepperoni\n")
    print("⚠️  This demo uses REAL CPU and memory, no fake delays")
    print("Watch your system monitor to see the resource usage!\n")
 

    input("Press ENTER to start the CHAOTIC KITCHEN demo... \n")
    
    # Run chaotic kitchen
    chaotic_demo = chaotic_kitchen_demo(500)
    
    print("=" * 50)

    input("Press ENTER to start the organised KITCHEN demo... ")
   
    
    # Run organised kitchen  
    organised_demo = organised_kitchen_demo(500)
    
    # Show comparison
  
    print("\nFINAL COMPARISON - WHICH KITCHEN WOULD YOU CHOOSE?")
 
    
    cpu_ratio = chaotic_demo.cpu_operations / organised_demo.cpu_operations
    memory_ratio = chaotic_demo.memory_allocations / organised_demo.memory_allocations
    storage_ratio = chaotic_demo.storage_trips / organised_demo.storage_trips
    cost_ratio = chaotic_demo.total_cost / organised_demo.total_cost
    cost_savings = chaotic_demo.total_cost - organised_demo.total_cost
    
    print(f"RESOURCE USAGE COMPARISON:")
    print(f"┌─────────────────────┬─────────────────┬─────────────────┬─────────────────┐")
    print(f"│ Kitchen Type        │ CPU Operations  │ Memory (MB)     │ Storage Trips   │")
    print(f"├─────────────────────┼─────────────────┼─────────────────┼─────────────────┤") 
    print(f"│  Chaotic Kitchen  │ {chaotic_demo.cpu_operations:>13,}   │ {chaotic_demo.memory_allocations:>13.1f}     │ {chaotic_demo.storage_trips:>13}     │")
    print(f"│  Organised Kitchen│ {organised_demo.cpu_operations:>13,}   │ {organised_demo.memory_allocations:>13.1f}     │ {organised_demo.storage_trips:>13}     │")
    print(f"└─────────────────────┴─────────────────┴─────────────────┴─────────────────┘")
    print()
    
    print(f"EFFICIENCY GAINS:")
    print(f"   CPU: Chaotic uses {cpu_ratio:.1f}x MORE CPU operations")
    print(f"   Memory: Chaotic uses {memory_ratio:.1f}x MORE memory")
    print(f"   Storage: Chaotic makes {storage_ratio:.1f}x MORE storage trips")
    print(f"   Cost: Chaotic costs {cost_ratio:.1f}x MORE (${cost_savings:.4f} waste per 100 orders)")
    print()
    
    print(f"REAL WORLD IMPACT:")
    daily_orders = 1000
    daily_savings = (cost_savings / 100) * daily_orders
    monthly_savings = daily_savings * 30
    annual_savings = monthly_savings * 12
    
    print(f"   • Daily (1,000 orders): ${daily_savings:.2f} saved")
    print(f"   • Monthly: ${monthly_savings:.2f} saved") 
    print(f"   • Annually: ${annual_savings:.2f} saved")
  
    
    print("\n CODE ANALOGY:")
    print("    Chaotic Kitchen = Inefficient Code")
    print("      • Separate database queries in loops (N+1 problem)")
    print("      • Fetching same data repeatedly") 
    print("      • No batching or caching")
    print("      • Excessive CPU and memory waste\n")
 
    print("    Organised Kitchen = Efficient Code")
    print("      • Batch database queries")
    print("      • Fetch data once, reuse many times")
    print("      • Smart caching and planning")
    print("      • Minimal resource usage\n")
  
    if annual_savings > 100:
        print(f"IN THE CLOUD: This inefficiency could cost ${annual_savings:,.0f} per year!")
    
    print("\n")
    print("Demo complete! Always organise your kitchen (code)!")
    print("\n")

# Quick version for presentations
def quick_demo():
    """Shorter version for time-constrained demos"""
    print("QUICK RESTAURANT DEMO - REAL RESOURCE USAGE\n")
    print("Making 20 pizzas with real CPU/memory operations...")

    
    print("Chaotic Kitchen:")
    chaotic_demo = chaotic_kitchen_demo(500)
    
    print("Organised Kitchen:")  
    organised_demo = organised_kitchen_demo(500)
    
    cpu_ratio = chaotic_demo.cpu_operations / organised_demo.cpu_operations
    cost_ratio = chaotic_demo.total_cost / organised_demo.total_cost
    print(f"Result: {cpu_ratio:.1f}x less CPU usage, {cost_ratio:.1f}x cheaper!")

if __name__ == "__main__":
    # Run the full interactive demo
    run_restaurant_demo()
    
    # Or run the quick version:
    # quick_demo()