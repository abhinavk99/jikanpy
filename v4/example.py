from jikanpy import Client
from jikan_api_client.api.anime.get_anime_by_id import sync_detailed

# Extremely basic test for now, just to see if this works


def main() -> None:
    # doesnt currently work, because of enum error
    client = Client(base_url="https://api.jikan.moe/v4", verify_ssl=True, timeout=2.0)
    resp = sync_detailed(1, client=client)
    assert resp.status_code == 200
    print(resp.parsed)

if __name__ == "__main__":
    main()
