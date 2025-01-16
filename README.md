# Package_Routing_Program

## WGUPS Routing Program

### <ins>Overview</ins>

The WGUPS Routing Program is a software solution designed to optimize the delivery of packages for the Western Governors University Parcel Service (WGUPS) in Salt Lake City. This program uses the Nearest Neighbor Algorithm to calculate the most efficient routes, minimizing mileage and meeting delivery deadlines. It also includes a user interface to display delivery details and statistics.


### <ins>Features</ins>

**Package Management:** Utilizes a hash table to efficiently store and manage package details.
**Route Optimization:** Implements the Nearest Neighbor Algorithm to calculate the shortest delivery routes.
**Time Constraints Handling:** Accounts for specific delivery deadlines and package updates during runtime.
**User Interface:** Provides options to view delivery status, total mileage, and specific package details.


### <ins>Requirements</ins>

**Software Requirements**
Python 3.9+

**Libraries:**
datetime
csv
timedelta



### <ins>Algorithms and Data Structures</ins>

**Nearest Neighbor Algorithm**

The Nearest Neighbor Algorithm is used to:
Determine the shortest path between the current location and the next delivery address.
Reduce the total distance traveled while meeting delivery deadlines.

**Hash Table**

The hash table is used to:
Efficiently store and retrieve package data by package ID.
Handle real-time updates, such as address corrections.



### <ins>Strengths and Limitations</ins>

**Strengths:**

Efficient routing reduces mileage and costs.
Modular code makes the project easy to maintain and expand.

**Limitations:**

The Nearest Neighbor Algorithm does not guarantee globally optimal solutions.
Real-world traffic conditions are not considered.

### <ins>Future Enhancements</ins>

Implement more advanced algorithms like Dijkstra's Algorithm or A* for global route optimization.
Integrate real-time traffic data for better route planning.
Add a graphical user interface (GUI) for improved user interaction.
