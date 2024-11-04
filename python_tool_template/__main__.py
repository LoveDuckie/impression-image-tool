import rich_click as click


@click.group(help="The base command-line interface for the tool.")
@click.pass_context
def cli(context: click.Context) -> None:
    """

    :param context:
    :return:
    """
    if not context:
        raise ValueError("The click context is invalid.")

    context.ensure_object(dict)
    context.exit(0)


if __name__ == "__main__":
    try:
        cli()
    except Exception as exc:
        pass
