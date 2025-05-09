def create_server(name, connections=0):
    return {"name": name, "connections": connections}

def create_load_balancer(servers, algorithm="round_robin"):
    return {
        "servers": servers,
        "current_index": 0,
        "algorithm": algorithm
    }

def add_server(load_balancer, server):
    load_balancer["servers"].append(server)

def get_next_server(load_balancer):
    if load_balancer["algorithm"] == "round_robin":
        servers = load_balancer["servers"]
        index = load_balancer["current_index"]
        server = servers[index]
        load_balancer["current_index"] = (index + 1) % len(servers)
        return server
    elif load_balancer["algorithm"] == "least_connections":
        return min(load_balancer["servers"], key=lambda s: s["connections"])
    else:
        raise ValueError("Unknown load balancing algorithm")

def assign_load(load_balancer, i):
    server = get_next_server(load_balancer)
    server["connections"] += 1  # Simulate handling a new request
    print(f"Request {i} assigned to server: {server['name']} (now handling {server['connections']} connections)")

# Simulate initial server setup
initial_servers = [
    create_server("S1", 2),  # S1 starts with 2 connections
    create_server("S2", 5),  # S2 starts with 5 connections
    create_server("S3", 1),  # S3 starts with 1 connection
]

# Test using Round Robin
print("\n--- Round Robin Load Balancing ---")
lb_rr = create_load_balancer([s.copy() for s in initial_servers], algorithm="round_robin")
for i in range(1, 7):
    assign_load(lb_rr, i)

# Test using Least Connections
print("\n--- Least Connections Load Balancing ---")
lb_lc = create_load_balancer([s.copy() for s in initial_servers], algorithm="least_connections")
for i in range(1, 6):
    assign_load(lb_lc, i)
