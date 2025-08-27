from simulator import KitchenDemo, simulate_ingredient_processing, simulate_storage_trip
 

# ============================================================================
# CHAOTIC KITCHEN (Inefficient Code)
# ============================================================================

def chaotic_kitchen_demo(num_orders):
    """
    CHAOTIC KITCHEN APPROACH
    
    Like inefficient code that:
    - Makes separate database calls in loops
    - Doesn't batch operations
    - Wastes CPU and memory resources
    """
    demo = KitchenDemo()
    print("CHAOTIC KITCHEN IS STARTING...")
    print("(This is like inefficient code - watch the resource waste!)\n")
    
    all_ingredients = []
    
    for order in range(num_orders):
        print(f"📋Order #{order + 1}: Making Ultimate Pizza...")
        
        # BAD: Go to storage for EACH ingredient separately
        # (Like making separate database queries for each piece of data)
        
        print("   🚶 Chef goes to storage for dough...")
        dough_data, cpu_ops = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(dough_data) / 1000  
        demo.total_cost += demo.cost_per_storage_trip + (cpu_ops * demo.cost_per_cpu_op)
        
        print("   🚶 Chef goes to storage AGAIN for sauce...")
        sauce_data, cpu_ops = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(sauce_data) / 1000
        demo.total_cost += demo.cost_per_storage_trip + (cpu_ops * demo.cost_per_cpu_op)
        
        print("   🚶 Chef goes to storage AGAIN for cheese...")
        cheese_data, cpu_ops = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(cheese_data) / 1000
        demo.total_cost += demo.cost_per_storage_trip + (cpu_ops * demo.cost_per_cpu_op)
        
        print("   🚶 Chef goes to storage AGAIN for pepperoni...")
        pepperoni_data, cpu_ops = simulate_storage_trip()
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(pepperoni_data) / 1000
        demo.total_cost += demo.cost_per_storage_trip + (cpu_ops * demo.cost_per_cpu_op)
        
        # Process each ingredient separately (more CPU waste)
        print("   🍕 Processing ingredients one by one...")
        processed_dough, ops = simulate_ingredient_processing(dough_data)
        demo.cpu_operations += ops
        
        processed_sauce, ops = simulate_ingredient_processing(sauce_data)
        demo.cpu_operations += ops
        
        processed_cheese, ops = simulate_ingredient_processing(cheese_data)
        demo.cpu_operations += ops
        
        processed_pepperoni, ops = simulate_ingredient_processing(pepperoni_data)
        demo.cpu_operations += ops
        
        # Store ingredients (memory waste - storing duplicates)
        all_ingredients.extend([processed_dough, processed_sauce, processed_cheese, processed_pepperoni])
        demo.memory_allocations += 4  # 4 separate storage operations
        
        demo.orders_completed += 1
        
        # Show progress every 10 orders
        if (order + 1) % 10 == 0:
            print(f"   Completed {order + 1} orders so far...")
            print(f"   Memory used: {demo.memory_allocations:.1f} MB")
            print(f"   CPU operations: {demo.cpu_operations:,}\n")
    
    
    print("CHAOTIC KITCHEN RESULTS:")
    print(f"   Storage trips: {demo.storage_trips} trips!")
    print(f"   CPU operations: {demo.cpu_operations:,}")
    print(f"   Memory allocated: {demo.memory_allocations:.1f} MB")
    print(f"   Total cost: ${demo.total_cost:.2f}")
    print("    Chef wasted so many resources!\n")

    
    return demo

