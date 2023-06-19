import hazelcast
import time

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

    map = hz.get_map("LAB2-NO_LOCK")
    key = "key"

    map.put_if_absent(key, 1)
    for i in range(100): #reduced to save processing time 
        value = map.get(key).result()
        time.sleep(0.1)
        value+=1
        map.put(key, value)

    print("Finalized with result: ", map.get(key).result())

    hz.shutdown()
