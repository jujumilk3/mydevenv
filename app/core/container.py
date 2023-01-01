from dependency_injector import containers


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoint.auth",
            "app.api.v1.endpoint.user",
            "app.core.dependency.authentication",
        ]
    )
