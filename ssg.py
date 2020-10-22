import typer

from ssg.site import Site


def main(source = "content", dest = "dist"):
    config = { config:"source", dest:"dest"}

    inst = Site(**config).build()

typer.run(main)
