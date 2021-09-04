from Rdf_thing import Rdf_thing
from utlis import xstr, obj_print
from datetime import datetime


class Experience(Rdf_thing):
    def __init__(self, id, role, place, location, start_date, end_date):
        super().__init__(id)
        self.role = xstr(role.strip())
        self.place = place  # corrisponde al predicato lkn:performedIn
        self.location = location.strip()
        self.start_date = start_date
        self.end_date = end_date

        if self.role:
            self.role = str(self.role.strip())
        if self.location:
            self.location = str(self.location.strip())
        if self.start_date:
            self.start_date = str(self.start_date.strip())
        if self.end_date:
            self.end_date = str(self.end_date.strip())

        if self.end_date and 'presente' in self.end_date:
            self.end_date = str(datetime.now().strftime("%b")) + " " + str(datetime.now().year)

    def print_rdf_info(self):
        rdf_id = self.get_rdf_id()
        if self.role:
            print(rdf_id + " lkn:role " + obj_print(self.role))
        if self.start_date:
            print(rdf_id + " lkn:startDate " + obj_print(self.start_date))
        if self.end_date:
            print(rdf_id + " lkn:endDate " + obj_print(self.end_date))
        if self.location:
            print(rdf_id + " lkn:location " + obj_print(self.location))
        if self.place:
            self.place.print_rdf_info()
            print(rdf_id + " lkn:happenedAt " + self.place.get_rdf_id() + ".")


class WorkingExperience(Experience):
    def __init__(self, id, role, place, location, start_date, end_date):
        super().__init__(id, role, place, location, start_date, end_date)

    def print_rdf_info(self):
        rdf_id = self.get_rdf_id()
        print(rdf_id + " rdf:type " + 'lkn:WorkingExperience.')
        super().print_rdf_info()

    def get_rdf_id(self):
        return "lkn:wrkExp" + xstr(self.id)


class EducationExperience(Experience):
    def __init__(self, id, role, place, location, start_date, end_date):
        super().__init__(id, role, place, location, start_date, end_date)

    def print_rdf_info(self):
        rdf_id = self.get_rdf_id()
        print(rdf_id + " rdf:type " + 'lkn:EducationExperience.')
        super().print_rdf_info()

    def get_rdf_id(self):
        return "lkn:eduExp" + xstr(self.id)
