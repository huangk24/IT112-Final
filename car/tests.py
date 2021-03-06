from django.test import TestCase
from  django.contrib.auth.models import User
from .models import CarType, Car, Review
import datetime
from .forms import CarForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class CarTypeTest(TestCase):
    def setUp(self):
        self.type = CarType(typename = 'Sports Car')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Sports Car')

    def text_tablename(self):
        self.assertEqual(str(CarType._meta.db_table), 'cartype')

class CarTest(TestCase):
    def setUp(self):
        self.type = CarType(typename = 'Sports Car')
        self.user = User(username = 'user1')
        self.car = Car(carname = 'BMW M8', cartype = self.type, user = self.user,
                       dateentered = datetime.date(2022,1,1), price = 100000, 
                       producturl = 'https://www.bmwusa.com/vehicles/m-models/m8-coupe/overview.html')
    
    def test_string(self):
        self.assertEqual(str(self.car), 'BMW M8')

    def test_discount(self):
        disc = self.car.price * 0.05
        self.assertEqual(self.car.discountAmount(), disc)

class NewCarForm(TestCase):
    def test_carform(self):
        data={
            'carname':'Audi A7', 
            'cartype':'Sports Car',
            'user': 'kai',
            'dateentered': '2021-1-1',
            'price': '69200',
            'producturl': 'http://audiusa.com/us/web/en/models/a7/a7-sportback/2022/overview.html' 
        }
        form = CarForm (data)
        self.assertTrue(form.is_valid)

class New_Car_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password='P@ssw0rd1')
        self.type = CarType.objects.create(typename='SUV')
        self.car = Car.objects.create(carname = 'BMW X5', cartype = self.type, user = self.test_user,
                       dateentered = datetime.date(2022,1,1), price = 100000, 
                       producturl = 'https://www.bmwusa.com/vehicles/m-models/m8-coupe/overview.html')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newcar'))
        self.assertRedirects(response, '/accounts/login/?next=/car/newcar/')

