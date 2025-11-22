import sqlite3
import random
import os

class KitchenDemo:
    def __init__(self):
        self.orders_completed = 0
        self.total_cost_zar = 0  
        self.cpu_operations = 0
        self.memory_allocations = 0
        self.storage_trips = 0
        
        # GCP pricing in ZAR (R17.00 / $1.00 - current 2024 rate)
        self.ZAR_PER_USD = 17.00
        
        # GCP Cloud SQL and Compute costs (realistic)
        self.cost_per_cpu_op_usd = 0.000000008      # Higher for GCP
        self.cost_per_memory_mb_usd = 0.000000015   # GCP memory pricing
        self.cost_per_db_query_usd = 0.000006       # Cloud SQL query cost
        
        self.cost_per_cpu_op_zar = self.cost_per_cpu_op_usd * self.ZAR_PER_USD
        self.cost_per_memory_mb_zar = self.cost_per_memory_mb_usd * self.ZAR_PER_USD
        self.cost_per_db_query_zar = self.cost_per_db_query_usd * self.ZAR_PER_USD
    
    def reset_stats(self):
        self.orders_completed = 0
        self.total_cost_zar = 0
        self.cpu_operations = 0
        self.memory_allocations = 0
        self.storage_trips = 0

DB_PATH = 'chaotic_kitchen.db'

def setup_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE ingredients (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, cost REAL)')
    
    ingredients = []
    for name in ['dough', 'sauce', 'cheese', 'pepperoni']:
        for _ in range(250):
            ingredients.append((name, random.randint(100, 500), random.uniform(1.0, 5.0)))
    
    conn.executemany('INSERT INTO ingredients (name, quantity, cost) VALUES (?, ?, ?)', ingredients)
    conn.commit()
    conn.close()

