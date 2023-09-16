from requests_html import HTMLSession

from misc import URL, HEADERS, PROXY, logger


class ProxyChecker:
    @staticmethod
    def get_html(session):
        try:
            response = session.get(URL, headers=HEADERS, proxies=PROXY)
        except Exception as e:
            logger.exception(e)
        else:
            if response.ok:
                return response.html
            return response.status_code

    def get_data(self, session):
        html = self.get_html(session)

        ip = html.find('#d_clip_button span', first=True).text
        location = html.find('.value-country', first=True).text.split()[0].strip()

        return ip, location

    def get_all(self):
        with HTMLSession() as session:
            return self.get_data(session)
