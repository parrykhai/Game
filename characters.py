import pymunk as pm
from pymunk import Vec2d


class Static_block():
    def __init__(self, x, y, length, depth, space):
        y_add = y-50
        static_body = pm.Body(body_type=pm.Body.STATIC)
        self.static_line_top = [pm.Segment(static_body, (x, y_add), (x + length, y_add), 0.0)]
        self.static_line_bottom = [pm.Segment(static_body, (x, y_add - depth), (x + length, y_add - depth), 0.0)]
        self.static_line_right = [pm.Segment(static_body, (x + length, y_add), (x + length, y_add - depth), 0.0)]
        self.static_line_left = [pm.Segment(static_body, (x, y_add), (x, y_add - depth), 0.0)]
        for line in self.static_line_top:
            line.elasticity = 0.9
            line.friction = 0.9
            line.collision_type = 3
        for line in self.static_line_bottom:
            line.elasticity = 0.9
            line.friction = 0.9
            line.collision_type = 3
        for line in self.static_line_right:
            line.elasticity = 0.9
            line.friction = 0.9
            line.collision_type = 3
        for line in self.static_line_left:
            line.elasticity = 0.9
            line.friction = 0.9
            line.collision_type = 3
        space.add(self.static_line_top)
        space.add(self.static_line_bottom)
        space.add(self.static_line_right)
        space.add(self.static_line_left)


class Bird():

    def __init__(self, distance, angle, x, y, space):
        self.life = 20
        mass = 5
        radius = 12
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        power = distance * 53
        impulse = power * Vec2d(1, 0)
        angle = -angle
        body.apply_impulse_at_local_point(impulse.rotated(angle))
        shape = pm.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape


class Pig():
    def __init__(self, x, y, space):
        self.life = 20
        mass = 5
        radius = 14
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        shape = pm.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 1
        space.add(body, shape)
        self.body = body
        self.shape = shape


