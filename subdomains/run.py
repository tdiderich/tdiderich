from googlesearch import search
from urllib.parse import urlparse
import argparse


def write_hostnames_to_file(site: str, hostnames: list):
    filename = f"{site}.txt"
    with open(file=filename, mode="wt") as file:
        file.write("\n".join(hostnames))
        file.write("\n")
        file.close()


def get_subdomains(site: str):
    query = f"site:{site} -inurl:www"
    hostnames = []

    for x in search(query, num=1000, pause=2):
        hostname = urlparse(x).netloc
        if hostname not in hostnames:
            print(hostname)
            hostnames.append(hostname)

    return hostnames


if __name__ == "__main__":
    # parse CLI args
    parser = argparse.ArgumentParser(
        description="Subdomain grabber",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-s", "--site", action="store", help="Site to capture subdomains for."
    )
    args = parser.parse_args()
    config = vars(args)

    # get subdomains if the site is passed
    if config["site"] is not None:
        site = config["site"]
        hostnames = get_subdomains(site=site)
        write_hostnames_to_file(site=site, hostnames=hostnames)
    else:
        print("Site (-s or --site) required")
