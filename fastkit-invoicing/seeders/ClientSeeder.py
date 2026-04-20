import asyncio
import random
import sys
import os

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

from fastkit_core.database import init_async_database, get_async_db_manager, AsyncRepository
from fastkit_core.config import ConfigManager

# All related models must be imported before SQLAlchemy mapper initializes.
# Clients has a relationship to Invoice — both must be visible at mapper time.
from modules.clients.models import Clients  # noqa
from modules.invoices.models import Invoice  # noqa
from modules.invoice_items.models import InvoiceItem  # noqa
from modules.products.models import Product  # noqa

configuration = ConfigManager(modules=['app', 'database'])
init_async_database(configuration)

LANGUAGES = ["en", "de", "es"]

COUNTRIES = ["US", "GB", "DE", "FR", "ES", "IT", "NL", "SE", "NO", "PL", "CA", "AU", "CH", "AT", "BE"]

CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "London", "Manchester", "Birmingham", "Leeds", "Glasgow",
    "Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne",
    "Paris", "Lyon", "Marseille", "Toulouse", "Nice",
    "Madrid", "Barcelona", "Valencia", "Seville", "Bilbao",
    "Milan", "Rome", "Naples", "Turin", "Florence",
    "Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Hague",
    "Stockholm", "Gothenburg", "Malmo", "Uppsala", "Vasteras",
    "Oslo", "Bergen", "Trondheim", "Stavanger", "Drammen",
    "Warsaw", "Krakow", "Lodz", "Wroclaw", "Poznan",
    "Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa",
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide",
    "Zurich", "Geneva", "Basel", "Bern", "Lausanne",
    "Vienna", "Graz", "Linz", "Salzburg", "Innsbruck",
    "Brussels", "Antwerp", "Ghent", "Bruges", "Liege",
]

COMPANY_PREFIXES = [
    "Alpha", "Beta", "Gamma", "Delta", "Apex", "Prime", "Elite", "Core",
    "Nexus", "Vertex", "Summit", "Peak", "Crest", "Zenith", "Vanguard",
    "Pioneer", "Frontier", "Horizon", "Meridian", "Pinnacle", "Atlas",
    "Titan", "Orion", "Stellar", "Nova", "Quantum", "Fusion", "Synergy",
    "Catalyst", "Momentum", "Velocity", "Clarity", "Insight", "Axiom",
    "Beacon", "Bridge", "Canvas", "Cipher", "Compass", "Conduit",
]

COMPANY_SUFFIXES = [
    "Solutions", "Technologies", "Systems", "Industries", "Enterprises",
    "Group", "Holdings", "Partners", "Associates", "Ventures",
    "Labs", "Studio", "Works", "Services", "Consulting",
    "Digital", "Global", "International", "Dynamics", "Analytics",
    "Software", "Networks", "Media", "Capital", "Resources",
]

BATCH_SIZE = 500
TOTAL = 10_000


def _generate_clients(count: int) -> list[dict]:
    clients = []
    for i in range(1, count + 1):
        prefix = random.choice(COMPANY_PREFIXES)
        suffix = random.choice(COMPANY_SUFFIXES)
        country = random.choice(COUNTRIES)
        city = random.choice(CITIES)
        language = random.choice(LANGUAGES)

        clients.append({
            "name": f"{prefix} {suffix} {i:05d}",
            "email": f"billing{i}@{prefix.lower()}{suffix.lower()}.com",
            "phone": f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "country": country,
            "city": city,
            "language": language,
            "address": f"{random.randint(1, 9999)} {random.choice(['Main St', 'Oak Ave', 'Park Rd', 'Lake Dr', 'Hill Blvd'])}",
            "postal_code": f"{random.randint(10000, 99999)}",
        })
    return clients


class ClientSeeder:
    def run(self) -> None:
        asyncio.run(self._seed())

    async def _seed(self) -> None:
        manager = get_async_db_manager()
        async with manager.session() as session:
            repo = AsyncRepository(Clients, session)

            existing = await repo.count()
            if existing >= TOTAL:
                print(f"  → ClientSeeder: skipped ({existing} clients already exist)")
                return

            remaining = TOTAL - existing
            print(f"  → ClientSeeder: generating {remaining} clients in batches of {BATCH_SIZE}...")

            data = _generate_clients(remaining)

            for batch_start in range(0, len(data), BATCH_SIZE):
                batch = data[batch_start:batch_start + BATCH_SIZE]
                await repo.create_many(batch)
                inserted = min(batch_start + BATCH_SIZE, len(data))
                print(f"     {inserted}/{remaining} inserted...")

            print(f"  → ClientSeeder: done — {remaining} clients inserted")
