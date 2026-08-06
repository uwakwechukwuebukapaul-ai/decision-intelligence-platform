{
    "nodes": [
        "incident",
        "ioc",
        "identity",
        "asset",
        "detection"
    ],
    "edges": [
        ("identity", "asset"),
        ("asset", "ioc"),
        ("ioc", "incident")
    ]
}