import sys
import jsonpickle

from urllib.parse import quote
from staticjinja import Site


if __name__ == "__main__":
    projects = None
    with open('projects.json', 'r') as f:
        projects = jsonpickle.decode(f.read())

    pgp_key = None
    with open('resources/Aaron_Rosser_aaron@aaronrosser.xyz-0x67765DE3715DB0EB-pub.asc', 'r') as f:
        pgp_key = f.read()

    site = Site.make_site(
        outpath="build",
        env_globals={
            'projects': projects,
            'pgp_key': {
                'data': pgp_key,
                'encoded_data': quote(pgp_key),
                'filename': 'Aaron_Rosser_aaron@aaronrosser.xyz-0x67765DE3715DB0EB-pub.asc'
            }
        }
    )
    auto_reload = 'reload' in sys.argv
    site.render(use_reloader=auto_reload)
