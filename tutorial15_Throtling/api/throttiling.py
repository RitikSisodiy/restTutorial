from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class onethrottle(UserRateThrottle):
    scope = 'one'