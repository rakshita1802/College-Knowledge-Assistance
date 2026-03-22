class Access:
    ROLES = {
        "student": ["public"],
        "faculty": ["public", "faculty"]
    }

    @staticmethod
    def check(doc, role):
        return doc.metadata.get("access", "public") in Access.ROLES[role]