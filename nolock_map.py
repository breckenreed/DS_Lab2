import hazelcast

if __name__ == "__main__":

    def write_no_lock():
        client = hazelcast.HazelcastClient(
        cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703"
    ],
    lifecycle_listeners=[
        lambda state: print("New event appeared in lifecycle: ", state),
    ])

        no_lock_map = client.get_map("NO-LOCK-MAP")
        key = "testing"
        no_lock_map.put_if_absent(key, 1)
        for i in range(100):
            val = no_lock_map.get(key).result()
            val += 1
            no_lock_map.put(key, val)

        print("Finalized with result: ", no_lock_map.get(key).result())
       
        client.shutdown()

write_no_lock()