def fetch_ingredient_data(ingredient_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute('SELECT quantity, cost FROM ingredients WHERE name = ? LIMIT 250', (ingredient_name,))
    data = cursor.fetchall()
    conn.close()
    return data, len(data) + 100 

def process_ingredient_data(ingredient_data):
    processed = [(qty * 2 + random.randint(1, 10), cost * 1.1) for qty, cost in ingredient_data]
    return processed, len(ingredient_data) + 1

def chaotic_kitchen_demo(num_orders_to_show):
    demo = KitchenDemo()
    print("\n" + "="*70)
    print("🍕 DOUGH RE MI - CHAOTIC KITCHEN DEMO 🍕")
    print("="*70)
    print("📊 Demonstrating: N+4 Query Problem (Classic Anti-Pattern)")
    print("🏢 Business Case: Debonairs Pizza SA Daily Operations")
    print("☁️  Cloud Platform: Google Cloud Platform (GCP)")
    print("💰 Currency: South African Rand (ZAR) @ R17.00/$1.00")
    print("="*70)
    
    setup_database()
    print("\n🔧 SETUP COMPLETE:")
    print(f"   ✅ Database initialized: {DB_PATH}")
    print("   ⚠️  Each pizza requires 4 separate database round trips")
    print(f"   🎯 Processing {num_orders_to_show:,} pizzas for demo\n")
    
    # Processing pizzas with N+4 query problem
    
    
    for order in range(num_orders_to_show):
        order_cost_start = demo.total_cost_zar
        
        if order < 5:  # Show first 5 orders for demo
            print(f"🍕 Pizza #{order + 1}: Making 4 separate DB calls...")
        elif (order + 1) % 1000 == 0:  # Progress updates every 1000 pizzas
            print(f"   📈 Progress: {order + 1:,} pizzas completed...")
        
        # 1. Fetching Dough from DB
        dough_data, cpu_ops = fetch_ingredient_data('dough')
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(dough_data) / 1000  
        step_cost = demo.cost_per_db_query_zar + (cpu_ops * demo.cost_per_cpu_op_zar) + (len(dough_data) / 1000 * demo.cost_per_memory_mb_zar)
        demo.total_cost_zar += step_cost
        
        # 2. Fetching Sauce from DB
        sauce_data, cpu_ops = fetch_ingredient_data('sauce')
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(sauce_data) / 1000
        step_cost = demo.cost_per_db_query_zar + (cpu_ops * demo.cost_per_cpu_op_zar) + (len(sauce_data) / 1000 * demo.cost_per_memory_mb_zar)
        demo.total_cost_zar += step_cost
        
        # 3. Fetching Cheese from DB
        cheese_data, cpu_ops = fetch_ingredient_data('cheese')
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        demo.memory_allocations += len(cheese_data) / 1000
        step_cost = demo.cost_per_db_query_zar + (cpu_ops * demo.cost_per_cpu_op_zar) + (len(cheese_data) / 1000 * demo.cost_per_memory_mb_zar)
        demo.total_cost_zar += step_cost
        
        # 4. Fetching Pepperoni from DB
        pepperoni_data, cpu_ops = fetch_ingredient_data('pepperoni')
        demo.storage_trips += 1
        demo.cpu_operations += cpu_ops
        step_cost = demo.cost_per_db_query_zar + (cpu_ops * demo.cost_per_cpu_op_zar) + (len(pepperoni_data) / 1000 * demo.cost_per_memory_mb_zar)
        demo.total_cost_zar += step_cost
        
        # 1. Using Dough
        processed_dough, ops = process_ingredient_data(dough_data)
        demo.cpu_operations += ops
        demo.total_cost_zar += (ops * demo.cost_per_cpu_op_zar)
        
        # 2. Using Sauce
        processed_sauce, ops = process_ingredient_data(sauce_data)
        demo.cpu_operations += ops
        demo.total_cost_zar += (ops * demo.cost_per_cpu_op_zar)
        
        # 3. Using Cheese
        processed_cheese, ops = process_ingredient_data(cheese_data)
        demo.cpu_operations += ops
        demo.total_cost_zar += (ops * demo.cost_per_cpu_op_zar)
        
        # 4. Using Pepperoni
        processed_pepperoni, ops = process_ingredient_data(pepperoni_data)
        demo.cpu_operations += ops
        demo.total_cost_zar += (ops * demo.cost_per_cpu_op_zar)
        
        demo.orders_completed += 1
        
        order_total_cost = demo.total_cost_zar - order_cost_start
        if order < 5:
            print(f"   💸 Cost: R{order_total_cost:.4f} (4 DB queries per pizza)\n")
        elif order == 5:
            print("   ⏳ Processing remaining pizzas (progress updates every 1000)...\n")
        
    
    cost_per_order = demo.total_cost_zar / demo.orders_completed
    
    print("\n" + "="*50)
    print("📊 CHAOTIC KITCHEN RESULTS")
    print("="*50)
    print(f"🍕 Total Pizzas Processed: {demo.orders_completed:,}")
    print(f"🔄 Total DB Queries: {demo.storage_trips:,} (4 per pizza - N+4 Problem)")
    print(f"💰 Cost per Pizza: R{cost_per_order:.4f}")
    print(f"💸 Total Processing Cost: R{demo.total_cost_zar:.2f}")
    
    print(f"\n⚡ GCP PERFORMANCE IMPACT:")
    print(f"   🔴 CPU Utilization: HIGH (excessive I/O blocking)")
    print(f"   🟡 Memory Pressure: MODERATE (repeated allocations)")
    print(f"   🔴 Cloud SQL Load: EXTREME ({demo.storage_trips:,} connections)")
    print(f"   🔴 Scalability: POOR (O(n) database calls)")
    
    print(f"\n🚨 GCP COST DRIVERS:")
    print(f"   💻 Requires n1-standard-4+ instances (R3.23/hour)")
    print(f"   🔌 Cloud SQL connection pool exhaustion")
    print(f"   🌐 Higher VPC network egress costs")
    print(f"   ⏰ Cloud Functions timeout risk (540s limit)")

    return demo

if __name__ == "__main__":
    # Demo with limited volume (chaotic is slow)
    print("Running demo with 15,000 pizzas (scaled to show Debonairs impact)\n")
    demo = chaotic_kitchen_demo(15000)
    
    print("\n" + "="*70)
    print("📈 SCALING ANALYSIS - DEBONAIRS PIZZA SA IMPACT")
    print("="*70)
    
    # Scale to Debonairs volume (80,000 pizzas)
    debonairs_daily = 80_000
    scale_factor = debonairs_daily / demo.orders_completed
    scaled_cost = demo.total_cost_zar * scale_factor
    scaled_queries = demo.storage_trips * scale_factor
    
    print(f"🏢 Debonairs Daily Volume: {debonairs_daily:,} pizzas")
    print(f"🔄 Daily GCP Cloud SQL Queries: {scaled_queries:,.0f}")
    print(f"💰 Daily Cost Impact: R{scaled_cost:,.2f}")
    print(f"📅 Annual Cost Impact: R{scaled_cost * 365:,.2f}")
    
    print(f"\n🔥 KEY INSIGHT:")
    print(f"   Code optimization = Direct cost optimization in South Africa!")
    print(f"   At R17.00/$1.00 exchange rate, every query matters!")
    print("="*70)