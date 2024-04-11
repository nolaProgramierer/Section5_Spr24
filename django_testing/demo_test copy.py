# from django.test import TestCase
# from .models import Flight, Airport, Employee


# class FlightTestCase(TestCase):
#     def setUp(self):
#         # Create airports
#         a1 = Airport.objects.create(code="AAA", city="City A")
#         a2 = Airport.objects.create(code="BBB", city="City B")

#         # Create flights
#         Flight.objects.create(origin=a1, destination=a2, duration=100)
#         Flight.objects.create(origin=a1, destination=a1, duration=200)
#         Flight.objects.create(origin=a1, destination=a2, duration=100)

#     def test_departure_count(self):
#         a = Airport.objects.get(code="AAA")
#         self.assertEqual(a.departures.count(), 3)

#     def test_arrivals_count(self):
#         a = Airport.objects.get(code="AAA")
#         self.assertEqual(a.arrivals.count(), 1)

#     def test_valid_flight(self):
#         a1 = Airport.objects.get(code="AAA")
#         a2 = Airport.objects.get(code="BBB")
#         f = Flight.objects.create(origin=a1, destination=a2, duration=100)
#         self.assertTrue(f.is_valid_flight())

#     def test_invalid_flight_destination(self):
#         a1 = Airport.objects.get(code="AAA")
#         f = Flight.objects.create(origin=a1, destination=a1, duration=100)

#     def test_invalid_flight_duration(self):
#         a1 = Airport.objects.get(code="AAA")
#         a2 = Airport.objects.get(code="BBB")
#         f = Flight.objects.create(origin=a1, destination=a2, duration=0)
#         self.assertFalse(f.is_valid_flight())


class EmployeeTestCase(TestCase):
    def setUp(self):
        # Create 8 employee
        # 2 of which are bosses: Bob & Benedict
        e1 = Employee.objects.create(fname="Bob", lname="Iger", boss=True)
        e2 = Employee.objects.create(fname="Sally", lname="Wilson")
        e3 = Employee.objects.create(fname="Billy", lname="Bigelow")
        e4 = Employee.objects.create(fname="Benedict", lname="VanMeter", boss=True)
        e5 = Employee.objects.create(fname="Tony", lname="DiSavio")
        e6 = Employee.objects.create(fname="Evie", lname="Thompson")
        e7 = Employee.objects.create(fname="Anne", lname="Arundel")
        e8 = Employee.objects.create(fname="Sad", lname="Sack", boss=True)

        # Make Benedict VanMeter the supervisor of Bob Iger
        e1.supervisor.add(e4)

        # Make Benedict VanMeter the supervisor of Sally Wilson
        e4.subordinates.add(e2)

        # Make Benedict VanMeter the supervisor of Billy Bigelow
        e3.supervisor.add(e4)

        # Make Benedict VanMeter the supervisor of himself
        e4.supervisor.add(e4)

        # Make Bog Iger the supervisor of Tony DiSavio
        e5.supervisor.add(e1)

        # Make Bog Iger the supervisor of Evie Thompson
        e6.supervisor.add(e1)

        # Make Bog Iger the supervisor of Anne Arundel
        e7.supervisor.add(e1)

        # Make Benedict VanMeter the supervisor of Bob Iger
        e1.supervisor.add(e4)


#----------------------------------------------------------------------------
    # Bob is supervisor of: 1)Tony diSavio, 2)Evie Thompson, 3)Anne Arundel
    # Benedict VanMeter is supervisor of: 1)Bob Iger, 2)Sally Wilson, 
    # 3)Billy Bigelow, & 4)himself 
#----------------------------------------------------------------------------
        
    #Test for all employees being in test DB
    def test_num_employees(self):
        """Test for total # of employees"""
        employees = Employee.objects.all()
        self.assertEqual(employees.count(), 8)
    
    # Test number of subordinates of Bob Iger
    def test_bob_subordinate_count(self):
        """Test for number of Bob's subordinates"""
        bob = Employee.objects.get(fname="Bob")
        self.assertEqual(bob.subordinates.count(), 3)
    
    # Test number of subordinates of Benedict VanMeter
    def test_benedict_subordinate_count(self):
        """Test for number of Benedict's subordinates"""
        benedict = Employee.objects.get(lname="VanMeter")
        self.assertEqual(benedict.subordinates.count(), 4)
    
    # Test if Benedict supervises a boss
    def test_big_boss(self):
        """Test for big boss"""
        benedict = Employee.objects.get(lname="VanMeter")
        self.assertTrue(benedict.is_boss_of_himself())
    
    # Test is Anne has multiple supervisors
    def test_has_multiple_supervisors(self):
        """Test for multiple supervisor"""
        anne = Employee.objects.get(fname="Anne")
        self.assertFalse(anne.has_multiple_bosses())

    # Test benedict has subordinates
    def test_boss_has_subordinates(self):
        """Test for subordinates of a boss"""
        benedict = Employee.objects.get(fname="Benedict")
        self.assertTrue(benedict.boss_has_subordinates())
    
    # Test Sad has no subordinates
    def test_boss_has_no_subordinates(self):
        """Test for no subordinates"""
        sad = Employee.objects.get(fname="Sad")
        self.assertFalse(sad.boss_has_subordinates())
                      
    # Test Sally Wilson is subordinate of Benedict vanMeter
    def test_sally_is_subordinate_benedict(self):
        """See if Benedict is Sally's boss""" 
        sally = Employee.objects.get(fname="Sally")
        anne = Employee.objects.get(fname="Anne")
        benedict = Employee.objects.get(fname="Benedict")
        benedict_subordinates = benedict.subordinates.all()
        self.assertFalse(benedict_subordinates.contains(anne))
    


 







    

