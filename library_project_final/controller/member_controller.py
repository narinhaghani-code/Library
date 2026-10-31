from model.member import Member
from tools.file_manager import *
from tools.validation import id_validator


class MemberController:
    def __init__(self, path):
        self.path = path
        self.members = []
        self.load()

    def load(self):
        try:
            for item in load_items(self.path):
                self.members.append(Member(item["member_id"], item["name"], item["email"]))
        except (KeyError, TypeError, ValueError):
            raise ValueError("Data file is damaged")

    def save(self):
        items = []
        for member in self.members:
            items.append(member.to_dict())
        save_items(self.path, items)

    def add_member(self, member_id, name, email):
        member = Member(member_id, name, email)
        for item in self.members:
            if item.member_id == member.member_id:
                raise ValueError(f"Member {member.member_id} already exists")
        self.members.append(member)
        self.save()
        return member

    def get_member(self, member_id):
        member_id = id_validator(member_id, "Member ID")
        for member in self.members:
            if member.member_id == member_id:
                return member
        raise ValueError(f"No member with ID {member_id}")
