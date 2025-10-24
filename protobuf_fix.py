"""
Protobuf compatibility fix for older protobuf versions
This file patches the missing runtime_version import
"""

try:
    from google.protobuf import runtime_version
except ImportError:
    # Create a dummy runtime_version for compatibility
    class DummyRuntimeVersion:
        def __getattr__(self, name):
            return None
    
    import google.protobuf
    google.protobuf.runtime_version = DummyRuntimeVersion()
