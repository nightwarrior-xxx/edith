import meetup.api
from api_key import api_key


groups = ['ilugdelhi', 'pydelhi', 'Mozilla_Delhi', 'LinuxChix-India-Meetup']
next_events_links = []
client = meetup.api.Client(api_key)

class links:

    def get_events_links(self):
        for grp in groups:
            try:
                group_info = client.GetGroup({'urlname': grp})
                next_event_id = group_info.next_event['id']
                group_link = group_info.link
                next_event_link = group_link + "events/" + next_event_id
                next_events_links.append(next_event_link)
            except AttributeError:
                pass
