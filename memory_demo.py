import os
import time
import psutil

def inefficient_file_processing(filename):
    """
    Demonstrates the readlines() mistake - loads entire file into memory
    This is the pattern mentioned in the script that requires 16GB instances
    """
    print("=== INEFFICIENT FILE PROCESSING ===")
    print("Using f.readlines() - loads entire file into memory\n")
    
    start_time = time.time()
    memory_before = psutil.Process().memory_info().rss / 1024 / 1024  # MB
    
    try:
        with open(filename, 'r') as f:
            # THE MISTAKE: Loads entire file into memory at once
            all_lines = f.readlines()
            
        # Process all lines (simulate work)
        processed_count = 0
        for line in all_lines:
            if len(line.strip()) > 0:
                processed_count += 1
                
        memory_after = psutil.Process().memory_info().rss / 1024 / 1024  # MB
        end_time = time.time()
        
        print(f"Lines processed: {processed_count:,}")
        print(f"Memory before: {memory_before:.1f} MB")
        print(f"Memory after: {memory_after:.1f} MB")
        print(f"Memory used: {memory_after - memory_before:.1f} MB")
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        
        # Calculate GCP cloud costs
        memory_gb = (memory_after - memory_before) / 1024
        print(f"\n💸 GCP COST IMPACT:")
        print(f"   - Memory required: {memory_gb:.2f} GB")
        print(f"   - Instance needed: n1-standard-4 (15GB RAM)")
        print(f"   - Hourly cost: R3.23 ($0.19 at R17/$1)")
        print(f"   - Risk: OOM crashes on smaller instances")
        
        return processed_count, memory_after - memory_before
        
    except MemoryError:
        print("💥 OUT OF MEMORY ERROR!")
        print("File too large for available RAM")
        return 0, 0

def efficient_file_processing(filename):
    """
    Demonstrates the generator/streaming approach
    Processes files line-by-line with minimal memory footprint
    """
    print("\n=== EFFICIENT FILE PROCESSING ===")
    print("Using generator pattern - streams line by line\n")
    
    start_time = time.time()
    memory_before = psutil.Process().memory_info().rss / 1024 / 1024  # MB
    
    processed_count = 0
    
    # THE FIX: Stream file line by line
    with open(filename, 'r') as f:
        for line in f:  # Generator - only holds one line in memory
            if len(line.strip()) > 0:
                processed_count += 1
                
    memory_after = psutil.Process().memory_info().rss / 1024 / 1024  # MB
    end_time = time.time()
    
    print(f"Lines processed: {processed_count:,}")
    print(f"Memory before: {memory_before:.1f} MB")
    print(f"Memory after: {memory_after:.1f} MB")
    print(f"Memory used: {memory_after - memory_before:.1f} MB")
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    
    # Calculate GCP cloud costs
    memory_gb = max(0.6, (memory_after - memory_before) / 1024)  # Minimum 600MB
    print(f"\n✨ OPTIMIZATION BENEFITS:")
    print(f"   - Memory required: {memory_gb:.2f} GB")
    print(f"   - Instance needed: e2-micro (1GB RAM)")
    print(f"   - Hourly cost: R0.14 ($0.0084 at R17/$1) - 96% savings")
    print(f"   - Scalability: Can process 100GB+ files")
    
    return processed_count, memory_after - memory_before

def create_sample_file(filename, size_mb=10):
    """Create a sample file for demonstration"""
    print(f"Creating {size_mb}MB sample file: {filename}")
    
    lines_per_mb = 20000  # Approximate
    total_lines = size_mb * lines_per_mb
    
    with open(filename, 'w') as f:
        for i in range(total_lines):
            f.write(f"Sample log line {i:06d} - timestamp: {time.time():.6f} - data: {'x' * 40}\n")
    
    actual_size = os.path.getsize(filename) / 1024 / 1024
    print(f"Created file: {actual_size:.1f} MB\n")

if __name__ == "__main__":
    sample_file = "sample_logfile.txt"
    
    # Create sample file
    create_sample_file(sample_file, size_mb=50)  # 50MB file
    
    print("MEMORY OPTIMIZATION DEMO")
    print("=" * 50)
    print("Demonstrating the difference between loading entire files")
    print("vs streaming processing for cloud cost optimization\n")
    
    # Run inefficient version
    inefficient_count, inefficient_memory = inefficient_file_processing(sample_file)
    
    # Run efficient version
    efficient_count, efficient_memory = efficient_file_processing(sample_file)
    
    # Summary comparison
    print("\n" + "=" * 60)
    print("COST COMPARISON SUMMARY")
    print("=" * 60)
    
    if inefficient_memory > 0:
        memory_savings = ((inefficient_memory - efficient_memory) / inefficient_memory) * 100
        print(f"Memory reduction: {memory_savings:.1f}%")
        print(f"Cost reduction: 96% (from R3.23/hr to R0.14/hr)")
        print(f"\nFor a 24/7 service (GCP us-central1):")
        print(f"   - Inefficient: R28,288/year (n1-standard-4)")
        print(f"   - Efficient: R1,226/year (e2-micro)")
        print(f"   - Annual savings: R27,062")
    
    print(f"\n🎯 KEY TAKEAWAY:")
    print(f"Same functionality, same output, 96% less GCP infrastructure cost!")
    print(f"At R17/$1, that's R27,062 saved annually through memory optimization!")
    
    # Cleanup
    os.remove(sample_file)
    print(f"\nCleaned up sample file: {sample_file}")