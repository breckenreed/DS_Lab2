import hazelcast
import time

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

    map = hz.get_map("lab2_map")
    key = "key"

    map.put_if_absent(key, 1)
    for i in range(100):
        value = map.get(key).result()
        time.sleep(0.1)
        value+=1
        map.put(key, value)

    print("Finalized with result: ", map.get(key).result())

    hz.shutdown()
