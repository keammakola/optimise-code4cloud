# Basic van: sequential checks
import time
def gdg_van(city, packages):
    delivered = []
    for pkg in packages:
        for house in city:
            if house == pkg:
                delivered.append(pkg)
                break
    print("GDG vans delivered", len(delivered), "packages!")
    

if __name__ == "__main__":
    city = []
    for i in range(4_000_000):
        city.append(f"house_{i}")
    
        
    packages = []
    for i in range(80000):
        packages.append(f"house_{i % 4_000_000}")
        
    # print(packages)
    
start = time.perf_counter()
gdg_van( city,packages)
end = time.perf_counter()
print("GDG van took", round(end - start, 2), "seconds")
  
  
# account for all delivery vehicles in gauteng - 5000

# also account for all possible addresses in sa -5 400 000   
