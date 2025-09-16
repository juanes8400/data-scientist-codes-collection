def test_import_scripts():
    """Smoke test to ensure example scripts can be imported without errors."""
    # Attempt to import a few modules from the main data-scientist codes collection.
    # If these modules cannot be imported, this test will fail.
    import importlib

    modules = [
        "ada_boost_classifier",
        "arima_time_series",
        "bagging_classifier",
    ]

    for module_name in modules:
        try:
            importlib.import_module(module_name)
        except ImportError:
            raise AssertionError(f"Failed to import {module_name}")