class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        new_emails = []
        for addr in emails:
            addr1 = addr.split('@', 1)[0]
            addr2 = addr.split('@', 1)[1]

            addr1 = addr1.split('+', 1)[0]
            addr1 = addr1.replace('.', '')
            new_emails.append(addr1 +'@'+ addr2)
        # print(new_emails)

        unr_emails = []
        for ele in new_emails:
            if ele not in unr_emails:
                unr_emails.append(ele)
        # print(unr_emails)
        
        return len(unr_emails)
