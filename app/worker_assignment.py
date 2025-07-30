WORKERS = ["worker1", "worker2", "worker3"]

def assign_worker(request_id: str) -> str:
    # Simple hash-based assignment for consistency
    return WORKERS[hash(request_id) % len(WORKERS)]
