import mlab
from movie import Movie
from resource import Resource

from faker import Faker

faker = Faker("en_US")
#for _ in range(5):
 #   print(faker.state())

mlab.connect()

#m = Movie.objects().with_id("")
#print(m.title)
#m.delete()

#movie_list = Movie.objects()

#for m in movie_list:
    #print(m.title)
    #print(m.image)
    #print(m.year)

#resource_list = Resource.objects()

#for r in resource_list:
    #print(r.name)
    #print(r.city)
    #print(r.yob)
    #print(r.height)
    #print(r.weight)

#m = Movie(title="batman", year=2005, image="https://images-na.ssl-images-amazon.com/images/I/81WciVYCtXL._SX342_.jpg")
#m.save()

#r = Resource(name="Ted", city="Ha Noi", yob=1993, height=178, weight=45)
#r.save()

#r = Resource.objects().with_id("5bf805c65b711a23e4d6ed43")
#if r is None:
#    print("Not found")
#else:
#    print("found")
#    r.delete()

#resource_list = Resource.objects()#.first() de delete phan tu dau tien
#r = resource_list[0]
#r.delete()

from random import randint

#for _ in range(100):
 #   name = faker.name()
  #  city = faker.state()
   # yob = randint(1953, 2000)
    #height = randint(150, 200)
    #weight = randint(40, 150)
    #r = Resource(name=name, city=city, yob=yob, height=height, weight=weight)
    #r.save()

#records = Resource.objects(name="Nicholas Knox")
#for r in records:
 #   print(r.city)
  #  print(r.weight)
   # print(r.height)

#records = Resource.objects(height=172)
#for r in records:
 #   print(r.name)

#records = Resource.objects(name__contains="Knox")
#print(len(records))

#records = Resource.objects(height__lt=170, name__icontains="je")
#for r in records:
 #   print(r.name)
  #  print(r.height)

#records = Resource.objects()

#for r in records:
 #   r.update(set__available=False)

r = Resource.objects().with_id("5bf80cdc5b711ab6f0fa9041")
r.update(set__available=True)