
from api.models import Medicos, Especialidad, ObraSocial, Sede, User, Turnos
from .serializers import MedicosSerializer, EspecialidadSerializer, ObraSocialSerializer, \
    SedeSerializer, RegisterSerializer, MeSerializer, TurnosSerializer
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, generics

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

@api_view(['get'])
@permission_classes([IsAuthenticated])
def me(request):
    print(MeSerializer(request.user).data)
    return Response(MeSerializer(request.user).data)

class MedicosViewSet(viewsets.ModelViewSet):
    serializer_class = MedicosSerializer
    queryset = Medicos.objects.all()

    #@action(methods=['post'], detail=False)
#@api_view(['get'])
#def medico_especialidad(self):
    #print(Medico_detalleSerializer(request.user).data)
    #return Medico_detalleSerializer(self.Medicos).data
       # return Response(status=200)


class EspecialidadViewSet(viewsets.ModelViewSet):
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()

class ObraSocialViewSet(viewsets.ModelViewSet):
    serializer_class = ObraSocialSerializer
    queryset = ObraSocial.objects.all()
   # permission_classes = [IsAuthenticated]

class SedeViewSet(viewsets.ModelViewSet):
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()

class TurnosViewSet(viewsets.ModelViewSet):
    serializer_class = TurnosSerializer
    queryset = Turnos.objects.all()






