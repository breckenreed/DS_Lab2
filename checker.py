import time
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

    def сhecker():
        dist_map = hz.get_map("HZ-DIST_MAP")

        tasks = set()
        for i in range(1000):
            tasks.add(dist_map.get(str(i)))

        for t in tasks:
            if t.result() != "value":
                print("The map was corrupted")
                hz.shutdown()
                return
        print("Map sucessfully passed integrity check")

    сhecker()
    hz.shutdown()