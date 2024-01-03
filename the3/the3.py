def area(Q,T):
    intersections = get_intersections(Q,T)
    A_T = A(T)
    A_Q = A(Q)
    inner_points = [i for i in Q if abs(inner_point(i,T)-A_T)<0.000001] + [i for i in T if abs(inner_point(i,Q)-A_Q)<0.000001]
    all_points = intersections+inner_points
    for i in all_points:
        if all_points.count(i) > 1:
            all_points.remove(i)
    all_points = normalize_points(all_points)
    return A(all_points)
def get_intersections(A,B):
    #find lines of shapes
    A_lines = []
    B_lines = []
    intersect_points = []
    for i in range(len(A)):
        if i == (len(A)-1):
            A_lines.append((A[i],A[0]))
        else:
            A_lines.append((A[i],A[i+1]))
    for i in range(len(B)):
        if i == (len(B)-1):
            B_lines.append((B[i],B[0]))
        else:
            B_lines.append((B[i],B[i+1]))
    for line_1 in A_lines:
        for line_2 in B_lines:
            if (((line_2[1][1]-line_2[0][1])*(line_1[1][0]-line_1[0][0]))-((line_1[1][1]-line_1[0][1])*(line_2[1][0]-line_2[0][0]))) != 0: 
                #Apply intersection formula
                Tm = ((line_2[1][1]-line_2[0][1])*(line_2[0][0]-line_1[0][0])-(line_2[0][1]-line_1[0][1])*(line_2[1][0]-line_2[0][0]))/((line_2[1][1]-line_2[0][1])*(line_1[1][0]-line_1[0][0])-(line_1[1][1]-line_1[0][1])*(line_2[1][0]-line_2[0][0]))
                Ex = line_1[0][0] + (line_1[1][0]-line_1[0][0])*Tm
                Ey = line_1[0][1] + (line_1[1][1]-line_1[0][1])*Tm
                if min([line_1[0][0],line_1[1][0]])-0.000001 <= Ex <= max([line_1[0][0],line_1[1][0]])+0.000001 and min([line_1[0][1],line_1[1][1]])-0.000001 <= Ey <= max([line_1[0][1],line_1[1][1]])+0.000001 and min([line_2[0][0],line_2[1][0]])-0.000001 <= Ex <= max([line_2[0][0],line_2[1][0]])+0.000001 and min([line_2[0][1],line_2[1][1]])-0.000001 <= Ey <= max([line_2[0][1],line_2[1][1]])+0.000001:
                    intersect_points.append((Ex,Ey))
    return intersect_points
def inner_point(point,toward_points):
    #find triangles
    triangles = []
    for i in range(len(toward_points)):
        if i == (len(toward_points)-1):
            triangles.append((toward_points[i],toward_points[0],point))
        else:
            triangles.append((toward_points[i],toward_points[i+1],point))
    #find sum of triangle areas
    sum =0
    for i in triangles:
        sum += A(list(i))
    return sum
def normalize_points(points):
    if len(points) == 0:
        return []
    #find first point which has minimum x value
    x_values = [i[0] for i in points]
    first_point = ()
    for i in points:
        if i[0] == min(x_values):
            first_point = i
            break
    #sort by clockwise order
    points.remove(first_point)
    slope_list = []
    for i in points:
        if (i[0]-first_point[0]) == 0:
            if i[1] > first_point[1]:
                m = float("inf")
            else:
                m = float("-inf")
        else:
            m = (i[1]-first_point[1])/(i[0]-first_point[0])
        slope_list.append(m)
    for i in range(len(slope_list)):
        for i in range(len(slope_list)-1):
            if slope_list[i] < slope_list[i+1]:
                slope_list[i],slope_list[i+1] = slope_list[i+1],slope_list[i]
                points[i],points[i+1] = points[i+1],points[i]
    points.insert(0,first_point)
    return points
def A(points):
    if len(points) < 3:
        return 0
    points.append(points[0])
    sum =0
    sum2 = 0
    for i in range(0,len(points)-1):
        sum += points[i][0]*points[i+1][1]
    for i in range(0,len(points)-1):
        sum2 += points[i][1]*points[i+1][0]
    return abs((sum-sum2)/2)