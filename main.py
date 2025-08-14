import time

# Basic van: sequential checks
def basic_van(city, packages):
    delivered = []
    for pkg in packages:
        for house in city:
            if house == pkg:
                delivered.append(pkg)
                break
    print("Basic van delivered", len(delivered), "packages!")

# Smart van: pre-mapped lookup
def smart_van(city, packages):
    house_map = {}
    for house in city:
        house_map[house] = True

    delivered = []
    for pkg in packages:
        if pkg in house_map:
            delivered.append(pkg)
    print("Smart van delivered", len(delivered), "packages!")

if __name__ == "__main__":
    city = []
    for i in range(100_000):
        city.append("house_" + str(i))

    packages = []
    for i in range(50_000):
        packages.append("house_" + str(i % 100_000))

    print("--- Mr K Delivery Demo ---")

    start = time.perf_counter()
    # basic_van(city, packages)
    end = time.perf_counter()
    print("Basic van took", round(end - start, 2), "seconds → moderate cost")

    start = time.perf_counter()
    smart_van(city, packages)
    end = time.perf_counter()
    print("Smart van took", round(end - start, 2), "seconds → lower cost")