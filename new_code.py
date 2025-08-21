
import random
import time
def driver_creator(driver_count):
    drivers = []
    for driver in range(driver_count):
        drivers.append(f"Driver-{driver}")
    return drivers

def house_collector(houses_num):
    house_addresses = []
    for i in range(houses_num):
        house_addresses.append(f"house_{i}")
    return house_addresses

def package_assigner(package_count,num_houses):
    packages = set()
    while len(packages) != package_count:
        packages.add(f"house_{random.randrange(num_houses)}")

    return packages


def deliver(drivers_req,packages,houses):
    delivered = []
    for pack in packages:
        for house in houses:
            if pack == house:
                delivered.append(pack)
                break
    print(delivered)
    
 
    

if __name__ == '__main__':
    num_drivers = 500
    num_houses = 1500000
    num_packages = 5000
    
    
    driver_list = driver_creator(num_drivers)
    houses_list = house_collector(num_houses)
    package_list = package_assigner(num_packages,num_houses)
    start = time.perf_counter()
    deliver(driver_list,package_list,houses_list)
    end = time.perf_counter()
    
    
    
    
 
 
 