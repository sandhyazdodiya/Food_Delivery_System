from app.models.admin import *
from app.models.customer import *
from app.models.delivery import *
from app.models.restaurant import *



def add_user_name_to_context(request):

    """
    It returns logged in user name from profile models in context variable.
    """

    user_name=""

    customer=Customer.get_customer_by_user_id(request.user.id)
    restaurant=Restaurant.get_restaurant_by_user_id(request.user.id)
    admin=Admin.get_admin_by_user_id(request.user.id)
    delivery_person=DeliveryPerson.get_delivery_person_by_user_id(request.user.id)

    if customer:
        user_name=customer.name
    elif admin:
        user_name=admin.name
    elif delivery_person:
        user_name=delivery_person.name
    elif restaurant:
        user_name=restaurant.name
        
    return {
        'user_name': user_name
    }
