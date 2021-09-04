from Member import global_skills
from Rdf_thing import Rdf_thing
from utlis import xstr, obj_print, print_and_write


class Skill(Rdf_thing):
    def __init__(self, id, name):
        super().__init__(id)
        self.skill_name = name

    def get_rdf_id(self):
        return "lkn:skill" + xstr(self.id)

    def print_rdf_info(self):
        rdf_id = self.get_rdf_id()
        if self.skill_name not in [s.skill_name for s in global_skills]:
            global_skills.append(self)
            print_and_write(rdf_id + " rdf:type " + "lkn:Skill.")
            if self.skill_name:
                print_and_write(rdf_id + " lkn:skillName " + obj_print(self.skill_name))
        else:
            for skill in global_skills:
                if skill.skill_name == self.skill_name:
                    self.id = skill.id

