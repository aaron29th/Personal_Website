import sys
import jsonpickle

from staticjinja import Site


if __name__ == "__main__":
    projects = None
    with open('projects.json', 'r') as f:
        projects = jsonpickle.decode(f.read())

    site = Site.make_site(
        outpath="build",
        env_globals={
            'projects': projects
        }
    )
    auto_reload = 'reload' in sys.argv
    site.render(use_reloader=auto_reload)
