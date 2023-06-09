import hazelcast

if __name__ == "__main__":
    hz = hazelcast.HazelcastClient( 
        cluster_members=[
        "172.24.0.2:5701",
        "172.24.0.3:5701",
        "172.24.0.4:5701"
    ],
    lifecycle_listeners=[
        lambda state: print("Event appeared in lifecycle: ", state),
    ])
    map = hz.get_map("lab2-distributed-map").blocking()
    for i in range(1000):
        map.set(i, "value")
    hz.shutdown()
