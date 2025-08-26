
# ============================================================================
# 🎬 INTERACTIVE DEMO RUNNER
# ============================================================================

def run_restaurant_demo():
    """
    Run the interactive restaurant demo with REAL resource usage
    Perfect for explaining inefficient code to anyone!
    """
    print("=" * 70)
    print("🍕 WELCOME TO THE RESTAURANT KITCHEN EFFICIENCY DEMO!")
    print("=" * 70)
    print()
    print("Today we're comparing two kitchens making 100 Ultimate Pizzas...")
    print("Each pizza needs: dough, sauce, cheese, pepperoni")
    print()
    print("⚠️  This demo uses REAL CPU and memory - no fake delays!")
    print("Watch your system monitor to see the resource usage!")
    print()
    
    input("Press ENTER to start the CHAOTIC KITCHEN demo... 🔴")
    print()
    
    # Run chaotic kitchen
    chaotic_demo = chaotic_kitchen_demo(num_orders=100)
    
    print("=" * 50)
    print()
    input("Press ENTER to start the ORGANIZED KITCHEN demo... 🟢")
    print()
    
    # Run organized kitchen  
    organized_demo = organized_kitchen_demo(num_orders=100)
    
    # Show comparison
    print("=" * 70)
    print("🏆 FINAL COMPARISON - WHICH KITCHEN WOULD YOU CHOOSE?")
    print("=" * 70)
    print()
    
    cpu_ratio = chaotic_demo.cpu_operations / organized_demo.cpu_operations
    memory_ratio = chaotic_demo.memory_allocations / organized_demo.memory_allocations
    storage_ratio = chaotic_demo.storage_trips / organized_demo.storage_trips
    cost_ratio = chaotic_demo.total_cost / organized_demo.total_cost
    cost_savings = chaotic_demo.total_cost - organized_demo.total_cost
    
    print(f"📊 RESOURCE USAGE COMPARISON:")
    print(f"┌─────────────────────┬─────────────────┬─────────────────┬─────────────────┐")
    print(f"│ Kitchen Type        │ CPU Ops         │ Memory (MB)     │ Storage Trips   │")
    print(f"├─────────────────────┼─────────────────┼─────────────────┼─────────────────┤") 
    print(f"│ 🔴 Chaotic Kitchen  │ {chaotic_demo.cpu_operations:>13,}   │ {chaotic_demo.memory_allocations:>13.1f}     │ {chaotic_demo.storage_trips:>13}     │")
    print(f"│ 🟢 Organized Kitchen│ {organized_demo.cpu_operations:>13,}   │ {organized_demo.memory_allocations:>13.1f}     │ {organized_demo.storage_trips:>13}     │")
    print(f"└─────────────────────┴─────────────────┴─────────────────┴─────────────────┘")
    print()
    
    print(f"🎯 EFFICIENCY GAINS:")
    print(f"   ⚙️  CPU: Chaotic uses {cpu_ratio:.1f}x MORE CPU operations")
    print(f"   💾 Memory: Chaotic uses {memory_ratio:.1f}x MORE memory")
    print(f"   🚶 Storage: Chaotic makes {storage_ratio:.1f}x MORE storage trips")
    print(f"   💰 Cost: Chaotic costs {cost_ratio:.1f}x MORE (${cost_savings:.4f} waste per 100 orders)")
    print()
    
    print(f"📈 REAL WORLD IMPACT:")
    daily_orders = 1000
    monthly_orders = daily_orders * 30
    daily_savings = (cost_savings / 100) * daily_orders
    monthly_savings = daily_savings * 30
    annual_savings = monthly_savings * 12
    
    print(f"   • Daily (1,000 orders): ${daily_savings:.2f} saved")
    print(f"   • Monthly: ${monthly_savings:.2f} saved") 
    print(f"   • Annually: ${annual_savings:.2f} saved")
    print()
    
    print("🔗 CODE ANALOGY:")
    print("   🔴 Chaotic Kitchen = Inefficient Code")
    print("      • Separate database queries in loops (N+1 problem)")
    print("      • Fetching same data repeatedly") 
    print("      • No batching or caching")
    print("      • Excessive CPU and memory waste")
    print()
    print("   🟢 Organized Kitchen = Efficient Code")
    print("      • Batch database queries")
    print("      • Fetch data once, reuse many times")
    print("      • Smart caching and planning")
    print("      • Minimal resource usage")
    print()
    
    if annual_savings > 100:
        print(f"🚨 IN THE CLOUD: This inefficiency could cost ${annual_savings:,.0f} per year!")
    
    print("=" * 70)
    print("🎬 Demo complete! Always organize your kitchen (code)! 🚀")
    print("=" * 70)

# Quick version for presentations
def quick_demo():
    """Shorter version for time-constrained demos"""
    print("🍕 QUICK RESTAURANT DEMO - REAL RESOURCE USAGE")
    print("=" * 50)
    print("Making 20 pizzas with real CPU/memory operations...")
    print()
    
    print("🔴 Chaotic Kitchen (like bad code):")
    chaotic_demo = chaotic_kitchen_demo(num_orders=20)
    
    print("🟢 Organized Kitchen (like good code):")  
    organized_demo = organized_kitchen_demo(num_orders=20)
    
    cpu_ratio = chaotic_demo.cpu_operations / organized_demo.cpu_operations
    cost_ratio = chaotic_demo.total_cost / organized_demo.total_cost
    print(f"🏆 Result: {cpu_ratio:.1f}x less CPU usage, {cost_ratio:.1f}x cheaper!")

if __name__ == "__main__":
    # Run the full interactive demo
    run_restaurant_demo()
    
    # Or run the quick version:
    # quick_demo()