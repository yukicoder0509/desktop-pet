from math import sqrt

def routeByTop(curPos:tuple, topPos:tuple, gravity:float, samplePoint:int):
    """
    Route the projectile by the top point.

    Parameters:
    curPos:tuple - Current position of the projectile.
    topPos:tuple - Top position of the projectile.
    gravity:float - Gravity of the projectile.
    samplePoint:int - Number of sample points.

    Returns:
    list - List of positions of the projectile.
    """
    # Calculate the time of flight
    timeOfFlight = 2 * sqrt(2 * (curPos[1] - topPos[1]) / gravity)
    # Calculate the horizontal velocity
    horizontalVelocity = (2 * (topPos[0] - curPos[0])) / timeOfFlight
    # Calculate the vertical velocity
    verticalVelocity = gravity * timeOfFlight / 2
    # Calculate the time interval
    timeInterval = timeOfFlight / samplePoint
    # Calculate the positions
    positions = []
    for i in range(samplePoint + 1):
        t = i * timeInterval
        x = curPos[0] + horizontalVelocity * t
        y = curPos[1] - ( verticalVelocity * t - 0.5 * gravity * (t ** 2) )
        positions.append((x, y))
    print("Route generate by Top position: ", positions)
    return positions