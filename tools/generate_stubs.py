"""Compatibility entry point for regenerating the per-domain CDP bindings."""

if __package__:
    from .generate_domains import main
else:
    from generate_domains import main

if __name__ == "__main__":
    main()
