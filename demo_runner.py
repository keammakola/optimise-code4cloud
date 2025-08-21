import time
from turtle_courier import run_inefficient_demo
from cheetah_courier import run_efficient_demo

def main():
    print("CLOUD COST DEMONSTRATION")
    print("=" * 50)
    print("Showing how inefficient code increases cloud bills")
    print("=" * 50)
    
    # Run inefficient demo
    time.sleep(2)  # Pause for dramatic effect
    inefficient_time, inefficient_cost = run_inefficient_demo()
    
    print("COMPARING")
    print("Now let's compare with efficient code...")
    time.sleep(3)
    
    # Run efficient demo
    print("\n2. Running efficient code...")
    efficient_time, efficient_cost = run_efficient_demo()
    
    # Show comparison
    print("\n" +  " RESULTS " )
    print("=" * 50)
    print(f"Inefficient time: {inefficient_time:.4f} seconds")
    print(f"Efficient time:   {efficient_time:.6f} seconds")
    print(f"Speed improvement: {inefficient_time/efficient_time:.1f}x faster!")
    
    print(f"\nInefficient cost: ${inefficient_cost:.6f}")
    print(f"Efficient cost:   ${efficient_cost:.6f}")
    print(f"Cost savings:     {inefficient_cost/efficient_cost:.1f}x cheaper!")
    
    # Calculate projected annual savings
    hourly_savings = (inefficient_cost - efficient_cost) * 3600
    daily_savings = hourly_savings * 24
    annual_savings = daily_savings * 365

    print(f"\n PROJECTED ANNUAL SAVINGS: ${annual_savings:.2f}")
    
    # Explain the difference
    print("\n" +  " KEY INSIGHT " )
    print("Inefficient code: O(n×m) complexity")
    print("  - For each package, check EVERY house")
    print("  - 800 packages × 15,000 houses = 12,000,000 operations!")
    print("\nEfficient code: O(n) complexity") 
    print("  - Convert houses to set once: O(m)")
    print("  - Check each package: O(n)")
    print("  - Total: O(n + m) = 15,800 operations!")
    print("\n Lesson: Efficient algorithms save real money in the cloud!")

if __name__ == "__main__":
    main()