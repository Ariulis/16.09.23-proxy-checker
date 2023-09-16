from misc import timeit
from scraper import ProxyChecker


def get_ip_and_location():
    parser = ProxyChecker()
    return parser.get_all()


@timeit()
def main():
    ip, location = get_ip_and_location()
    print(f'Your IP: {ip}\nYour location: {location}')


if __name__ == '__main__':
    main()
