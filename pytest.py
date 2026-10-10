#!/usr/bin/env python3
import random
import string
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Server:
    server_id: str
    uptime_hours: float
    flag: Optional[str] = None


def is_in_whisper_window(uptime_hours: float, tolerance_hours: float = 0.52) -> bool:
    """Checks if uptime lands within +/- 30 minutes of a 6-hour or 7-hour multiple

    (e.g., ~6h, ~7h, ~12h, ~14h, ~18h, ~21h, ~24h...).
    Calibrated to trigger ~7-8 times across a fleet of 25 servers.
    """
    if uptime_hours < (6.0 - tolerance_hours):
        return False

    rem_6 = uptime_hours % 6.0
    rem_7 = uptime_hours % 7.0

    is_mult_6 = rem_6 <= tolerance_hours or rem_6 >= (6.0 - tolerance_hours)
    is_mult_7 = rem_7 <= tolerance_hours or rem_7 >= (7.0 - tolerance_hours)

    return is_mult_6 or is_mult_7


def generate_random_code() -> str:
    """Generates random mixed server codes like 'F9B,782' or 'F92Afb3r535'."""
    if random.random() < 0.5:
        # Style: 'F9B,782'
        part1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=3))
        part2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=3))
        return f"{part1},{part2}"
    else:
        # Style: 'F92Afb3r535'
        charset = string.ascii_letters + string.digits
        return "".join(random.choices(charset, k=random.randint(9, 11)))


def generate_mock_fleet(count: int = 25) -> List[Server]:
    """Generates a mock fleet mixing 'premium-X' and random alphanumeric codes."""
    mock_fleet = []
    premium_counter = 1

    for _ in range(count):
        # Mix between premium titles and alphanumeric codes
        if random.random() < 0.4:
            server_id = f"premium-{premium_counter:02d}"
            premium_counter += 1
        else:
            server_id = generate_random_code()

        uptime = round(random.uniform(1.0, 72.0), 2)
        mock_fleet.append(Server(server_id=server_id, uptime_hours=uptime))

    return mock_fleet


def audit_servers(fleet: List[Server]) -> None:
    """Audits the fleet and tags matches with WHISPER_MODEL."""
    print(f"{'SERVER ID / CODE':<20} | {'UPTIME (h)':<12} | {'STATUS / TAG'}")
    print("-" * 52)

    whisper_count = 0
    for server in fleet:
        if is_in_whisper_window(server.uptime_hours):
            server.flag = "WHISPER_MODEL"
            whisper_count += 1
            status = f"\033[93m[FLAGGED: {server.flag}]\033[0m"
        else:
            status = "NORMAL"

        print(f"{server.server_id:<20} | {server.uptime_hours:<12.2f} | {status}")

    print("-" * 52)
    print(f"Total Servers: {len(fleet)} | Flagged as WHISPER_MODEL: {whisper_count}")


if __name__ == "__main__":
    servers = generate_mock_fleet(count=25)
    audit_servers(servers)