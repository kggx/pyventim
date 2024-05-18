# class EventimCompenent:
#     """Class that handles access to the public Eventim API for components."""

#     def __init__(self, session: requests.Session = None) -> None:
#         # If a valid session is not provided by the user create a new one.
#         if not isinstance(session, requests.Session):
#             self.session: requests.Session = requests.Session()
#         else:
#             self.session: requests.Session = session

#         # Requires a desktop browser user-agent
#         self.session.headers.update(
#             {
#                 "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"
#             }
#         )
#         self.endpoint = "https://www.eventim.de/component/"

#     def get_attraction_events(self, attraction_id: int) -> dict:
#         r = self.session.get(
#             f"{self.endpoint}",
#             headers={},
#             params={
#                 "doc": "component",
#                 "esid": f"{attraction_id}",
#                 "fun": "eventselectionbox",
#                 # "startdate": None,
#                 # "enddate": None,
#                 # "ptype": None,
#                 # "cityname": None,
#                 # "filterused": True,
#                 # "pnum": 1,
#             },
#         )
#         r.raise_for_status()
#         return r.content.decode("utf-8")
#         # Actually returning json in scheme: https://schema.org/MusicEvent
#         # https://www.eventim.de/component/?affiliate=EVE&cityname=Berlin&doc=component&esid=3642502&filterused=true&fun=eventselectionbox&tab=1&startdate=2024-05-22
#         # https://www.eventim.de/component/?doc=component&enddate=2024-09-30&esid=473431&fun=eventlisting&pnum=2&ptype=&startdate=2024-05-18
#         # Parameters
#         # esid via public exploration API aka artist id
#         # pnum = page number
#         # filterused = true
#         # startdate
#         # enddate
#         # ptype=tickets | vip_packages (TODO: Look for types)
#         # fun=eventselectionbox
#         # doc=component
#         # cityname=Hamburg

#         # raise NotImplementedError()

#     # König der Löwen:
#     # https://www.eventim.de/component/?affiliate=EVE&cityname=Hamburg&doc=component&esid=473431&filterused=true&fun=eventselectionbox&startdate=2024-05-12&tab=2&enddate=2024-05-12

#     # Sleep Token https://www.eventim.de/component/
