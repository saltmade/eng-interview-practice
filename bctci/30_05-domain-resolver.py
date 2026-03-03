"""You manage a shared web hosting server with multiple IP addresses, and
where multiple domains can share the same IP address. Each domain can have
multiple subdomains.

Implement a class, DomainResolver, that supports three methods:

    - register_domain(ip, domain): associates a domain with an IP. You can
      assume that this function will be called at most once for a given domain.
    - register_subdomain(domain, subdomain): adds a subdomain to a domain. You
      can assume that the domain will have been previously registered.
      Different domains can have a subdomain with the same name.
    - has_subdomain(ip, domain, subdomain): returns whether there is a domain
      registered at that IP that has the given subdomain.

IPs, domains, and subdomains are strings.
"""


class DomainResolver:
    def __init__(self):
        self.domain_to_ips = {}
        self.domain_to_subdomains = {}

    def register_domain(self, ip, domain):
        self.domain_to_ips[domain] = ip

    def register_subdomain(self, domain, subdomain):
        if domain not in self.domain_to_subdomains:
            self.domain_to_subdomains[domain] = set()
        self.domain_to_subdomains[domain].add(subdomain)

    def has_subdomain(self, ip, domain, subdomain):
        return (
            domain in self.domain_to_ips
            and self.domain_to_ips[domain] == ip
            and domain in self.domain_to_subdomains
            and sudomain in self.domain_to_subdomains[domain]
        )


"""
Tip: sketch out the expected shape of your data structure to clearly
communicate it to the interviewer, e.g.

    192.168.0.1: example.com example.org
    10.168.0.1: foo.com

"""
