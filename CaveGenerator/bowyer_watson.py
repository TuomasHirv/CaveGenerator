"""Module for Bowyer_Watson algorithm"""


#This file will feature alot more comments than necessary as it is quite complex.


def in_circle(tri, point):
    """Function that checks the validity of a triangle given point"""
    a_original, b_original, c_original = tri
    d_original = point


    orientation = ((b_original[0] - a_original[0]) * (c_original[1] - a_original[1])
                   - (b_original[1] - a_original[1]) * (c_original[0] - a_original[0]))

    #In essence we set the calculation so that origo (0,0) is the new point.
    adx, ady = a_original[0] - d_original[0], a_original[1] - d_original[1]
    bdx, bdy = b_original[0] - d_original[0], b_original[1] - d_original[1]
    cdx, cdy = c_original[0] - d_original[0], c_original[1] - d_original[1]

    #Turning a non-linear calculation into linear by projecting it into a plane.
    #_lift is essentially a new z coordinate.

    alift = adx**2 + ady**2
    blift = bdx**2 + bdy**2
    clift = cdx**2 + cdy**2

    #We calculate where the created plane is in regards to the origo.
    determinant = (adx *(bdy * clift - cdy * blift)
                   - ady *(bdx * clift - cdx *blift)
                   + alift * (bdx * cdy - cdx *bdy))


    if orientation < 0:
        determinant = -determinant

    #If the determinant is higher than origo new point is in the sphere.
    if determinant > 0:
        return True
    if determinant < 0:
        return False
    #we need an arbitrary decider.
    return a_original[0] < d_original[0]


def get_super_triangle(screen_length, screen_width):
    """Generates the first triangle for B_W"""
    margin = max(screen_length, screen_width)*10
    p1 = (-margin, -margin)
    p2 = (screen_width//2, margin *2)
    p3 = (screen_width + margin, -margin)
    return (p1, p2, p3)

def bowyer_watson(points, screen_length, screen_width):
    """Triangulates points"""
    #This algorithm works by creating and destroying existing triangles.
    super_triangle = get_super_triangle(screen_length, screen_width)
    triangles = [super_triangle]
    for p in points:
        #We add points one by one and check for triangles that need to be destroyed.
        bad_triangles = []

        for tri in triangles:
            if in_circle(tri, p):
                bad_triangles.append(tri)

        #When destroying triangles we create a polygon in to the super triangle.
        polygon_edges = []
        for tri in bad_triangles:
            edges = [(tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])]
            #Sorting edges so they are identical. We remove any edges that appear twice.
            for edge in edges:
                edges_s = tuple(sorted(edge))
                if edges_s in polygon_edges:
                    polygon_edges.remove(edges_s)
                else:
                    polygon_edges.append(edges_s)

        for tri in bad_triangles:
            triangles.remove(tri)

        #Creating new triangles from the boundary of the polygon
        #The edges that remained are the ones on the boundary.
        #The ones that were in bad triangles twice were in the middle of the polygon.
        for edge in polygon_edges:
            created = (edge[0], edge[1], p)
            triangles.append(created)
    #Now we need to remove triangles that include the super triangle as that is not a part of this.
    final = []

    #Need set() here to speed up the lookup
    super_set = set(super_triangle)
    for tri in triangles:
        if not set(tri) & super_set:
            final.append(tri)

    #Turning triangles into a list of connections
    connections = get_connections(final)

    return connections


def get_connections(triangles):
    """Turns triangulation in to singular edges"""
    result = set()

    for tri in triangles:
        edges = [(tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])]

        for edge in edges:
            edge_s = tuple(sorted(edge))
            result.add(edge_s)

    return list(result)
