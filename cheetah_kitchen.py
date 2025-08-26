
# ============================================================================
# 🟢 ORGANIZED KITCHEN (Efficient Code)  
# ============================================================================

from simulator import KitchenDemo, simulate_ingredient_processing, simulate_storage_trip


def organized_kitchen_demo(num_orders=100):
    """
    🟢 ORGANIZED KITCHEN APPROACH
    
    Like efficient code that:
    - Batches database operations
    - Minimizes resource usage
    - Reuses data efficiently
    """
    demo = KitchenDemo()
    print("🟢 ORGANIZED KITCHEN IS STARTING...")
    print("(This is like efficient code - watch the resource efficiency!)")
    print()
    
    # SMART: Get ALL ingredients at once!
    # (Like batching database queries or API calls)
    print("🧠 Smart chef thinks ahead...")
    print(f"📝 Planning: Need ingredients for {num_orders} pizzas")
    print()
    
    print("🚶 Chef makes ONE trip to storage room...")
    print("📦 Getting ALL ingredients at once:")
    
    # Single batch operation for all ingredients
    all_dough_data, cpu_ops1 = simulate_storage_trip()
    demo.storage_trips += 1
    demo.cpu_operations += cpu_ops1
    
    all_sauce_data, cpu_ops2 = simulate_storage_trip()
    demo.storage_trips += 1
    demo.cpu_operations += cpu_ops2
    
    all_cheese_data, cpu_ops3 = simulate_storage_trip()
    demo.storage_trips += 1
    demo.cpu_operations += cpu_ops3
    
    all_pepperoni_data, cpu_ops4 = simulate_storage_trip()
    demo.storage_trips += 1
    demo.cpu_operations += cpu_ops4
    
    print(f"   • Got enough dough for {num_orders} pizzas")
    print(f"   • Got enough sauce for {num_orders} pizzas") 
    print(f"   • Got enough cheese for {num_orders} pizzas")
    print(f"   • Got enough pepperoni for {num_orders} pizzas")
    
    # Process ALL ingredients at once (batch processing)
    print("🔄 Batch processing all ingredients together...")
    processed_dough, ops1 = simulate_ingredient_processing(all_dough_data)
    processed_sauce, ops2 = simulate_ingredient_processing(all_sauce_data)
    processed_cheese, ops3 = simulate_ingredient_processing(all_cheese_data)
    processed_pepperoni, ops4 = simulate_ingredient_processing(all_pepperoni_data)
    
    demo.cpu_operations += ops1 + ops2 + ops3 + ops4
    
    # Store efficiently - only once per ingredient type
    demo.memory_allocations += 4  # Only 4 storage operations total
    
    demo.total_cost += (demo.storage_trips * demo.cost_per_storage_trip) + \
                       (demo.cpu_operations * demo.cost_per_cpu_op) + \
                       (demo.memory_allocations * demo.cost_per_memory_mb)
    
    print()
    print("🍕 Now making pizzas assembly-line style...")
    print("   (Reusing the same ingredients for all pizzas - no waste!)")
    
    # Now make all pizzas efficiently - just counting, no resource waste
    for order in range(num_orders):
        demo.orders_completed += 1
        
        # Show progress every 25 orders (less frequent - we're faster!)
        if (order + 1) % 25 == 0:
            print(f"   ✅ Completed {order + 1} orders - reusing ingredients!")
    
    print()
    print("🟢 ORGANIZED KITCHEN RESULTS:")
    print(f"   🚶 Storage trips: Only {demo.storage_trips} trips total!")
    print(f"   ⚙️  CPU operations: {demo.cpu_operations:,}")
    print(f"   💾 Memory allocated: {demo.memory_allocations:.1f} MB")
    print(f"   💰 Total cost: ${demo.total_cost:.4f}")
    print("    😊 Chef used resources efficiently!")
    print()
    
    return demo