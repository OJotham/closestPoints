# closestPoints
Given a list of points, get a pair with the shortest distance between them. Points to be pulled from transportAPI

When Autodesk was designing a new rail tunnel, architecture, engineering, and design consultancy Norconsult made a large risk smaller by applying advanced technology to a critical-yet-cumbersome design requirement - the railway signaling system. To prevent costly construction delays due to inadequate signs and signals, Norconsult used 3D modeling and VR gamification in infrastructure design to help foresee potential design problems.

Now it's time to test the system. You have been given a task - to find the best stations for testing. Your co-workers gave you a list of stations, which can be chosen as a start and finish, and also said that it would be great to choose two different stations as close as possible, because it's boring to watch a VR game all day long.

More formally, with the given list of station names, find the minimal distance between any two of them.

We assume that the distance between two stations is the Euclidian distance of their coordinates (latitude and longitude).

Useful APIs

For this task, you can use the following APIs or any other public APIs that provide the necessary functionality.

    Transport API.

Note that you are not allowed to access resources created specifically for solving this task (like your own service).

You can access Transport API with the following parameters.

    App ID: 8b9cd4d9, Key: 69eaf54e2f7d2f279a03077acab2721b.
    App ID: ae6d5a90, Key: 5c6b8d92f7c423c588ab1ef7a03c1bce.
    App ID: b6b818ca, Key: 03e4aec30ef27c673a08ea02d4567e28.

Example

For stations = ["Euston", "Mossley Hill", "Glasgow Central"], the output should be closestStations(stations) = 2.82054384773.

The closest stations are "Mossley Hill", and "Glasgow Central". The distance between them is 2.8205438477.

Input/Output

    [execution time limit] 22 seconds (py3)

    [input] array.string stations

    The names of the stations that can be chosen. All station names contain only English letters and spaces.

    Guaranteed constraints:
    2 ≤ stations.length ≤ 10,
    1 ≤ stations[i].length ≤ 100.

    [output] float
        The minimal distance between two stations. Your answer will be considered correct if its absolute error doesn't exceed 10-5.

