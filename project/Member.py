from Rdf_thing import Rdf_thing
from utlis import xstr, obj_print

global_skills = []

global_companies = []

global_schools = []


class Member(Rdf_thing):
    def __init__(self, id, url, about):
        super().__init__(id)
        self.URL = url
        self.about = about
        if self.URL:
            self.URL = xstr(self.URL.strip())
        if self.about:
            self.about = xstr(self.about.strip())
            self.about = self.about.replace("\n", " ")
            self.about = self.about.replace("\r", " ")
            self.about = self.about.replace('"', " ")


class MyPerson(Member):
    def __init__(self, id, url, about, location, firstName, secondName):
        super().__init__(id, url, about)
        self.first_name = firstName
        self.second_name = secondName
        self.location = location

        self.working_experiences = []
        self.education_experiences = []
        self.skills = []
        self.interests = []

    def add_working_experience(self,exp):
        self.working_experiences.append(exp)

    def add_education_experience(self,exp):
        self.education_experiences.append(exp)

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_interest(self,interest):
        self.interests.append(interest)

    def get_rdf_id(self):
        return 'lkn:person' + xstr(self.id)

    def print_rdf_info(self):
        rdf_id = self.get_rdf_id()
        print(rdf_id + " rdf:type " + "lkn:Person.")
        if self.first_name:
            print(rdf_id + " lkn:firstName " + obj_print(self.first_name))
        if self.second_name:
            print(rdf_id + " lkn:secondName " + obj_print(self.second_name))
        if self.location:
            print(rdf_id + " lkn:location " + obj_print(self.location))
        if self.URL:
            print(rdf_id + " lkn:URL " + obj_print(self.URL))
        if self.about:
            print(rdf_id + " lkn:about " + obj_print(self.about))
        for exp in self.working_experiences:
            exp.print_rdf_info()
            print(rdf_id + " lkn:hasWorkingExperience " + exp.get_rdf_id()+ ".")
        for edu in self.education_experiences:
            edu.print_rdf_info()
            print(rdf_id + " lkn:hasEducationExperience " + edu.get_rdf_id()+ ".")
        for skill in self.skills:
            skill.print_rdf_info()
            print(rdf_id + " lkn:hasSkill " + skill.get_rdf_id()+ ".")
        for interest in self.interests:
            interest.print_rdf_info()
            print(rdf_id + " lkn:hasInterest " + interest.get_rdf_id()+ ".")


class Place(Member):
    def __init__(self, id, url, about, placeName, website, phone, industry, companySize, headquarter, type, founded, speciality):
        super().__init__(id, url, about)

        self.placeName = placeName
        self.website = website
        self.phone = phone
        self.industry = industry
        self.companySize = companySize
        self.headquarter = headquarter
        self.type = type
        self.founded = founded
        self.speciality = speciality

        if placeName:
            self.placeName = xstr( self.placeName.strip())
        if website:
            self.website = xstr(self.website.strip())
        if phone:
            self.phone = xstr(self.phone.strip())
            self.phone = self.phone.replace("\n", " ")
            self.phone = self.phone.replace("\r", " ")
        if industry:
            self.industry = xstr(self.industry.strip())
        if companySize:
            self.companySize = xstr(self.companySize.strip())
        if headquarter:
            self.headquarter = xstr(self.headquarter.strip())
        if type:
            self.type = xstr(self.type.strip())
        if founded:
            self.founded = xstr(self.founded.strip())
        if speciality:
            self.speciality = xstr(self.speciality.strip())

    def print_rdf_info(self):
        rdf_id = self.get_rdf_id()
        if self.website:
            print(rdf_id + " lkn:website " + obj_print(self.website))
        if self.phone:
            print(rdf_id + " lkn:phone " + obj_print(self.phone))
        if self.companySize:
            print(rdf_id + " lkn:companySize " + obj_print(self.companySize))
        if self.about:
            print(rdf_id + " lkn:about " + obj_print(self.about))
        if self.industry:
            print(rdf_id + " lkn:industry " + obj_print(self.industry))
        if self.headquarter:
            print(rdf_id + " lkn:headquarter " + obj_print(self.headquarter))
        if self.type:
            print(rdf_id + " lkn:type " + obj_print(self.type))
        if self.founded:
            print(rdf_id + " lkn:founded " + obj_print(self.founded))
        if self.speciality:
            print(rdf_id + " lkn:speciality " + obj_print(self.speciality))


class Company(Place):
    def __init__(self, id, url, about, place_name, website, phone, industry, companySize, headquarter, type, founded, speciality):
        super().__init__(id, url, about, place_name, website, phone, industry, companySize, headquarter, type, founded, speciality)

    def print_rdf_info(self):

        rdf_id = self.get_rdf_id()
        if self.placeName not in [s.placeName for s in global_companies]:
            global_companies.append(self)
            print(rdf_id + " rdf:type " + "lkn:Company.")
        if self.placeName:
            print(rdf_id + " lkn:placeName " + obj_print(self.placeName))

        super().print_rdf_info()


    def get_rdf_id(self):
        return 'lkn:company' + xstr(self.id)


class School(Place):
    def __init__(self, id, url, about, place_name, website, phone, industry, companySize, headquarter, type, founded, speciality):
        super().__init__(id, url, about, place_name, website, phone, industry, companySize, headquarter, type, founded, speciality)

    def print_rdf_info(self):

        rdf_id = self.get_rdf_id()
        if self.placeName not in [s.placeName for s in global_schools]:
            global_schools.append(self)
            print(rdf_id + " rdf:type " + "lkn:School.")
        if self.placeName:
            print(rdf_id + " lkn:placeName " + obj_print(self.placeName))

        super().print_rdf_info()

    def get_rdf_id(self):
        return 'lkn:school' + xstr(self.id)