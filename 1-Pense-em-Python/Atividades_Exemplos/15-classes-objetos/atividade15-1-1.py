class Point:
    """Represents a point in 2-D space."""


blank = Point()

blank.x = 3.0
blank.y = 4.0


def distance_between_points(p):
    distancia = (p.x**2 + p.y**2) ** 0.5
    return distancia


print(distance_between_points(blank))
