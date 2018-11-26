import mlab
from river import River

mlab.connect()

#exe2
africa_river = River.objects(continent__icontains = "Africa")
print(len(africa_river))
for r in africa_river:
    print(r.name)

#exe3
river_length = River.objects(continent__icontains = "S.America", length__lt = 1000)
print(len(river_length))
for l in river_length:
    print(r.name)