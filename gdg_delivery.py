# Basic van: sequential checks
import time
def gdg_van(city, packages):
    delivered = []
    for pkg in packages:
        for house in city:
            if house == pkg:
                delivered.append(pkg)
                break
    print("GDG van delivered", len(delivered), "packages!")
    

if __name__ == "__main__":
    city = []
    for i in range(1_800_000):
        city.append(f"house_{i}")
    
        
    packages = []
    for i in range(50000):
        packages.append(f"house_{i % 100000}")
        
    # print(packages)
    
start = time.perf_counter()
gdg_van( city,packages)
end = time.perf_counter()
print("GDG van took", round(end - start, 2), "seconds")
        
