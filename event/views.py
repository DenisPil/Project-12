import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Event
from staff.models import Staff
from customer.models import Customer
from contract.models import Contract
from .serializers import CreateEventSerializer, EventListSerializer, EventDetailSerializer
from .permissions import IsSupportTeam, IsSalesContact, IsManagementTeam


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("account.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class MultipleSerializerMixin:

    """ Mixin permet d'afficher les vues en détail ou en liste"""

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class EventViewSet(MultipleSerializerMixin, ModelViewSet):

    """ Le ModelViewSet des événements"""

    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [IsAuthenticated, IsSalesContact | IsManagementTeam | IsSupportTeam]

    def get_queryset(self, *args, **kwargs):
        queryset = Event.objects.all()
        customer_email = self.request.GET.get('email')
        customer_name = self.request.GET.get('name')
        event_date = self.request.GET.get('date')
        if customer_email:
            customer = Customer.objects.get(email=customer_email)
            contract = Contract.objects.get(customer=customer.id)
            queryset = Event.objects.filter(contract_event=contract)
        elif customer_name:
            customer = Customer.objects.get(last_name=customer_name)
            contract = Contract.objects.get(customer=customer.id)
            queryset = Event.objects.filter(contract_event=contract)
        elif event_date:
            queryset = Event.objects.filter(event_date=event_date)
        logger.debug("current user is: {}.".format(self.request.user))
        logger.debug("http method: {} status code: {}.".format(self.request.method,
                                                               Response().status_code))
        return queryset

    def create(self, request):
        serializer = CreateEventSerializer(data=request.data)
        data = {}
        valid_staff = Staff.objects.get(pk=request.data['support_contact'])
        valid_contract = Event.objects.filter(contract_event=request.data['contract_event'])
        if len(valid_contract) != 0:
            data['response'] = "This contract is already linked to an event."
            response = Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
            logger.debug("current user is: {}.".format(self.request.user))
            logger.debug("http method: {} status code: {}, {}.".format(self.request.method,
                                                                       response.status_code,
                                                                       data['response']))
            return response
        if valid_staff.role != 'support team':
            data['response'] = "Staff is not from support team."
            response = Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
            logger.debug("current user is: {}.".format(self.request.user))
            logger.debug("http method: {} status code: {}, {}.".format(self.request.method,
                                                                       response.status_code,
                                                                       data['response']))
            return response
        else:
            if serializer.is_valid(request):
                serializer.save()
                data['response'] = "Successfully registered a new user."
                response = Response(data, status=status.HTTP_201_CREATED)
                logger.debug("current user is: {}.".format(self.request.user))
                logger.debug("http method: {} status code: {}, {}.".format(self.request.method,
                                                                           response.status_code,
                                                                           data['response']))
            return response

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        response = Response(serializer.data, status=status.HTTP_202_ACCEPTED, headers=headers)
        logger.debug("current user is: {}.".format(self.request.user))
        logger.debug("http method: {} status code: {}.".format(self.request.method,
                                                               response.status_code))
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        data = {"response": "The event is deleted."}
        response = Response(data, status=status.HTTP_204_NO_CONTENT)
        logger.debug("current user is: {}.".format(self.request.user))
        logger.debug("http method: {} status code: {}, {}.".format(self.request.method,
                                                                   response.status_code,
                                                                   data['response']))
        return