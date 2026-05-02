import httpx
from config import LOG_URL
from auth import get_token

VALID_STACK = {"backend"}
VALID_LEVEL = {"debug", "info", "warn", "error", "fatal"}
VALID_PACKAGE = {
    "cache", "controller", "cron_job", "db", "domain",
    "handler", "repository", "route", "service", "config", "auth", "middleware", "utils"
}
async def log(stack, level, package, message):
    # strict validation
    if stack not in VALID_STACK:
        return
    if level not in VALID_LEVEL:
        return
    if package not in VALID_PACKAGE:
        return

    token = await get_token()
    if not token:
        return  # don't proceed if auth failed

    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        async with httpx.AsyncClient(timeout=1.0) as client:
            res = await client.post(LOG_URL, json=payload, headers=headers)

            # optional check (good practice)
            if res.status_code != 200:
                print("Log failed:", res.text)

    except Exception as e:
        print("Logging error:", e)  # safe debug
    print("LOG SENT:", payload)
