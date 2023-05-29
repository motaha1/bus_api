from django.shortcuts import render
from django.urls import path
from rest_framework import generics
from rest_framework.response import Response
from users.firebase_realtime import *

from users.models import *
from users.serializers import BusSerializer, CapSerializer, PassengerSerializer
# Create your views here.


class checkout (generics.CreateAPIView):
        def post(self, request, *args, **kwargs):
            id = request.data['id']
           
            pas =Passenger.objects.get(card = id)

            travel = Captine.objects.get(id=1).travel
            bus = Bus.objects.get(id = Captine.objects.get(id=1).bus_no)
            items= bus.passenger.all()
            if(pas in items ):
                return Response("duplication" , status=502)
            pas.funds = pas.funds - travel.price 
            pas.save()

                 
            #if(bus.pass_set.filter(id = ))
            bus.passenger.add(pas)
            bus.save()


            return Response(pas.funds)
        

class add (generics.CreateAPIView):
      def post(self, request, *args, **kwargs): 
        id = request.data['id']
        amount = request.data['amount']
        pas =Passenger.objects.get(card = id)
        pas.funds = pas.funds + int(amount)
        pas.save()
        return Response(pas.funds)
      

class new (generics.CreateAPIView) :
     def post(self, request, *args, **kwargs):
          pass
          


class pass_info(generics.CreateAPIView) :
     serializer_class  = PassengerSerializer
     def post(self, request, *args, **kwargs): 
        id = request.data['id']
        pas =Passenger.objects.get(card = id)
        return Response(PassengerSerializer(pas).data)


class pass_info_test(generics.CreateAPIView) :
     serializer_class  = PassengerSerializer
     def post(self, request, *args, **kwargs): 
        id = request.data['id']
        pas =Passenger.objects.get(card = id)
        return Response(PassengerSerializer(pas).data)

        



class firebase_realtime(generics.CreateAPIView) :

     def post(self, request, *args, **kwargs): 
        fire = realtime()
       
        return Response('ok')


class new_travel(generics.CreateAPIView) :

     def post(self, request, *args, **kwargs): 
        id = request.data['id']
        travel =Travel.objects.get(id=id)
        cap = Captine.objects.get(id=1)
        cap.travel = travel
        
        
        bus = Bus.objects.create( travel = travel , captine =Captine.objects.get(id=1))
        cap.bus_no = bus.id
        cap.save()
        bus.save()
        #bus.passenger.add(pas)

        return Response(bus.id)


class cap_info(generics.CreateAPIView):
        def post(self, request, *args, **kwargs): 
       
        
          cap = Captine.objects.get(id=1)
       
          

          return Response(CapSerializer(cap).data)



class buss (generics.CreateAPIView) : 
          def post(self, request, *args, **kwargs): 
               pas = Passenger.objects.get(id=1)
        
               busss = Bus.objects.filter(passenger = pas)
          
               

               return Response(BusSerializer(busss , many = True ).data)



class checkout_new (generics.CreateAPIView):
        def post(self, request, *args, **kwargs):
            id = request.data['id']
           
            pas =Passenger.objects.get(card = id)

            travel = Captine.objects.get(id=1).travel
            bus = Bus.objects.get(id = Captine.objects.get(id=1).bus_no)
            items= bus.passenger.all()
            if(pas in items ):
                return Response("duplication" , status=502)
            pas.funds = pas.funds - travel.price 
            pas.save()

                 
            #if(bus.pass_set.filter(id = ))
            bus.passenger.add(pas)
            bus.save()


            return Response({
                'funds':pas.funds , 
                'phone' : pas.phone, 
                'travel' : travel.name})



class get_gps (generics.CreateAPIView):
        def post(self, request, *args, **kwargs):
                lat = get_gsp_lat()
                longg = get_gsp_long()

                return Response({
                        'lat' : lat , 
                        'long' : longg 
                })
    
# class test (generics.CreateAPIView)  :
#                def post(self, request, *args, **kwargs): 
#                     pas = Passenger.objects.get(id=1)
        
#                     ts = Bus.objects.get(id = 1)
#                     ts.passenger.add(pas)
#                     ts.save()
          
               

#                     return Response('ok')


# class test (generics.CreateAPIView)  :
#                def post(self, request, *args, **kwargs): 
#                     pas = Passenger.objects.get(id=1)
        
#                     ts = Bus.objects.get(id = 4)
#                     ts.passenger.clear()
#                     ts.save()
          
               

#                     return Response('ok')