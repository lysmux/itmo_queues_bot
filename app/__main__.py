import argparse
import logging

from app.application.bot import run_bot
from app.container import init_container
from app.core.settings import Settings


def main() -> None:
    settings = Settings()  # type: ignore[reportCallIssue]
    container = init_container(settings)
    logging.basicConfig(level=settings.log_level)

    run_bot(container)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--reload", action="store_true")
    args = parser.parse_args()

    if args.reload:
        from watchfiles import run_process

        run_process("./app", target="app.__main__.main")
    else:
        main()
