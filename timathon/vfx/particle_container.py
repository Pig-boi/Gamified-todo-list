from collections import UserList

class ParticleContainer(UserList):

    def update(self, delta_time = 1):
        for particle in self:
            particle.update(self, delta_time)

    def draw(self, surface, camera = [0, 0]):
        for particle in self:
            particle.draw(surface, camera)

foo = ParticleContainer()
