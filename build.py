from staticjinja import Site

projects = [

]

if __name__ == "__main__":
    site = Site.make_site(outpath="build")
    # enable automatic reloading
    site.render(use_reloader=True)