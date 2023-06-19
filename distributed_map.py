import hazelcast

if __name__ == "__main__":
    hz = hazelcast.HazelcastClient( 
        cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703"
    ],
    lifecycle_listeners=[
        lambda state: print("New event appeared in lifecycle: ", state),
    ])
    map = hz.get_map("HZ-DIST_MAP").blocking()
    for i in range(1000):
        map.set(i, "value")
    hz.shutdown()
