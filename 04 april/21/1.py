from typing import List


class Solution:

    def __init__(self):
        self.unique_emails = []

    def numUniqueEmails(self, emails: List[str]) -> int:

        for email in emails:
            address, domain = email.split("@")
            new_address = address.replace(".", "")

            if "+" in new_address:
                new_address = new_address[:new_address.find("+")]

            new_email = f"{new_address}@{domain}"

            if new_email not in self.unique_emails:
                self.unique_emails.append(new_email)

        return len(self.unique_emails)


# emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
#           "testemail+david@lee.tcode.com"]

emails = "a@leetcode.com","b@leetcode.com","c@leetcode.com"

test = Solution()
print(test.numUniqueEmails(emails=emails))
